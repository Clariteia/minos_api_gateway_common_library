# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

"""MinosProxyHTTP is responsible for the communication http(s).

This module is responsible for establishing the connection to the microservice
of the corresponding domain. The circuit breaker pattern is used.

    Typical usage example:
        
        class OrdersMinosApiProxy(MinosApiProxy):
            pass
        
        params = {'address': 'test'}
        body = {'body': 'data'}
        
        foo = OrdersMinosApiProxy(ip, port)
        bar = foo.request(method='GET', url, params=params, data=body)
"""

from abc import ABC, abstractmethod
from ..common.minos_http_client import MinosClientHttp
class MinosProxyHTTP(MinosClientHttp):
    """Class that connects to Redis and returns the configuration values according to domain..

    Attributes:
        base_url: A string which specifies the base url or ip. Example: 127.0.0.1, localhost.
        port: Integer which specifies the port number.
        cb_fail_max: Integer which specifies a Circuit Breaker max fails.
        cb_reset_timeout: Integer which specifies a Circuit Breaker unlock time.
    """
    pass
