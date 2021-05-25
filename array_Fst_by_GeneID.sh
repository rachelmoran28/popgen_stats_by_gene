#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=200gb
#SBATCH -t 1:00:00
#SBATCH -J Fst
#SBATCH --array=1-325


module load python2/2.7.12_anaconda4.2

cd /panfs/roc/groups/14/mcgaughs/shared/Datasets/all_sites_LARGE_vcfs/filtered_surfacefish/combined_filtered/246Indvs_RepsMasked/phased_masked/dxy/Fst/FstByGene


CMD_LIST="Fst_by_Gene_Un_commands.txt"
#CMD_LIST="Fst_by_gene_commands_gzip.txt"

CMD="$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${CMD_LIST})"
eval ${CMD}


