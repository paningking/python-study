from rx import Observable,from_, operators as ops
from csv import DictReader

# from_(DictReader(open('python-study/reactive-python/src/file/datafile.csv', 'r'))

# ).subscribe(
#     lambda row: print("{0:4}\t{1:<35}".format(row['iata'], row['airport'][:35]))
# )
        
# from_(open("python-study/reactive-python/src/file/rxtest.txt")).pipe(
#     ops.distinct(),
#     ops.map(lambda l: l.strip()),
#     ops.filter(lambda l: l != "")
# ).subscribe(print)

from_(DictReader(open('python-study/reactive-python/src/file/mth_six_record.csv', 'r', encoding='utf-8'))).pipe(
    ops.filter(lambda row: row['channel_id'] == "BOSS")
).subscribe(lambda row: print(row))