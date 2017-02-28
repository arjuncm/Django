#from django.test import TestCase
from django.core.urlresolvers import reverse
import unittest
import app.tests

class TddInPythonExample(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

    if __name__ == '__main__':
    tests.main()    