from django.db import models #type:ignore
class Register(models.Model):
    email=models.CharField(max_length=20,null=True)
    psw=models.CharField(max_length=10,null=True)
    repeatpassword=models.CharField(max_length=10,null=True)
def __str__(self):
    return self.email+''+self.psw+','+self.repeatpassword

    


