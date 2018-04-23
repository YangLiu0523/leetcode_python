#!/usr/bin/python
#Filename:Longest_Common_Prefix.py

class Solution:
    def longestCommonPrefix(self,strs):
        if len(strs)==0:
            return ''
        elif len(strs)==1:
            return strs[0]
        stlength=len(strs[0])

        for i in range(len(strs)):
            stlength=min(len(strs[i]),stlength)
        if stlength==0:
            return ''
        
        for i in range(stlength):
            for j in range(1,len(strs)):
                if strs[0][i]!=strs[j][i]:
                    return strs[0][0:i]
        return strs[0][0:stlength]

strs=['c','c']
print Solution().longestCommonPrefix(strs)
