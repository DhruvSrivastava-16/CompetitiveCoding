#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:42:22 2021

@author: dhruv
"""

class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
            
        self.gdict = gdict
        
    def findedges(self):
        edgename = []
        for v in self.gdict:
            for i in self.gdict[v]:
                if {v,i} not in edgename:
                    edgename.append({v,i})
            
        return edgename
        
    def edges(self):
        return self.findedges()
        
G = {'a' : ['b','c'],'b' : ['c','a']}

s = Graph(G)
print (s.edges())