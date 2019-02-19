#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-11-08 14:18:01
# 
def _buildMap(s):
    m = {}
    for index, value in enumerate(s):
        if value in m:
            m[value].append(index)
        else:
            m[value] = [index]
    return m

def _isSubsequence(s, w):
    index_s = -1
    for index_w, value in enumerate(w):
        if value not in s or s[value][-1] <= index_s:
            return False
        for i in s[value]:
            if i > index_s:
                index_s = i
                break
    return True

def longestSubsequence(s, d):
    s = _buildMap(s)
    d.sort(key=lambda w: len(w), reverse=True)
    for w in d:
        if _isSubsequence(s, w):
            return w
    return None


if __name__ == '__main__':
    print longestSubsequence('abppplee', ["able", "ale", "apple", "bale", "kangaroo"])
