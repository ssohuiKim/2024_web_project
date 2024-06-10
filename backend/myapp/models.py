from django.db import models

class MeetingInfo(models.Model):
    meetingName = models.CharField(max_length=100)
    startDate = models.DateField()
    startTime = models.TimeField()
    endDate = models.DateField()
    endTime = models.TimeField()
    applyDate = models.DateField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    details = models.TextField()
    categories = models.JSONField() 

    def __str__(self):
        return self.meetingName
