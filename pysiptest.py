import socket
import pysipcall
#import sys

class PySipTest:

    def SendMessage(self, msg):
        print "sending message %s" % msg
        sent = self.sock.sendto(msg, self.client_address)
        return sent

    def SetStateHandler(self, handler):
        self.state_handler = handler
        return

    def DoNothing(self):
        print ">>> DoNothing function"
        return

    def LoadPattern(self, filename):
        with open(filename, 'r') as myfile:
            message = myfile.read()
        myfile.close()
        message = self.pysipcall.Substitute(message)
        message = self.pysipcall.ConvertEOLs(message)
        return message

    def Process(self):
        self.scenario.Transition_Start(self)
        try:
            while True:
                # Receive response
                #print 'waiting to receive'
                data, server = self.sock.recvfrom(4096)
                print 'received "%s"' % data
                self.state_handler(self, 'message', data)
        except KeyboardInterrupt:
            print 'Keyboard Interrupt\nExiting'

        return

    def SetClientAddress(self, host, port):
        self.client_address = (host, port)
        return

    def __init__(self, host, port, scenario):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (host, port)
        self.SetClientAddress(host, port)
        self.sock.bind(self.server_address)
        self.scenario = scenario
        self.SetStateHandler(self.DoNothing)
        self.pysipcall = pysipcall.PySipCall(self)
        return

    def __del__(self):
        print 'Destructor'
        self.sock.close()
