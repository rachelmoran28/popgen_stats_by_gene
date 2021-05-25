#!/bin/bash
#PBS -l mem=62gb,nodes=1:ppn=1,walltime=24:00:00
#PBS -m abe
#PBS -j oe
#PBS -M rmoran@umn.edu
#PBS -q mangi
#PBS -t 1-27

# set paths
#BCFTOOLS="/panfs/roc/groups/14/mcgaughs/shared/Software/bcftools-1.6/bcftools"
#BCFTOOLS="/panfs/roc/msisoft/bcftools/1.9_gcc-7.2.0_haswell/bin/bcftools"
VCFTOOLS="/panfs/roc/groups/14/mcgaughs/shared/Software/bin/vcftools"
VCF_LIB="/panfs/roc/groups/14/mcgaughs/shared/Software/share/perl5"

# Set the PERL5LIB variable for vcftools
export PERL5LIB=${VCF_LIB}


SRC="/home/mcgaughs/shared/Datasets/all_sites_LARGE_vcfs/filtered_surfacefish/combined_filtered/246Indvs_RepsMasked/phased_masked/biallelicSNPs_wInvar_noIndels_phased_masked_ExcludeHet/MAF01"

BIGVCF="Concat_HardFilt_246Indv_biSNPs_wInvar_noIndels3bpBuffer.AllRepsRemoved.Phased.ExcludeHet.MAF01.Miss02.vcf.gz"

cd /home/mcgaughs/shared/Datasets/all_sites_LARGE_vcfs/filtered_surfacefish/combined_filtered/246Indvs_RepsMasked/phased_masked/dxy


# And the command list
CMD_LIST="make_vcf_commands.txt"

CMD="$(sed "${PBS_ARRAYID}q;d" ${CMD_LIST})"
eval ${CMD}
