#!/usr/bin/python
# coding=utf-8
#
# Title:    Jewelry from TopCoder
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-22 23:11:42
#
class Jewelry(object):
    def howMany(self, values):
        values.sort()
        width = sum(values)
        # no_bob[value + width]
        no_frank = [0] * (width * 2 + 1)
        no_frank[0 + width] = 1
        # yes_bob[value + width]
        yes_frank = [0] * (width * 2 + 1)
        temp_frank = [0] * (width * 2 + 1)
        last_value = 0

        for value in values:
            new_no_frank = [0] * (2 * width + 1)
            new_yes_frank = [0] * (2 * width + 1)
            new_temp_frank = [0] * (width * 2 + 1)

            for i in range(-width / 2, width / 2 + 1):
                new_no_frank[i + width] += no_frank[i + width]
                new_yes_frank[i + width] += yes_frank[i + width]
                if last_value == value:
                    new_temp_frank[i + width] += temp_frank[i + width]

                if i + value <= width:
                    new_no_frank[i + width] += no_frank[i + value + width]
                    if last_value == value:
                        new_yes_frank[i + width] += temp_frank[i + value + width]
                        new_temp_frank[i + width] += temp_frank[i + value + width]

                if i - value >= -width:
                    new_yes_frank[i + width] += yes_frank[i - value + width]
                    new_yes_frank[i + width] += no_frank[i - value + width]
                    new_temp_frank[i + width] += no_frank[i - value + width]
                    if last_value == value:
                        new_temp_frank[i + width] += temp_frank[i - value + width]

            no_frank = new_no_frank
            yes_frank = new_yes_frank
            temp_frank = new_temp_frank
            last_value = value

        return yes_frank[width]


if __name__ == '__main__':
    # cases = [1, 2, 5, 3, 4, 5]
    # cases = [1, 2, 3, 4, 5, 5]
    # cases = [7, 7, 8, 9, 10, 11, 1, 2, 2, 3, 4, 5, 6]
    cases = [
        1000, 1000, 1000, 1000, 1000,
        1000, 1000, 1000, 1000, 1000,
        1000, 1000, 1000, 1000, 1000,
        1000, 1000, 1000, 1000, 1000,
        1000, 1000, 1000, 1000, 1000,
        1000, 1000, 1000, 1000, 1000,
    ]
    print Jewelry().howMany(cases)
