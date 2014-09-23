"""
@todo: Add unittests involving escape and control characters
"""
from __future__ import absolute_import
import unittest

from argfactory.strings import *

#==============================================================================
#        Unit-Tests
#==============================================================================
class ReTests(unittest.TestCase):
    def test_re_find(self):
        _string = 'aa a bbbaccccaddaaaa'
        self.assertEquals(re_find('a', _string), 'a')
        self.assertEquals(re_find('(a)', _string), 'a')

    def test_not_found(self):
        _string = 'aa a bbbaccccaddaaaa'
        self.assertEquals(re_find('e', _string), None)
        self.assertEquals(re_all('e', _string), [])
        self.assertRaises(StopIteration, lambda: re_iter('e', _string).next())
        self.assertEquals(re_test('e', _string), False)

    def test_re_all(self):
        _string = 'aa a bbbaccccaddaaaa'
        self.assertEquals(re_all('aa',_string),['aa', 'aa', 'aa'])
    
    def test_equivalents(self):
        _string = 'aa a bbbaccccaddaaaa'
        def compare(regex):
            A = re_find(regex, _string)
            B = re_iter(regex, _string).next() #Errors if not found
            C = re_finder(regex)(_string)
            D = re_all(regex, _string)[0]
            self.assertEquals(A, B)
            self.assertEquals(A, C)
            self.assertEquals(A, D)
        
        compare('a')
        compare('(a)')
        compare('(aa)')
        compare('(ba)')
        compare('b')
        compare('.')
        compare('^a')
        compare('a$')
    
    def test_re_test(self):
        _string = 'aa a bbbaccccaddaaaa'
        self.assert_(re_test('a', _string))
        self.assert_(re_test(' ', _string))
        self.assert_(not re_test('e', _string))
        self.assert_(not re_test('12', _string))
    
    def test_unicode(self):
        _string = 'aa a bbbaccccaddaaaa'
        self.assertEquals(re_find('d', 'aaadbbb'), 'd')
        self.assertEquals(re_find(u'd', 'aaadbbb'), 'd')
        self.assertEquals(re_find('d', u'aaadbbb'), 'd')
        self.assertEquals(re_find(u'd', u'aaadbbb'), 'd')
        
        self.assert_(not isinstance(re_find('d','aaadbbb'), unicode))
        self.assert_(not isinstance(re_find(u'd','aaadbbb'), unicode))
        self.assert_(isinstance(re_find('d',u'aaadbbb'), unicode))
        self.assert_(isinstance(re_find(u'd',u'aaadbbb'), unicode))
        
    def test_typeerror(self):
        _string = 'aa a bbbaccccaddaaaa'
        
        def bug(func, input):
            self.assertRaises(TypeError, lambda: func(input, _string))
        
        def check_all(input):
            bug(re_find, input)
            bug(re_iter, input)
            bug(re_all, input)
            bug(re_test, input)
        
        check_all(1)
        check_all(None)
        check_all(['a'])
        check_all(('a',))

if __name__ == "__main__":
    unittest.main()