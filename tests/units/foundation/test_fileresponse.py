from framework.Foundation.FileReponse import FileReponse


class TestFileReponse:
    def test_static_routes(self):
        assert FileReponse.is_static('/index') == False
        assert FileReponse.is_static('/css/app.css') == True
