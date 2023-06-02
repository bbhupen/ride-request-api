apiRoutesData = ({
    "message": "please access the routes below",
    "data": {
        "POST /register": {
            "Sample request": {
                "username": "rapidoRider0",
                "email": "rapidoRider@test.com",
                "password": "password"
            },
            "Sample response": {
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
        },

        "POST /login": {
            "Sample Request": {
                "username": "username",
                "password": "password"
            },
            "Sample Response": {
                "status": "success",
                "data": {
                    "user": 25,
                    "token": "c3f0926c3b83758c3a871543a300e04446336368"
                }
            }
        },

        "POST /api/register-driver": {
            "Sample Request": {
                "driver_vehicle": "Swift Desire 2",
                "user": "14",
                        "driver_license_no": "AS09-2255",
                        "is_driver": True
            },
            "Sample Response": {
                "status": "success",
                "data": {
                    "id": 5,
                    "is_driver": True,
                    "driver_vehicle": "Swift Desire 2",
                    "driver_license_no": "AS09-2255",
                    "user": 25
                }
            }
        },

        "POST /api/ride/request": {
            "Sample Request": {
                "request_user_id": 2,
                "request_pickup_location": "Jalukbari",
                "request_drop_location": "Guwahati 7th Mile",
                "request_status": "pending"
            },
            "Sample Response": {
                "status": "success",
                "data": {
                    "id": 2,
                    "request_user_id": 22,
                    "request_pickup_location": "Jalukbari",
                    "request_drop_location": "Guwahati 7th Mile",
                    "request_status": "pending"
                }
            }
        },

        "POST /api/ride/accept": {
            "Sample Request": {
                "ride_id": 1,
                "driver_id": 2
            },
            "Sample Response": {
                "status": "success",
                "message": "Ride Accepted"
            }
        },

        "POST /api/review/add": {
            "Sample Request": {
                "review_driver_id": 22,
                "review_user_id": 2,
                "review_text": "Very Professional",
                "review_stars": 4
            },
            "Sample Response": {
                "status": "success",
                "data": {
                    "id": 3,
                    "review_driver_id": "22",
                    "review_user_id": "1",
                    "review_text": "Very Professional",
                    "review_stars": "4"
                }
            }
        },

        "GET /api/review/view": {
            "Sample Params": "?review_driver_id=22",
            "Response": {"status": "success",
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
                         ]}
        },
        "POST /api/ride/cancel": {
            "Sample Request": {
                "ride_id": 2
            },
            "Sample Response": {
                "status": "success",
                "message": "Ride Cancelled"
            }
        },
        "POST /api/ride/cancel": {
            "Sample Params": "driver_id for driver ride history and ride id for user_id for user ride hitory",
            "Sample Response": {
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
        }
    }
})
