#!/usr/bin/env python
# coding: utf-8

# Q1.Breadth First Traversal for a Graph.

# In[3]:


import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal of Graph: ")
    bfs(graph, 0)


# Q2.Depth First Traversal for a Graph.

# In[4]:


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')


# Q3.Count the number of nodes at given level in a tree using BFS.

# In[7]:



class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
    
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    
    def BFS(self, s, l):
        visited = [False] * self.V
        level = [0] * self.V
        
        queue = []
        visited[s] = True
        queue.append(s)
        level[s] = 0
        
        count = 0
        while queue:
            s = queue.pop(0)
            for i in self.adj[s]:
                if not visited[i]:
                    level[i] = level[s] + 1
                    visited[i] = True
                    queue.append(i)
        
        for j in range(self.V):
            if level[j] == l:
                count += 1
        
        return count

n = int(input("Enter the number of nodes: "))
g = Graph(n)
for _ in range(n):
    level, data = map(int, input().split())
    g.addEdge(level, data)

level1 = int(input("Enter the level: "))
print(g.BFS(0, level1))


# Q4.Count number of trees in a forest.

# In[11]:




def add_edge(adj_matrix, u, v):
    adj_matrix[u].append(v)
    adj_matrix[v].append(u)

def dfs(u, adj_matrix, visited):
    visited[u] = True
    for i in range(len(adj_matrix[u])):
        if visited[adj_matrix[u][i]] == False:
            dfs(adj_matrix[u][i], adj_matrix, visited)

def countTrees(adj_matrix, V):
    visited = np.zeros(V, dtype=bool)
    res = 0
    for u in range(V):
        if visited[u] == False:
            dfs(u, adj_matrix, visited)
            res += 1
    return res

V = 5
adj_matrix = [[] for _ in range(V)]
add_edge(adj_matrix, 0, 1)
add_edge(adj_matrix, 0, 2)
add_edge(adj_matrix, 3, 4)
print("Counted Number Of Trees Are: ")
print(countTrees(adj_matrix, V))


# Q5.Detect Cycle in a Directed Graph.

# In[13]:


from enum import Enum

class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

def hasCycleDFS(graph, visited, node):
    visited[node] = Color.GRAY
    for neighbor in graph[node]:
        if visited[neighbor] == Color.GRAY:
            return True
        elif visited[neighbor] == Color.WHITE:
            if hasCycleDFS(graph, visited, neighbor):
                return True
    visited[node] = Color.BLACK
    return False

def hasCycle(graph):
    visited = {}
    for key in graph:
        visited[key] = Color.WHITE
    for key in graph:
        if visited[key] == Color.WHITE:
            if hasCycleDFS(graph, visited, key):
                return True
    return False

graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]
}

if hasCycle(graph):
    print("The graph has a cycle")
else:
    print("The graph does not have a cycle")


# In[ ]:




