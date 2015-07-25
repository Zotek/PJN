import json


files = {
    'polish':['polski','polski2','polski3'],
    'english':["Harry Potter 1 Sorcerer's_Stone","Harry Potter 2 Chamber_of_Secrets","Harry Potter 3 Prisoner of Azkaban","Harry Potter 4 and the Goblet of Fire"],
    'finnish':['finnish','finnish1'],
    'spanish':['spanish','spanish1'],
    'german':['2momm10','4momm10','5momm10','8momm10'],
    'italian':['54','q']
}

def build_ngrams(word,n=4):
    ngramslist = []
    tmp = word
    while len(tmp)>n:
        ngramslist.append(tmp[:n])
        tmp = tmp[1:]
    return ngramslist

def buildstatistic(files):
    ngramsletters = {}

    lines = []
    for f in files:
        fd = file(f+".txt")
        lines.append(fd.readlines())
        fd.close()
    lines = [unicode(line, errors='replace') for inner_list in lines for line in inner_list]
    for line in lines:
        words = list(line.split())
        ngrams = [x for inner_list in map(build_ngrams,words) for x in inner_list]
        for ngram in ngrams:
            ngramsletters[ngram] = ngramsletters.get(ngram,0)+1
    return ngramsletters

for k,v in files.iteritems():
    stat = buildstatistic(v)
    f = file(k+".json","w")
    json.dump(stat,f)

