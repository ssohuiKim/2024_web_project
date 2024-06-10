from django.db import models

class Meeting(models.Model):
    meeting_name = models.CharField(max_length=25)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    apply_date = models.DateField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    details = models.TextField()
    selected_categories = models.JSONField()
    current_participants = models.IntegerField(default=1)

    def __str__(self):
        return self.meeting_name