from django.contrib import admin
from  .models import *

class IncorrectInline(admin.StackedInline):
    model = Incorrect
    extra = 1

class CorrectAdmin(admin.ModelAdmin):
    inlines = [IncorrectInline]


class IncorrectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Correct, CorrectAdmin)
admin.site.register(Incorrect, IncorrectAdmin)