
import io, sys
from math import log

from nltk.corpus import wordnet as wn

def sense_entropy(lemma):
    ss = wn.synsets(lemma)
    if len(ss) == 0:
        return 0
    _h = 1/float(len(ss))
    return sum([_h*log(_h,2)]*8)

infile = sys.argv[1]
with io.open(infile, 'r', encoding='utf8') as fin:
    for line in fin:
        lemma, sent = line.split(' <s> ')
        print lemma, sense_entropy(lemma)
