from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form' : musician_form})