"""
Unittests for the binary search tree methods
"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test_remove(self):
        print('\nTests BST remove')
        print('*** Should be implemented! ***')

        bst = BST()
        for x in [10, 5, 3, 8, 1, 4, 6, 9, 2, 7]:
            bst.insert(x)

        bst.remove(2)
        self.assertEqual(str(bst), '<1, 3, 4, 5, 6, 7, 8, 9, 10>')
        #bst.remove(7)
        #self.assertEqual(str(bst), '<1, 3, 4, 5, 6, 8, 9, 10>')
        bst.remove(1)
        self.assertEqual(str(bst), '<3, 4, 5, 6, 7, 8, 9, 10>')
        bst.remove(4)
        self.assertEqual(str(bst), '<3, 5, 6, 7, 8, 9, 10>')
        bst.remove(6)
        self.assertEqual(str(bst), '<3, 5, 7, 8, 9, 10>')
        bst.remove(8)
        self.assertEqual(str(bst), '<3, 5, 7, 9, 10>')
        bst.remove(9)
        self.assertEqual(str(bst), '<3, 5, 7, 10>')
        bst.remove(5)
        self.assertEqual(str(bst), '<3, 7, 10>')



if __name__ == "__main__":
    unittest.main()
