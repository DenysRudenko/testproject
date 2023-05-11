
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserPreference(models.Model):

    # this will delete a preference that belong to the user
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(User) + 's' + 'preferences'
