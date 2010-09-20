""":mod:`bendy.symbol` --- Symbol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
class Symbol(object):
    """The symbol for bendy

    .. sourcecode:: pycon

       >>> Symbol('x')
       x
    
    :param sym: a symbol name
    :type sym: str e.g. :class:`str`
    
    """


    def __init__(self, sym):
        self.sym = sym

    def __str__(self):
        return str(self.sym)
