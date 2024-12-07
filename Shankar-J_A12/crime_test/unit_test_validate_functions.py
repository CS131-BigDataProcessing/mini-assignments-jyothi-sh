import unittest
from validate_functions import type_check

class testvalidateFunctions(unittest.TestCase):
    def type_check_test(self):
        self.assertEqual(type_check(), "Types are Correct")

    if __name__ == '__main__': unittest.main()

