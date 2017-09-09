from benchmark import *
from report import *
from counter import *

from quicksort1_ops import quicksort

def nbops():
    sizes = [10, 20, 30]

    report = count_ops(quicksort, sizes=[10, 20, 30], ops=[comparisons])
    report.add_formats([FormatRST]).report().stdout()

nbops()
