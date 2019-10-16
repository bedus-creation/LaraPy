class Application:
    registry = {}

    @staticmethod
    def bind(key, value):
        Application.registry[key] = value

    @staticmethod
    def get(key):
        if key in Application.registry.keys():
            return Application.registry[key]
        raise Exception('Key is not binded in container')
