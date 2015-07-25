# -*- coding: utf-8 -*-
import re,codecs
from collections import Counter
import operator
from gensim import corpora

class StandardFormMaker:
    def __init__(self,lines):
        self._formMap = {}
        for line in lines:
            self._appendWords(line)

    def _appendWords(self,wordsList):
        stForm = wordsList[0]
        for form in wordsList:
            self._formMap[form] = stForm

    def getForm(self,word):
        return self._formMap.get(word,word)

    def getStandardFormSet(self):
        return set(self._formMap.values())

if __name__=='__main__':
    texts = re.split("#\d+", " ".join(map(lambda x: re.sub("[\\n\\r\,\.\:-]","",x), codecs.open("pap.txt",encoding="utf-8"))))

    odm = map(lambda x: re.sub("[\\n\\r]","",x).split(", "),codecs.open("odm.txt",encoding="utf-8"))
    normForm = StandardFormMaker(odm)
    preparedtexts = map(lambda x: x.split(),
        map(lambda x:
            " ".join(filter(lambda z: z!=None,map(lambda y: normForm.getForm(y)
            ,x.split())))
            ,texts))
    dictionary = corpora.Dictionary(preparedtexts)
    dictionary.filter_extremes(1,0.7)
    dictionary.save('pap.dict')
    corpus = [dictionary.doc2bow(text) for text in preparedtexts]
    corpora.MmCorpus.serialize('corpus.mm',corpus)


