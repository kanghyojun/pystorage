""":mod:`storage.run` --- start server program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import time

from optparse import OptionParser

from storage.server import Server
from storage.manage import Manager
from storage.manage import FileManager

opt_parse = OptionParser()
opt_parse.add_option("-p", "--port", type="int", default="7777",
                     help="host to listen [%default]")
opt_parse.add_option("-H", "--host", default="127.0.0.1",
                     help="host to listen [%default]")

(option, args) = opt_parse.parse_args()

def main():
    sv = Server(option.host, option.port)
    store = FileManager().set_cache_storage() 
    sock = sv.get_sock()
    while True:
        conn, addr = sock.accept()
        manager = Manager(conn, addr)
        manager.start()

if __name__ == "__main__":
    main()
