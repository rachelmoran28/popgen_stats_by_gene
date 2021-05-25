#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=62gb
#SBATCH -t 3:00:00
#SBATCH -J fixFst
#SBATCH --array=1-325


cd /home/mcgaughs/shared/Datasets/all_sites_LARGE_vcfs/filtered_surfacefish/combined_filtered/246Indvs_RepsMasked/phased_masked/dxy/Fst


CMD_LIST="Un_325_sed_commands.txt"

#CMD_LIST="fix_commands.txt"

CMD="$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${CMD_LIST})"
eval ${CMD}
