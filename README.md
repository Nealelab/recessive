# recessive
Phenotypic consequences of recessive mutation carriers

This document describes the beginning stages of a pipeline for analyzing the phenotypic consequences of carrying recessive mutations. Both genotyped and imputed datasets from the UK Biobank were imported and annotated in parallel. The genotyped dataset was taken further through the pipeline for filtering and quality control, and is ready for analysis in R. The imputed dataset is ready for filtering and variant qc prior to R analysis.

UK Biobank inputs and locations:

1. Genotyped: 'gs://phenotype_31063/hail/ukb31063.genotype.mt'
2. Imputed: 'gs://fc-7d5088b4-7673-45b5-95c2-17ae00a04183/imputed/ukb_imp_chr[0-9]*_v3.bgen'


### Genotyped Data
**annot_genotype.py**: Read in genotyped matrix table, annotate variants using vep command, write a new matrix table that is read into ipython notebook 'Hail_&_Export_Pipeline_Genotyped_dataset'

**Hail_&_Export_Pipeline_Genotyped_dataset.nb**: takes matrix table from the output of the annot_genotype.py script, annotates, variant quality control, subsets subjects, filtered to include only the ~175 genes included in [Counsyl Foresight Carrier Screen disease list](https://s3.amazonaws.com/static.counsyl.com/website/PDFs/Foresight+Universal+Disease+List.pdf), filtered based on allele frequency (kept variants with frequency < 5% and > 95%), filtered AC, filtered based on vepped "most severe consequence", and parsed to make two different outputs for exports **1.) annotations x variant, and 2.) variant entries (genotypes) x samples**. Exports these two datasets as bgz to local machine for use with R.

### Imputed Data
**write_mt.py**: imports multiple bgen files (imputed data for each chromosome), takes rows of matrix table and writes to new matrix table.

**annot_updated_imputed.py**: reads in matrix table (output of write_mt.py), annotates variants using vep command, writes new matrix table 

### Other files:
**rec_genes_search.xlsx**: literature search of recessive genes

**vep config file**: 'gs://hail-common/vep/vep/vep85-loftee-gcloud.json', required for vep command

**connecting instance to bucket**: connecting gcloud VM to 'gd://rec_project' bucket

**counsyl_recessive_gene_list.txt**: genes used to subset variants after vep annotation annotates 'gene with most severe consequence'

**ukb31063.gwas_samples.both_sexes.txt**: 'gs://rec_project/ukb31063.gwas_samples.both_sexes.txt', used to subset individuals to include only white Europeans
