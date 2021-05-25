#!/bin/bash
#SBATCH -p small,amdsmall
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=62gb
#SBATCH -t 5:00:00
#SBATCH -J Fst
#SBATCH --array=1-26

# set paths
#BCFTOOLS="/panfs/roc/groups/14/mcgaughs/shared/Software/bcftools-1.6/bcftools"
#BCFTOOLS="/panfs/roc/msisoft/bcftools/1.9_gcc-7.2.0_haswell/bin/bcftools"
VCFTOOLS="/panfs/roc/groups/14/mcgaughs/shared/Software/bin/vcftools"
VCF_LIB="/panfs/roc/groups/14/mcgaughs/shared/Software/share/perl5"

# Set the PERL5LIB variable for vcftools
export PERL5LIB=${VCF_LIB}


SRC="/home/mcgaughs/shared/Datasets/all_sites_LARGE_vcfs/filtered_surfacefish/combined_filtered/246Indvs_RepsMasked/phased_masked/biallelicSNPs_wInvar_noIndels_phased_masked_ExcludeHet/MAF01"

#BIGVCF="Concat_HardFilt_246Indv_biSNPs_wInvar_noIndels3bpBuffer.AllRepsRemoved.Phased.ExcludeHet.MAF01.Miss02.vcf.gz"
#BIGVCF="Concat_HardFilt_246Indv_biSNPs_wInvar_noIndels3bpBuffer.AllRepsRemoved.Phased.ExcludeHet.MAF01.Miss02.FIXED.vcf.gz" 
BIGVCF="Concat_HardFilt_246Indv_biSNPs_wInvar_noIndels3bpBuffer.AllRepsRemoved.Phased.ExcludeHet.MAF01.Miss02.FIXED.UnRedo.vcf.gz"

cd /home/mcgaughs/shared/Datasets/all_sites_LARGE_vcfs/filtered_surfacefish/combined_filtered/246Indvs_RepsMasked/phased_masked/dxy


# And the command list
CMD_LIST="Fst_Commands_redo_26_CM_Eyed_Un.txt"
#CMD_LIST="Fst_Commands_Un.txt"

CMD="$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${CMD_LIST})"
eval ${CMD}

