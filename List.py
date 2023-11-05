# -*- coding: utf-8 -*-

################################  Linked_list  ################################## 

class Frame:
    '''
    attributes :
    - data :  
    - next : next Frame or None
    
    Dependencies : None
    '''
    def __init__(self,x):
        self.data=x
        self.next=None
        
class Linked_list:
    '''
    class for a linked list
    
    attributes :
    - head : Frame or None
    
    methods :
    - is_empty() : return true is the list is empty, false otherwise
    - append(x) : add the data x at the head 
    - pop() : if the linked list is not empty, pop the head, else do nothing and return None
    - print() : print the list
    
    Dependencies : class Frame
    '''
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None
        
    def append(self,x):
        new_head = Frame(x)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        if self.head is None:
            return None
        x=self.head.data
        self.head=self.head.next
        return x

    def print(self):  # fonction d'affichage de la liste
        print('Liste chainees= ',end='')
        current=self.head
        while current:
            print(current.data,end=' ')
            current=current.next
        print()    
################################  Tests  ################################## 
'''
print()       
l=Linked_list()
for i in range(3):
    l.append(i)
    l.print()

for i in range(4):
    print('element retiré :',l.pop())
    l.print() 
'''