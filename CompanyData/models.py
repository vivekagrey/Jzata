from django.db import models

class Basic(models.Model):
    name=models.TextField(null=True)
    website=models.TextField(null=True)
    Industry=models.TextField(null=True)
    Headquatars=models.TextField(null=True)
    type=models.TextField(null=True)
    founded=models.TextField(null=True)
    specialities=models.TextField(null=True)
    linkedin=models.TextField(null=True)
    domain=models.TextField(null=True)
    logo=models.TextField(null=True)
    description=models.TextField(null=True)
    company_no=models.TextField(null=True)
    incorporation_date=models.TextField(null=True)
    register_address=models.TextField(null=True)
    Industry_code=models.TextField(null=True)
 


    def __str__(self):
        return self.name

