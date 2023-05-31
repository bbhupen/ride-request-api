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
from base.views import UserView, RideRequestView, AddDriverView, RideAcceptView, RideCancelView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('register', UserView.as_view(), name='register' ),
    path('api/ride/request', RideRequestView.as_view(), name="ride-request"),
    path('api/register-driver', AddDriverView.as_view(), name="add-driver"),
    path('api/ride/accept', RideAcceptView.as_view(), name="accept-request"),
    path('api/ride/cancel', RideCancelView.as_view(), name="accept-request")
]
