#!/bin/bash
#SBATCH -p small,amdsmall
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=250gb
#SBATCH -t 4:00:00
#SBATCH -J DxySmPops
#SBATCH --array=1-75

# set paths
#BCFTOOLS="/panfs/roc/groups/14/mcgaughs/shared/Software/bcftools-1.6/bcftools"
#BCFTOOLS="/panfs/roc/msisoft/bcftools/1.9_gcc-7.2.0_haswell/bin/bcftools"
VCFTOOLS="/panfs/roc/groups/14/mcgaughs/shared/Software/bin/vcftools"
VCF_LIB="/panfs/roc/groups/14/mcgaughs/shared/Software/share/perl5"

# Set the PERL5LIB variable for vcftools
export PERL5LIB=${VCF_LIB}

cd /home/mcgaughs/shared/Datasets/all_sites_LARGE_vcfs/filtered_surfacefish/combined_filtered/246Indvs_RepsMasked/phased_masked/dxy


# And the command list
CMD_LIST="All_Small_Pop_Commands.txt"

CMD="$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${CMD_LIST})"
eval ${CMD}
