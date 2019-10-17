from framework.Foundation.bootstrap import Bootstrap
from framework.Foundation.app import Application
from framework.Foundation.Response import Response
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound
import os.path
import os


class Server(object):
    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        return Bootstrap(environ, start_response).run()

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(with_static=True):
    app = Server()
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/':  os.path.join(os.path.dirname(__file__), 'public')
    })
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
