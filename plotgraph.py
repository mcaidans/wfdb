import wfdb
record = wfdb.rdsamp('data/100', sampto = 15000)
annotation = wfdb.rdann('data/100', 'atr', sampto = 15000)

wfdb.plotrec(record, annotation = annotation, title='Record 100 from MIT-BIH Arrhythmia Database', timeunits = 'seconds')
