from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Note
from .forms import NoteForm

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})