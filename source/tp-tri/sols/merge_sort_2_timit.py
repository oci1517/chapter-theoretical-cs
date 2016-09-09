from benchmark import *
from report import *
from counter import *

from merge_sort_2 import merge_sort

def timeit():
    sizes = [500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]
    # bench(selection_sort_1, distribution=random_list_alldifferent, sizes=sizes, output="csv")
    report = bench(merge_sort, distribution=random_list_alldifferent, sizes=sizes)
    report.add_formats([FormatRST]).report().stdout()

timeit()
