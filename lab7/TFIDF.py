# -*- coding: utf-8 -*-
from __future__ import division
from StandardFormMaker import StandardFormMaker
from collections import Counter
import re,codecs
import operator
import math


class TFIDFMatrix:
    def __init__(self, texts,normalizer):
        self.N = len(texts)
        self.docCounts=map(lambda x: Counter(x.lower().split()),texts)
        self.corpCounts = Counter(" ".join(texts).lower().split())
        self.tfidf=map(lambda x:dict([(y,self.corpCounts[y]*math.log1p(len(texts)/x[y])) for y in x.elements()]),self.docCounts)
        self.normalizer = normalizer

    def getKeywords(self,noteNr,n):
        try:
            tfidf = self.tfidf[noteNr]
        except IndexError:
            return None
        return sorted(tfidf.items(),key=operator.itemgetter(1))[:n]

    def makeMetricsForNewText(self,text):
        words = filter(lambda y: y!=None,map(lambda x:self.normalizer.getForm(x),text.split()))
        counts = Counter(words)
        metrics = dict([(y,self.corpCounts[y]*math.log1p(self.N/counts[y])) for y in counts.elements()])
        return metrics

    def vlen(self,v):
        return math.sqrt(reduce(lambda x,y : x + y**2,v,0))

    def metric(self,a,b):
        c = zip(a,b)
        v = reduce(lambda x,y: x + y[0]*y[1],c,0)
        l = (self.vlen(a)*self.vlen(b))
        return v/l if l!=0 else 0

    def findNoteByWords(self,text,ignore=None):
        newMetric = self.makeMetricsForNewText(text)
        print newMetric
        a=map(lambda x: 1/x,newMetric.values())
        max = 0
        maxi = None

        for i,x in enumerate(self.tfidf):
            if i == ignore:
                continue
            b = []
            for y in newMetric:
                m = 1/x[y] if y in x else 0
                b.append(m)
            met = self.metric(a,b)
            if met>max:
                maxi = i
                max = met

        return maxi

    def findSimiliarNote(self,n):
        note = self.getKeywords(n,20)
        return self.findNoteByWords(" ".join(dict(note).keys()),ignore=n)


if __name__ == '__main__':
    texts = re.split("#\d+", " ".join(map(lambda x: re.sub("[\\n\\r\,\.\:-]","",x), codecs.open("t.txt",encoding="utf-8"))))

    odm = map(lambda x: re.sub("[\\n\\r]","",x).split(", "),codecs.open("odm.txt",encoding="utf-8"))
    normForm = StandardFormMaker(odm)
    preparedtexts = map(lambda x:
                " ".join(filter(lambda z: z!=None,map(lambda y: normForm.getForm(y)
                ,x.split())))
                ,texts)


    tfidf = TFIDFMatrix(preparedtexts,normForm)

    print tfidf.makeMetricsForNewText("Dzisiaj byłem sobie w szkole i bardzo się nudziłem dlatego też nie siedziałem tam zbyt długo bo na polskim były same nudy i gdybym jeszcze tam dłużej siedział to bym nie miał siły")
