# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

"""MinosClientHttp is responsible for the communication http(s).

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
from .minos_client import MinosClient
from ..exceptions import *
import requests
import pybreaker

class MinosClientHttp(MinosClient):
    """Class that connects to Redis and returns the configuration values according to domain..

    Attributes:
        base_url: A string which specifies the base url or ip. Example: 127.0.0.1, localhost.
        port: Integer which specifies the port number.
        cb_fail_max: Integer which specifies a Circuit Breaker max fails.
        cb_reset_timeout: Integer which specifies a Circuit Breaker unlock time.
    """
    
    def __init__(self, base_url: str, port: int, cb_fail_max: int=3, cb_reset_timeout: int=6, **kwargs):
        self.breaker = self.initialize_circuitbreaker(cb_fail_max,cb_reset_timeout)
        
        self.base_url = ":".join((base_url, str(port))) if port != None else base_url

        self.session = requests.Session()
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])
    
    def request(self, method:str, path:str, timeout: int=12, **kwargs) -> str:
        """Performs http(s) request.

        Retrieves rows pertaining to the given keys from the Table instance
        represented by table_handle.  String keys will be UTF-8 encoded.

        Args:
            method: GET, PUT, POST, DELETE, PATCH.
            path: Path according to the domain name. Example: order, customer...
            timeout: Maximum timeout to terminate the connection if no response is received.

        Returns:
            The requests.Response() Object contains the server's response to the HTTP request.
            Read more: https://www.w3schools.com/python/ref_requests_response.asp
            example:
            
            {'firstname': 'John', 'lastname': 'Doe'}

            The above example has used requests.Response().json() to get the response in JSON format.

        Raises:
            ApiTimeoutError: An error occurred due to the timeout.
            ApiConnectionError: An error occurred due to connection problems.
            ApiCircuitBreaker: An error occurred related to circuitbreaker.
        """
        
        try:
            url = "/".join((self.base_url,path))
            
            request = self.breaker.call(
                self.session.request,
                method=method,
                url=url,
                timeout=timeout,
                **kwargs
            )
            
        except requests.exceptions.Timeout:
            raise ApiTimeoutError(
                "The request to {} took too long".format(url)
            )
        except pybreaker.CircuitBreakerError:
            raise ApiCircuitBreaker(
                "Requests are closed because of too many failures {}".format(url)
            )
        except requests.exceptions.ConnectionError:
            raise ApiConnectionError(
                "Failed to establish connection to {}.".format(url)
            )
        
        return request
        
    @staticmethod
    def __deep_merge(source, destination):
        """Merge arguments"""
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RequestsApi.__deep_merge(value, node)
            else:
                destination[key] = value
        return destination