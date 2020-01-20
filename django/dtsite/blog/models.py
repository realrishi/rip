from django.db import models

# Create your models here.



class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=60)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return 'Post By  ' +self.author
    