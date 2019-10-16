from framework.Foundation.bootstrap import Bootstrap
from framework.Foundation.app import Application
from framework.Foundation.Response import Response


def app(environ, start_response):
    """Simplest possible application object"""
    return Bootstrap(environ, start_response).run()
    Bootstrap(environ, start_response).run()
    return Application.get('response').sendResponse('this is fine', '200')
