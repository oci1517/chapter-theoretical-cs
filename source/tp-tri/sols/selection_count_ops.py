from benchmark import count_ops
from report import FormatCSV
from counter import comparisons, swaps
from selection_sort_2 import selection_sort_2

# compte le nombre d'échanges (swaps) nécessaires par le tri sélection pour les
# tailles 1000, 2000, 5000, 10000, 20000 et affiche le résultat au format CSV
# qui peut directement être inséré dans Excel ou dans un tableau Desmos
ops_report = count_ops(selection_sort_2, sizes=[1000, 2000, 5000, 10000, 20000], ops=[swaps])
ops_report.add_formats([FormatCSV]).report().stdout()

# idem pour compter les comparaisons
ops_report = count_ops(selection_sort_2, sizes=[1000, 2000, 5000, 10000, 20000], ops=[comparisons])
ops_report.add_formats([FormatCSV]).report().stdout()

# idem pour faire la somme des swaps et des compaisons (total d'opérations)
ops_report = count_ops(selection_sort_2, sizes=[1000, 2000, 5000, 10000, 20000], ops=[comparisons, swaps])
ops_report.add_formats([FormatCSV]).report().stdout()
