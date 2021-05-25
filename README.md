# popgen_stats_by_gene
Scripts used to generate population genetic stats (Dxy, Fst, Pi) for each gene in an annotation file.



Dxy Scripts Order


array_make_vcf.sh
#This uses vcftools to make vcfs and frq.count files for each population

array_Dxy.sh
#first uses Cave_fish_Dxy.py, which takes two count files and calculates Dxy at each site in the genome
#second uses  Dxy_Summary_stats.py, which takes the pairwise _Dxy.txt file and gives a summary table (*summary_Dxy.txt)
#third uses Fixed_Differences_FASTSITES.py  which takes the pairwise _Dxy.txt and finds fixed sites (fixed_differences_*.txt)

#  Use All_351_Dxy_Commands.txt or All_351_Dxy_Commands_Un.txt

### Need to redo part two and three for Un - python syntax error with print? 
### Add module load python2 and rerun


array_Dxy_StatsFixed.sh
#uses Dxy_Summary_per_gene_ensemblGTF.py, which takes AllScaffLengths.txt, _Dxy.txt , and Astyanax_mexicanus-2.0.ensembl101_NCBI_renamed.gtf and gives Dxy-by-gene for a pop pair

## Use First178_Commands_Dxy_Summary_per_Gene_ID_gzip_Un.txt and  Last173_Commands_Dxy_Summary_per_Gene_ID_gzip_Un.txt OR All_351_Commands_Dxy_Summary_per_Gene_ID_gzip_Un.txt


******************************

array_Dxy_small_pops.sh
Need to use this script for smaller pops (Micos, Toro, Japlin) bc they have more missing data sites that were not filtered out from the whole data set (earlier in the pipeline I applied a filter that removed any sites with >20% missing data in any population that had 4+ samples; for Japlin and Micos n=1, for Toro n=3).

This takes Japlin_Micos_Commands.txt or All_351_Dxy_Commands_Un_SmallPops.txt, which contains commands to run Cave_fish_Dxy_small_pops.py with AllScaffLengths.txt and COUNT_* files for two populations provided. 
(Array 1-75)

———————————————————————————————————————

Fst Scripts Order

array_Fst.sh
Takes the big vcf and calculates pairwise Fst between two populations with vcftools and two sample lists (*_samples.txt ) 


