import lexer
import parse
import evaluate
import env
import pystoragefunc as func

def get_eval(src, store):
    token = lexer.Lex().tokenize(src)
    parsed = parse.Parser().parse(token)
    envs = get_init_env()
    return evaluate.evaluate(parsed[0], envs, store)

def get_init_env():
    """Set Initial environment item
    
    .. sourcecode:: pycon

       >>> init_env = get_init_env()
       >>> init_env.val
       {'+': bendy.runtime.arithmetic.addition, ... }

    :returns: a Environment which contains bendy primitive procedure 
              e.g. :class:`bendy.env.Environment`

    """
    envs = env.Environment()
    envs['set!'] = func.set_value 
    envs['get'] = func.get_value 
    envs['del'] = func.del_value 
    return envs
