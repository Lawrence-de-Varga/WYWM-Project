####################################### Decorator Functions ###################################################

import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug
 
# NOTE for myself applying should_i_exit to a function with the @should_i_exit syntax is equivalent to 
# decorated_func = should_i_exit(objects)(decorated_func) for example with update_knights
# update_knights = should_i_exit(knights)(update_knights)
# Which then reduces to update_knights = func_wrapper(update_knights)
def should_i_exit(objects):
    """ A number of functions need to check whether knights or some other dict or list is empty
         and whether they have been passed 'exit' as input by the user, the decorator below
         keeps that code out of those functions"""
    def func_wrapper(function):
        def wrapper(*args, **kwargs):
            if not objects or not args[0] or 'exit' in args[0]:                            
                return
            else:
                return function(*args, **kwargs)
                                                                                                                  
        return wrapper

    return func_wrapper

