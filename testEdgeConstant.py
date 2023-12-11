import Graph
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Test sur un nombre d'arcs constant et un nombre de noeuds qui diffère :
duree = list()
longueur = list()
for n in range(1,5999):
    f = open("testEC/test{}EdgeConstant.txt".format(n),"r")
    line = f.read().splitlines()
    L = [i for i in range(int(line[0]))]
    G = Graph.Graph(L)
    for i in range(1,len(line)):
        edg = line[i].split(";")
        G.add_edge(int(edg[0]),int(edg[1]))
        G.weight[int(edg[0])][int(edg[1])]=int(edg[2])

    longueur.append(int(line[0]))
    start = time.perf_counter()
    print(G.EdmondsKarp(L[0],L[-1]))
    end = time.perf_counter()
    duree.append((end-start)*1000)
    print(n)



df = pd.DataFrame(data=list(zip(longueur,duree)),columns=["Nombre d'arcs","Temps d'execution"])
moyenne = df.groupby("Nombre d'arcs").mean()
x = np.linspace(1000,4500)
y = (x)/5000-0.15
plt.plot(x,y,label="x/5000 -0.15")
plt.plot(moyenne,label="Edmonds-Karp")
plt.xlabel("Nombre de noeuds")
plt.ylabel("Temps d'execution (en ms)")
plt.legend(loc='best')
plt.show()