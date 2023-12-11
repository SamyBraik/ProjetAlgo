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
    def __init__(self,l=[]):  # l est optionnel : liste le noms de noeuds
        self.size = len(l)
        self.nodes=list()
        self.weight = np.zeros((self.size,self.size),int)
        self.flow = np.zeros((self.size,self.size),int)
        self.residual_graph = np.zeros((self.size,self.size),int)
        for i in range(len(l)):
            n=Node(i,l[i])
            self.nodes.append(n)
        # for i in range(len(edg)):
        #     self.add_edge(edg[i][0],edg[i][1])
        #     self._weight[edg[i][0]][edg[i][1]] = edg[i][2]

 
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
                if not c[v] and abs(self.residual_graph[u][v])>0:
                    c[v]=1
                    p[v]=u
                    if v == t:
                        return True
                    f.enqueue(v)
                current=current.next
            c[u]=2
        return False
    
    
    def EdmondsKarp(self,source,puit):
        #Construction du graphe résiduel
        # l = [i for i in range(self.size)]
        # residual_graph = Graph(l)
        # edg = [(u,v) for u in l for v in l if u!=v]
        # for x in edg:
        #     residual_graph.add_edge(x[0],x[1])
        #     residual_graph._weight[x[0]][x[1]]=int(abs(self._weight[x[0]][x[1]]-self._flow[x[0]][x[1]]))
        self.residual_graph = self.weight


        p = [-1]*self.size #Garde en mémoire les noeuds déjà visité
        maxFlow = 0 #Initialisation du flot à 0
        
        #Tant qu'il y a un chemin entre la source et le puit qui augmente le flot
        while self.BFS(source,puit,p):
            currentFlow = float("Inf")
            s = puit
            while s!=source:
                currentFlow = min (currentFlow, self.residual_graph[p[s]][s])
                s = p[s]
        

            maxFlow += currentFlow

            y = puit
            while y!=source:
                x = p[y]
                self.residual_graph[x][y] -= currentFlow
                self.residual_graph[y][x] += currentFlow
                self.flow[x][y]+=currentFlow
                y=p[y]
        return maxFlow