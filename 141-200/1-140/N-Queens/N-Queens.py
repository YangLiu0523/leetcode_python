class Solution(object):
    def solveNQueens(self, n):
        queen_map = {1<<i: ('.' * i + 'Q' + '.' * (n - i - 1)) for i in range(n)}
        cases = [[[], 0, 0, 0]]
        fil = (1 << n) - 1

        for _ in range(n):
            new_cases = []
            for record, row, ld, rd in cases:
                ld = (ld << 1) & fil
                rd = rd >> 1
                pos = (~(ld | rd | row)) & fil
                while pos:
                    p = pos & (~pos + 1)
                    pos = pos - p
                    new_cases.append([record + [p], row + p, ld + p, rd + p])
            cases = new_cases

        return [[queen_map[i] for i in case[0]] for case in cases]


if __name__ == '__main__':
    Solution().solveNQueens(11)
