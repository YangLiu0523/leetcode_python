class Solution(object):
    def solveNQueens(self, n):
        ret = []
        queen_map = {1<<i: ('.' * i + 'Q' + '.' * (n - i - 1)) for i in range(n)}
        ret = [[queen_map[i] for i in case[0]] for case in self._solve_by_3_list([[[], 0, 0, 0]], n)]
        return ret

    def _solve_by_3_list(self, cases, div):
        fil = (1 << div) - 1
        for _ in range(div):
            new_cases = []
            for record, row, ld, rd in cases:
                ld = (ld << 1) & fil
                rd = rd >> 1
                pos = (~(ld | rd | row)) & fil
                while pos:
                    p = pos & (~pos + 1)
                    pos = pos - p
                    new_cases.append([
                        record + [p],
                        row + p,
                        ld + p,
                        rd + p,
                    ])
            cases = new_cases
        return cases


if __name__ == '__main__':
    print Solution().solveNQueens(11)
