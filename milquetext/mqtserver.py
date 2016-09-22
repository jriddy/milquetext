from twisted.application.internet import TCPServer
from twisted.application.service import Application

from milquetext.mqtfactory import MilquetextFactory


site = MilquetextFactory()
application = Application('Milquetext Email-to-text service')
server = TCPServer(8880, site)
server.setServiceParent(application)
