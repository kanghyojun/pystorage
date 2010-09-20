import threading 
import storage.bendy.program
import storage.memory

store = storage.memory.Store()

class Manager(threading.Thread):
    
    def __init__(self, sock_conn, addr):
        threading.Thread.__init__(self)
        self.conn = sock_conn 
        self.addr = addr
        print "Connected at {0}".format(self.addr[0])

    def run(self):
        self.conn.send("pystorage 0.1, Type 'help' for more information. you log in {0}".format(self.addr[0]))
        try:
            while True:
                cmd = self.conn.recv(2048)
                if cmd.strip() == "exit":
                    self.conn.send("exit server")
                    self.conn.close()
                    break
                elif cmd.strip() == "help":
                    self.conn.send("some-help-massage")
                else:
                    try:
                        evaluated = storage.bendy.program.get_eval(cmd.strip(), store)
                        if evaluated is not None:
                            self.conn.send(evaluated)
                        else:
                            self.conn.send("ok")
                    except Exception as inst:
                        self.conn.send("Error!")
                    
        except KeyboardInterrupt:
            print "exit server"
            self.conn.close()
