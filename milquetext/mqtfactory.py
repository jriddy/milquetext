import json

from twisted.internet import defer
from twisted.web.resource import Resource
from twisted.web.server import Site


class SendMessage(Resource):
    isLeaf = True

    def render_GET(self, request):
        request.setResponseCode(403, message='Forbidden')

    def render_PUT(self, request):
        request.setHeader('Content-Type', 'application/json')
        request.setResponseCode(501, 'Coming Soon')
        request.write(json.dumps({'error': 'NotImplemented'}))
        request.finish()


class MilquetextFactory(Site):

    def __init__(self):
        self.resource = Resource()
        self.resource.putChild('send', SendMessage)

    def _logDateTimeCall(self):
        pass
