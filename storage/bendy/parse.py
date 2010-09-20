""":mod:`bendy.parse` --- S-expression parser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import re
import env
from symbol import Symbol 

class Parser(object):
    """The class for parser."""

    def parse(self, tokens):
        """Parse tokens.

        .. sourcecode:: pycon

           >>> parser = Parser()
           >>> tokens = ['(', '+', 1, 2, ')'] 
           >>> parser.parse(tokens)
           [[Symbol('+'), 1, 2]]
        
        :param tokens: a list of tokens
        :type tokens: iterable object
        :returns: a parsed form e.g. :class:`list`, :class:`int`,
                  :class:`long`, :class:`basestring`,
                  :class:`bendy.quote.Quote`, :class:`bendy.symbol.Symbol`

        """
        tokens = list(tokens)
        cnt = 0 
        for t in tokens:
            if type(t) is not Symbol and type(t) is str \
               and re.match(env.SYMBOL_REG,t) is not None:
                tokens[cnt] = Symbol(t)
            cnt += 1
        cnt = 0
        for t in tokens:
            if t == ')':
                parsed, d =  self._parse(tokens[:cnt])
                tokens[cnt - d - 1:cnt + 1] = [parsed]

                return self.parse(tokens)
            cnt += 1

        return tokens

    def _parse(self, token):
        cnt = 0
        for t in token:
            if t == '(':
                start = cnt
            cnt += 1
        parsed = []
        for t in token[start+1:len(token)]:
            parsed.append(t)

        return parsed, len(parsed) 
