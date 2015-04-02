#!/usr/bin/python 
#Filename:Letter_Combinations_of_a_Phone_Number.py

class Solution:
    def letterCombinations(self,digits):
        list={
                '2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z'],
                '0':['_']
                }
        self.list=list
        if len(digits)==0:
            return []
        res=list[digits[0]]
        while len(digits)!=1:
            digits=digits[1:]
            res=self.combinations(digits,res)
        return res
    def combinations(self,digits,res):
        result=[]
        for i in res:
            for j in self.list[digits[0]]:
                result.append(i+j)
        return result

digits='23'
print Solution().letterCombinations(digits)
