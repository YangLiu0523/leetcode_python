class Node(object):
    def __init__(self, value):
        self.value = str(value)

    def __gt__(self, another):
        a = self.value
        b = another.value
        return a + b > b + a


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nodes = [Node(n) for n in nums]
        nodes.sort(reverse=True)
        s = ''.join(n.value for n in nodes)
        start = 0
        while start < len(s) - 1 and s[start] == '0':
            start += 1
        return s[start:]


