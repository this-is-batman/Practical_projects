# create a program that will create a graph from the links that are provided to you
#works correctly for valid URL inputs www.abc.com
from collections import defaultdict # we will implement graphs using a linked list
def check_connect(link1,link2):
    str1 = str(link1)
    str2 = str(link2)
    if str2.startswith(str1,0,len(str2)) and len(str1)!=len(str2) or str1.startswith(str2,0,len(str1)) and len(str1)!=len(str2):
        return 1
    else:
        return 0
def create_graph(g,parent,child):
    g.add_edge(parent,child)

def traverse_graph(g,parent):
    g.find_children(parent)

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) #graph is a set of vertices each containing a list to all the neighbors
    def add_edge(self,u,v): #create a directed edge from u to v 
        self.graph[u].append(v)  #doing for directed edges
    def find_children(self,u):
        print(u)
        for i in self.graph[u]:
            print('|')
            print(i,end="\n")
    
    def find_length(self,u): #find length of the list of vertices adjacent to u
        return len(self.graph[u])

g = Graph()
list_url = [] #empty list containing all the url's
roots = [] #empty list containing the starting path of all the routes 
while True:
    n =input("Do you want to enter another link? ")
    if n is 'Y':
        link = input("Enter the URL: ")
        if list_url.__contains__(link):
            print("Already present")
        else:
            flag = 0 #means no link is parent of this node
            list_url.append(link)
            for i in list_url:  #if no link is found
                if check_connect(i,link)!=1:
                     pass
                else:
                    print("A new link is created!")
                    create_graph(g,i,link)
                    flag =1
            if flag is 0:
                roots.append(link)
    else:
        break  #end the true loop

###Here we will display the entire graph along with the links
for i in roots:  #print all the links or trees with different parents
    print("\n")
    traverse_graph(g,i)