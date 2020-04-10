import unittest

def add(x,y):
    return x + y

class MyTest(unittest.TestCase):
    def test_hi(self):
        self.assertEqual(add(3,4), 7)
