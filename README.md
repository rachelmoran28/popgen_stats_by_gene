# popgen_stats_by_gene
Scripts used to generate population genetic stats (Dxy, Fst, Pi) for each gene in an annotation file.



Dxy Scripts Order


array_make_vcf.sh
#This uses vcftools to make vcfs and frq.count files for each population

array_Dxy.sh
# Commands list to use: All_351_Dxy_Commands.txt OR All_351_Dxy_Commands_Un.txt
#First uses Cave_fish_Dxy.py, which takes two count files and calculates pairwise Dxy at each site in the genome
#Second uses  Dxy_Summary_stats.py, which takes the pairwise _Dxy.txt file generated in the first step (with Cave_fish_Dxy.py), and gives a summary table (*summary_Dxy.txt)
#Third uses Fixed_Differences_FASTSITES.py  which takes a pairwise _Dxy.txt file and finds fixed sites (fixed_differences_*.txt)
### Use module load python2 


array_Dxy_StatsFixed.sh
## Commands list to use: All_351_Commands_Dxy_Summary_per_Gene_ID_gzip.txt OR All_351_Commands_Dxy_Summary_per_Gene_ID_gzip_Un.txt
#uses Dxy_Summary_per_gene_ensemblGTF.py, which takes AllScaffLengths.txt, _Dxy.txt , and Astyanax_mexicanus-2.0.ensembl101_NCBI_renamed.gtf and gives Dxy-by-gene for a pop pair



******************************

array_Dxy_small_pops.sh
#This takes the commnads list ALL_Japlin_Micos_Commands.txt, which contain commands to run Cave_fish_Dxy_small_pops.py with AllScaffLengths.txt and COUNT_* files for two populations provided. 
(Array 1-75)
#Need to use this script for smaller pops (Micos, Toro, Japlin) bc they have more missing data sites that were not filtered out from the whole data set (earlier in the pipeline I applied a filter that removed any sites with >20% missing data in any population that had 4+ samples; for Japlin and Micos n=1, for Toro n=3).



———————————————————————————————————————

Fst Scripts Order


Generate_Fst_Commands.txt
#Takes list of each pair of populations (Amex_Pop_Pairs.txt) and generates Fst_Commands.txt for use in array_Fst.sh

array_Fst.sh
#Commnads list to use: Fst_Commands.txt
#Takes the big vcf and calculates pairwise Fst between two populations with vcftools and two sample lists (*_samples.txt ) 

array_sed.sh
#Commnads list to use: fix_commnads.txt
#Removes NAs ("-nan") in _Fst.txt.weir.fst and replaces them with 0s.


array_Fst_by_GeneID.sh
#Commands list to use: Fst_by_gene_commands_gzip.txt
#Uses FST_Summary_by_geneID.py, which takes AllScaffLengths.txt, a pairwise _Fst.txt.weir.fst_fixed file, and the gtf (Astyanax_mexicanus-2.0.ensembl101_NCBI_renamed.gtf), and produces the file *_Fst_by_geneID.txt for a population pair




