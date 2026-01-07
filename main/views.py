from django.shortcuts import render
from .models import *

def index(request):
    correct = None
    incorrects = None
    message = None
    search = request.GET.get('search')
    if search:
        word = search.lower()
        corrects = Correct.objects.filter(word=word)
        if corrects.exists():
            correct = corrects.first()
            incorrects = correct.incorrect_set.all()
        else:
            incorrects = Incorrect.objects.filter(word=word)
            if incorrects.exists():
                incorrect = incorrects.first()
                correct = incorrect.correct
                incorrects = correct.incorrect_set.all()
            else:
                if 'x' not in word and 'h' not in word:
                    message = "So'z tarkibida x yoki h mavjud emas!"
                else:
                    message = "Ro'yxatda mavjud emas!"

    context = {
        'correct': correct,
        'incorrects': incorrects,
        'message': message,
    }
    return render(request, 'index.html', context)
