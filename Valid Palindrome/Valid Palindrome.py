class Solution(object):
    def isPalindrome(self, s):
        for i in string.punctuation+' ':
            s = s.replace(i,"")
        s = s.lower()
        if s == s[::-1]:
            return True
        return False
