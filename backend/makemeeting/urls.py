# from django.urls import path
# from .views import MeetingListCreate

# urlpatterns = [
#     path('meetings/', MeetingListCreate.as_view(), name='meeting-list-create'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('meetings/', views.create_meeting),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingViewSet

router = DefaultRouter()
router.register(r'meetings', MeetingViewSet, basename='meeting')

urlpatterns = [
    path('', include(router.urls)),
]
