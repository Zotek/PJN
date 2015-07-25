from __future__ import division
import numpy as np
import random

class MarkovChainBuilder:
    def __buildDict(self, ngramChains):
        markovDict = {}
        ngramSet = set()
        for chain in ngramChains:
            first = None
            second = None
            for ngram in chain:
                first = second
                second = ngram
                ngramSet.add(second)
                if first==None:
                    continue
                if first not in markovDict:
                    markovDict[first] = {}
                markovDict[first][second] = markovDict[first].get(second,0)+1
        return markovDict,ngramSet

    def __buildLegend(self,ngramSet):
        index = 0
        legend = {}
        for ngram in ngramSet:
            legend[ngram] = index
            index+=1
        return legend


    def buildChain(self,ngramChains):
        markovDict,ngramSet = self.__buildDict(ngramChains)
        legend = self.__buildLegend(ngramSet)
        return MarkovChain(markovDict,legend)



mcb = MarkovChainBuilder()




class MarkovChain:
    def __init__(self, markovDict,legend):
        self.__d = markovDict
        random.seed()

    def getProbabilitiesForNgram(self,ngram):
        occurences = self.__d.get(ngram,{})
        if occurences=={}:
            return []
        occSum = reduce(lambda x,y :x+y,occurences.values())
        return map(lambda x: (x[0],x[1]/occSum),occurences.items())

    def __makeDistribution(self,probs):
        distributions = [0]
        for prob in probs:
            distributions.append(distributions[-1]+prob[1])

        l = [x[0] for x in probs]
        return zip(l,distributions)

    def pickRandom(self,ngram):
        distr = self.__makeDistribution(self.getProbabilitiesForNgram(ngram))
        x = random.random()
        last = None
        for tup in distr:
            if tup[1]>x:
                break
            last = tup[0]
        return last

    def takeSample(self):
        return random.choice(self.__d.keys())
