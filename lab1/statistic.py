from Predictor import Predictor

pred = Predictor()
f = file("polski.txt")
i=0
y=0
for line in f:
    ngrams = pred.ngrams_from_sentence(line)
    vectors = pred.get_vectors(ngrams)
    if pred.find(ngrams.values(),vectors) == 'polish':
        y+=1.0
    i+=1.0

print y/i