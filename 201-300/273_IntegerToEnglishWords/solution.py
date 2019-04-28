#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-03-02 16:26:41


class Solution:
    NUMBERS_1 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    NUMBERS_2 = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    NUMBERS_3 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    def _less_than_thousand(self, num):
        words = []

        hundred = self.NUMBERS_1[num // 100]
        if hundred:
            words.append(hundred)
            words.append('Hundred')
        num = num % 100

        if 10 <= num < 20:
            words.append(self.NUMBERS_3[num-10])
            return words

        teens = self.NUMBERS_2[num // 10]
        if teens:
            words.append(teens)
        num = num % 10

        bit = self.NUMBERS_1[num]
        if bit:
            words.append(bit)

        return words

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        words = []
        billion = self._less_than_thousand(num // (10 ** 9))
        if billion:
            words.extend(billion)
            words.append('Billion')
        num = num % (10 ** 9)

        million = self._less_than_thousand(num // (10 ** 6))
        if million:
            words.extend(million)
            words.append('Million')
        num = num % (10 ** 6)

        thousand = self._less_than_thousand(num // (10 ** 3))
        if thousand:
            words.extend(thousand)
            words.append('Thousand')
        num = num % (10 ** 3)

        words.extend(self._less_than_thousand(num))
        return ' '.join(words)
