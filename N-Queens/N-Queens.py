class Solution(object):
    def solveNQueens(self, n):
        ret = []
        for case in self._solve_by_3_list([[[-1] * n, [0] * n, [0] * n]], n, 0):
            solution = ['' for _ in range(n)]
            for i in range(n):
                solution[case[0][i]] = '.' * i + 'Q' + '.' * (n - i - 1)
            ret.append(solution)
        return ret

    def _solve_by_3_list(self, cases, div, n):
        if cases == [] or div == n:
            return cases
        new_cases = []
        for row, ld, rd in cases:
            ld = ld[1:] + [0]
            rd = [0] + rd[:-1]
            for i in range(div):
                if row[i] != -1 or ld[i] != 0 or rd[i] != 0:
                    continue
                new_cases.append([
                    row[:i] + [n] + row[i+1:],
                    ld[:i] + [1] + ld[i+1:],
                    rd[:i] + [1] + rd[i+1:],
                ])
        return self._solve_by_3_list(new_cases, div, n+1)


if __name__ == '__main__':
    print Solution().solveNQueens(9)
