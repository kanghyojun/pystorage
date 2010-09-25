""":mod:`storage.run` --- start server program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import time
from optparse import OptionParser

from storage.server import Server
from storage.manage import Manager

opt_parse = OptionParser()
opt_parse.add_option("-s", "--start", action="store_true",
                     help="start the server")
(option, args) = opt_parse.parse_args()

def main():
    if option.start or option.start is None:
        sv = Server()
        sock = sv.get_sock()
        while True:
            conn, addr = sock.accept()
            manager = Manager(conn, addr)
            manager.start()
    else:
        print "type with -s option to start server" 

if __name__ == "__main__":
    main()

