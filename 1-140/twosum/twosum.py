#edit by crazydyz(http://www.crazydyz.cc)
class Solution:
    # @return a tuple, (index1, index2)
    #O(n^2)
    def twoSum(self, num, target):
        process={}
        for index in range(len(num)):
            if target-num[index] in process:
                return (process[target-num[index]]+1,index+1)
            process[num[index]]=index

print Solution().twoSum([0,1],1)
