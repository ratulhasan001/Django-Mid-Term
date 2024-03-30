from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms
from car.models import Car
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
# Create your views here.

class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

def update_quantity(request, id):
    car = Car.objects.get(pk=id)
    car.quantity -= 1
    car.buyers.add(request.user)
    car.save()
    return redirect("homepage")