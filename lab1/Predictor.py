import json,sys,math

class Predictor:
    def __init__(self):
        self.stats = {}
        self.langFiles = {
            'polish':'polish.json',
            'german':'german.json',
            'finnish':'finnish.json',
            'spanish':'spanish.json',
            'english':'english.json',
            'italian':'italian.json'}

        for k,v in self.langFiles.iteritems():
            f = file(v)
            self.stats[k] = json.load(f)
            f.close()


    def ngrams_from_sentence(self,sentence,n=4):
        vector = {}
        words = sentence.split()
        for word in words:
            tmp = word
            while len(tmp)>=n:
                vector[tmp[:n]] = vector.get(tmp,0)+1
                tmp = tmp[1:]
        return vector

    def get_vectors(self,ngrams):
        '''
        @type ngrams: dict
        '''

        vectors = {
        'polish':[],
        'german':[],
        'finnish':[],
        'spanish':[],
        'english':[],
        'italian':[]
        }

        for ngram in ngrams.iterkeys():
            for lang in vectors.iterkeys():
                vectors[lang].append(self.stats[lang].get(ngram,0))

        return vectors

    def vlen(self,v):
        return math.sqrt(reduce(lambda x,y : x + y**2,v,0))


    def metric(self,a,b):
        c = zip(a,b)
        v = reduce(lambda x,y: x + y[0]*y[1],c,0)
        l = (self.vlen(a)*self.vlen(b))
        return v/l if l!=0 else 0


    def find(self,ngram,vectors):
        max = 0
        lang = ''
        for k,v in vectors.iteritems():
            val = self.metric(ngram,v)
            print k,val
            # print val
            if val>max:
                max = val
                lang = k
        return lang




if __name__ == '__main__':
    print "write sentence"
    sentence = sys.stdin.readline()
    pred = Predictor()
    ngrams = pred.ngrams_from_sentence(sentence)

    vectors = pred.get_vectors(ngrams)

    print pred.find(ngrams.values(), vectors)





