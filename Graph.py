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
            print(edge.head.name, end=' ; ')
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
        - w : weight
    
    Dependencies : None
    '''
    def __init__(self,n):
        self.head = n  


class Graph:
    def __init__(self,l=[],edg=[]):  # l est optionnel : liste ne noms de noeuds
        self.size = len(l)
        self.nodes=list()
        self._weight = np.zeros((self.size,self.size),int)
        self._flow = np.zeros((self.size,self.size),int)
        for i in range(len(l)):
            n=Node(i,l[i])
            self.nodes.append(n)
        for i in range(len(edg)):
            self.add_edge(edg[i][0],edg[i][1])
            self._weight[edg[i][0]][edg[i][1]] = edg[i][2]

 
    def add_edge(self,i,j):
        if i<len(self.nodes) and j<len(self.nodes):
            e=Edge(self.nodes[j])
            self.nodes[i].adj.append(e)
            
    def print_adj_list(self):
        for n in self.nodes:
            print('Noeud :', n.index,n.name )
            n.adj.print()

    #Property nous permet d'utiliser la notion de graphe résiduel
    

    #On implemente un parcours en largeur qui va de la source jusqu'au puit
    #Si un chemin existe il renvoie True sinon False
    def BFS(self,s,t,p):
        n=self.size
        c=[0]*n  # code couleur blanc=0 (Faux), gris=1 (Vrai), noir=2 (Vrai)
        f=Queue.Queue()
        p[s]=-1
        f.enqueue(s)
        c[s]=1
        while not f.is_empty():
            u=f.dequeue()
            current=self.nodes[u].adj.head
            while current :
                v=current.data.head.index
                if not c[v]:
                    c[v]=1
                    p[v]=u
                    f.enqueue(v)
                    if v == t:
                        return True
                current=current.next
            c[u]=2
        return False
    

    def EdmondKarp(self,source,puit):
        p=[-1]*self.size 
        flow = 0

        while self.BFS(source,puit,p)==True: #Tant qu'il y a un chemin entre la source et le puit on essaye d'augmenter le flow
            current_flow = float('inf')
            t = puit
            while t!=source:
                current_flow = min(current_flow,self._flow[p[t]][[t]])
                t = p[t]

        flow += current_flow
        u = puit
        while u!=source:
            v = p[u]
            self.flow[v][u] -= current_flow
            self.flow[u][v] += current_flow
            u = p[v]

        return flow
    
    
    
    
                
################################  Tests  ################################## 

l=[0,1,2,3,4,5]
edg = [(0,1,11),(0,2,12),(2,1,1),(1,3,12),(2,4,11),(4,3,7),(3,5,19),(4,5,4)]

g2=Graph(l,edg)

source = 0 
puit = 5
print(g2.EdmondKarp(source,puit))





