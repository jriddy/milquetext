import json

from twisted.internet import defer
from twisted.web.resource import Resource
from twisted.web.server import Site


class SendMessage(Resource):
    isLeaf = True

    def render_PUT(self, request):
        pass


class MilquetextFactory(Site):

    def __init__(self):
        self.resource = Resource()
        self.resource.putChild('send', SendMessage)

    def _logDateTimeCall(self):
        pass
