from django.urls import path
from .views import NoteListView, NoteDetailView, add_note

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('note/add/', add_note, name='add_note'),
]