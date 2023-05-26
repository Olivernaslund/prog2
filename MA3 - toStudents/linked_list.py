""" linked_list.py

Student: Oliver Näslund
Mail: oliver.naslund@gmail.com
Reviewed by: Joacim Stenlund
Date reviewed: 2 Maj 2023
"""




from re import X


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

        def length(self): #Tillägg
            def _length(f):
                if f is None:
                    return 0
                else:
                    return 1 + _length(f.succ)
            return _length(self.first)

        def insert(self, x):
            if self.succ is None or x <= self.succ.data:
                self.succ = LinkedList.Node(x, self.succ)
            else:
                self.succ.insert(x)


    def __init__(self):
        self.first = None
    
    def __iter__(self):       # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):      # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x): #Metod 2
        self.first = self._insert(x, self.first)   
    
    def _insert(self, x, f): #Metod 2 hjälp
        if f is None or x <= f.data:
            return LinkedList.Node(x, f)
        else:
            f.succ = self._insert(x, f.succ)
        return f

   # def insert(self, x): #Metod 1
   #     if self.first is None or x <= self.first.data:
   #         self.first = LinkedList.Node(x, self.first)
   #     else:
   #         self.first.insert(x)

   # def insert(self, x): #Gammal insert
   #     if self.first is None or x <= self.first.data:
   #         self.first = self.Node(x, self.first)
   #     else:
   #         f = self.first
   #         while f.succ and x > f.succ.data:
   #             f = f.succ
   #         f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Optional
        len = 0
        f = self.first
        while f:
            len +=1
            f = f.succ
        return len

    def mean(self):               # Optional
        sum = 0
        f = self.first
        while f:
            sum += f.data
            f = f.succ
        return sum / self.length()
    
    def remove_last(self):        # Optional
        f = self.first 
        if not f:
            raise ValueError 
        while f.succ:
            fp = f
            f = f.succ
            if not f.succ:
                last = f.data 
                fp.succ = None             
        return last 

    def remove(self, x):          # Compulsory
        f = self.first ; #ff = f.succ
        
        if f == None:
            return False
            #raise AttributeError("Empty list")
        ff = f.succ

        if f.succ == None: 
            if f.data == x:
                self.first = None
                return True
            else:
                return False

        if f.data == x:
                #f = ff
                #f = f.succ
                self.first = ff 
                return True

        while f.succ != None:
            if ff.data == x:
                f.succ = ff.succ
                return True
            elif ff.data !=x:
                f = f.succ ; ff = f.succ
                
        return False


    def count(self, x):           # Optional
        f = self.first
        return self._count(x, f)  

    def _count(self, x, f):
            if f == None:
                return 0
            elif f.data == x:
                return 1 + self._count(x, f.succ) 
            else:
                return self._count(x, f.succ)        


    def to_list(self):            # Compulsory
        f = self.first
        return self._to_list(f)
    
    def _to_list(self, f):
        if f == None:
            return []
        else:
            return [f.data] + self._to_list(f.succ)


    def remove_all(self, x):      # Compulsory
        f = self.first
        if f == None:
           return 0
        else: 
            return self._remove_all(x, f)     
    

    def _remove_all(self, x, f): 
        if f == None:
           return 0
        elif f.succ == None: #one node
            if f.data == x:
                self.first = None
                f = None
                return 1
            else:
                return 0
        elif f.data == x:
            self.first = f.succ
            return 1 + self._remove_all(x, f.succ)
        elif f.succ.data == x:
            f.succ = f.succ.succ
            return 1 + self._remove_all(x, f)  
        else:
            return self._remove_all(x, f.succ)
   

    def __str__(self):            # Compulsary
        str = '('
        if self.first == None:
            return '()'
      
        for i in self:
            str += f'{i}, '
        return str[:-2] + ')'
            

    def copy2(self):               # Compulsary
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
        List goes through one at a time and insert using recursion: O(n^2)
    '''

    def copy(self):               # Compulsary  # Should be more efficient
        result = LinkedList()
        f = self.first

        if f == None:
                return result

        def _copy(f):
            if f.succ == None:
                return result.Node(f.data, None)
            else:
                return result.Node(f.data, _copy(f.succ)) 

        result.first = _copy(f)

        return result                    
    ''' Complexity for this implementation:
    Data is already sorted we just need to insert into nodes O(n)
    '''

    def __getitem__(self, ind):   # Optional
        count = 0
        for x in self:
            if count == ind:
                return x
            count += 1
        else:
            raise IndexError("index out of range")



class Person:                     # Compulsory
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"
    
    def __It__(self, other): # < , >
        return self.name < other.name 

    def __le__(self, other): # <= , >=
        return self.name <= other.name

    def __eq__(self, other): # =
        return self.name == other.name



def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    plist = LinkedList()
    p = Person("Oliver", '010830')
    q = Person("Blah", '214212')

    plist.insert(p)
    plist.insert(q)

    plist.print()

    # Test code:
    print('---------')
  
    print('str rep',str(lst))




if __name__ == '__main__':
    main()
