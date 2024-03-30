from django.db import models

# Create your models here.

list_instrument = (
    ("Guitar", "Guitar"),
    ("Drums", "Drums"),
    ("Violin", "Violin"),
    ("Piano", "Piano")
)

class Musician(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    phone_no = models.CharField(max_length = 50)
    instrument_type = models.CharField(max_length=50, choices=list_instrument)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

