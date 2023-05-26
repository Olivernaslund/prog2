""" bst.py

Student: Oliver Näslund
Mail: oliver.naslund@gmail.com
Reviewed by: Joacim Stenlund
Date reviewed: 2 Maj 2023
"""

import math
from random import random
from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert2(self, key):
        self.root = self._insert(self.root, key)

    def _insert2(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def insert(self, key):
        r = self.root
        while r:
            if key < r.key:
                if r.left == None:
                    r.left = self.Node(key)
                else: r = r.left
            elif key > r.key:
                if r.right == None:
                    r.right = self.Node(key)
                else: r = r.right
            else: break
        if r is None:
            self.root = self.Node(key)


    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains2(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def contains(self, k):
        n = self.root
        def _contains(n, k):
            if n == None:
                return False
            elif n.key == k:
                return True
            elif k < n.key:
                return _contains(n.left, k)
            elif k > n.key:
                return _contains(n.right, k)

        return _contains(n, k)

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        n = self.root
        def _height(n):
            if n == None:
                return 0
            else:
                return max(1 + _height(n.left), 1 + _height(n.right))

        return _height(n)

    def __str__(self):                            # Compulsory
        str = '<'
        if self.root == None:
            return '<>'
        for i in self.root:
            str += f'{i}, '
        return str[:-2] + '>'
            

    def to_list(self):                            # Compulsory
        lst = []
        if self.root == None:
            return lst
        for i in self.root:
            lst.append(i)
        return lst #Komplexitet O(n) (eller O(n^2) eftersom append måste går genom hela listan eller kan den bara placera vid slutet på en gång?)


    def to_LinkedList(self):                      # Compulsory
        if self is None:
            return LinkedList()

        lst = LinkedList()
        count = 0

        for i in self.root:
            if count == 0:
                lst.first = lst.Node(i, None)
                f = lst.first
                count += 1
            else:
                f.succ = lst.Node(i, None)
                f = f.succ
        return lst # O(n)


    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            #pass
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)
            #pass
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                rr = r.right
                for i in rr:
                    if rr.left == None:
                        smallest = rr.key
                    else:
                        rr = rr.left
                r.key = smallest
                r.right = self._remove(r.right, smallest)
                
                #pass
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def ipl(self):                                # Compulsory
        n = self.root
        
        def _ipl(n, inter):
            if n == None:
                return 0
            else: 
                return _ipl(n.left, inter + 1) + _ipl(n.right, inter + 1) + inter
        
        return _ipl(n, 1)
            
        #pass


def random_tree(n):                               # Useful
    tree = BST()
    for i in range(n):
        tree.insert(random())
    return tree
    #pass


def main():
    t = BST()

    print(t)

    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)

    print(t)

    lst = t.to_LinkedList()
    print(lst)


    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")


    print('Övn 20')
    for k in range(5000, 100000, 5000):
        ref = random_tree(5000).ipl()/5000
        tree = random_tree(k)
        print(f'Genomsnitt nodhöjd n = {k}: {tree.ipl()/k} ; Teori: {1.39*math.log2(k)}')
        print(f'Höjd n = {k}: {tree.height()}')

    #Höjden bör växa som log, då det finns 2^n flera platers per höjd

if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size?
Ja, då är det bara att räkna hur lång interationen är
2. computing height?
Nej
3. contains?
Ja
4. insert?
Nej, måste placers på rätt plats iter ger inte den info
5. remove?
Nej, måste tas bort på rätt sätt




Results for ipl of random trees
===============================






"""
