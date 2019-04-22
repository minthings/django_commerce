from django.db import models

class profiles(models.Model):
    name = models.CharField(max_length = 120)
    description = models.TextField(default = 'description default text')

    def __unicode(self):
        return self.name
# Create your models here.
