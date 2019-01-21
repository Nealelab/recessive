import hail as hl

ht = hl.read_table('gs://rec_project/updated_imputed.mt')
ht = hl.vep(ht, 'gs://hail-common/vep/vep/vep85-loftee-gcloud.json')
ht.write('gs://rec_project/updated_imputed_annotated_11.28.mt', overwrite=True)