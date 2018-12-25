class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        begin = 0
        end = 0
        count = 0
        size = 0
        
        while end<len(s):
            if count >= 0:
                if s[end] == '(':
                    count += 1
                else:
                    count -= 1
                end += 1
                if count == 0 and end - begin > size:
                    size = end - begin
            
            if count < 0:
                if s[begin] == '(':
                    count -= 1
                else:
                    count += 1
                begin += 1
        
        if count > 0:
            s=s[::-1]
            replace_len = len(s) - begin - 1
            begin = 0
            end = 0
            count = 0
            #size = 0
            
            while end < replace_len:
                if count >= 0:
                    if s[end] == ')':
                        count += 1
                    else:
                        count -= 1
                    end += 1
            
                if count < 0:
                    if s[begin] == ')':
                        count -= 1
                    else:
                        count += 1
                    begin += 1
                elif count == 0:
                    if end - begin > size:
                        size = end - begin
        
        return size
