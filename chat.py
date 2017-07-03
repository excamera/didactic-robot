import sys
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver

class Chat(LineReceiver):
    def connectionMade(self):
        self.factory.connects.append(self)
    def lineReceived(self, data):
        for prot in self.factory.connects:
            if prot != self:
                prot.sendLine(data)

class ChatFactory(Factory):
    connects=[]
    protocol=Chat

reactor.listenTCP(int(sys.argv[1]), ChatFactory())
reactor.run()
