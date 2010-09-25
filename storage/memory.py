class Store(object):

    def __new__(cls):
        if not "_the_instance" in cls.__dict__:
            cls._the_instance = object.__new__(cls)
            cls._the_instance.data = {}
        return cls._the_instance

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __delitem__(self, key):
        del self.data[key]
