#!/usr/bin/env python

import glob
from collections import Counter
from stopwords import allStopWords
import string

all_files = glob.glob('../Gutenberg SF/*.*')
def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()
datasource = dict((file_name, file_contents(file_name)) for file_name in all_files)

results = Counter()

def get_word_count(content):
    words = []
    for w in v.split():
        # remove punctuation and convert to lowercase
        word = w.translate(None, string.punctuation).lower()

        if len(word) > 1 and word not in allStopWords:
            words.append(word)

    return Counter(words)

for k,v in datasource.items():
    result = get_word_count(v)
    # add each word with its count to the results 
    for x,y in result.items():
        results[x] += y

# sort results from high to low
results = sorted(results.items(), key=lambda x: x[1], reverse=True)

# show a nice top 10
for x in results[:10]:
    print x[0] + ' ' + str(x[1])
