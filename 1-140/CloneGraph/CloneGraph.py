#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-12-15 10:21:37
# 
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        
        # DFS
        dictGraph = {}
        queue = [node]
        visited = set()
        visited.add(node.label)
        while queue:
            n = queue.pop(0)
            neighbors = []
            for neighbor in n.neighbors:
                neighbors.append(neighbor.label)
                if neighbor.label not in visited:
                    visited.add(neighbor.label)
                    queue.append(neighbor)
            dictGraph[n.label] = neighbors
        
        # new graph
        graph = {}
        for k in dictGraph.keys():
            graph[k] = UndirectedGraphNode(k)
        for k in dictGraph.keys():
            for n in dictGraph[k]:
                graph[k].neighbors.append(graph[n])
        
        return graph[node.label]
