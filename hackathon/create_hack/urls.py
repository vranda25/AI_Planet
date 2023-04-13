from django.urls import path
from .views import *

urlpatterns = [
    # create hackathon (Login is required)
    path('', CreateHackView.as_view()),

    # list all of all hackathons (Login is required)
    path('hackathons/list/', ListHacksView.as_view()),
]