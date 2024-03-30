from django.contrib import admin
from .models import Brand
# Register your models here.
# admin.site.register(Brand)

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']

admin.site.register(Brand, BrandAdmin)