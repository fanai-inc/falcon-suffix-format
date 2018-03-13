import pickle

from falcon.errors import HTTPBadRequest
from falcon.media import BaseHandler


class PickleHandler(BaseHandler):
    def deserialize(self, raw):
        try:
            return pickle.loads(raw)
        except pickle.UnpicklingError:
            raise HTTPBadRequest(
                'Invalid pickle',
                'Could not parse given pickle')

    def serialize(self, media):
        return pickle.dumps(media)
