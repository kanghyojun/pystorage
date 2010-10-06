""":mod:`client.bendy.env` --- Bendy Environment Table  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import sys
import operator

SYMBOL_REG = "[^\s\(\)\d\'\"][^\s\(\)\"]+|[^\s\d\'\"\(\)]+"
NUM_REG = "\d+"
STR_REG  = "\"[^\"]*\""


import pystoragefunc as func

class Environment(object):
    """A Lisp Environment. contain primitive environment 
    
    :param parent: a parent Environment
    :type parent: :class:`Environment`

    """
    
    def __init__(self, parent=None):
        self.val = {}
        self.parent = None
        if parent is not None:
            self.parent = parent
    
    def __setitem__(self, key, item):
        self.val[key] = item

    def __getitem__(self, key):
        return self.val[key]

    def get(self, key):
        """Find environment by symbol, get method can find parent environment

        .. sourcecode:: pycon

           >>> parent_env = Environment() 
           >>> parent_env.val 
           {'x': 1, 'y': 2}
           >>> parent_env.get('x')
           1
           >>> child_env = Environment(parent_env)
           >>> child_env.val
           {'y': 2}
           >>> child_env.get('x')
           1

        :param key: a Symbol name which want get value
        :type key: :class:`basestring`
        :returns: a value that correspond with symbol name.
                  if there is no corresponded value, 
                  return find the parents' e.g. :class:`int`,
                  :class:`basestring`, :class:`long`, 
                  :class:`bendy.quote.Quote`,
                  :class:`bendy.runtime.bendylambda.BendyLambda`,
                  :class:`bendy.runtime.bendylet.let`,
                  :class:`bendy.runtime.bendylet.let_seq_eval`,
                  :class:`bendy.logic.bendyif`

        """
        if self.val.has_key(key):
            return self.val[key]
        else:
            return self.parent.get(key)

def get_init_env():
    """Set Initial environment item
    
    .. sourcecode:: pycon

       >>> init_env = get_init_env()
       >>> init_env.val
       {'+': bendy.runtime.arithmetic.addition, ... }

    :returns: a Environment which contains bendy primitive procedure 
              e.g. :class:`bendy.env.Environment`

    """
    envs = Environment()
    envs['set!'] = func.set_value 
    envs['get'] = func.get_value 
    envs['del'] = func.del_value 
    return envs
