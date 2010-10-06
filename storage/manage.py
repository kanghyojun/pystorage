import marshal
import threading 
import struct

from cStringIO import StringIO

import storage.memory
import storage.bendy

import storage.config as config

caches = storage.memory.CacheList()

class BaseManager(threading.Thread):

    def __init__(self):
        self.lock = threading.Lock()

class SaveManager(BaseManager):

    def __init__(self, storage_name="data", page=100):
        self.page = page 
        caches.page = page
        self.file_name = "{0}.st".format(storage_name) 

    def check(self, data):
        r = False
        if int((len(data) / float(self.page)) * 100) >= 70:
            r = True
        return r

    def fill_in(self, data):
        zero_hex = struct.pack("h", 0)
        length = len(data)
        space = (self.page - length) / 2 
        buf = StringIO()
        buf.write(data)
        for x in xrange(1, space + 1):
            buf.write(zero_hex)
        if length % 2 == 1:
            buf.write(zero_hex[0])
        filled = buf.getvalue()
        buf.close()
        return filled

    def _thread(self, store):
        threading.Thread.__init__(self)
        self.store = store

    def run(self):
        binary = self.store.binary()
        with open(self.file_name, "ab") as f:
            f.seek(0)
            f.write(self.fill_in(binary))
        caches.insert(storage.memory.CacheStore(self.store))
        self.store.reset()

class Manager(BaseManager):

    store = storage.memory.Store()
    sav = SaveManager(config.conf["file"], config.conf["page"])

    def __init__(self, sock_conn, addr):
        threading.Thread.__init__(self)
        self.conn = sock_conn 
        self.addr = addr
        print "Connected at {0}".format(self.addr[0])

    def run(self):
        self.conn.send("pystorage 0.1, Type 'help' for more information. you log in {0}\n".format(self.addr[0]))
        while True:
            self.conn.send(">> ")
            cmd = self.conn.recv(2048)
            if cmd.strip() == "exit":
                self.conn.close()
                break
            elif cmd.strip() == "help":
                self.conn.send("some-help-massage")
            elif cmd.strip() == "logging":
                storage.log.logging(self.store.__dict__, caches)
            elif cmd.strip() == '':
                pass
            else:
                try:
                    print "received {0}".format(cmd)
                    evaluated = self.evaluate_cmd(cmd)
                    print repr(evaluated)
                    if evaluated is not None:
                        self.conn.send(evaluated)
                    else:
                        self.conn.send("ok\n")
                    if self.sav.check(self.store.binary()):
                            self.sav._thread(self.store)
                            self.sav.start()
                except Exception as inst: 
                    storage.log.logging(inst, '', "expt")
                    self.conn.send("Error!\n")

    def evaluate_cmd(self, cmd):
        token = storage.bendy.lexer.Lex().tokenize(cmd)
        parsed = storage.bendy.parse.Parser().parse(token)
        envs = storage.bendy.env.get_init_env()
        return storage.bendy.evaluate.evaluate(parsed[0], envs, self.store)
        r_key = parsed[0][1]
        self.lock.acquire()
        if not store.has_key(r_key):
            i, key = caches.has_key(r_key)
            if idx is None and str(parsed[0][0]) != "set!":
                raise Exception("Nonexistence Key :: {0}\n".format(r_key))
            if idx is not None:
                if str(parsed[0][0]) == "get":
                    self.store[key] = caches[i][key]
                del caches[i][key]
                caches[i].changed()
        self.lock.release()

class FileManager(BaseManager):

    def set_cache_storage(self):
        with open("data.st", "rb") as f:
            for x in xrange(0, config.conf["cache"]):
                f.seek(config.conf["page"] * x)
                caches.insert(marshal.loads(f.read(config.conf["page"])))

    def insert(self, p, data):
        with open(config.con["full_file"], "wb+") as f:
            f.seek(p)
        f.write(data.binary())
