""":mod:`bendy.evaluate` --- Bendy evaluator 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import types
from symbol import Symbol

def evaluate(form, env, mem=None):
    """Bendy evaluatoar evaluate AST(Abstract Syntax Tree)

    .. sourcecode:: pycon

       >>> import bendy.lexer
       >>> import bendy.parse
       >>> import bendy.env
       >>> src = "(+ 1 2)"
       >>> parsed = bendy.parse.Parser().parse(bendy.lexer.Lex().tokenzie(src))[0]
       >>> env = get_init_env()
       >>> evaluate(parsed, env)
       3
       >>> src = "(+ 1 2) (* 2 4)"
       >>> parsed = bendy.parse.Parser().parse(bendy.lexer.Lex().tokenzie(src))
       >>> for p in parsed:
       ...     evaluate(p, env) 
       ... 
       3
       8

    :param form: bendy AST(Abstract Syntax Tree) 
    :type form: a python list
    :param env: bendy Environment
    :type env: bendy Environment
    :returns: if form is int or str, return form itself. 
              if form is special form, return each evaluated speical form. 
              if form is combination, return apply.

    """
    if type(form) is int:
        return form
    if type(form) is str:
        return form[1:len(form) - 1]
    elif type(form) is Symbol:
        key = str(form)
        try:
            return env.get(key)
        except:
            raise Exception("Nonexistent Symbol :: {0}".format(key)) 
    elif type(form) is list:
        args = []
        for arg in form:
            args.append(evaluate(arg, env))

        args.append(mem)
        return apply(args[0], args[1:])

def apply(proc, args):
    """Bendy apply call procedure and execute.

    :param proc: a procedure, which contains in environment(primitive procedure)
                 or user-define-procedure 
    :type proc: a function which can call
    :param args: arguments that procedure's parameter
    :type args: iterable object e.g. :class:`list`

    """
    return proc(*args)

