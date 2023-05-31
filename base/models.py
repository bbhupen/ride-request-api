from django.db import models
from django.contrib.auth.models import User


class Request(models.Model):

    REQUEST_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled')
    ]

    request_user_id = models.CharField(max_length=20)
    request_driver_id = models.CharField(max_length=20)
    request_pickup_location = models.CharField(max_length=20)
    request_drop_location = models.CharField(max_length=20)
    request_status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES)
    
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)
    driver_vehicle = models.CharField(max_length=256)
    driver_license_no = models.CharField(max_length=256, default="AS09")
    

class Review(models.Model):
    review_driver_id = models.CharField(max_length=20)
    review_user_id = models.CharField(max_length=20)
    review_text = models.CharField(max_length=500)
    review_stars = models.CharField(max_length=1)