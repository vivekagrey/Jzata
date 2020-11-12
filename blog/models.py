from django.db import models


class Blog(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    img=models.ImageField(blank=True ,null=True)

    def __str__(self):
        return self.name