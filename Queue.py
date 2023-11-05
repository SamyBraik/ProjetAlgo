# -*- coding: utf-8 -*-

################################  Queue  ################################## 

class Frame:
    '''
    attributes :
    - data :  
    - next : next Frame or None
    - prev : previous Frame or None
    
    Dependencies : none
    '''
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None


class Queue:
    '''
    class for a queue
    
    attributes :
    - head : Frame or None
    - tail : Frame or None
    
    methods :
    - is_empty() : return true is the queue is empty, false otherwise
    - enqueue(x) : enqueue the data x  
    - dequeue() : if the queue is not empty, dequeue the head, else do nothing and return None
    - print() : print the queue

    Dependencies : class Frame
    '''
    def __init__(self):
        self.head=None
        self.tail=None
        
    def is_empty(self):
        return self.head is None
    
    def enqueue(self,x):
        new_tail=Frame(x)
        # écriture du chainage aller : 2 cas
        new_tail.next=None
        if self.tail is None:
        # si la file est vide, self.head doit pointer sur new_tail
            self.head= new_tail
        else:
        # Sinon, self.tail.next est valide et doit pointer sur new_tail
            self.tail.next=new_tail
        # écriture du chainage retour : 1 cas
        new_tail.prev=self.tail 
        self.tail=new_tail 

    def dequeue(self):
        #si la liste est vide, on ne fait rien
        if self.head is None:
            return None    
        # sinon sauvegarde de l'élément défiler
        x=self.head.data
        # écriture du chainage aller : 1 cas
        self.head=self.head.next 
        # écriture du chainage retour : 2 cas
        if self.head is None:
        # si la liste devient vide
            self.tail=None
        # sinon self.head.prev est valide
        else:
            self.head.prev=None
        return x
        
    def print(self):  # fonction d'affichage de la file
        print('File= ',end='')
        current=self.head
        while current:
            print(current.data,end=' ')
            current=current.next
        print()    

################################  Tests  ################################## 
'''
f=Queue()
f.print()

for i in range(3):
    f.enqueue(i)
    f.print()

for i in range(4):
    print('element défilé :',f.dequeue())
    f.print() 
'''