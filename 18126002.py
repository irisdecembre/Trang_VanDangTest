import sys
import matplotlib
import numpy as np
import networkx as nx
from graph import Graph
# quoc vua sua cai file nay do nha
print("quoc handsome boiz !")

def getAdjMatrix():
    AdjMatrix = []
    with open("graph1.txt", "r") as f:
        temp = f.readline()
        n = int(temp)

        for line in f:
            AdjMatrix.append([int(i) for i in line.split(' ')])

    print(n)

    for i in range(0, n):
        count = 0
        check = np.zeros(n)

        for j in range(0, n):
            if (AdjMatrix[i][j] == 1):
                count+=1
                check[j] = 1

        print(count, end=' ')

        for idx in range(0, n):
            if (check[idx] == 1):
                print(idx, end=' ')

        print(end='\n')

def getAdjList():
    AdjList = np.array

    with open("graph2.txt", "r") as f:
        temp = f.readline()
        n = int(temp)
        AdjList = [[int(i) for i in line.split(' ')] for line in f]

    AdjMatrix = np.zeros(shape=(n, n))

    for i in range(0, n):
        m = AdjList[i][0] + 1

        for j in range(1, m):
            AdjMatrix[i][AdjList[i][j]] = 1

    return AdjMatrix

def checkGraph():
    graph = getAdjList()
    v = len(graph)

    ok = True

    for i in range(0, v):
        for j in range(0, v):
            if (graph[i][j] != graph[j][i]):
                ok = False
                break
    if ok:
        print("This is undirected graph.")
        G = nx.from_numpy_matrix(graph, create_using=nx.Graph())
      
        print("Number of vertices: ", v)
        print("Number of edges: ", G.number_of_edges())
        print("Number of degrees: ", G.degree())
        
        check = True
        for i in range(0, v):
            if (graph[i][0] != v - 1):
                check = False
        if check:
            print("This is complete graph.")
    else:
        print("This is directed graph.")
        G = nx.from_numpy_matrix(graph, create_using=nx.DiGraph())
      
        print("Number of vertices: ", v)
        print("Number of edges: ", G.number_of_edges())
        print("Number of in-degrees: ", G.in_degree())
        print("Number of out-degree: ", G.out_degree())
        
        
    pendants = [n for n, d in G.degree() if d == 1]
    print("List of pendant vertices: ", pendants)
    isolates = [n for n, d in G.degree() if d == 0]
    print("List of isolated vertices: ", isolates)

    if (nx.is_bipartite(G)):
        print("This is bipartite graph.")

def basedGraph():
    matrix = getAdjList()
    n = len(matrix)

    new_matrix = np.zeros(shape=(n, n))

    for i in range(0, n):
        for j in range(0, n):
            if (matrix[i][j] == 1):
                new_matrix[i][j] = new_matrix[j][i] = 1

    return new_matrix

def complementGraph():
    matrix = getAdjList()
    n = len(matrix)

    new_matrix = np.zeros(shape=(n, n))

    for i in range(0, n):
        for j in range(0, n):
            if (i != j):
                if (matrix[i][j] == 0):
                    new_matrix[i][j] = 1
                else:
                    new_matrix[i][j] = 0

    return new_matrix

def getList():
    list = {}
    matrix = getAdjList()

    for idx, row  in enumerate(matrix):
        vertexs = [i for i in range(len(row)) if row[i] > 0]
        list[idx] = [sum(np.array(row)>0), vertexs]
        
    return list

def BFS(start):
    G = getList()

    queue = []
    visited = [False] * (len(getAdjList()))

    queue.append(start)
    visited[start] = True

    while queue:
        start = queue.pop(0)
        print(start, end = " ")
        for i in G[start]: 
                if (visited[i] == False): 
                    visited[i] = True
                    queue.append(i) 

visited = [False] * (len(getAdjList()))
def DFS(start, dfs):
  
    visited[start] = True

    dfs.append(start)
    AdjMatrix = getAdjList()
    n = len(AdjMatrix)

    for i in range(0, n):
        if (not visited[i] and AdjMatrix[start][i] == 1) :
            DFS(i, dfs)

def isConnected():
    G = nx.from_numpy_matrix(getAdjList())
    if (list(nx.connected_components(G)).count == len(getAdjList())):
        return True
    else:
        return False
       
def isBipartite():
    graph = getAdjList()
    v = len(graph)

    ok = True

    for i in range(0, v):
        for j in range(0, v):
            if (graph[i][j] != graph[j][i]):
                ok = False
                break
    if ok:
        G = nx.from_numpy_matrix(graph, create_using=nx.Graph())
    else:
        G = nx.from_numpy_matrix(graph, create_using=nx.DiGraph())

    if (nx.is_bipartite(G)):
        return True
    else:
        return False

def isCompleteBipartite():
    graph = getAdjList()
    v = len(graph)

    check_complete = True
    for i in range(0, v):
        if (graph[i][0] != v - 1):
            check = False

    if (check_complete & isBipartite()):
        return True
    return False

def bridgeEdge():
    G = nx.from_numpy_matrix(getAdjList())
    return list(nx.bridges(G))  

def cutVertex():
    G = nx.from_numpy_matrix(getAdjList())
    return list(nx.articulation_points(G))

def main():
    getAdjMatrix()
    print(getAdjList())
    checkGraph()

    print("Based graph: \n", basedGraph())
    print("Complement graph: \n", complementGraph())

    print("BFS: ")
    #BFS(0)

    dfs = []
    DFS(0, dfs)
    print("DFS: ", dfs)
    print("Graph is connected: ", isConnected())
    print("Graph is bipartite graph: ", isBipartite())
    print("Graph is complete bipartite graph: ", isCompleteBipartite())

    print("Cut vertices: ", cutVertex())
    print("Bridges edges: ", bridgeEdge())

if __name__ == '__main__':
	main()


