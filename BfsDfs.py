class Node:
    def __init__(self,value):
        self.value=value
        self.adj=[]
    def __str__(self):
        return f"{self.value}"

class Graph:
    def __init__(self,nodes):
        self.nodes=nodes
        self.visited=list(False for i in self.nodes)
        self.queue=[]
    def reset(self):
        self.visited = list(False for i in self.nodes)
        self.queue = []
    def dfs(self,index):
        self.visited[index] = True
        print(self.nodes[index])
        for i in self.nodes[index].adj:
            if not self.visited[i]:
                self.dfs(i)

    def bfs(self,index):
        print(self.nodes[index])
        for i in self.nodes[index].adj:
            if not self.visited[i]:
                self.visited[i] = True
                self.queue.append(i)
        if len(self.queue):
            self.bfs(self.queue.pop(0))

def menu():
    return int(input('''
Enter Choice:
1. DFS
2. BFS
3. Exit
'''))

def initialize_nodes(n):
    nodes=list(Node(i) for i in range(n))
    return Graph(nodes)
def initialize_edges(graph):
    t=int(input("Enter total edges:"))
    print("Enter space seperated adjacent vertex numbers for every edge\n")
    for i in range(t):
        u,v=map(int,input().split())
        graph.nodes[u].adj.append(v)
        graph.nodes[v].adj.append(u)

graph=initialize_nodes(int(input("Number of nodes: ")))
initialize_edges(graph)
while True:
    choice=menu()
    if choice==3:
        print("Exitting...")
        break
    elif choice==1:
        graph.reset()
        graph.dfs(int(input("Enter Start index: ")))
    elif choice==2:
        graph.reset()
        index=int(input("Enter Start index: "))
        graph.visited[index] = True
        graph.bfs(index)
    else:
        print("Enter valid choice\n")
'''
    2
  /   \
0     1
 \   /
   3
   |
   4
'''