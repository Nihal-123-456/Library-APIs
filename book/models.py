from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    image = models.ImageField(upload_to='book/media/uploads')
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to='book/media/uploads')
    publication_date = models.DateField()
    genre = models.ManyToManyField(Genre)
    availability_status = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

STAR_CHOICE = {
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
}

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICE, max_length=20)