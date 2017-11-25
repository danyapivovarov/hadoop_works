#!/usr/bin/env python2
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

with open('stop_words_en.txt', 'r') as stop_file:
    stop_words_str=stop_file.read()
stop_words_list = re.split('\n', stop_words_str, flags=re.UNICODE)

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue
    
    text = re.sub("^\W+|\W+$", "", text, flags=re.UNICODE)    
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    
    for word in words:
        word = word.lower()
        '''if word in stop_words_list:
            print >> sys.stderr, "reporter:counter:Words stat,Stop words,%d" % 1
        else:
            key = ''.join(sorted(word))
            print "%s\t%s\t%d" % (key, word, 1)'''
        if not(word in stop_words_list):
            key = ''.join(sorted(word))
            print "%s\t%s\t%d" % (key, word, 1)