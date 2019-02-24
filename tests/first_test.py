import unittest
import sys
sys.path.append('..')
import testrepo

class TestAddMethods(unittest.TestCase):

    def test_integer(self):
        self.assertAlmostEqual(testrepo.addition(1, 2), 3)
    
    def test_float(self):
        self.assertAlmostEqual(testrepo.addition(1.1, 2.2), 3.3)
    
    def test_keyword(self):
        self.assertAlmostEqual(testrepo.addition(a=1.1, b=2.2), 3.3)
        self.assertAlmostEqual(testrepo.addition(1.1, b=2.2), 3.3)
        self.assertAlmostEqual(testrepo.addition(a=2.2), 2.2)

if __name__ == '__main__':
    unittest.main()
