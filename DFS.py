#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:19:38 2021

@author: dhruv
"""


from collections import defaultdict

 
class Graph:
 
    # Constructor
    def __init__(self):
 
        self.g = defaultdict(list)
 
    def addEdge(self, u, v):
        self.g[u].append(v)
        
    def DFSUtil(self, v, visited):
        visited.append(v)
        print (" ",v)
        
        for i in self.g[v]:
            if i not in visited:
                self.DFSUtil(i,visited)
        print("V: ",v)
                
        return visited
        
        

        
    def DFS(self,root):
        visited = []
        
        ans =  self.DFSUtil(root,visited)
        return ans
        
        

g = Graph()
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
 
print("Following is DFS from (starting from vertex 2)")
ans = g.DFS(0)
 