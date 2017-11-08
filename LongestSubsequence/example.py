#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-08 14:40:56
# 
import collections


def find_longest_word_in_string(letters, words):
    letter_positions = collections.defaultdict(list)
    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)

    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0
        for letter in word:
            if letter not in letter_positions:
                break
            possible_posetions = [p for p in letter_positions[letter] if p >= pos]
            if not possible_posetions:
                break
            pos = possible_posetions[0] + 1
        else:
            return word

