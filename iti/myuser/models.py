from django.db import models
class myuser(models.Model):

    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=20,null=True)

