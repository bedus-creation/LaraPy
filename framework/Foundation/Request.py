from framework.Foundation.app import Application


class Request:
    @staticmethod
    def uri():
        return Application.get('env')['PATH_INFO'].strip('/')

    @staticmethod
    def method():
        return Application.get('env')['REQUEST_METHOD']
