#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-17 17:12:34
# 
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return 
        layer = [root]
        while layer:
            new_layer = []
            for i in range(len(layer) - 1):
                layer[i].next = layer[i+1]
                if layer[i].left:
                    new_layer.append(layer[i].left)
                if layer[i].right:
                    new_layer.append(layer[i].right)
            if layer[-1].left:
                new_layer.append(layer[-1].left)
            if layer[-1].right:
                new_layer.append(layer[-1].right)
            layer = new_layer
