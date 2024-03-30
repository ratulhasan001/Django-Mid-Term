# from django.shortcuts import redirect, render
# from . import forms
# from . import models
# from django.contrib.auth.decorators import login_required
# # Create your views here.
# @login_required
# def add_album(request):
#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('add_album')
#     else:
#         album_form = forms.AlbumForm()
#     return render(request, 'add_album.html', {'form' : album_form})

# @login_required
# def edit_album(request, id):
#     album = models.Album.objects.get(pk = id)
#     album_form = forms.AlbumForm(instance=album)
#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST, instance=album)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('homepage')
#     return render(request, 'add_album.html', {'form' : album_form})
# @login_required
# def delete_album(request, id):
#     album = models.Album.objects.get(pk = id)
#     album.delete()
#     return redirect('homepage')

from django.shortcuts import redirect, render
from django.views import View
from . import forms
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

class AddAlbumView(LoginRequiredMixin, View):
    def get(self, request):
        album_form = forms.AlbumForm()
        return render(request, 'add_album.html', {'form': album_form})
    
    def post(self, request):
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
        return render(request, 'add_album.html', {'form': album_form})

class EditAlbumView(LoginRequiredMixin, View):
    def get(self, request, id):
        album = models.Album.objects.get(pk=id)
        album_form = forms.AlbumForm(instance=album)
        return render(request, 'add_album.html', {'form': album_form})

    def post(self, request, id):
        album = models.Album.objects.get(pk=id)
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
        return render(request, 'add_album.html', {'form': album_form})

class DeleteAlbumView(LoginRequiredMixin, View):
    def get(self, request, id):
        album = models.Album.objects.get(pk=id)
        album.delete()
        return redirect('homepage')
