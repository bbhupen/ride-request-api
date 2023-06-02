from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RequestSerializer, DriverSerializer, ReviewSerializer, RegisterSerializer, RideHistorySerializer
from .models import Request, Review, Request, Driver
from .helpers.constants import apiRoutesData


class HomeView(APIView):

    def get(self, request):
        return Response(
            apiRoutesData
        )

# Register User


class UserView(APIView):
    serializer_class = RegisterSerializer

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        return {"request": self.request}

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "success",
            "data": {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": token.key
            }

        })


# Login
class LoginView(APIView):

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'status': 'success',
                'data': {
                    'user': user.id,
                    'token': token.key
                }
            }
        )

# Apply for driver


class ApplyDriver(APIView):

    permission_classes = [IsAuthenticated]

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


# Ride Request
class RideRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        serializer = RequestSerializer(data=request.data)

        try:
            driver_obj = Driver.objects.get(user=data['request_user_id'])
            if (driver_obj.is_driver):
                return Response(
                    {
                        "status": "failed",
                        "message": "some unexpected error occurred"
                    }
                )
        except Driver.DoesNotExist:
            pass


        if serializer.is_valid():
            new_ride_request = serializer.save()
            
            #
            # some FUNCTION which sends the ride request to the drivers near to the pickup location using somekind of notification system
            # Logic of the function
            # func(ride_id):
            #       sort all drivers who are currently in is_driving=False state, according to the distance from the pickup location
            #       distance might be calculate using some libraries
            #       driver closest to the pickup location will get the request first
            #       driver can accept or pass using 'api/ride/accept or using some pass function respectively'
            #

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


# Ride Accept
class RideAcceptView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        request_obj = Request.objects.get(id=data["ride_id"])
        driver_obj = Driver.objects.get(user=data['driver_id'])
        if (request_obj and driver_obj.driver_is_active == True and driver_obj.driver_is_driving == False):

            request_obj.request_driver_id = data["driver_id"]
            request_obj.request_status = "approved"
            driver_obj.driver_is_driving = True

            driver_obj.save()
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

# Ride Start


class RideStartView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        request_obj = Request.objects.get(id=data["ride_id"])

        if (request_obj.request_status == "approved"):

            request_obj.request_status = "active"
            request_obj.save()
            return Response(
                {
                    "status": "success",
                    "message": "Ride Started"
                }
            )

        return Response(
            {
                "status": "failed",
                "message": "Some unexpected error occurred"
            }
        )


# Ride End
class RideEndView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        request_obj = Request.objects.get(id=data["ride_id"])
        driver_obj = Driver.objects.get(user=data['driver_id'])
        if (request_obj.request_status == "active" and driver_obj.driver_is_active == True and driver_obj.driver_is_driving == True):

            request_obj.request_status = "ended"
            driver_obj.driver_is_driving = False

            driver_obj.save()
            request_obj.save()
            return Response(
                {
                    "status": "success",
                    "message": "Ride Ended"
                }
            )

        return Response(
            {
                "status": "failed",
                "message": "Some unexpected error occurred"
            }
        )


# Ride Cancel
class RideCancelView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        request_obj = Request.objects.get(id=data["ride_id"])

        if 'driver_id' in data:
            driver_obj = Driver.objects.get(user=data['driver_id'])

        # executes when the user cancels before any driver approves the ride request
        if (request_obj.request_status == "pending"):

            request_obj.request_status = "cancelled"
            request_obj.save()
            return Response(
                {
                    "status": "success",
                    "message": "Ride Cancelled"
                }
            )

        # executes when the user cancels after any driver approves the ride request
        if (request_obj.request_status == "approved" and driver_obj.driver_is_active == True and driver_obj.driver_is_driving == True):

            request_obj.request_status = "cancelled"
            driver_obj.driver_is_driving = False

            driver_obj.save()
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

# Ride Complete


class RideCompleteView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        request_obj = Request.objects.get(id=data["ride_id"])
        driver_obj = Driver.objects.get(user=data['driver_id'])
        if (request_obj.request_status == "active" and driver_obj.driver_is_active == True and driver_obj.driver_is_driving == True):

            request_obj.request_status = "completed"
            driver_obj.driver_is_driving = False

            driver_obj.save()
            request_obj.save()
            return Response(
                {
                    "status": "success",
                    "message": "Ride Completed"
                }
            )

        return Response(
            {
                "status": "failed",
                "message": "Some unexpected error occurred"
            }
        )


# Ride End
class RideEndView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        request_obj = Request.objects.get(id=data["ride_id"])
        driver_obj = Driver.objects.get(user=data['driver_id'])
        if (request_obj.request_status == "active" and driver_obj.driver_is_active == True and driver_obj.driver_is_driving == True):

            request_obj.request_status = "ended"
            driver_obj.driver_is_driving = False

            driver_obj.save()
            request_obj.save()
            return Response(
                {
                    "status": "success",
                    "message": "Ride Ended"
                }
            )

        return Response(
            {
                "status": "failed",
                "message": "Some unexpected error occurred"
            }
        )


# Add Review
class AddReviewView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            new_review = serializer.save()
            serialized_review = ReviewSerializer(new_review)

            return Response(
                {
                    "status": "success",
                    "data": serialized_review.data
                }
            )


# View Reviews
class ReviewView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        review_driver_id = request.GET.get('review_driver_id')

        if (review_driver_id):
            reviews = Review.objects.filter(review_driver_id=review_driver_id)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(
                {
                    "status": "success",
                    "data": serializer.data
                }
            )

        return Response(
            {
                "status": "failed",
                "data": 'review_driver_id is required'
            }
        )


class RideHistoryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        driver_id = request.GET.get('driver_id')
        user_id = request.GET.get('user_id')

        if (driver_id and user_id):
            return Response(
                {
                    "status": "failed",
                    "data": "Some unexpected error occurred"
                }
            )

        if (driver_id):
            ride_history = Request.objects.filter(request_driver_id=driver_id)
            serializer = RideHistorySerializer(ride_history, many=True)
            return Response(
                {
                    "status": "success",
                    "data": serializer.data
                }
            )

        if (user_id):
            ride_history = Request.objects.filter(request_user_id=user_id)
            serializer = RideHistorySerializer(ride_history, many=True)
            return Response(
                {
                    "status": "success",
                    "data": serializer.data
                }
            )

        return Response(
            {
                "status": "failed",
                "data": "Some unexpected error occurred"
            }
        )
