# -*- coding: utf-8 -*-
from __future__ import division
import re,codecs,math
from StandardFormMaker import StandardFormMaker
from TFIDF import TFIDFMatrix



switch = 1

texts = re.split("#\d+", " ".join(map(lambda x: re.sub("[\\n\\r\,\.\:-]","",x), codecs.open("pap.txt",encoding="utf-8"))))

odm = map(lambda x: re.sub("[\\n\\r]","",x).split(", "),codecs.open("odm.txt",encoding="utf-8"))
normForm = StandardFormMaker(odm)
preparedtexts = map(lambda x:
            " ".join(filter(lambda z: z!=None,map(lambda y: normForm.getForm(y)
            ,x.split())))
            ,texts)


tfidf = TFIDFMatrix(preparedtexts,normForm)

if switch == 0:
    print tfidf.getKeywords(1,10)
elif switch == 1:
    print tfidf.findNoteByWords(u"AWS".lower())
elif switch == 2:
    a =tfidf.findSimiliarNote(2)
    print a
    print tfidf.getKeywords(a,10)
