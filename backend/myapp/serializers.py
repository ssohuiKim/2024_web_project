from rest_framework import serializers
from .models import MeetingInfo

class MeetingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingInfo
        fields = '__all__'
