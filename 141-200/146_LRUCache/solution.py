#!/usr/bin/python
# coding=utf-8
#
# Title: 146, LRU Cache
# Author: Lucas
# Date: 2018-04-30 11:47:42
#
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return "<Node %d: %d>" % (self.key, self.val)


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.newest = Node(-2, -2)
        self.oldest = Node(-3, -3)
        self.newest.next = self.oldest
        self.oldest.prev = self.newest

        self.len = 0
        self.cap = capacity

        self.location = {}

    def _remove(self, node):
        """Remove from list"""
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def _add(self, node):
        node.next = self.newest.next
        node.prev = self.newest
        self.newest.next.prev = node
        self.newest.next = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.location:
            return -1

        node = self.location[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.location:
            self.location[key].val = value
            self.get(key)
            return

        if self.cap == 0:
            return

        if self.len >= self.cap:
            del self.location[self.oldest.prev.key]
            self._remove(self.oldest.prev)
            self.len -= 1

        node = Node(key, value)
        self._add(node)
        self.location[key] = node
        self.len += 1


if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(2, 1)
    obj.put(2, 2)
    print(obj.get(2))
    obj.put(1, 1)
    obj.put(4, 1)
    print(obj.get(2))
