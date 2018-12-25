class Solution(object):
    def judge(self,s):
        begin = 0
        end = 0
        for i in range(len(s)):
            if s[i] == '(':
                begin += 1
            else:
                end += 1
            if end > begin:
                return False
        
        if end == begin:
            #print s
            return True
        else:
            return False
        
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = 0
        for i in range(len(s)-1,-1,-1):
            for j in range(i):
                if self.judge(s[j:i]) and i - j > size:
                    size = i - j
                    break
        return size            
