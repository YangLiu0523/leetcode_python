#!/usr/bin/python
#Filename:3Sum_Closet.py

class Solution:
    def threeSumClosest(self,num,target):
        num.sort()
        small = num[0]+num[1]+num[2]
        for i in range(len(num)-2):
            j=i+1
            k=len(num)-1
            while k-j>=1:
                z=num[i]+num[j]+num[k]
                if abs(small-target)>abs(z-target):
                    small=z
                if z-target>0:
                    k=k-1
                else:
                    j=j+1
        return small



num=[1,1,1,2,3,2,321,123,32,142,4223,12342,1233,2,124,212,3,12,3,123,1,23,123,2,3,523,213,42,34,23,4,234,123,234,234,2,34,234,23,4]
target = 100
print Solution().threeSumClosest(num,target)
