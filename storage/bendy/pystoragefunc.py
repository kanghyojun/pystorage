def set_value(key, value, store):
    store[key] = value
    return;

def get_value(key, store):
    try:
        return store[key]
    except KeyError:
        raise Exception("storage.memory.Store Error:: {0} is nonexistent key".format(key))

def del_value(key, store):
    try:
        del store[key]
    except KeyError:
        raise Exception("storage.memory.Store Error:: {0} is nonexistent key".format(key))
    return;
