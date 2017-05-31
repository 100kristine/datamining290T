#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from ftp://ftp.fec.gov/FEC/2012/pas212.zip - data dictionary is at
http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributionstoCandidates.shtml
"""

import fileinput
import csv
total = 0.0

allTransactions = []
Candidates = []
candidateStats = {} 
for row in csv.reader(fileinput.input(), delimiter='|'):
    if not fileinput.isfirstline():
        total += float(row[14])
        ###
        # TODO: calculate other statistics here
        # You may need to store numbers in an array to access them together
        ##/
        allTransactions += [float(row[14])]
        Candidates += [row[16]]
        if row[16] in candidateStats.keys():
            candidateStats[row[16]] += [float(row[14])]
        else:
            candidateStats[row[16]] = [float(row[14])]

def mean(lst):
    return sum(lst)/float(len(lst))

def variance(lst):
    average = mean(lst)
    sumSquares = reduce(lambda x,y:x+y,[(average - i)**2 for i in lst])
    return sumSquares/float(len(lst))

def standardDev(lst):
    return variance(lst)**0.5

def minimum(lst):
    lst = sorted(lst) 
    return lst[0]

def maximum(lst):
    lst = sorted(lst)
    return lst[-1]

def median(lst):
    lst = sorted(lst)
    mid = len(lst)/2
    if len(lst) %2 != 0:
        return lst[mid]
    else:
        return (float(lst[mid-1]) + lst[mid])/2

def zscore(x,mean,stdev):
    return float(x-average)/stdev


Candidates = set(Candidates)
mini = minimum(allTransactions)
maxi = maximum(allTransactions)
average = mean(allTransactions)
var = variance(allTransactions)
stdev = standardDev(allTransactions)
med = standardDev(allTransactions)


###
# TODO: aggregate any stored numbers here
#
##/

##### Print out the stats
print "Total: %s" % total
print "Minimum: %s" % mini
print "Maximum: %s" % maxi
print "Mean: %s" % average
print "Median: %s" % med
# square root can be calculated with N**0.5
print "Standard Deviation: %s" % stdev

##### Comma separated list of unique candidate ID numbers
Cand = ",".join(Candidates)
print "Candidates: %s" % Cand

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations
    global mini
    global maxi
    norm = float(value - mini)/(maxi-mini)
    ###/
    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])

print "Extra credit"
def prntStats(userid,lst):
    print "USER %s" % userid
    total = sum(lst)
    mini = minimum(lst)    
    maxi = maximum(lst)
    average = mean(lst)
    var = variance(lst)
    stdev = standardDev(lst)
    med = standardDev(lst)
    print "Total: %s" % total
    print "Minimum: %s" % mini
    print "Maximum: %s" % maxi
    print "Mean: %s" % average
    print "Median: %s" % med
# square root can be calculated with N**0.5
    print "Standard Deviation: %s" % stdev
    return 

for candidate in candidateStats.keys():
    prntStats(candidate,candidateStats[candidate])

print "Zscores"
print ",".join([str(zscore(trans,mean,stdev)) for trans in allTransactions])