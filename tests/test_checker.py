from unittest import TestCase
from checker.checker import get_instance_url_from_params, _construct_url


class TestEnginesChecker(TestCase):

    def test_params_parsing(self):
        self.assertEqual(get_instance_url_from_params(['check_engines_results.py', 'localhost']), 'localhost')
        self.assertRaises(SystemExit, get_instance_url_from_params, ['check_engines_results.py'])
        self.assertRaises(SystemExit, get_instance_url_from_params, ['check_engines_results.py', 'localhost', '8888'])

    def test_query_sent(self):
        self.assertIn('http://localhost/', _construct_url('http://localhost', 'test', 'go'))
        self.assertIn('format=json', _construct_url('http://localhost', 'test', 'go'))
        self.assertIn('q=%21go+test', _construct_url('http://localhost', 'test', 'go'))
