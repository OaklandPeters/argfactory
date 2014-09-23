

from .shared import identity, NotPassed, _re_type





#==============================================================================
#                    Selector
#==============================================================================
#        value                     Function    
#    -----------------         ----------------
#        None                      identity
#        string                    re_finder(value)
#        int or slice              itemgetter(value)
#        mapping                   __getitem__
#        set                       __contains__
def make_selector(value):
    """
    Based closely on 'make_func' from funcy/funcmakers.py.
    
    @todo: In the 'value is None' clause -- add support for NotPassed/NullType
    """
    if callable(value):
        return value
    elif value is None:
        return identity
    elif isinstance(value, (basestring, _re_type)):
        return re_finder(value)










#==============================================================================
#                    Predicate
#==============================================================================
#        value                     Function    
#    -----------------         ----------------
#        None                      bool
#        string                    
#        int or slice              
#        mapping                   
#        set                       
def make_predicate(value):
    pass



print('try identity()')
import pdb
pdb.set_trace()
print('try identity()')