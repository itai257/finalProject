import numpy

class GenerateNGramsFromTexts:
    NG = []
    docs_ngram = []
    def __init__(self, documents, n):
        for doc in documents:
            single_doc_ngram = []
            distinct_single_doc_ngram = []
            for p in range(len(doc)-n):
                gram = doc[p:p+n]
                single_doc_ngram.append(gram)
            self.NG = numpy.unique(self.NG+single_doc_ngram).tolist()
