# -*- coding: utf-8 -*-
from MarkovChainBuilder import MarkovChainBuilder


class NgramBuilder:
    def build_ngrams(self,chain,n=2):
        ngramslist = []
        tmp = chain
        while len(tmp)>=n:
            ngramslist.append(tuple(tmp[:n]))
            tmp = tmp[1:]
        return ngramslist

    def build_ngram_chains(self,chainList):
        return map(self.build_ngrams,chainList)
