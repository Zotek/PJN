from gensim import corpora,models,similarities

import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = corpora.Dictionary.load('pap.dict')
corpus = corpora.MmCorpus('corpus.mm')

tfidf = models.TfidfModel(corpus)

lsi = models.LsiModel(tfidf[corpus], id2word=dictionary,num_topics=50)
lsi.save('corp.lsi')

lda = models.LdaModel(tfidf[corpus],id2word=dictionary,num_topics=50)
lda.save('corp.lda')