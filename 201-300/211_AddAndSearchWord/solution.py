# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-03 21:14:41

class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}

    def add_child(self, val):
        if val not in self.children:
            self.children[val] = Node(val)

    def get_child(self, val):
        return self.children.get(val, None)


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('\0')

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word + '\0':
            node.add_child(c)
            node = node.get_child(c)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_from_node(self.root, word)

    def search_from_node(self, node, word):
        for index, c in enumerate(word + '\0'):
            if c == '.':
                for child in node.children.values():
                    if self.search_from_node(child, word[index+1:]):
                        return True
                return False
            node = node.get_child(c)
            if node is None:
                return False
        return True
