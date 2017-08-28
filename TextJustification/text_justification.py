#!/usr/bin/python
# coding=utf-8
#
# Title:    Text Justification
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-28 22:53:39
#
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        line = []
        count = -1
        for w in words:
            if count + 1 + len(w) > maxWidth:
                lines.append([line, count])
                count = -1
                line = []
            count += 1 + len(w)
            line.append(w)
        
        ret = []
        for l, length in lines:
            if len(l) == 1:
                ret.append(l[0] + ' ' * (maxWidth - len(l[0])))
                continue
            spaces = (maxWidth - length) / (len(l) - 1) + 1
            additional_spaces = (maxWidth - length) % (len(l) - 1)
            s = ''
            for w in l[:-1]:
                if additional_spaces > 0:
                    s += w + ' ' * (spaces + 1)
                else:
                    s += w + ' ' * spaces
                additional_spaces -= 1
            ret.append(s + l[-1])
        ret.append((' '.join(line) + ' ' * maxWidth)[:maxWidth])
        return ret
