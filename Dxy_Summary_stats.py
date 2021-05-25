import os, sys, re
import subprocess
from collections import OrderedDict
from operator import itemgetter
from itertools import groupby
import numpy
from numpy import mean, median, maximum, minimum, std

#After you get a VCF file from a certain population this script simply takes the mean and median across the entire genome for pi


#to run
#python PI_Summary_stats.py output_Pi_Tinaja_all_3.3.txt

hashy3={}

summary=[]
counter=0
for line in open(sys.argv[1]):
    if counter>0:
        line = line.strip().split('\t')
        if line[2]=="-nan":
            summary.append(float(0))
        else:
            summary.append(float(line[2]))
    counter+=1

print str('name')+'\t'+str('mean')+'\t'+str('median')+'\t'+str('stdev')+'\t'+str('maximum')+'\t'+str('minimum')
#print summary
#print 
print str(sys.argv[1])+'\t'+str(mean(summary))+'\t'+str(median(summary))+'\t'+str(std(summary))+'\t'+str(max(summary))+'\t'+str(min(summary))
   
