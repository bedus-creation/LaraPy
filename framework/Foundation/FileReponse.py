from webob import Request, Response
import mimetypes


class FileReponse:

    @staticmethod
    def is_static(filename):
        return FileReponse().get_mimetype(filename) != None

    def get_mimetype(self, filename):
        type, encoding = mimetypes.guess_type(filename)
        return type

    def make_response(self, filename):
        res = Response(content_type=self.get_mimetype(filename))
        res.body = open(filename, 'rb').read()
        return res
