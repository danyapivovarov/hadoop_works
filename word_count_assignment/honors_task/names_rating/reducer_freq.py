#!/usr/bin/env python2
import sys

current_key = None
word_sum = 0
total = 0

with open('paart-00000') as f:
    tmp = f.readline()
total = int(tmp.strip().split('\t', 1)[1])

for line in sys.stdin:
    try:
        key, count = line.strip().split('\t', 1)
        count = int(count)
    except ValueError as e:
        continue
    if current_key != key:
        if current_key:
            freq = (word_sum / (total * 1.0)) * 100
            if freq < 0.5:
                print "%s\t%d\t%f" % (current_key, word_sum, freq)
        word_sum = 0
        current_key = key
    word_sum += count

if current_key:
    freq = (word_sum / (total * 1.0)) * 100
    if freq < 0.5:
        print "%s\t%d\t%f" % (current_key, word_sum, freq)