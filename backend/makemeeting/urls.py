# from django.urls import path
# from .views import MeetingListCreate

# urlpatterns = [
#     path('meetings/', MeetingListCreate.as_view(), name='meeting-list-create'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('meetings/', views.create_meeting),
]
