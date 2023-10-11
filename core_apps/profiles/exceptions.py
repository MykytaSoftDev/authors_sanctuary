from rest_framework.exceptions import APIException

class CantFollowYourself(APIException):
    statuscode = 403
    default_detail = "You can't follow yourself."
    default_code = "forbidden"