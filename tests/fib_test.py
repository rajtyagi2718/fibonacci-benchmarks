import random
import unittest

from fib.fib import fibs


test_funcs = []

def register(func):
    test_funcs.append(func)
    def decorator(*args):
        return func(*args)
    return decorator


@register
def test_base_cases(name, fib):

    class BaseCasesTestCase(unittest.TestCase):

        def test_zero(self):
            self.assertEqual(0, fib(0))

        def test_one(self):
            self.assertEqual(1, fib(1))

        __qualname__ = name + '.' + __qualname__.split('.')[-1]

    return BaseCasesTestCase 

@register
def test_first_ten(name, fib):

    class FirstTenTestCase(unittest.TestCase):

        def test_zero_to_ten(self):
            for i,r in enumerate([0,1,1,2,3,5,8,13,21,34]):
                with self.subTest(i=i):
                    self.assertEqual(r, fib(i))

        __qualname__ = name + '.' + __qualname__.split('.')[-1]

    return FirstTenTestCase 

@register
def test_thirty(name, fib):

    class ThirtyTestCase(unittest.TestCase):

        def test_thirty(self):
            self.assertEqual(832040, fib(30))

        __qualname__ = name + '.' + __qualname__.split('.')[-1]

    return ThirtyTestCase 


test_cases = [*(test_func(*item) for item in fibs.items() 
              for test_func in test_funcs)]

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite
