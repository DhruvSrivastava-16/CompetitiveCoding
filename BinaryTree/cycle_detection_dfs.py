# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 16:15:36 2021

@author: DHRUV
"""


from collections import defaultdict
 
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
 
       
        visited[v] = True
        recStack[v] = True
        
        for i in self.graph[v]:
            if not visited[i]:
                 if (self.isCyclicUtil(i, visited, recStack)):
                     return True
                 
            elif recStack[i] == True:
                return True
            
        recStack[v] = False
        
        return False
 
     
        
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        
        for i in range(0,self.V):
            if not visited[i]:
                if (self.isCyclicUtil(i,visited,recStack)):
                    return True
        
        return False
                
                
        
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)

g.addEdge(2, 3)

if (g.isCyclic()):
    print ("Graph has a cycle")
else:
    print ("Graph has no cycle")
 
# Thanks to Divyanshu Mehta for contributing this code