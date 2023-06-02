from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Request(models.Model):

    REQUEST_STATUS_CHOICES = [
        ('pending', 'Pending'),         # default status, when the request is created.
        ('active', 'Active'),           # when the ride is started
        ('approved', 'Approved'),       # when the driver accepts the request, the status is changed to approved.
        ('cancelled', 'Cancelled'),     # when the driver or user cancels the ride after the approval, the status is changed to cancelled.
        ('ended', 'Ended'),             # when the driver or user end the ride while the status is on active.
        ('completed', 'Completed'),     # when the ride completes without any problem
        
    ]

    request_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    request_driver_id = models.CharField(max_length=20)
    request_pickup_location = models.CharField(max_length=20)
    request_drop_location = models.CharField(max_length=20)
    request_status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES)


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)
    driver_vehicle = models.CharField(max_length=256)
    driver_license_no = models.CharField(max_length=256, default="AS09")
    driver_current_location = models.CharField(max_length=30, default=0)
    driver_is_driving = models.BooleanField(default=False)
    driver_is_active = models.BooleanField(default=True)


class Review(models.Model):
    review_driver_id = models.CharField(max_length=5)
    review_user_id = models.CharField(max_length=5)
    review_text = models.CharField(max_length=500)
    review_stars = models.CharField(max_length=1)
    review_ride_id = models.CharField(max_length=5, default=0)
