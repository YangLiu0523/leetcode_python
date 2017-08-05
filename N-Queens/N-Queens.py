import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        init_case = [['x'] * n for _ in range(n)]
        return [[''.join(j) for j in i] for i in self._solve([init_case], 0)]
    
    def _solve(self, cases, count):
        if cases == [] or count >= len(cases[0]):
            return cases
        new_cases = []
        for case in cases:
            if not 'x' in case[count]:
                continue
            last = -1
            for _ in xrange(case[count].count('x')):
                last = case[count].index('x', last + 1)
                new_cases.append(self._add(case, count, last))
        return self._solve(new_cases, count+1)
        
    def _add(self, case, x, y):
        new_case = copy.deepcopy(case)
        new_case[x][y] = 'Q'
        for i in xrange(len(new_case)):
            if i != y:
                new_case[x][i] = '.'
            if i > x:
                new_case[i][y] = '.'
            if x + i < len(new_case) and y + i < len(new_case) and i != 0:
                new_case[x+i][y+i] = '.'
            if x + i < len(new_case) and y - i >= 0 and i != 0:
                new_case[x+i][y-i] = '.'
        return new_case


if __name__ == '__main__':
    print Solution().solveNQueens(2)
