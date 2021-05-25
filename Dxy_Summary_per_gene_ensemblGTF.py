import os, sys, re
import numpy
from numpy import mean, median, maximum, minimum, std
#from common import pairwise, Hash
#from collections import defaultdict, deque
##to run
#python FST_Summary_stats_sliding_Window.py Scaffolds_and_lengths.txt Rascon_Molino_Dxy.txt

#hash_of_scaffolds={}
#for line in open(sys.argv[1]): #Scaffolds_and_lengths.txt
#    line = line.strip().split('\t')
#    if line[0] not in hash_of_scaffolds:
#        hash_of_scaffolds[line[0]]=line[2]
#    else:
#        hash_of_scaffolds[line[0]]=line[2]
#        

counter=1
hash_of_Dxy_values={}
for line in open(sys.argv[2]): #Dxy_Tinaja_Choy.txt.weir.fst
    if counter>1:
        line = line.strip().split('\t')
        if str(line[0]) not in hash_of_Dxy_values:   
            hash_of_Dxy_values[str(line[0])]={line[1]:line[2]}
        else:
            hash_of_Dxy_values[str(line[0])][line[1]]=line[2]
    counter+=1

values=[]
hash_of_cds={} #/panfs/roc/groups/14/mcgaughs/mcgaughs/Cavefish/Astyanax_mexicanus.AstMex102.80.gtf
for line in open(sys.argv[3]):
    line = line.strip().split('\t')
    End=''
    Start=''
    p=''
    gene1=''
    exord=''
    Scaffold=''
    ID_section=[]
    gene_name=''
    #exon_number=''
    if len(line)>2:
        if str(line[2])=='CDS':
            Scaffold=line[0]
            End_of_exon=line[4]
            Start_of_exon=line[3]
            ID_section=line[8].split(';')
            gene_name=ID_section[0].split(' ')[1]
            gene_symbol=ID_section[5].split(' ')[2]
            #exon_number=ID_section[4].split(' ')[1]        
            k=[]
            o=()
            h=()
            j=[]
            if Scaffold not in hash_of_cds:
                hash_of_cds[Scaffold]={gene_name:[]}                               
                if str(line[6])=='+': #checking strand
                    for n in range(int(Start_of_exon), (int(End_of_exon)+1)):
                        if n not in hash_of_cds[Scaffold][gene_name]:
                            hash_of_cds[Scaffold][gene_name].append(n)
                elif str(line[6])=='-': #checking strand
                    for n in range(int(End_of_exon),int(Start_of_exon)-1,-1):
                        if n not in hash_of_cds[Scaffold][gene_name]:
                            hash_of_cds[Scaffold][gene_name].append(n)                    
            else:
                if gene_name not in hash_of_cds[Scaffold]:
                    hash_of_cds[Scaffold][gene_name]=[]
                    if str(line[6])=='+': #checking strand
                        for n in range(int(Start_of_exon), (int(End_of_exon)+1)):
                            if n not in hash_of_cds[Scaffold][gene_name]:
                                hash_of_cds[Scaffold][gene_name].append(n)
                    elif str(line[6])=='-': #checking strand
                        for n in range(int(End_of_exon),int(Start_of_exon)-1,-1):
                            if n not in hash_of_cds[Scaffold][gene_name]:
                                hash_of_cds[Scaffold][gene_name].append(n)
                else:
                    if str(line[6])=='+': #checking strand
                        for n in range(int(Start_of_exon), (int(End_of_exon)+1)):
                            if n not in hash_of_cds[Scaffold][gene_name]:
                                hash_of_cds[Scaffold][gene_name].append(n)
                    elif str(line[6])=='-': #checking strand
                        for n in range(int(End_of_exon),int(Start_of_exon)-1,-1):
                            if n not in hash_of_cds[Scaffold][gene_name]:
                                hash_of_cds[Scaffold][gene_name].append(n)

scaffolds=hash_of_cds.keys()
#print scaffolds

summary_Dxy_hash={}
for h in range(0,len(scaffolds)): #for each scaffold
    if str(scaffolds[h]) in hash_of_cds:
        if str(scaffolds[h]) in hash_of_Dxy_values:
            for i in hash_of_cds[str(scaffolds[h])]:#for each gene
                #print str(scaffolds[h])+'\t'+str(i)+'\t'+(str(hash_of_cds[str(scaffolds[h])][str(i)]))        
                for j in hash_of_cds[str(scaffolds[h])][str(i)]: #for each base in the gene
                    if str(j) in hash_of_Dxy_values[str(scaffolds[h])]:
                        if str(i) not in summary_Dxy_hash: #if gene name not in summary pi
                            summary_Dxy_hash[str(i)]=[float(hash_of_Dxy_values[str(scaffolds[h])][str(j)])]
                        else:
                            summary_Dxy_hash[str(i)].append(float(hash_of_Dxy_values[str(scaffolds[h])][str(j)]))
                            
                            

print "Scaffold"+'\t'+"Gene_name"+'\t'+'Mean_Dxy'+'\t'+'Median_Dxy'+'\t'+'Max_Dxy'+'\t'+'Min_Dxy'+'\t'+'Stdev'+'\t'+'fixed'+'\t'+'invariant'+'\t'+'total_sites_with_data'
for h in range(0,len(scaffolds)): #for each scaffold
    if str(scaffolds[h])in hash_of_cds:
        for i in hash_of_cds[str(scaffolds[h])]:
            if i in summary_Dxy_hash:
                print str(scaffolds[h])+'\t'+str(i)+'\t'+str(mean(summary_Dxy_hash[str(i)]))+'\t'+str(median(summary_Dxy_hash[str(i)]))+'\t'+str(max(summary_Dxy_hash[str(i)]))+'\t'+str(min(summary_Dxy_hash[str(i)]))+'\t'+str(std(summary_Dxy_hash[str(i)]))+'\t'+str(summary_Dxy_hash[str(i)].count(1))+'\t'+str(summary_Dxy_hash[str(i)].count(0))+'\t'+str(len(summary_Dxy_hash[str(i)]))




 
