""":mod:`storage.run` --- start server program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import time
from optparse import OptionParser

from storage.server import Server

opt_parse = OptionParser()
opt_parse.add_option("-s", "--start", action="store_true",
                     help="start the server")
(option, args) = opt_parse.parse_args()

def main():
    if option.start or option.start is None:
        sv = Server()
        conn, addr = sv.get_accept()
        print "Connected by {0}".format(addr)
        while True:
            data = conn.recv(1024)
            print "Server Recived {0}".format(data)
            if data == 'exit':
                break
            conn.send("ok")
        conn.close()
    else:
        print "type with -s option to start server" 

if __name__ == "__main__":
    main()

