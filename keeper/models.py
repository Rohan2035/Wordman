from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class profile(models.Model):

    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='User Profiles')
    key = models.BooleanField(default=False)

    def __str__(self) -> str:
        
        return str(self.user_profile)

class password_store(models.Model):

    class Meta:

        verbose_name_plural = 'Password Stores'
        

    id = models.AutoField
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    password_label =  models.CharField(max_length=250, null=True, verbose_name='Label')
    password =  models.CharField(max_length=250, null=True)

    def __str__(self):

        return str(self.id)

