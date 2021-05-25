import os, sys, re
import numpy
from numpy import mean, median, maximum, minimum, std


counter=1
hash_of_FST_values={}
for line in open(sys.argv[2]): #FST_Tinaja_Choy.txt.weir.fst
    if counter>1:
        line = line.strip().split('\t')
        if line[0] not in hash_of_FST_values:
            if line[2]!='-nan':
                if float(line[2])>=0:
                    hash_of_FST_values[str(line[0])]={line[1]:line[2]}
        else:
            if line[2]!='-nan':
                if float(line[2])>=0:
                    hash_of_FST_values[str(line[0])][line[1]]=line[2]
    counter+=1

#hash_of_genes={}
#for line in open(sys.argv[3]): #/panfs/roc/groups/14/mcgaughs/mcgaughs/Cavefish/Astyanax_mexicanus.AstMex102.80.gtf
#    line = line.strip().split('\t')
#    if str(line[2])=='CDS':
#        p=line[8].split(';')
#        gene=p[0].split(' ')[1]
#        exord=p[4].split(' ')[1]
#        if gene not in hash_of_genes:
#            hash_of_genes[gene]=str(line[3])+str(_)+str(line[4])
#        else:
#            hash_of_genes[gene].append(str(line[3])+str(_)+str(line[4]))            


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

summary_FST_hash={}
for h in range(0,len(scaffolds)): #for each scaffold
    if str(scaffolds[h]) in hash_of_cds:
        if str(scaffolds[h]) in hash_of_FST_values:
            for i in hash_of_cds[str(scaffolds[h])]:#for each gene
                #print str(scaffolds[h])+'\t'+str(i)+'\t'+(str(hash_of_cds[str(scaffolds[h])][str(i)]))        
                for j in hash_of_cds[str(scaffolds[h])][str(i)]: #for each base in the gene
                    if str(j) in hash_of_FST_values[str(scaffolds[h])]:
                        if str(i) not in summary_FST_hash: #if gene name not in summary pi
                            summary_FST_hash[str(i)]=[float(hash_of_FST_values[str(scaffolds[h])][str(j)])]
                        else:
                            summary_FST_hash[str(i)].append(float(hash_of_FST_values[str(scaffolds[h])][str(j)]))



print "Gene_name"+'\t'+'Number.of.sites'+'\t'+'Mean_FST'+'\t'+'Median_FST'+'\t'+'Max_FST'+'\t'+'Min_FST'+'\t'+'Stdev'
for h in range(0,len(scaffolds)): #for each scaffold
    if str(scaffolds[h])in hash_of_cds:
        for i in hash_of_cds[str(scaffolds[h])]:
            if i in summary_FST_hash:
                print str(i)+'\t'+str(len(summary_FST_hash[str(i)]))+'\t'+str(mean(summary_FST_hash[str(i)]))+'\t'+str(median(summary_FST_hash[str(i)]))+'\t'+str(max(summary_FST_hash[str(i)]))+'\t'+str(min(summary_FST_hash[str(i)]))+'\t'+str(std(summary_FST_hash[str(i)]))
            
    

            
        #if str(line[6])=='+': #checking strand
        #    if str(line[7])=='0':
        #        o=(int(End)+1-int(Start))/3
        #        h=o+1
        #        k=[0, 1, 2]*h
        #        for n in range(int(Start), (int(End)+1)):
        #            j.append(n)
        #        for i in range(0,len(j)):
        #            if j[i] not in gff_hash:
        #                gff_hash[line[0]][j[i]]=[Strand, k[i], line[6], gene, exord]
        #            else:
        #                gff_hash[line[0]][j[i]]=[Strand, k[i], line[6], gene, exord]
        #    elif Phase=='1':
        #        o=(int(End)+1-int(Start))/3
        #        h=o+1
        #        k=[1, 2, 0]*h
        #        for n in range(int(Start), (int(End)+1)):
        #            j.append(n)
        #        for i in range(0,len(j)):
        #            if j[i] not in gff_hash:
        #                gff_hash[j[i]]=[Strand, k[i], Source, Type, gene1, exord]
        #            else:                      
        #                donotuse.append(gff_hash[j[i]][4])
        #                donotuse.append(gene1)
        #
        #    elif Phase=='2':
        #        o=(int(End)+1-int(Start))/3
        #        h=o+1
        #        k=[2, 0, 1]*h
        #        for n in range(int(Start), (int(End)+1)):
        #            j.append(n)
        #        for i in range(0,int(len(j))):
        #            if j[i] not in gff_hash:
        #               gff_hash[j[i]]=[Strand, k[i], Source, Type, gene1, exord]
        #            else:
        #                donotuse.append(gff_hash[j[i]][4])
        #                donotuse.append(gene1)
        #
        #if Strand=='-':
        #    if Phase=='0':
        #        o=(int(End)+1-int(Start))/3
        #        h=o+1
        #        k=[0, 1, 2]*h
        #        for n in range(int(End),int(Start)-1,-1):
        #            j.append(n)
        #        for i in range(0,len(j)):
        #            if j[i] not in gff_hash:
        #                gff_hash[j[i]]=[Strand, k[i], Source, Type, gene1, exord]
        #            else:
        #                donotuse.append(gff_hash[j[i]][4])
        #                donotuse.append(gene1)
        #    elif Phase=='1':
        #        o=(int(End)+1-int(Start))/3
        #        h=o+1
        #        k=[1, 2, 0]*h
        #        for n in range(int(End),int(Start)-1,-1):
        #            j.append(n)
        #        for i in range(0,len(j)):
        #            if j[i] not in gff_hash:
        #                gff_hash[j[i]]=[Strand, k[i], Source, Type, gene1, exord]
        #            else:
        #                donotuse.append(gff_hash[j[i]][4])
        #                donotuse.append(gene1)
        #
        #    elif Phase=='2':
        #        o=(int(End)+1-int(Start))/3
        #        h=o+1
        #        k=[2, 0, 1]*h
        #        for n in range(int(End),int(Start)-1,-1):
        #            j.append(n)
        #        for i in range(0,len(j)):
        #            if j[i] not in gff_hash:
        #                gff_hash[j[i]]=[Strand, k[i], Source, Type, gene1, exord]
        #            else:
        #                donotuse.append(gff_hash[j[i]][4])
        #                donotuse.append(gene1)
        #
        #
        #
        #
