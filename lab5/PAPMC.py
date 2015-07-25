# -*- coding: utf-8 -*-
from NgramBuilder import NgramBuilder
from MarkovChainBuilder import MarkovChainBuilder
import codecs
import re

__SENTENCES = True

lines = (filter(lambda x: not x.startswith("#"), codecs.open("pap.txt",encoding="utf-8")))
sentences = re.sub("[\\r\\n\,\:\'\"\(\\-)]",""," ".join(lines)).split(". ")
words = map(lambda x: x.split(" "),sentences)
if not __SENTENCES:
    words = [item for sublist in words for item in sublist]
ngb = NgramBuilder()
chains = ngb.build_ngram_chains(words)
mcb = MarkovChainBuilder()
MC = mcb.buildChain(chains)
curr = MC.takeSample()
l = []
for i in range(15):
    picked = MC.pickRandom(curr)
    if picked==None:
        break
    l.append(picked)
    curr = picked

if __SENTENCES:
    sep = " "
else:
    sep = ""

print sep.join(map(lambda x:unicode(x[0]),l))
