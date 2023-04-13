from django.db import models
from django.utils import timezone
from datetime import datetime
import os


# Create your models here.

# upload background image of the hackathon to specified path
def upload_background_image(instance, filename):
    filename = f"{instance.title}"
    return os.path.join('create_hack/images/background',filename)


# upload hackathon image of the hackathon to specified path
def upload_hack_image(instance, filename):
    filename = f"{instance.title}"
    return os.path.join('create_hack/images/hack',filename)


# choices for submission type
SUBMISSION_TYPE_CHOICES = [
        ("image", "image"),
        ("file", "file"),
        ("link", "link"),
    ]


# create hackathon
class CreateHack(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    background_image = models.ImageField(upload_to=upload_background_image, null=True, blank=True)
    hack_image = models.ImageField(upload_to=upload_hack_image, null=True, blank=True)
    type_of_submission = models.CharField(max_length=5, choices=SUBMISSION_TYPE_CHOICES, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    reward_prize = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.id)+' : '+self.title
