class Solution(object):
    mapping = {
        '1': '1',
        '6': '9',
        '9': '6',
        '0': '0',
        '8': '8'
    }
    def _rotate_same(self, num):
        num = str(num)
        i = 0
        j = len(num) - 1
        while i <= j:
            if num[i] != self.mapping[num[j]]:
                return False
            i += 1
            j -= 1
        return True

    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        spe = ('0', '1', '6', '8', '9')
        index = [0] * 9
        ans = 0
        while True:
            num = int(''.join(spe[i] for i in index))
            if num > N:
                break
            if not self._rotate_same(num):
                ans += 1
            index[-1] += 1
            i = len(index) - 1
            while index[i] >= 5:
                index[i-1] += 1
                index[i] -= 5
                i -= 1
        return ans


def main():
    cases = [
        618
    ]
    for case in cases:
        print(case, Solution().confusingNumberII(case))


if __name__ == '__main__':
    main()
