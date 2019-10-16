from jinja2 import Environment, FileSystemLoader, select_autoescape
from framework.Foundation.app import Application


class View:
    def __init__(self):
        file_loader = FileSystemLoader('resources/views')
        self.env = Environment(loader=file_loader,
                               autoescape=select_autoescape(enabled_extensions=('html', 'htm', 'xml'),
                                                            disabled_extensions=(), default_for_string=True, default=False))

    def view(self, name, data=None):
        template = self.env.get_template(name + '.html')
        data = template.render(data=data)
        return Application.get('response').sendResponse(data, '200')
