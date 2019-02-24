import unittest
import testrepo

class TestAddMethods(unittest.TestCase):

    def test_integer(self):
        self.assertAlmostEqual(testrepo.add(1, 2), 3)
    
    def test_float(self):
        self.assertAlmostEqual(testrepo.add(1.1, 2.2), 3.3)
    
    def test_keyword(self):
        self.assertAlmostEqual(testrepo.add(a=1.1, b=2.2), 3.3)
        self.assertAlmostEqual(testrepo.add(1.1, b=2.2), 3.3)
        self.assertAlmostEqual(testrepo.add(a=2.2), 2.2)

if __name__ == '__main__':
    unittest.main()