from django.contrib import admin
from .models import *

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name',]}
    
admin.site.register(Genre,GenreAdmin)
admin.site.register(Book)
admin.site.register(Review)