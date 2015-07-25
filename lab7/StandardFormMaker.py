# -*- coding: utf-8 -*-
import re,codecs


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
    lines = map(lambda x: re.sub("[\\n\\r]","",x).split(", "),codecs.open("odm.txt",encoding="utf-8"))

    sfm = StandardFormMaker(lines)
    print sfm.getForm(u"piłek")
