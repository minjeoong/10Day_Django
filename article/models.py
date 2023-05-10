from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(
        'user.User', 
        on_delete=models.CASCADE,
    )
    title = models.TextField()
    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,

    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )