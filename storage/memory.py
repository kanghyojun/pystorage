import marshal

import storage.log 
import storage.manage

import storage.config as config

class BaseStore(object):

    def binary(self):
        return marshal.dumps(self.data)

class Store(BaseStore):

    def __new__(cls):
        if not "_the_instance" in cls.__dict__:
            cls._the_instance = object.__new__(cls)
            cls._the_instance.data = {}
        return cls._the_instance

    def __setitem__(self, key, value):
        self.data[key] = value
        storage.log.logging(self.__dict__, '')

    def __getitem__(self, key):
        return self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    def reset(self):
        self.data = {}

class CacheStore(BaseStore):

    def __init__(self, data={}):
        self.data = data 
        self.has_changed = False
    
    def __getitem__(self, key):
        return self.data[key]

    def __delitem__(self, key):
        self.changed()
        del self.data[key]

    def has_key(self, key):
        return self.data.has_key(key)

    def changed(self):
        self.has_changed = True

class CacheList(object):

    cache_list_size = config.conf["cache"] 
    page = config.conf["page"] 

    def __new__(cls):
        if not "_the_instance" in cls.__dict__:
            cls._the_instance = object.__new__(cls)
            cls._the_instance.data_list = [] 
            cls._the_instance.count = 0
        return cls._the_instance

    def __setitem__(self, index, value):
        storage.log.logging('', value) 
        self.data_list[index] = value

    def __getitem__(self, index):
        return self.data_list[index]
    
    def insert(self, value):
        self.count += 1
        if self.count > self.cache_list_size:
            self.pop()
        self.data_list.insert(0, value)
        storage.log.logging('', self.data_list) 

    def pop(self):
        return;
        poped_data = self.data_list.pop()
        length = len(self.data_list)
        if poped_data.has_changed:
            storage.manage.FileManager().insert( \
              cache_list_size * page, \
              poped_data \
            )

    def has_key(self, key):
        for i, d in enumerate(self.data_list):
            if d.has_key(key):
                return i, key
        return None, key 
