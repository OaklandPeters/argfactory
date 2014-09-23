import re
import abc
import types

def identity(*args, **kwargs):
    """Identity function accounting for complicated possibilities"""
    if len(args) == 0 and len(kwargs) == 0:
        return None
    elif len(args) == 1 and len(kwargs) == 0:
        return args[0]
    elif len(args) > 1 and len(kwargs) == 0:
        return args
    elif len(args) == 0 and len(kwargs) != 0:
        return kwargs
    elif len(args) == 1 and len(kwargs) != 0:
        return (args[0], kwargs)
    elif len(args) > 1 and len(kwargs) != 0:
        return (args, kwargs)

def _identity(x):
    #Very simple identity function
    return x

class NullType(object):
    """Superclass of NoneType, NotPassed, and optional."""
    __metaclass__ = abc.ABCMeta
NullType.register(types.NoneType)

class NotPassedType(NullType):
    """Represents non-passed arguments. Alternative to using None, useful
    in cases where you want to distinguish passing in the value of 'None' from
    'No-value-was-provided'."""
    def __init__(self):
        pass
NotPassed = NotPassedType()


# ~ itertools.imap
# def imap(function, *iterables):
#     iterables = map(iter, iterables)
#     while True:
#         args = [next(it) for it in iterables]
#         if function is None:
#             yield tuple(args)
#         else:
#             yield function(*args)
