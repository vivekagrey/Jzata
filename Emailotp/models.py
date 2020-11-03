from django.db import models
from django.contrib.auth.models import User

class UserOTP(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time_st=models.DateField(auto_now=True)
    otp=models.IntegerField()


class price(models.Model):
    plane1=models.IntegerField()
    plane2=models.IntegerField()
    plane3=models.IntegerField()

    def __str__(self):
        return 