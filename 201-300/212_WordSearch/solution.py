from collections import defaultdict


class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}


class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        if not board or not board[0]:
            return []

        self.board = board
        self.positions = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.positions[board[i][j]].append((i, j))

        root = Node('')
        for word in words:
            node = root
            for c in word + '\0':
                if c not in node.children:
                    node.children[c] = Node(c)
                node = node.children[c]

        self.word = []
        self.result = []
        self.visited = set()

        self._dfs_search(None, root)

        return sorted(list(set(self.result)))

    def _dfs_search(self, start, node):
        if start is None:
            for child in node.children.values():
                for start in self.positions[child.val]:
                    self._dfs_search(start, child)
            return

        self.word.append(node.val)
        self.visited.add(start)

        if '\0' in node.children:
            self.result.append(''.join(self.word))

        x, y = start
        for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if (i, j) in self.visited:
                continue
            if i < 0 or j < 0 or i >= len(self.board) or j >= len(self.board[0]):
                continue

            if self.board[i][j] in node.children:
                self._dfs_search((i, j), node.children[self.board[i][j]])

        self.word.pop()
        self.visited.remove(start)

