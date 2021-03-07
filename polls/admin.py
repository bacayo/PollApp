from django.contrib import admin
from .models import Question, Choice

# Register your models here.
admin.site.site_header = "PollEksi"
admin.site.index_title = "Welcome to PollEksi admin area"
admin.site.site_title = "PollEksi admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date'],'classes':
        ['collapse']}),
    ]
    inlines = [ChoiceInline]    

admin.site.register(Question,QuestionInline)
