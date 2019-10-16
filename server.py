from framework.Foundation.bootstrap import Bootstrap
from framework.Foundation.app import Application
from framework.Foundation.Response import Response
import os.path


def app(environ, start_response):
    """Simplest possible application object"""
    path = 'public/' + environ['PATH_INFO']
    if os.path.isfile(path):
        data = bytes(open(path, "rt").read(), 'utf-8')
        return Application.get('response').sendResponse(data, '200')
    return Bootstrap(environ, start_response).run()
