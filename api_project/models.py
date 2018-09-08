from django.db import models

class Users(models.Model):
    uid = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=255, null=False)

def __str__(self):
    return "{} - {}".format(self.uid, self.name)
