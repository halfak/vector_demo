from revscoring.datasources.meta import (frequencies, gramming, hashing,
                                         selectors)
from revscoring.extractors import api
from revscoring.features import wikitext
from revscoring.features.meta import vectorizers

# 1-4 grams and all the skipgrams inbetween.
my_grams = [(0,), (0,1),
            (0,1,2), (0,2),
            (0,1,2,3), (0,2,3), (0,1,3), (0,3)]

parent_hash_table = frequencies.table(
    hashing.hash(gramming.gram(wikitext.revision.parent.datasources.words, grams=my_grams), n=2**20))

revision_hash_table = frequencies.table(
    hashing.hash(gramming.gram(wikitext.revision.datasources.words, grams=my_grams), n=2**20))

hash_delta = frequencies.delta(parent_hash_table, revision_hash_table)

important_hash_delta = selectors.tfidf(
    hash_delta, name="revision.diff.important_hash_delta", weight=False,
    max_terms=250)
