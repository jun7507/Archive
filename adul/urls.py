from django.urls import path

from .views import base_views, question_views, answer_views, book_views, bom_views

app_name = 'adul'

urlpatterns = [
    # base
    path('', base_views.index, name='index'),
    path('', base_views.home, name='home'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    
    # question
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    # answer
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
    
    #Booklist
    path("book/select/", book_views.select, name='select'),
    path("book/insert/", book_views.insert, name='insert'),
    path("book/update/", book_views.update, name='update'),
    path("book/delete/", book_views.delete, name='delete'),

    #Bomlist
    path("bom/select_b/", bom_views.select_b, name='select_b'),
    # path("bom/insert/", bom_views.insert, name='insert_b'),
    path("book/update_b/", bom_views.update, name='update_b'),
]