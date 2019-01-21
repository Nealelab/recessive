import hail as hl
hl.init()

imputed = hl.import_bgen('gs://fc-7d5088b4-7673-45b5-95c2-17ae00a04183/imputed/ukb_imp_chr[0-9]*_v3.bgen', entry_fields=[], n_partitions=10000)
imputed = imputed.rows()
imputed.write('gs://rec_project/updated_imputed.mt', overwrite=True)