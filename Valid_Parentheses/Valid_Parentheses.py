class Solution:
    # @param s, a string
    # @return a boolean
    def isValid(self, s):
        a=''
        for i in s:
            if i in ['(','[','{']:
                a=i+a
            if i in [')',']','}']:
                if len(a)==0:
                    return False
                if not ((a[0]=='(' and i==')') or (a[0]=='[' and i==']') or (a[0]=='{' and i=='}')):
                    return False
                a=a[1:]
        if a=='':
            return True
        else:
            return False
s='()[]{}'
print Solution().isValid(s)
