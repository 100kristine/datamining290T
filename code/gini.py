#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
from collections import defaultdict,Counter

(
    CMTE_ID, AMNDT_IND, RPT_TP, TRANSACTION_PGI, IMAGE_NUM, TRANSACTION_TP,
    ENTITY_TP, NAME, CITY, STATE, ZIP_CODE, EMPLOYER, OCCUPATION,
    TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID, CAND_ID, TRAN_ID, FILE_NUM,
    MEMO_CD, MEMO_TEXT, SUB_ID
) = range(22)

CANDIDATES = {
    'P80003338': 'Obama',
    'P80003353': 'Romney',
}

############### Set up variables
# TODO: declare datastructures
byZipCode = defaultdict(Counter)
byCandidateId = Counter()

############### Read through files
for row in csv.reader(fileinput.input(), delimiter='|'):
    candidate_id = row[CAND_ID]
    if candidate_id not in CANDIDATES:
        continue

    candidate_name = CANDIDATES[candidate_id]
    zip_code = row[ZIP_CODE]

    ###
    # TODO: save information to calculate Gini Index
    ##/
    byCandidateId[candidate_name] += 1
    byZipCode[zip_code][candidate_name] +=1

def getGini(dct):
    """Gini(D) = 1 - sum(frac**2 for frac in classes)
    Where frac =  total things of that type in class n/total things of that type
    >>> dct = {"male":10,"female":10}
    >>> gini(dct)
    0.5
    """
    total = 0
    for key in dct.keys():
        total += dct[key]
    lst = [dct[key]/float(total) for key in dct.keys()]
    return 1 - sum([i**2 for i in lst])

def weightedGini(dct):
    """ Assuming dct is a dictionary of dictionaries, where each sub dictionary represents
    the tallies for one zipcode.
    >>> dct = {"one":{"male":10,"female":10},"two":{"male":1,"female":2}}
    >>> weightedGini(dct)
    0.5072463768115942
    """
    lst = []
    total = 0
    for key in dct.keys():
        subTotal = 0
        for otherKey in dct[key].keys():
            total += dct[key][otherKey]
            subTotal += dct[key][otherKey]
        lst += [(subTotal,getGini(dct[key]))]
    return 1 - sum([(float(tup[0])/total)*float(tup[1] for tup in lst])

###
# TODO: calculate the values below:
gini = 0  # current Gini Index using candidate name as the class
split_gini = 0  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/
gini = getGini(byCandidateId)
weightedGini = weightedGini(byZipCode)
print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini