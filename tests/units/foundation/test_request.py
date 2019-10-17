from framework.Foundation.Request import Request
from werkzeug.test import EnvironBuilder
from framework.Foundation.app import Application
import pytest


class TestRequest:
    pathData = [
        ("/index", "index"),
        ("/index?query=asdfsf", "index")
    ]
    @pytest.mark.parametrize("path,uri", pathData)
    def test_uri(self, path, uri):
        Application.bind('env', EnvironBuilder(
            method='GET', path=path).get_environ())
        assert Request.uri() == uri
