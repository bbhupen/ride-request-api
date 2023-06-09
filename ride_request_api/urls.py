"""
URL configuration for ride_request_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base.views import UserView, RideRequestView, ApplyDriver, RideAcceptView, RideCompleteView, RideEndView, RideStartView, RideCancelView,HomeView, LoginView, AddReviewView, ReviewView, RideHistoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('register', UserView.as_view(), name='register' ),
    path('login', LoginView.as_view(), name="login"),
    path('api/register-driver', ApplyDriver.as_view(), name="add-driver"),
    path('api/ride/request', RideRequestView.as_view(), name="ride-request"),
    path('api/ride/accept', RideAcceptView.as_view(), name="accept-request"),
    path('api/ride/cancel', RideCancelView.as_view(), name="cancel-ride"),
    path('api/ride/end', RideEndView.as_view(), name="end-ride"),
    path('api/ride/start', RideStartView.as_view(), name="start-ride"),
    path('api/ride/complete', RideCompleteView.as_view(), name="complete-ride"),
    path('api/ride/history', RideHistoryView.as_view(), name="view-ride-history"),
    path('api/review/add', AddReviewView.as_view(), name="add-review"),
    path('api/review/view', ReviewView.as_view(), name="view-review")
]
