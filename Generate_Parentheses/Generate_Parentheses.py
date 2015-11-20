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
            i='(('+i
            #print i
            first=i.index(')')
            for j in range(1,first):
                #i[j]=')'
                new=i[:j]+')'#+i[i.index(')')+1:]
                #raw_input(i)
                if j+1!=len(i):
                    new+=i[j+1:]
                if not new in list_now:
                    list_now.append(new)
        return list_now

print Solution().generateParenthesis(1)
print Solution().generateParenthesis(2)
print Solution().generateParenthesis(3)
