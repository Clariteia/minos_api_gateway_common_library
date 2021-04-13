# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

#!/usr/bin/env python
"""Tests for `minos` package."""
# pylint: disable=redefined-outer-name

import json
import pytest
from minos.api_gateway.router import MinosRouter

def test_minos_api_router_controlled_exception():
    """If no value, raise exception"""

    r = MinosRouter('non_existing_endpoint')

    with pytest.raises(Exception):
        ip, port, name, status = r.get_endpoint_info()

@pytest.mark.server(url='/discover/', response={'ip': 'http://localhost', 'port': 5000, 'name': 'test', 'status': True}, method='GET')
def test_minos_api_router_get_correct_value():
    """Check if return correct values"""

    r = MinosRouter('test')

    ip, port, name, status = r.get_endpoint_info()

    assert name == 'test'
