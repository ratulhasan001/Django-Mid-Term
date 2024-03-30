from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User


class Car(models.Model):
    model = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='car/media/images/')
    buyers = models.ManyToManyField(User, blank=True)
        
    def __str__(self):
        return self.model
    
class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"