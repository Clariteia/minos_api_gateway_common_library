# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

#!/usr/bin/env python
"""Tests for `minos` package."""
# pylint: disable=redefined-outer-name
import datetime
import requests
import time
import pytest
from . import mock_server

from minos.api_gateway.proxy import MinosProxyHTTP

FAILURES = 3
TIMEOUT = 6

class OrdersMinosApiProxy(MinosProxyHTTP):
    pass

proxy_instance = OrdersMinosApiProxy("localhost", 5000)

@pytest.mark.skip(reason="no way of currently testing this")
def circuit_breaker_test(iterations=10, delay=1, url="localhost", port=5000):
    for i in range(iterations):
        try:
            req = proxy_instance.request(method='GET', path='test')
            print(req)
            #get_greeting(url, port)
        except:
            pass

        time.sleep(delay)


if __name__ == "__main__":
    print("Server is turned OFF...")
    circuit_breaker_test()

    print("Server is turning ON...")
    with mock_server.app.run("localhost", 5000):
        print(mock_server.app)
        circuit_breaker_test()
