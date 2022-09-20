from dataclasses import fields
from django.contrib import admin

from .models import Question, Answers

class ChoiceInline(admin.TabularInline):
    model = Answers
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'really_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)