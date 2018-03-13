import pickle

import falcon

from falcon import testing

from falcon_suffix_format.handlers import PickleHandler
from falcon_suffix_format.middleware import SetContentType
from falcon_suffix_format.routers import FormatRouter


TEST_DATA = {
    'a': 'b',
    'c': 'd',
}


class TestEndpoint:

    def on_post(self, req, resp):
        """
        Echo endpoint
        """
        if req.params.get('check_test_data'):
            assert req.media == TEST_DATA
        resp.media = req.media


class TestApp(testing.TestCase):
    def setUp(self):
        super().setUp()

        self.app = falcon.API(
            middleware=[SetContentType()],
            router=FormatRouter())

        self.app.req_options.media_handlers['application/pkl3'] \
            = PickleHandler()
        self.app.resp_options.media_handlers['application/pkl3'] \
            = PickleHandler()

        self.app.add_route('/test_endpoint', TestEndpoint())

    def test_response_pickle(self):
        pickled_data = pickle.dumps(TEST_DATA)

        request_params = {
            'check_test_data': True,
        }

        response = self.simulate_post(
            '/test_endpoint.pkl3', body=pickled_data, params=request_params)

        self.assertEqual(pickled_data, response.content)

        unpickled_data = pickle.loads(response.content)

        self.assertEqual(unpickled_data, TEST_DATA)

    def test_response_bad_pickle(self):
        not_pickled_data = str(TEST_DATA)

        response = self.simulate_post(
            '/test_endpoint.pkl3', body=not_pickled_data)

        self.assertEqual(response.status, falcon.HTTP_400)

    def test_response_default(self):
        request_params = {
            'check_test_data': True,
        }

        response = self.simulate_post(
            '/test_endpoint', json=TEST_DATA, params=request_params)

        self.assertEqual(TEST_DATA, response.json)

    def test_response_json(self):
        request_params = {
            'check_test_data': True,
        }

        response = self.simulate_post(
            '/test_endpoint.json', json=TEST_DATA, params=request_params)

        self.assertEqual(TEST_DATA, response.json)

    def test_bad_format(self):
        response = self.simulate_post('/test_endpoint.badformat')

        self.assertEqual(response.status, falcon.HTTP_415)
