noteNr = 3
N=3
M=3
import math
import operator

def vlen(v):
    return math.sqrt(reduce(lambda x,y : x + y**2,v,0))

def metric(a,b):
    c = zip(a,b)
    v = reduce(lambda x,y: x + y[0]*y[1],c,0)
    l = (vlen(a)*vlen(b))
    return v/l if l!=0 else 0

def makeVec(d,n):
    vec = []
    for i in range(n):
        vec.append(d.get(i,0))
    return vec

from gensim import models,corpora
import logging


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = models.LsiModel.load('corp.lsi')


corpus = corpora.MmCorpus('corpus.mm')

noteVec = makeVec(dict(model[corpus[noteNr]]),50)

ddist = []

for i,doc in enumerate(corpus):
    if i==noteNr:
        continue

    vec = makeVec(dict(model[doc]),50)
    ddist.append((i,metric(noteVec,vec)))


ddist.sort(key=lambda x: x[1],reverse=True)

best = ddist[:N]

for x in best:
    print "#",x[0]
    topics = model[corpus[x[0]]]
    topics.sort(key=lambda x: x[1],reverse=True)
    for topic in topics[:M]:
        print model.print_topic(topic[0])



