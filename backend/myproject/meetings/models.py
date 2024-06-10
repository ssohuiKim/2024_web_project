from django.db import models

class Meeting(models.Model):
    meeting_name = models.CharField(max_length=255)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    apply_date = models.DateField()
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    current_participants = models.PositiveIntegerField(default=1)
    details = models.TextField()
    selected_categories = models.JSONField()

    def __str__(self):
        return self.meeting_name