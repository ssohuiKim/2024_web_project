from django.shortcuts import render
from rest_framework import viewsets
from .models import MeetingInfo
from .serializers import MeetingInfoSerializer

class MeetingInfoViewSet(viewsets.ModelViewSet):
    queryset = MeetingInfo.objects.all()
    serializer_class = MeetingInfoSerializer

