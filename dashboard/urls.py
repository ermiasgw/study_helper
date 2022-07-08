from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.notes, name='notes'),
    path('delete_note/<int:pk>', views.delete_note, name='delete note'),
    path('notes_derail/<int:pk>', views.NotesDetail.as_view(), name='notes detail'),

    path('homework', views.homework, name='homework'),
    path('homework_update/<int:pk>', views.update_homework, name='homework_update'),
    path('homework_delete/<int:pk>', views.delete_homework, name="homework_delete"),

    path('youtube', views.youtube, name='youtube'),

    path('todo', views.todo, name="todo"),
    path('update_todo/<int:pk>', views.update_todo, name="update_todo"),
    path('delete_todo/<int:pk>', views.delete_todo, name="delete_todo"),

    path('book', views.book, name='book'),

    path('dictionary', views.dictionary, name="dictionary"),

    path('wiki', views.wiki, name="wiki"),

    path('conversion', views.conversion, name="conversion"),

]