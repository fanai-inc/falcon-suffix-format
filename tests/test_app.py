import pickle

import falcon

from falcon import testing

from falcon_suffix_format.handlers import PickleHandler
from falcon_suffix_format.middleware import SetContentType
from falcon_suffix_format.routers import FormatRouter


class TestEndpoint:

    def on_post(self, req, resp):
        """
        Echo endpoint
        """
        resp.media = req.media


class TestApp(testing.TestCase):
    def setUp(self):
        super().setUp()

        self.app = falcon.API(middleware=[SetContentType()], router=FormatRouter())

        self.app.req_options.media_handlers['application/pkl3'] = PickleHandler()
        self.app.resp_options.media_handlers['application/pkl3'] = PickleHandler()

        self.app.add_route('/test_endpoint', TestEndpoint())

    def test_response_pickle(self):
        test_data = {
            'a': 'b',
            'c': 'd',
        }

        pickled_data = pickle.dumps(test_data)

        response = self.simulate_post('/test_endpoint.pkl3', body=pickled_data)

        self.assertEqual(pickled_data, response.content)

        unpickled_data = pickle.loads(response.content)

        self.assertEqual(unpickled_data, test_data)

    def test_response_default(self):
        test_data = {
            'a': 'b',
            'c': 'd',
        }

        response = self.simulate_post('/test_endpoint', json=test_data)

        self.assertEqual(test_data, response.json)
