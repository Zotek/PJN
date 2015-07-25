# -*- coding: utf-8 -*-
#!/usr/bin/env python

# from __future__ import print_function
from bayes import BayesClasifier
import sys
from levenshtein import levenshtein
from operator import itemgetter
from heapq import nsmallest
import codecs



def correct(dictionary,word):
    bc = BayesClasifier('dramat.iso.utf8',62715,'bledy.txt')
    lines = [line for line in codecs.open(dictionary,encoding="utf-8")]
    lines_map = {}
    i = 0
    for line in lines:
        lines_map[line] = -bc.probability_cw(word,line)
        i+=1
        if i%10000==0: print (i*100)/len(lines),"%"
    for line, score in nsmallest(5, lines_map.items(), key=itemgetter(1)):
        print line, " : ", score

if __name__=='__main__':
    correct("d2.txt",u"nienlenzy")