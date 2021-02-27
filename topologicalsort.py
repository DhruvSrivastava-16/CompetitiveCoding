#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:18:32 2021

@author: dhruv
"""

from collections import defaultdict


class Graph:
 
    # Constructor
    def __init__(self, vertices): 
        self.g = defaultdict(list)  # dictionary containing adjacency List 
        self.V = vertices 
 
    def addEdge(self, u, v):
        self.g[u].append(v)
        
    
    def DFSUtil(self,s,visited,stack):
        visited.append(s)
        
        for i in self.g[s]:
            if i not in visited:
                self.DFSUtil(i,visited,stack)
        
        stack.append(s)
        
    
    def topologicalsort(self,s):
        visited = []
        stack = []
        
        for i in range(self.V):
            if i not in visited:
                self.DFSUtil(i,visited,stack)
        
        return stack[::-1]
        

g = Graph(6)
g.addEdge(0, 2) 
g.addEdge(5, 0) 
#g.addEdge(4, 0) 
#g.addEdge(4, 1) 
g.addEdge(2, 3) 
#g.addEdge(3, 1) 
 
print("Following is DFS from (starting from vertex 2)")
ans = g.topologicalsort(0)
 
        
