# ride-request-api

This is a Django application for a ride-request service. It allows users to register as user, riders, request rides, accept ride requests, and add reviews for riders. Below you will find the details of the application and the API endpoints.

## Installation

1. Clone the repository:

```git clone git@github.com:bbhupen/ride-request-api.git```


2. Install the dependencies:

```pip install -r requirements.txt```


3. Run the migrations:

```python manage.py migrate```

4. Start the development server:

```python manage.py runserver```


5. Access the application at [http://localhost:8000](http://localhost:8000)

## API Endpoints

The following API endpoints are available for interacting with the application:
```Please check the file located on base/helpers/constants.py for updated API enpoints```

1. ```POST /register``` Registers a new user (rider).

Sample Request:

```json
{
    "username": "rapidoRider0",
    "email": "rapidoRider@test.com",
    "password": "password"
}
```
Sample Response
```json
{
    "message": "success",
    "data": {
        "user": {
            "id": 24,
            "username": "rapidoRider0",
            "email": "rapidoRider@test.com"
        },
        "token": "618d685d4891c0b1255bb6e0858a9dbb60a2b687"
    }
}
```

2. ```POST /login``` Logs in a user (rider) and returns an authentication token.

Sample Request
```json
{
    "username": "username",
    "password": "password"
}

```
Sample Response:

```json
{
    "status": "success",
    "data": {
        "user": 25,
        "token": "c3f0926c3b83758c3a871543a300e04446336368"
    }
}
```

3. ```POST /api/register-driver``` Registers a new driver.

Sample Request
```json 
{
    "driver_vehicle": "Swift Desire 2",
    "user": "14",
    "driver_license_no": "AS09-2255",
    "is_driver": true
}
```
Sample Response
```json
{
  {
    "status": "success",
    "data": {
        "id": 5,
        "is_driver": true,
        "driver_vehicle": "Swift Desire 2",
        "driver_license_no": "AS09-2255",
        "user": 25
    }
}
```

4. ```POST /api/ride/request``` Creates a new ride request.

Sample Request
```json
{
    "request_user_id": 2,
    "request_pickup_location": "Jalukbari",
    "request_drop_location": "Guwahati 7th Mile",
    "request_status": "pending"
}
```
Sample Response
```json 
{
    "status": "success",
    "data": {
        "id": 2,
        "request_user_id": 22,
        "request_pickup_location": "Jalukbari",
        "request_drop_location": "Guwahati 7th Mile",
        "request_status": "pending"
    }
}

```

5. ```POST /api/ride/accept``` Accepts a ride request.

Sample Request

```json
{
    "ride_id": 1,
    "driver_id": 2
}

```
Sample Response
```json
{
    "status": "success",
    "message": "Ride Accepted"
}

```

6. ```POST /api/ride/start``` Starts a ride request.

Sample Request

```json
{
    "ride_id": 1,
    "driver_id": 2
}

```
Sample Response
```json
{
    "status": "success",
    "message": "Ride Started"
}

```

7. ```POST /api/ride/end``` Ends a ride request.

Sample Request

```json
{
    "ride_id": 1,
    "driver_id": 2
}

```
Sample Response
```json
{
    "status": "success",
    "message": "Ride Ended"
}

```

8. ```POST /api/ride/complete``` Completes a ride request.

Sample Request

```json
{
    "ride_id": 1,
    "driver_id": 2
}

```
Sample Response
```json
{
    "status": "success",
    "message": "Ride Completed"
}

```

9. ```GET api/ride/history``` View ride history of either driver or user at a time

Sample Params

```driver_id for driver ride history and ride id for user_id for user ride history```

Sample Response
```json
{
  "status": "success",
      "data": [
      {
          "id": 1,
          "request_driver_id": "22",
          "request_pickup_location": "Jalukbari",
          "request_drop_location": "Guwahati 7th Mile",
          "request_status": "approved",
          "request_user_id": 21
      },
      {
          "id": 4,
          "request_driver_id": "22",
          "request_pickup_location": "Jalukbari",
          "request_drop_location": "Guwahati 7th Mile",
          "request_status": "approved",
          "request_user_id": 22
        }
    ]
}

```

10. ```POST /api/review/add``` Adds a review for a driver.

Sample Request
```json
{
    "review_driver_id": 22,
    "review_user_id": 2,
    "review_text": "Very Professional",
    "review_stars": 4
}
```
Sample Response
```json
{
    "status": "success",
    "data": {
        "id": 3,
        "review_driver_id": "22",
        "review_user_id": "1",
        "review_text": "Very Professional",
        "review_stars": "4"
    }
}
```

11. ```GET /api/review/view``` Retrieves reviews for a driver.

Sample Params

```?review_driver_id=22```

Sample Response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "review_driver_id": "22",
            "review_user_id": "21",
            "review_text": "Professional",
            "review_stars": "3"
        },
        {
            "id": 2,
            "review_driver_id": "22",
            "review_user_id": "21",
            "review_text": "Very good driver",
            "review_stars": "4"
        }
    ]
}

```
12. ```POST /api/ride/cancel``` Cancels a ride.

Sample Request
```json
{
    "ride_id": 2
}

```

Sample Response
```json
{
    "status": "success",
    "message": "Ride Cancelled"
}

```

## Authentication Mechanism:

1. Token Authentication:
   - The code imports the necessary modules for token authentication: `from rest_framework.authtoken.serializers import AuthTokenSerializer` and `from rest_framework.authtoken.models import Token`.
   - The `LoginView` class handles the login functionality. When a user sends a POST request with valid credentials, it generates a token using `AuthTokenSerializer` and associates it with the user.
   - The generated token is then returned in the response, allowing the user to include it in subsequent requests as a means of authentication.

2. Permission Classes:
   - The code uses permission classes provided by DRF to enforce authentication on certain views. The `IsAuthenticated` class is used as the permission class, which ensures that only authenticated users can access the views decorated with it.
   - The `permission_classes` attribute is defined within each view class to specify the required permissions.

3. User Registration:
   - The `UserView` class handles user registration. It uses a custom serializer (`RegisterSerializer`) to validate and create new user accounts.
   - After successful registration, a token is generated for the user using `Token.objects.get_or_create(user=user)`. The token is then returned in the response along with the user data.

4. Authentication in Routes:
   - After successfull login or registrations a user receives the token, which can be stored on the local storage or somewhere. Which later needs to be passed on to the Header with `Token <token>` on the authenticated request routes. 
   - Only requests with valid tokens will be allowed access.
