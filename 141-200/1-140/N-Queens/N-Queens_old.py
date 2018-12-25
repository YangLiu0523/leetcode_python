import copy
class Solution(object):
    def nextNums(self,case,n):
        index = case.index(".")
        nums = []
        for i in range(n):
            flag = True
            if str(i) in case:
                flag = False
            for j in range(index):
                if i in [int(case[j]) - (index - j),int(case[j]) + (index - j)]:
                    flag = False
                    break
            if flag:
                nums.append(i)
        return (index,nums)
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        new_result = []
        for i in range(n):
            result.append(str(i)+'.'*(n-1))
        print result

        index = 0
        while index < n - 1:
            for i in result:
                index,nums = self.nextNums(i,n)
                for j in nums:
                    new_result.append(i[:index]+str(j)+'.'*(n-index-1))
            result = copy.deepcopy(new_result)
            new_result = []
        format_result = []
        for i in result:
            format_case = []
            for j in i:
                format_case.append('.'*int(j)+'Q'+'.'*(n-int(j)-1))
            format_result.append(format_case)

        return format_result
        
if __name__ == "__main__":
    #print Solution().nextNums("13..")
    print Solution().solveNQueens(1)
