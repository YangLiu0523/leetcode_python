class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==1:
            return ['()']
        list_before=self.generateParenthesis(n-1)
        list_now=[]
        for i in list_before:
            if not i+'()' in list_now:
                list_now.append(i+'()')
            if not '()'+i in list_now:
                list_now.append('()'+i)
            if not '('+i+')' in list_now:
                list_now.append('('+i+')')
        return list_now

print Solution().generateParenthesis(1)
print Solution().generateParenthesis(2)
print Solution().generateParenthesis(3)
