#from __future__ import division
import os, sys, re
import subprocess
#import math
#import numpy
from collections import OrderedDict
from operator import itemgetter
from itertools import groupby

#to run
#python Cave_fish_Dxy.py Scaffolds_and_lengths.txt COUNT_Rascon_all_3.3_TEST.txt.frq.count COUNT_Tinaja_all_3.3_TEST.txt.frq.count>out.txt

hash_of_scaffolds={}
for line in open(sys.argv[1]): #Scaffolds_and_lengths.txt
    line = line.strip().split('\t')
    if line[0] not in hash_of_scaffolds:
        hash_of_scaffolds[str(line[0])]=int(line[2])
    else:
        hash_of_scaffolds[str(line[0])]=int(line[2])

allowed=['A','T','C','G']

#['KB871578.1', '2822719', '4', '20', 'G:20', 'T:0', 'A:0', 'C:0'] #8
#['KB871578.1', '2822719', '4', '20', 'G:20', 'T:0', 'A:0'] #7
#['KB871578.1', '2822719', '4', '20', 'G:20', 'T:0'] #6
#['KB871578.1', '2822719', '4', '20', 'G:20'] #5

hash_pop1={}
hash_pop2={}


counter=1
for line in open(sys.argv[2]): # COUNT_Pachon_all_3.3.txt.frq.count 
    if counter>1:
        line = line.strip().split('\t')
        if str(line[0]) not in hash_pop1:
            hash_pop1[str(line[0])]={int(line[1]):line[3:]}
        else:
            hash_pop1[str(line[0])][int(line[1])]=line[3:]
    counter+=1

counter=1
for line in open(sys.argv[3]): #COUNT_Tinaja_all_3.3.txt.frq.count
    if counter>1:
        line = line.strip().split('\t')
        if str(line[0]) not in hash_pop2:   
            hash_pop2[str(line[0])]={int(line[1]):line[3:]}
        else:
            hash_pop2[str(line[0])][int(line[1])]=line[3:]
    counter+=1

#l=line[3:]
#for p in range(0,len(l)):
#    a=l[p].split(':')
#    if str(a[0])=='A':
print ('scaffold base    dxy A_pop1  A_pop2  T_pop1  T_pop2  C_pop1  C_pop2  G_pop1  G_pop2')
values=[]
for i in hash_of_scaffolds:
    scaffold_length=''
    scaffold_length=hash_of_scaffolds[i]
    if i in hash_pop1 and i in hash_pop2:
        for pp in range(1, (int(scaffold_length)+1)):
            A_pop1=0
            A_pop2=0
            C_pop1=0
            C_pop2=0
            G_pop1=0
            G_pop2=0
            T_pop1=0
            T_pop2=0
            N_pop1=0
            N_pop2=0            
            pop1=[]
            pop2=[]
            if int(pp) in hash_pop1[i] and int(pp) in hash_pop2[i]:
                alleles_pop1=hash_pop1[i][int(pp)]
                alleles_pop2=hash_pop2[i][int(pp)]
                for p in range(0, len(alleles_pop2)):
                    a=[]
                    a=alleles_pop2[p].split(':')
                    if str(a[0])=='A':
                        A_pop2=a[1]
                    if str(a[0])=='T':
                        T_pop2=a[1]
                    if str(a[0])=='C':
                        C_pop2=a[1]
                    if str(a[0])=='G':
                        G_pop2=a[1]
                    if str(a[0])=='N':
                        N_pop2=a[1]
                for mm in range(0, len(alleles_pop1)):
                    aa=[]
                    aa=alleles_pop1[mm].split(':')        
                    if str(aa[0])=='A':
                        A_pop1=aa[1]
                    if str(aa[0])=='T':
                        T_pop1=aa[1]
                    if str(aa[0])=='C':
                        C_pop1=aa[1]
                    if str(aa[0])=='G':
                        G_pop1=aa[1]
                    if str(aa[0])=='N':
                        N_pop1=aa[1]
                if N_pop2==0 and N_pop1==0:
                    pop1.append(int(A_pop1))
                    pop1.append(int(T_pop1))
                    pop1.append(int(C_pop1))
                    pop1.append(int(G_pop1))
                    pop2.append(int(A_pop2))
                    pop2.append(int(T_pop2))
                    pop2.append(int(C_pop2))
                    pop2.append(int(G_pop2))
                    #print pop1
                    #print pop2
                    #NUMER = numpy.float64(sum([iii*jjj for iii,jjj in zip(pop1, pop2)])) 
                    #DENOM= numpy.float64(sum(pop1)*sum(pop2))
                    #print str(NUMER)+'\t'+str(DENOM)
                    #dxy = 1-NUMER/DENOM
                    dxy = 1- sum([iii*jjj for iii,jjj in zip(pop1, pop2)]) / float(sum(pop1)*sum(pop2))
                    print (str(i)+'\t'+str(pp)+'\t'+str(dxy)+'\t'+str(A_pop1)+'\t'+str(A_pop2)+'\t'+str(T_pop1)+'\t'+str(T_pop2)+'\t'+str(C_pop1)+'\t'+str(C_pop2)+'\t'+str(G_pop1)+'\t'+str(G_pop2))

