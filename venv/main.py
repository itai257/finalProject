import codecs
import os
import numpy
import random
import string
import HausdorffMetricMatrix
from GenerateImpostors import GenerateImpostors
from GenerateNGramsFromTexts import GenerateNGramsFromTexts
PATH = "Corpus/"

def get_docs_without_punctuation(str):
    str = str.replace(',',' ')
    str = str.replace('.',' ')
    only_words = ''.join([x for x in str if x in string.ascii_letters + '\\\n\' '])
    only_words = [x.replace('\\','') for x in only_words.split()]
    doc = ''
    for w in only_words:
        doc += ' ' + w
    return doc

def get_mock_dist_matrix():
    dist = []
    for i in range(41):
        row = []
        for j in range(41):
            row.append(random.uniform(0, 100))
        dist.append(row)
    return dist

## ADD FILTERING TO SOME FILE TYPE (OPTIONAL)

text = []

for filename in os.listdir(PATH):
    # Open a file: file
    file = open(PATH+filename, mode='r+')
    # read all file
    file_content = file.read()
    # append text to array
    text.append(file_content)
    # close the file
    file.close()

#temp--
for t in text:
    t = get_docs_without_punctuation(t)
#
impostors = GenerateImpostors(text, 5).impostors
NG = GenerateNGramsFromTexts(impostors+text, 4).NG

D = HausdorffMetricMatrix(get_mock_dist_matrix())

