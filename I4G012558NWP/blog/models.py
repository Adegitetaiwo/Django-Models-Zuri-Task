from zlib import DEF_BUF_SIZE
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    """
    This is the Post Model. It takes care of creating our tables 
    and validating entries in our database.
    """
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = ''
        managed = True
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return (f"{self.title} by {self.author}").__str__()
