from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feature_vector = models.JSONField()
    ip_address = models.GenericIPAddressField()
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name