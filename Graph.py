# -*- coding: utf-8 -*-

################################  Graphs  ################################## 
import List
import Queue
import numpy as np


class Adj_list(List.Linked_list): 
    '''
    class for a adjacency list
    
    attributes inherited from Linked_list :
    - head : Frame1 or None
    
    methods inherited from Linked_list :
    - is_empty() : return true is the queue is empty, false otherwise
    - append(x) : add the data x at the head 
    - pop() : if the linked list is not empty, pop the head, else do nothing and return None
    
    new method
    - print() : print the list of node name
    
    Dependencies : class Linked_list
'''

    def print(self):  # surcharge la methode print des listes pour afficher les noms des noeuds
        print("Liste d'adjacence = ",end='')
        current=self.head
        while current:
            edge=current.data
            print(edge.head.name,',',edge.w, end=' ; ')
            current=current.next
        print()    


class Node: 
    '''
    Class for nodes of a graph
    
    Attributes :
    - index : index of the node in the graph list
    - name : string (default '')
    - adj : Adj_list of Edge

    Dependencies : class Adj_list
    '''
    def __init__(self,index=0,name=''):
        self.index = index
        self.name = name
        self.adj = Adj_list()


class Edge: 
    '''
        Class for edges of a graph
        
        Attributes :
        - head : Node   # dans l'arc (x,y), y est nommé head en anglais (tete de la fleche), et x tail (queue de la fleche)
    
    Dependencies : None
    '''
    def __init__(self,n):
        self.head = n  


class Graph:
    '''
    Class for graph
    
    Attributes :
    - nodes : list (instance of list class) of Node  (default empty list)
    
    Methods :
    - add_edge(i,j,w=1) : if i and j are not out of range, add an edge between i and j with the weight w (default edge = 1), do nothing otherwise
    
    Dependencies : classes Node, Edge and Adj_list
    '''
    def __init__(self,l=[]):  # l est optionnel : liste ne noms de noeuds
        self.nodes=list()
        for i in range(len(l)):
            n=Node(i,l[i])
            self.nodes.append(n)
        self.size = len(self.nodes)
        self._weight = np.zeros((self.size, self.size),int)
        self._flow = np.zeros((self.size, self.size),int)
 
    def add_edge(self,i,j):
        if i<len(self.nodes) and j<len(self.nodes):
            e=Edge(self.nodes[j])
            self.nodes[i].adj.append(e)

    def print_adj_list(self):
        for n in self.nodes:
            print('Noeud :', n.index,n.name )
            n.adj.print()

    @property
    def flow(self):
        return self._flow
    
    @flow.setter
    def flow(self, i,j, v):
        #Verifier si on peut assigner le flow v à l'arc (i,j)
        #On regarde la somme des flows entrant j + le flow v que l'on veut ajouter et si elle est inférieur ou égale à la somme des capacités
        #sortant du noeud j alors le flow v est valide
        if self._flow[:,j].sum() -self._flow[i][j] + v == self._flow[j,:].sum() and v <= self._weight[i][j]:
            self._flow[i][j] = v

################################  Tests  ################################## 

l=[0,1,2,3,4]
edg = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4)]
poids = [8,3,7,3,4,1]
g2=Graph(l)
for i in range(len(edg)):
    g2.add_edge(edg[i][0],edg[i][1])
    g2._weight[edg[i][0]][edg[i][1]]=poids[i]

print(g2._weight)
print(g2.flow)
g2.flow(0,1,8)
print(g2.flow)
