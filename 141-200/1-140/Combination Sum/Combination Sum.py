class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        if candidates == []:
            return []

        for i in candidates:
            if i > target:
                break
            elif i == target:
                result.append([i])
            temp_result = self.combinationSum(candidates, target - i)
            for j in range(len(temp_result)):
                temp_result[j].append(i)
                temp_result[j].sort()
                if not temp_result[j] in result:
                    result.append(temp_result[j])

        return result

if __name__ == '__main__':
    print Solution().combinationSum([2,3,6,7], 7)
