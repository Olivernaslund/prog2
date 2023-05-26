
"""
Unittests for the linked lists remove
"""

import unittest

from linked_list import *


class Test(unittest.TestCase):

    def test_remove(self):
        print('\nTests remove')
        print('*** Should be implemented! ***')

        lst = LinkedList()
        for x in [1, 1, 2, 2, 3, 5, 10]:
            lst.insert(x)

        self.assertEqual(lst.remove(1), True)
        self.assertEqual(str(lst), '(1, 2, 2, 3, 5, 10)')
        self.assertEqual(lst.remove(1), True)
        self.assertEqual(str(lst), '(2, 2, 3, 5, 10)')
        self.assertEqual(lst.remove(3), True)
        self.assertEqual(str(lst), '(2, 2, 5, 10)')
        self.assertEqual(lst.remove(2), True)
        self.assertEqual(str(lst), '(2, 5, 10)')
        self.assertEqual(lst.remove(9), False)
        self.assertEqual(str(lst), '(2, 5, 10)')
        self.assertEqual(lst.remove(10), True)
        self.assertEqual(str(lst), '(2, 5)')
        self.assertEqual(lst.remove(10), False)
        self.assertEqual(str(lst), '(2, 5)')
        self.assertEqual(lst.remove(5), True)
        self.assertEqual(str(lst), '(2)')
        self.assertEqual(lst.remove(3), False)
        self.assertEqual(str(lst), '(2)')
        self.assertEqual(lst.remove(2), True)
        self.assertEqual(str(lst), '()')
        self.assertEqual(lst.remove(2), False)
        self.assertEqual(str(lst), '()')

if __name__ == "__main__":
    unittest.main()
