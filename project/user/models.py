from django.db import models



class User(models.Model):
    Name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    c_password = models.CharField(max_length=200)
    # p_image=models.ImageField(upload_to='profiles/')
    
    def __str__(self):
        return 