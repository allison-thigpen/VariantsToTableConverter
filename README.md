# VariantsToTableConverter

This converter was created because of the default settings of the VariantsToTable tool from gatk. The VariantsToTable tool extracts fields from the VCF to a table format which makes it easier to work with for analysis later on. However, the VariantsToTable tool converts the alleles in the VCF from, as an example, 0/0 to T/T which makes downstream analysis harder. So this python program was written to remedy this issue. It takes an input file (generated from the gatk tool VariantsToTable script included in this repository) and converts the alleles from T/T format back to 0/0 format. It ignores all instances of ./. and */* and leaves them as-is because we do not want false reads on these individuals.    

## Getting Started

To get started, simply 
```
clone
```
this repository, run the provided script with gatk (with a few alterations according to your local settings), and finally, run the python program on the output from the gatk script.  This respository assumes you already have a working version of gatk installed and have a VCF file to run through VariantsToTable tool. 
The only columns included for consideration in this python program are CHROM (column 1), POS (column 2), REF (column 3), ALT (column 4) and subsequent SUBJECT columns (column 5 onward), the script and program have been written to follow this pattern, feel free to edit the code in any way you deem necessary to successfully complete your analysis. 
