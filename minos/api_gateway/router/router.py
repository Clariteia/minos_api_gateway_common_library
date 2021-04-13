# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

"""API Router is responsible for obtaining the connection values for each domain name.

This module obtains the IP, port and status of a microservice. Using the domain name,
it performs a http call to discovery service.

    Typical usage example:
        
        r = MinosRouter('test')
        ip, port, name, status = r.get_endpoint_info()
"""

from abc import ABC, abstractmethod
import os
import json
from ..common.minos_http_client import MinosClientHttp
from ..exceptions import exceptions

class MinosRouter(ABC):
    """Class that connects to Discovery Service and returns the configuration values according to domain name.
    
    The connection to Discovery Service is made via the environment variables: DISCOVERY_SERVICE_URL, DISCOVERY_SERVICE_PORT, DISCOVERY_SERVICE_PATH.
    
    Attributes:
        domain: A string which specifies the Domain Name. Example: order, cart, customer ....
    """
    
    def __init__(self, domain: str):
        """Perform initial configuration and connection to Redis"""
        self.domain = domain
        self.discovery_service_url = os.environ.get('DISCOVERY_SERVICE_URL', "http://localhost")
        self.discovery_service_port = os.environ.get('DISCOVERY_SERVICE_PORT', 5000)
        self.discovery_service_path = os.environ.get('DISCOVERY_SERVICE_PATH', 'discover')
        
    def get_endpoint_info(self) -> str:
        """Retrieves ip, port, name, status from Discovery Service.

        Retrieves connection data for specified Domain Name.

        Returns:
            ip: IP adress or url with http(s) protocol
            port: Port number
            name: name of domain model
            status: Check health

        Raises:
            Exception: An error occurred retrieving data.
        """
        
        try:
            cli = MinosClientHttp(self.discovery_service_url, self.discovery_service_port)
            params = {'domain': self.domain}
            request = cli.request('GET', self.discovery_service_path, params=params)
            json_data = request.json()
        except Exception as ex:
            print('Error:', ex)
        
        return json_data['ip'], json_data['port'], json_data['name'], json_data['status']



