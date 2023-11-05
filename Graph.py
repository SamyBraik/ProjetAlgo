import List
import Queue
import numpy as np


class Adj_list(List.Linked_list): 
    def print(self):  # surcharge la methode print des listes pour afficher les noms des noeuds
        print("Liste d'adjacence = ",end='')
        current=self.head
        while current:
            edge=current.data
            print(edge.head.name, end=' ; ')
            current=current.next
        print()    


class Node: 
    def __init__(self,index=0,name=''):
        self.index = index
        self.name = name
        self.adj = Adj_list()


class Edge: 
    
    def __init__(self,n):
        self.head = n  


class Graph:
    def __init__(self,l=[],edg=[]):  # l est optionnel : liste ne noms de noeuds
        self.size = len(l)
        self.nodes=list()
        self._weight = np.zeros((self.size,self.size),float)
        self._flow = np.zeros((self.size,self.size),float)
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
    

    #On implemente un parcours en largeur qui va de la source jusqu'au puit
    #Si un chemin existe et a une capacité résiduelle minimum strictement positive renvoyer True sinon False
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
                if not c[v] and abs(self._weight[u][v]-self._flow[u][v])>0:
                    c[v]=1
                    p[v]=u
                    if v == t:
                        return True
                    f.enqueue(v)
                current=current.next
            c[u]=2
        return False
    

    def EdmondKarp(self,source,puit):
        #Construction du graphe résiduel
        residual_graph = Graph(l[0],[(u,v,abs(self._weight[u][v]-self._flow[u][v])) for u in l[0] for v in l[0] if u!=v])
        p = [-1]*self.size #Garde en mémoire les noeuds déjà visité
        maxFlow = 0 #Initialisation du flot à 0
        
        #Tant qu'il y a un chemin entre la source et le puit qui augmente le flot
        while residual_graph.BFS(source,puit,p):
            currentFlow = float("Inf")
            s = puit
            while s!=source:
                currentFlow = min (currentFlow, residual_graph._weight[p[s]][s])
                s = p[s]

            maxFlow += currentFlow

            y = puit
            while y!=source:
                x = p[y]
                residual_graph._weight[x][y] -= currentFlow
                residual_graph._weight[y][x] += currentFlow
                self._flow[x][y]+=currentFlow
                y=p[y]
        return maxFlow
    
                
################################  Tests  ################################## 

l=[[0,1,2,3,4,5,6,7],[(0,1,5),(0,2,4),(1,3,7),(2,3,3),(3,4,3),(4,5,4),(4,6,6),(5,7,2),(6,7,8)]]

g=Graph(l[0],l[1])

parent = [-1]*len(l)
source = l[0][0]
puit = l[0][len(l[0])-1]
print(g.EdmondKarp(source,puit))

