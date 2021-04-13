# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

#!/usr/bin/env python
"""Tests for `minos` package."""
# pylint: disable=redefined-outer-name

import pytest
import requests
from minos.api_gateway.proxy import MinosProxyHTTP
from minos.api_gateway.exceptions import *


@pytest.mark.server(url='/orders/', response=[{'id': 1}], method='GET')
def test_minos_api_proxy_get():
    """API Proxy GET."""

    proxy_instance = MinosProxyHTTP('http://localhost', 5000)

    params = {'address': 'test'}
    body = {'body': 'data'}

    req = proxy_instance.request(method='GET', path='/orders', params=params, data=body)

    assert req.status_code == 200
    assert req.json() == [{'id': 1}]

def test_minos_api_proxy_get_kwargs():
    """API Proxy GET."""

    proxy_instance = MinosProxyHTTP('http://localhost', 5000, headers={"content-type":"text"})

    params = {'address': 'test'}
    body = {'body': 'data'}

    req = proxy_instance.request(method='GET', path='/orders', params=params, data=body)

    assert req.status_code == 200
    assert req.json() == [{'id': 1}]

@pytest.mark.server(url='/order/', response=[{'id': 1}], method='POST')
def test_minos_api_proxy_post():
    """API Proxy POST."""

    proxy_instance = MinosProxyHTTP('http://localhost', 5000)

    params = {'address': 'test'}
    body = {'body': 'data'}

    req = proxy_instance.request(method='POST', path='/order', params=params, data=body)

    assert req.status_code == 200
    assert req.json() == [{'id': 1}]


@pytest.mark.server(url='/customers/', response=[{'id': 1}], method='PUT')
def test_minos_api_proxy_put():
    """API Proxy PUT."""

    proxy_instance = MinosProxyHTTP('http://localhost', 5000)

    params = {'address': 'test'}
    body = {'body': 'data'}

    req = proxy_instance.request(method='PUT', path='/customers', params=params, data=body)

    assert req.status_code == 200
    assert req.json() == [{'id': 1}]


@pytest.mark.server(url='/customer/', response=[{'id': 1}], method='PATCH')
def test_minos_api_proxy_patch():
    """API Proxy PATCH."""

    proxy_instance = MinosProxyHTTP('http://localhost', 5000)

    params = {'address': 'test'}
    body = {'body': 'data'}

    req = proxy_instance.request(method='PATCH', path='/customer', params=params, data=body)

    assert req.status_code == 200
    assert req.json() == [{'id': 1}]


@pytest.mark.server(url='/cart/', response=[{'id': 1}], method='DELETE')
def test_minos_api_proxy_delete():
    """API Proxy DELETE."""

    proxy_instance = MinosProxyHTTP('http://localhost', 5000)

    params = {'address': 'test'}
    body = {'body': 'data'}

    req = proxy_instance.request(method='DELETE', path='/cart', params=params, data=body)

    assert req.status_code == 200
    assert req.json() == [{'id': 1}]

def test_minos_api_proxy_controlled_exception_unreachable():
    """If no value, raise exception"""

    proxy_instance = MinosProxyHTTP('http://localhost', 5001)

    params = {'address': 'test'}
    body = {'body': 'data'}

    with pytest.raises(MicroserviceUnreacheableError):
        req = proxy_instance.request(method='GET', path='/orders', params=params, data=body)


def test_minos_api_proxy_controlled_exception_timeout():
    """If no value, raise exception"""

    proxy_instance = MinosProxyHTTP('http://localhost', 5001)

    params = {'address': 'test'}
    body = {'body': 'data'}

    with pytest.raises(ApiTimeoutError):

        raise ApiTimeoutError('Throwing an exception here!')
        req = proxy_instance.request(method='GET', path='/orders', params=params, data=body)


def test_minos_api_proxy_controlled_exception_cb():
    """If no value, raise exception"""

    proxy_instance = MinosProxyHTTP('http://localhost', 5001)

    params = {'address': 'test'}
    body = {'body': 'data'}

    with pytest.raises(ApiCircuitBreaker):

        raise ApiCircuitBreaker('Throwing an exception here!')
        req = proxy_instance.request(method='GET', path='/orders', params=params, data=body)
