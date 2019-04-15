from typing import List


class Solution:
    def _helper(self, prefix, prev, diff, num):
        if not num:
            yield prefix, prev
            return StopIteration

        # TODO: num starts with zero

        if not prefix:
            for i in range(1, len(num) + 1):
                start = num[:i]
                if len(start) > 1 and start[0] == '0':
                    break
                for s, v in self._helper(start, int(start), int(start), num[i:]):
                    yield s, v
            return StopIteration

        for i in range(1, len(num) + 1):
            start = num[:i]
            if len(start) > 1 and start[0] == '0':
                break
            for s, v in self._helper(prefix + '+' + start, prev + int(start), int(start), num[i:]):
                yield s, v
            for s, v in self._helper(prefix + '-' + start, prev - int(start), -int(start), num[i:]):
                yield s, v
            mul_diff = diff * int(start)
            for s, v in self._helper(prefix + '*' + start, (prev - diff) + mul_diff, mul_diff, num[i:]):
                yield s, v



    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        for s, v in self._helper('', 0, 0, num):
            if v == target:
                ans.append(s)
        return ans


def main():
    cases = [
        # ("123456789", 45),
        ("105", 5),
        ("000", 0)
    ]
    for case in cases:
        print(case, Solution().addOperators(*case))


if __name__ == '__main__':
    main()
