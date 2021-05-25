import os, sys, re
import subprocess
from collections import OrderedDict
from operator import itemgetter
from itertools import groupby
import numpy
from numpy import mean, median, maximum, minimum
#from common import pairwise, Hash
#from collections import defaultdict, deque
##to run
#python Fixed_Differences_FAST.py Rascon_POPULATION1_Dxy.txt
#pop1 POPULATION1, Pop2, POPULATION2
counter=0
nonvariantsites=0
fixed_diff=0
variable=0
intersec=[]
variable_ok=0
variable_not_ok=0

for line in open(sys.argv[1]): 
    line = line.strip().split('\t')
    pop1=[]
    pop2=[]
    if counter>1:
        pop1=[]
        pop2=[]
        # if float(line[2])==float(1):
        #     nonvariantsites+=1

        POPULATION1=''
        POPULATION2=''
        if float(line[2])==float(1):
            if int(line[3])>int(0) and str(line[5])=='0' and str(line[7])=='0' and str(line[9])=='0':
                POPULATION1='A'
            elif int(line[5])>int(0) and str(line[3])=='0' and str(line[7])=='0' and str(line[9])=='0':
                POPULATION1='T'
            elif str(line[3])=='0' and str(line[5])=='0' and str(line[9])=='0' and int(line[7])>int(0):
                POPULATION1='C'
            elif str(line[3])=='0' and str(line[5])=='0' and str(line[7])=='0' and int(line[9])>int(0):
                POPULATION1='G'
            else:
                POPULATION1='complicated'
            
            if int(line[4])>int(0) and str(line[6])=='0' and str(line[8])=='0' and str(line[10])=='0':
                POPULATION2='A'
            elif int(line[6])>int(0) and str(line[4])=='0' and str(line[8])=='0' and str(line[10])=='0':
                POPULATION2='T'
            elif int(line[8])>int(0) and str(line[4])=='0' and str(line[6])=='0' and str(line[10])=='0':
                POPULATION2='C'
            elif int(line[10])>int(0) and str(line[4])=='0' and str(line[6])=='0' and str(line[8])=='0':
                POPULATION2='G'
            else:
                POPULATION2='complicated'
                
                
            print str(line[0])+'\t'+str(line[1])+'\t'+str('POPULATION1')+'\t'+str(POPULATION1)+'\t'+str('POPULATION2')+'\t'+str(POPULATION2)

        # elif float(line[2])!=float(0) and float(line[2])!=float(1):
        #     variable+=1
        #     if float(line[2])>float(0.3):#must change this threshold based on # individuals in pop.
        #         if int(line[3])!=int(0):
        #             pop1.append('A')
        #         if int(line[4])!=int(0):
        #             pop2.append('A')
        #         if int(line[5])!=int(0):
        #             pop1.append('T')
        #         if int(line[6])!=int(0):
        #             pop2.append('T')
        #         if int(line[7])!=int(0):
        #             pop1.append('C')
        #         if int(line[8])!=int(0):
        #             pop2.append('C')
        #         if int(line[9])!=int(0):
        #             pop1.append('G')
        #         if int(line[10])!=int(0):
        #             pop2.append('G')
        # pop1=set(pop1)
        # pop2=set(pop2)
        # intersec=[]
        # intersec=pop2.intersection(pop1)
        # if len(intersec)==1:
        #     variable_ok+=1 #Have one allele in common, and because of the 0.3 filter this must mean that it is fixed in one population and het in the others; informative for recombination.
        # elif len(intersec)>1:
        #     variable_not_ok+=1 #Indicates that there are two or more alleles in common between pops and so messy for recombination.
        
    counter+=1
    
#     
# print str(variable_ok)+'\t'+'variable_ok'
# print str(variable_not_ok)+'\t'+'variable_not_ok'
# print str(fixed_diff)+'\t'+'fixed_diff'
# print str(nonvariantsites)+'\t'+'nonvariantsites'
# 
# print str(variable)+'\t'+'variable'

    
            
        
