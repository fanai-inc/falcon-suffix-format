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

        self.test_data = {
            'a': 'b',
            'c': 'd',
        }

    def test_response_pickle(self):
        pickled_data = pickle.dumps(self.test_data)

        response = self.simulate_post('/test_endpoint.pkl3', body=pickled_data)

        self.assertEqual(pickled_data, response.content)

        unpickled_data = pickle.loads(response.content)

        self.assertEqual(unpickled_data, self.test_data)

    def test_response_bad_pickle(self):
        not_pickled_data = str(self.test_data)

        response = self.simulate_post('/test_endpoint.pkl3', body=not_pickled_data)

        self.assertEqual(response.status, falcon.HTTP_400)

    def test_response_default(self):
        response = self.simulate_post('/test_endpoint', json=self.test_data)

        self.assertEqual(self.test_data, response.json)
