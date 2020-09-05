import unittest

class MainTest(unittest.TestCase):
    def test(self):
        result = 1 + 1
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()