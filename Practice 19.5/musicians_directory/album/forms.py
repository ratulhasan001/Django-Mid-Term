from django import forms
from .models import Album
from django.forms import DateInput

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            'release_date': DateInput(attrs={'type': 'date'})
        }