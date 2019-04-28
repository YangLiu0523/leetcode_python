# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-01-19 15:47:04
"""
LeetCode

208. Implement Trie (Prefix Tree)
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.tree
        for c in (word + '\0'):
            if c not in node:
                node[c] = {}
            node = node[c]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.tree
        for c in (word + '\0'):
            if c not in node:
                return False
            node = node[c]
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.tree
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


def main():
    obj = Trie()
    obj.insert('apple')
    print(obj.search('apple'), True)
    print(obj.search('app'), False)
    print(obj.startsWith('app'), True)
    obj.insert('app')
    print(obj.search('app'), True)


if __name__ == '__main__':
    main()
