# -*- coding: utf-8 -*-
from __future__ import division
# ↑グラフ描画次に使う数値が少数になるようにするため必要
import nltk

def bar_chart(categories, words, counts):
    "Plot a bar chart showing counts for each word by category"
    import pylab
    ind = pylab.arange(len(words))
    width = 1 / (len(categories) + 1)
    bar_groups = []
    colors = 'rgbcmyk'
    for c in range(len(categories)):
        color = colors[c % len(colors)]
        bars = pylab.bar(ind + c * width, counts[categories[c]], width, color=color)
        bar_groups.append(bars)

    pylab.xticks(ind + width, words)
    pylab.legend([b[0] for b in bar_groups], categories, loc='upper left')
    pylab.ylabel('Frequency')
    pylab.title('Frequency of Six Modal Verbs by Genre')
    #pylab.show()

    import matplotlib
    matplotlib.use('Agg')
    pylab.savefig('modals.png')

def main():
    genres = ['news', 'religion', 'hobbies', 'government', 'adventure']
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    cfdist = nltk.ConditionalFreqDist(
             (genre, word)
             for genre in genres
             for word in nltk.corpus.brown.words(categories=genre)
             if word in modals)
    counts = {}
    for genre in genres:
        counts[genre] = [cfdist[genre][word] for word in modals]
    bar_chart(genres, modals, counts)
