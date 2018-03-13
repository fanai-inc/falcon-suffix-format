import pickle

from falcon.media import BaseHandler


class PickleHandler(BaseHandler):
    def deserialize(self, raw):
        return pickle.loads(raw)

    def serialize(self, media):
        return pickle.dumps(media)
