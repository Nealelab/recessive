import hail as hl

an_gen = hl.read_matrix_table('gs://phenotype_31063/hail/ukb31063.genotype.mt')
an_gen = hl.vep(an_gen, 'gs://hail-common/vep/vep/vep85-loftee-gcloud.json')
an_gen.describe()
#write to a bucket
an_gen.write('gs://rec_project/genotype_annotations.mt', overwrite=True)