class Response:
    def __init__(self, start_response):
        self.response = start_response

    def sendResponse(self, data, status):
        data = bytes(data, 'utf-16')
        response_headers = [
            ('Content-type', 'text/html'),
            ('Content-Length', str(len(data)))
        ]
        self.response(status, response_headers)
        return iter([data])
