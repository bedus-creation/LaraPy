from framework.Foundation.app import Application
from config.app import config
import pytest
import sys
import importlib


class TestApp():

    def test_key_value_can_bind_to_container(self):
        Application.bind('config', "data")
        assert Application.get('config') == 'data'

    def test_expection_is_thrown_if_undefined_key_is_asked(self):
        with pytest.raises(Exception):
            Application.get('nokey')

    def test_bind_function(self):
        Application.bind('config', config)
        assert Application.get('config')['basePath'] == '/path'
