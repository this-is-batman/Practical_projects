# we need to find whether the graph is connected or not given the graph as user input
# if DFS from a vertex returns all the vertices
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.DFS_count = 0 # number of elements in the DFS traversal
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u) #considering the graph to be undirected
    def DFSUtil(self,v,visited):
        self.DFS_count+=1
        visited[v] = True
        print(v,end=' ')
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i,visited)
    def DFS(self,v): #start the DFS from a vertex v
        visited = [False] * (len(self.graph))
        self.DFSUtil(v,visited)
    # submodule to check if the graph is connected or not
    def is_connected(self):  # just do a DFS from the 0th vertex and check if all the vertices are reachable from the 0th vertex
        self.DFS(0)
        if self.DFS_count == len(self.graph):
            print("The graph is connected!")
        else:
            print("The graph is not connected!")

if __name__=='__main__':
    g = Graph()
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(3,4)
    g.add_edge(2,3)
    g.is_connected()  # returns connected in this case