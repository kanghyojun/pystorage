""":mod:`storage.server` --- Pystorage server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: make a socket connection

"""

import socket

class Server(object):
    """a Server, make connections

    :param host: server host address, default is localhost
    :type host: :class:`basestring`
    :param port: server port number, default is 7777
    :type port: :class:`int`

    """

    def __init__(self, host="", port=7777):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_sock(self):
        """ return socket accept 

        :returns: socket accept

        """
        try:
            self.s.bind((self.host, self.port))
        except socket.error:
            print "storage.server error :: Address already used"
            self.s.close()
        self.s.listen(2)
        return self.s
