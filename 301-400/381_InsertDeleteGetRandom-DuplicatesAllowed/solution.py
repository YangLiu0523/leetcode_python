#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-24 21:44:57


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 0
        self.data = {}
        self.index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.data[self.n] = val
        if val not in self.index:
            self.index[val] = set()
        self.index[val].add(self.n)
        self.n += 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.index:
            return False
        i = self.index[val].pop()
        if not self.index[val]:
            self.index.pop(val)
        self.data.pop(i)

        if i != self.n - 1:
            v = self.data.pop(self.n - 1)
            self.data[i] = v
            self.index[v].remove(self.n - 1)
            self.index[v].add(i)
        self.n -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.data[random.randint(0, self.n-1)]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
