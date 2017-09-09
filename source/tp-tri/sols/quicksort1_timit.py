from benchmark import *
from report import *
from counter import *

from quicksort1 import quicksort

def timeit():
    sizes = [10, 20, 30]
    # bench(selection_sort_1, distribution=random_list_alldifferent, sizes=sizes, output="csv")
    report = bench(quicksort, distribution=reversed_list, sizes=sizes)
    report.add_formats([FormatRST]).report().stdout()


timeit()
