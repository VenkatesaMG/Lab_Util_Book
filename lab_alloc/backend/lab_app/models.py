from django.db import models
from django.core.exceptions import ValidationError

class User(models.Model):
    username = models.CharField(max_length = 20, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length = 128)
    
class Laboratory(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=30, unique=True)
    lab_capacity = models.IntegerField(default=5)
    icon_name = models.CharField(max_length=20, null=True)
    fallback_icon_url = models.URLField(null=True, blank=True)

class Admin(models.Model):
    username = models.CharField(max_length = 20, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length = 128)
    department = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)

class Schedules(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    lab_id = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    schedule_from = models.TimeField()
    schedule_to = models.TimeField()
    status = models.CharField(max_length=20, null=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'lab_id', 'schedule_date','schedule_from','schedule_to'], name='unique_schedule_per_user_lab')
        ]

class Daily(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    lab_id = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    hours = models.FloatField()
    num_bookings = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'lab_id'], name='daily_unique')
        ]

class Week(models.Model):
    id = models.AutoField(primary_key=True)
    week_label = models.CharField(max_length=25)
    week_num = models.IntegerField(blank=True, null=True)
    lab_id = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    total_hours = models.FloatField()
    num_bookings = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['week_num', 'lab_id'], name='weekly_unique')
        ]

class Month(models.Model):
    id = models.AutoField(primary_key = True)
    month = models.CharField(max_length = 25)
    lab_id = models.ForeignKey(Laboratory, models.CASCADE)
    total_hours = models.FloatField()
    num_bookings = models.IntegerField()

class ScheduleRequest(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    lab_id = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    schedule_from = models.TimeField()
    schedule_to = models.TimeField()
    status = models.CharField(max_length=30, default="pending")
    approved_by = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True, blank=True)
    decision_date = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'lab_id', 'schedule_date','schedule_from','schedule_to','status'], name='unique_schedule_request')
        ]

class Maintenance(models.Model):
    username = models.ForeignKey(Admin, on_delete=models.CASCADE)
    lab_id = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    main_reason = models.CharField(max_length=200)