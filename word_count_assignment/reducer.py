#!/usr/bin/env python

import sys

def update_top(top_list, pair):
    top_list.append(pair)
    sorted_by_value = sorted(top_list, key=lambda tup: tup[1], reverse=True)
    return sorted_by_value[:10]  

current_key = None
word_sum = 0
global_counter = 0

top_seven = []

for line in sys.stdin:
    try:
        key, count = line.strip().split('\t', 1)
        count = int(count)
    except ValueError as e:
        continue
    if current_key != key:
        if current_key:
            top_seven = update_top(top_seven, (current_key, word_sum))
            global_counter += word_sum
        word_sum = 0
        current_key = key
    word_sum += count

if current_key:
    top_seven = update_top(top_seven, (current_key, word_sum))
    global_counter += word_sum

#print global_counter
#print top_seven
print "%s\t%d" % (top_seven[6][0], top_seven[6][1])

'''for key, val in top_seven:
    print '%s\t%s' % (key, val)'''