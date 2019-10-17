from Chamak.Foundation.app import Application
from Chamak.view.view import View


class HomeController:
    def index(self):
        return View().view('index')

    def contact(self):
        return Application.get('response').sendResponse('<h1>This is html elements.</h1>', '200')
