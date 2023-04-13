from django.urls import path
from .views import *

urlpatterns = [
    # Registration to a hackathon by a user (Login is required)
    path('register/', RegisterHackView.as_view()),

    # Submissions of a registered hackathon by a user (Login is required)
    path('submission/', UploadSubmissionView.as_view()),
   
    # list of all hackathons registerd by a user (Login is required)
    path('list/registered/', ListAllRegisteredHacksView.as_view()),

    # list of submissions of all hackathons by a user (Login is required)
    path('list/submitted/', ListSubmissionView.as_view()),
]