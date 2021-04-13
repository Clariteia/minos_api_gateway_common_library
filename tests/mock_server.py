from http_server_mock import HttpServerMock
import requests
import pytest

app = HttpServerMock(__name__)

@pytest.mark.skip(reason="no way of currently testing this")
@app.route("/test/", methods=["GET"])
def index():
    ''' Main index page endpoint '''
    print("INSIDE /test route")
    return [{'id': 1}]
