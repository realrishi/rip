from django.db import models


# Create your models here.


class Cont(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,)
    email = models.CharField(max_length=90)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from ' +self.name+ ' with email '+self.email
    

