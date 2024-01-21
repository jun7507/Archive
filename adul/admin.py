from django.contrib import admin
from .models import Question, BookList, BookStore, BomAssemlist, BomList

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin, BookList, BookStore, BomAssemlist, BomList)
