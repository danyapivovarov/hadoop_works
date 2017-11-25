#!/usr/bin/env python2
import sys

current_key = None
current_word = None
current_word_sum = 0
isInit = True
current_words = {}

#for line in sys.stdin:
#with open('for_reducer.txt') as f:
#    for line in f:
for line in sys.stdin:
    try:
        key, word, count = line.strip().split('\t', 2)
        count = int(count)
    except ValueError as e:
        continue

    if isInit:
        isInit = False
        current_key = key
        current_words[word] = 0
        current_words[word] += count
        continue

    if current_key != key:
        if current_key:
            total = sum(current_words.itervalues())
            unique = len(current_words.keys())

            if unique <= 1:
                print >> sys.stderr, "reporter:counter:Words stat,Single word,%d" % 1
            else:
                word_list = ','.join(sorted(current_words.keys()))
                print "%d\t%d\t%s" % (total, unique, word_list)
        current_words.clear()
        current_words[word] = 0
        current_key = key
    if word not in current_words:
        current_words[word] = 0
    current_words[word] += count

if current_key:
    total = sum(current_words.itervalues())
    unique = len(current_words.keys())

    if unique <= 1:
        print >> sys.stderr, "reporter:counter:Words stat,Single word,%d" % 1
    else:
        word_list = ','.join(sorted(current_words.keys()))
        print "%d\t%d\t%s" % (total, unique, word_list)
