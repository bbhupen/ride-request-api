from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.views import Response

from .serializers import UserSerializer, RequestSerializer, DriverSerializer, ReviewSerializer
from .models import Request


class AddDriverView(APIView):
    def post(self, request):
        data = request.data.copy()
        data["is_driver"] = True
        serializer = DriverSerializer(data=data)
        if serializer.is_valid():
            new_driver = serializer.save()
            serialized_driver = DriverSerializer(new_driver)
            return Response(
                {
                    "status": "success",
                    "data": serialized_driver.data
                }
            )

        return Response(
            {
                "status": "failed",
                "message": serializer.errors
            }
        )


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            serialized_user = UserSerializer(new_user)
            return Response(
                {
                    "status": "success",
                    "data": serialized_user.data["id"]
                }
            )

        return Response(
            {
                "status": "failed",
                "message": serializer.errors
            }
        )


class RideRequestView(APIView):
    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            new_ride_request = serializer.save()
            serialized_request = RequestSerializer(new_ride_request)

            return Response(
                {
                    "status": "success",
                    "data": serialized_request.data
                }
            )

        return Response(
            {
                "status": "failed",
                "message": serializer.errors
            }
        )


class RideAcceptView(APIView):
    def post(self, request):
        data = request.data.copy()
        request_obj = Request.objects.get(id=data["ride_id"])
        if (request_obj):
            request_obj.request_driver_id = data["driver_id"]
            request_obj.request_status = "approved"
            request_obj.save()
            return Response(
                {
                    "status": "success",
                    "message": "Ride Accepted"
                }
            )

        return Response(
            {
                "status": "failed",
                "message": "Some unexpected error occurred"
            }
        )


class RideCancelView(APIView):
    def post(self, request):
        data = request.data.copy()
        request_obj = Request.objects.get(id=data["ride_id"])
        if not request_obj.request_status:
            request_obj.request_status = "cancelled"
            request_obj.save()
            return Response(
                {
                    "status": "success",
                    "message": "Ride Cancelled"
                }
            )

        return Response(
            {
                "status": "failed",
                "message": "Some unexpected error occurred"
            }
        )
    

