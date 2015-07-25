# -*- coding: utf-8 -*-
import re,codecs
from StandardFormMaker import StandardFormMaker
from collections import defaultdict
import math
import pickle

def createStoplist(f):
    with open(f) as sfile:
        stoplist = sfile.readlines()
    stoplist = map(lambda x: filter(lambda y: y!='\n',x),stoplist)
    return set(stoplist)

def makeGraph(text,k):
    graph = defaultdict(lambda : defaultdict(int))
    while len(text)>0:
        tmp = text[:k]
        for word in tmp:
            graph[text[0]][word]+=1
        text = text[1:]
    return graph

def makeGraphs(texts,k):
    graphs = []
    for text in texts:
        graphs.append(makeGraph(text,k))

    return graphs

def vlen(v):
    return math.sqrt(reduce(lambda x,y : x + y**2,v,0))

def metric(a,b):
    c = zip(a,b)
    v = reduce(lambda x,y: x + y[0]*y[1],c,0)
    l = (vlen(a)*vlen(b))
    return v/l if l!=0 else 0

def nodeMetric(n1,n2):
    v=0
    v1l,v2l=0,0
    for word,n in n1.items():
        v+= n2.get(word,0)*n
        v1l+=n**2
        v2l+=n2.get(word,0)**2
    v1l=math.sqrt(v1l)
    v2l=math.sqrt(v2l)
    l = v1l*v2l
    return v/l if l !=0 else 0

def graphMetric(g1,g2):
    x=[]
    for word,node2 in g2.items():
        node1 = g1.get(word,{})
        x.append(nodeMetric(node1,node2))
    return float(sum(x))/len(x) if len(x) > 0 else 0


texts = re.split("#\d+", " ".join(map(lambda x: re.sub("[\\n\\r\,\.\:\-\(\)\[\]]","",x), codecs.open("pap.txt",encoding="utf-8"))))
odm = map(lambda x: re.sub("[\\n\\r]","",x).split(", "),codecs.open("odm.txt",encoding="utf-8"))
normForm = StandardFormMaker([])
stoplist = createStoplist("stoplist.txt")
preparedtexts = map(lambda x: x.split(),
        map(lambda x:
            " ".join(filter(lambda z: z!=None ,map(lambda y: normForm.getForm(y.lower())
            ,x.split())))
            ,texts))

K,NoteID,TOP = 3,2,10

preparedtexts = map(lambda x: filter(lambda y: y.lower() not in stoplist, x),preparedtexts)
graphs = makeGraphs(preparedtexts,K)
graphs = map(lambda x : dict(map(lambda x:
         (x[0],dict(x[1]))
         ,x.items())),graphs)




myNote = graphs[NoteID]

ls = []

for i,note in enumerate(graphs):
    ls.append((i,graphMetric(myNote,note)))

ls.sort(key=lambda x: x[1],reverse=True)
print ls[:TOP]



# pickle.dump(graph,open("graph.dat", "wb"))



