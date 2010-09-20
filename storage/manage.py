import threading 

class Manager(threading.Thread):
    
    def __init__(self, sock_conn, addr):
        threading.Thread.__init__(self)
        self.conn = sock_conn 
        self.addr = addr
        print "Connected at {0}".format(self.addr[0])

    def run(self):
        self.conn.send("pystorage 0.1, Type 'help' for more information. you log in {0}".format(self.addr[0]))
        while True:
            cmd = self.conn.recv(2048)
            if cmd.strip() == "exit":
                self.conn.send("exit server")
                self.conn.close()
                break
            elif cmd.strip() == "help":
                self.conn.send("some-help-massage")
            else:
                self.conn.send("ok")
