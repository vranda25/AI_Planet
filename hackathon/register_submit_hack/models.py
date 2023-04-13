from django.db import models
from accounts.models import CustomUser
from create_hack.models import CreateHack
import os


# Create your models here.

# Registration to a hackathon by a user
class ResigterHack(models.Model):
    # a registration will belong to a user and a hackathon
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(CreateHack, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+' : '+str(self.user.first_name)+' : '+str(self.hackathon.title)



# function to upload cover image to specified path
def upload_cover_image(instance, filename):
    filename = f"{instance.title}_{instance.registered_hack.user.first_name}"
    return os.path.join('register_submit_hack/images/cover',filename)


# function to upload cover image to specified path
def upload_submission_image(instance, filename):
    filename = f"{instance.title}_{instance.registered_hack.user.first_name}"
    return os.path.join('register_submit_hack/images/submission',filename)


# function to upload cover image to specified path
def upload_submission_file(instance, filename):
    filename = f"{instance.title}_{instance.registered_hack.user.first_name}"
    return os.path.join('register_submit_hack/images/submission',filename)


# Submission for registered hackathon
class UploadSubmission(models.Model):
    # a submission can belong to only one registration and a registration can have only one submission, therefore OneToOne relation with ResgisterHack
    registered_hack = models.OneToOneField(ResigterHack, on_delete=models.CASCADE)            
    title = models.CharField(max_length=100, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=3000, null=True, blank=True)
    cover_image = models.ImageField(upload_to=upload_cover_image, null=True, blank=True)

    #only one field among below submission will be filled by user according to the submission type of hackathon registered in registered_hack field
    submission_link = models.CharField(max_length=200, null=True, blank=True)
    submission_image = models.ImageField(upload_to=upload_submission_image, null=True, blank=True)
    submission_file = models.FileField(upload_to=upload_submission_file, null=True, blank=True)

    def __str__(self):
        return str(self.id)+' : '+str(self.registered_hack)
    
