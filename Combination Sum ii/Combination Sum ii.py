import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
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
            elif i == target and (not [i] in result):
                result.append([i])
            new_candidates = candidates[candidates.index(i)+1:]
            temp_result = self.combinationSum2(new_candidates, target - i)
            for j in range(len(temp_result)):
                temp_result[j].append(i)
                temp_result[j].sort()
                if not temp_result[j] in result:
                    result.append(temp_result[j])

        return result
