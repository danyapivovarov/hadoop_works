#!/usr/bin/env python2
import sys

total = 0
cur_word = None
cur_numb = 0
cur_numb_str = ''
prev_word = None
prev_numb = 0
init = True

with open('part-00000') as f:
    tmp = f.readline()
total = int(tmp.strip().split('\t', 1)[1])

with open('before_filter_sorted.txt') as f:
    for line in f:
    #for line in sys.stdin:
        try:
            cur_word, cur_numb_str = unicode(line.strip()).split('\t', 1)
            cur_numb = int(cur_numb_str)

            if cur_word == 'the':
                print 'the case'

            if cur_word[0].isupper():
                if cur_word.lower() == prev_word.lower():
                    if float(prev_numb)/total < 0.005:
                        print "%s\t%d" % (cur_word, cur_numb)
                else:
                    print "%s\t%d" % (cur_word, cur_numb)
            else:
                prev_word = cur_word
                prev_numb = cur_numb
        except ValueError as e:
            continue
