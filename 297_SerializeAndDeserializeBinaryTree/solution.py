# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    @classmethod
    def _dfs_serialize(cls, node, data):
        if node is None:
            data.append(' ')
            return
        
        data.append(str(node.val))
        cls._dfs_serialize(node.left, data)
        cls._dfs_serialize(node.right, data)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        self._dfs_serialize(root, data)
        ans = ':'.join(data)
        print(ans)
        return ans
    
    @classmethod
    def _dfs_deserialize(cls, data):
        val = data.pop(0)
        if val == ' ':
            return None
        
        node = TreeNode(int(val))
        node.left = cls._dfs_deserialize(data)
        node.right = cls._dfs_deserialize(data)
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = list(data.split(':'))
        return self._dfs_deserialize(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
