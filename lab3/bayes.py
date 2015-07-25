# -*- coding: utf-8 -*-
from __future__ import division
import codecs
import re
from levenshtein import levenshtein


class BayesClasifier:
    def __init__(self,corpfile,formcount,errorfile):
        self.word_count = 0
        self.word_occurences = {}
        self.accepted_form_count = formcount
        self.error_occurences = {}
        f=codecs.open(corpfile,encoding="utf-8")
        for line in f:
            line = self._prepare_line(line)
            for word in re.split("\\s",line):
                self.word_occurences[word] = self.word_occurences.get(word,0)+1
                self.word_count+=1
        f=codecs.open(errorfile,encoding="utf-8")
        self.error_count = 0
        for line in f:
            self.error_count+=1
            splited = line.split(";")
            lev = levenshtein(splited[0],splited[1])
            self.error_occurences[lev] = self.error_occurences.get(lev,0)+1



    def _probability_c(self,correct):
        a = self.word_occurences.get(correct,0)
        return (a+1)/(self.word_count+self.accepted_form_count)

    def _probability_wc(self,word, correct):
        lev = levenshtein(word,correct)
        return self.error_occurences.get(lev,0)/self.error_count

    def probability_cw(self,word,correct):
        return self._probability_c(correct)*self._probability_wc(word,correct)

    def _prepare_line(self,line):
        "@type line: str"
        if(line.startswith("*")):
            return ""
        return re.sub(r"[.,]","",line)

if __name__ == '__main__':
    bc = BayesClasifier('dramat.iso.utf8',1374254,'bledy.txt')
    print bc.probability_cw(u"przedmiot",u"pszedmiot")