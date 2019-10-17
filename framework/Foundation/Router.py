import importlib
from framework.Foundation.app import Application
from werkzeug.exceptions import HTTPException
from framework.Foundation.FileReponse import FileReponse


class Router:
    routes = {
        'GET': {},
        'POST': {}
    }

    @staticmethod
    def get(uri, controller):
        Router.routes['GET'][uri.strip('/')] = controller

    @staticmethod
    def post(uri, controller):
        Router.routes['POST'][uri.strip('/')] = controller

    @staticmethod
    def load(file):
        importlib.import_module(file)
        return Router()

    def direct(self, uri, requestType):
        if FileReponse.is_static(uri):
            return FileReponse().make_response("public/"+uri)

        if uri in Router.routes[requestType].keys():
            data = Router.routes[requestType][uri].split('@')
            return self.callAction(data[0], data[1])
        raise HTTPException('Routes not defined yet.')

    def callAction(self, controllerClass, action):
        controller = 'app.Http.Controllers.' + controllerClass
        module = importlib.import_module(controller)
        class_ = getattr(module, controllerClass)
        return getattr(class_(), action)()
