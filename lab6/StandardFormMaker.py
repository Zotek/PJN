# -*- coding: utf-8 -*-
import codecs
import re
import operator

class StandardFormMaker:

    def __init__(self,odm):
        self.__d={}
        self.__buildStStructure(odm)

    def __buildStStructure(self,odms):
        for o in odms:
            commonPrefix = self.__getCommonPrefix(o)
            self.__d[commonPrefix] = self.__d.get(commonPrefix,[]) + [o]

    def __getCommonPrefix(self,words):
        index = 0
        words = filter(lambda x : not x.startswith("nie"),words) + map(lambda x : x[3:],filter(lambda x : x.startswith("nie"),words))
        for z in zip(*words):
            if len(set(z))>1:
                break
            index+=1
        return words[0][:index]

    def getStandardForm(self,word):
        if word.startswith("nie"):
            word = word[3:]
        found = ""
        for prefix in self.__d.keys():
            if word.startswith(prefix) and len(prefix)>len(found):
                found = prefix

        for s in self.__d[found]:
            if word in s:
                return s[0]
        return None


lines = map(lambda x: re.sub("[\\n\\r]","",x).split(", "),codecs.open("odm.txt",encoding="utf-8"))
sfm = StandardFormMaker(lines)

corp = " ".join(map(lambda x: re.sub("[\\n\\r\,\.\:]","",x), codecs.open("a.txt",encoding="utf-8"))).split(" ")

occurences = {}
print len(corp)
i = 0
for word in corp:
    if i%50 == 0:
        print i
    stform = sfm.getStandardForm(word)
    occurences[stform] = occurences.get(stform,0)+1
    i+=1

sorted_x = sorted(occurences.items(),key=operator.itemgetter(1))

print sorted_x[:-20]