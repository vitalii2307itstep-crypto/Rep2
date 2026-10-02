import unittest
from Дз import timer
class TestTimer(unittest.TestCase):
    def test_result(self):
        @timer
        def add(a, b):
            return a + b
        self.assertEqual(add(2, 3), 5)
    def test_function(self):
        @timer
        def hello():
            return "Hello"
        self.assertEqual(hello(), "Hello")
if __name__ == "__main__":
    unittest.main()