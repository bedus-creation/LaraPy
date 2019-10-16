from framework.Foundation.app import Application
from config.database import database


class TestDatabaseConfig():

    def test_default_database_config(self):
        Application.bind('database', database)
        assert Application.get('database')['default'] == database['default']
