# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

class MicroserviceUnreacheableError(Exception):
    """
    Base exception for any errors in the API layer
    """

    pass

class ApiConnectionError(MicroserviceUnreacheableError):
    """
    Communication with the API failed
    """

    pass


class ApiTimeoutError(MicroserviceUnreacheableError):
    """
    Communication with the API timed out
    """

    pass


class ApiResponseDecodeError(MicroserviceUnreacheableError):
    """
    We failed to properly decode the response from the API
    """

    pass


#class ApiResponseError(MicroserviceUnreacheableError):
#    """
#    The API responded with an error
#    """
#
#    def __init__(self, message, status_code):
#        self.status_code = status_code
#        return super().__init__(message)
#
#
#class ApiResponseErrorList(ApiResponseError):
#    """
#    The API responded with a list of errors,
#    which are included in self.errors
#    """
#
#    def __init__(self, message, status_code, errors):
#        self.errors = errors
#        return super().__init__(message, status_code)


class ApiCircuitBreaker(MicroserviceUnreacheableError):
    pass