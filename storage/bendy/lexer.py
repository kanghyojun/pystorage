""":mod:`bendy.lexer` --- Lexer for bendy 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import re
import env

class Lex(object):
    """The Class for Lexer"""

    def __init__(self):
        regexp_list = [
          "[()]",
          env.SYMBOL_REG,
          env.NUM_REG,
          env.STR_REG,
          "'",
        ] 
        regexp = '|'.join(regexp_list)
        self.token_regexp = re.compile(regexp)

    def tokenize(self, source):
        """Make Tokens

        .. sourcecode:: pycon

           >>> src = "(+ 1 (* 2 3))"  
           >>> tokens = Lex().tokenize(src)
           ['(', 1, '(', '*', 2, 3, ')', ')']
        
        :param source: a bendy source 
        :type source: str 
        :returns: a tokens e.g. :class:`list`

        """

        tokenized = []
        for t in self.token_regexp.findall(source):
            if re.match(env.NUM_REG, t) is not None:
                t = int(t)
            elif re.match(env.STR_REG, t) is not None:
                t = str(t) 
            tokenized.append(t)

        return tokenized
