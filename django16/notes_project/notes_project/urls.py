from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # keep the app under /notes/
    path('notes/', include('notes.urls')),
    # root -> notes list (named in notes/urls.py as 'note_list')
    path('', RedirectView.as_view(pattern_name='note_list', permanent=False)),
]