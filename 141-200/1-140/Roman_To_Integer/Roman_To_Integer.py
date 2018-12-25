#!/usr/bin/python
#Filename:Roman_To_Integer.py

class Solution:
    def romanToInt(self,s):
        value={
                'M':1000,
                'D':500,
                'C':100,
                'L':50,
                'X':10,
                'V':5,
                'I':1
                }
        key=['M','D','C','L','X','V','I']
        result=0
        while len(s)!=0:
            for i in key:
                if i in s:
                    j=0
                    while s[j]!=i:
                        j+=1
                    result+=value[i]
                    k=j
                    while j!=0:
                        result-=value[s[j-1]]
                        j=j-1
                    s=s[k+1:]
                    break
        return result

print Solution().romanToInt('MCMXCVI')
print Solution().romanToInt('XCVI')
print Solution().romanToInt('X')

