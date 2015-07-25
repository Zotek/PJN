# -*- coding: utf-8 -*-
import re,codecs

class StandardFormMaker:
    def __init__(self,lines):
        self._formMap = {}
        for line in lines:
            self._appendWords(line)

    def _appendWords(self,wordsList):
        stForm = wordsList[0].lower()
        for form in wordsList:
            self._formMap[form.lower()] = stForm

    def getForm(self,word):
        return self._formMap.get(word.lower(),word)

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


