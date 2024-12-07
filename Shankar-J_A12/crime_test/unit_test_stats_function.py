import unittest
from stats_function import remove_null, mean, median

class testStatFunctions(unittest.TestCase):
    def mean_test(self):
        self.assertEqual(mean(), 28.934301576798635)
    def median_test(self):
        self.assertEqual(median(), 30)
    def remove_null_test(self):
        self.assertEqual(remove_null(), 0)
    

    if __name__ == '__main__': unittest.main()
