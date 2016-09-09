from random import shuffle, randint
from time import time

# classes permettant de formatter les résultats de la mesure
from report import *
from counter import *

default_sizes = [500 * i**2 for i in range(20)]

###################################################################
### Fonctions permettant de générer différents types de listes
###################################################################

all_list_types = []
### Définition du décorateur @title(...)
def title(name):
    def add_title(f):
        f.title = name
        all_list_types.append(f)
        return f

    return add_title

@title('Random')
def random_list_alldifferent(size=1000, minvalue=1, maxvalue=1000):
    return list([randint(minvalue, maxvalue) for i in range(size)])

def random_almostsame(size=1000, minvalue=1, maxvalue=10):
    return list([randint(minvalue, maxvalue) for i in range(size)])

@title('Few uniques')
def few_uniques(size=1000):
    return random_almostsame(size, maxvalue=10)

@title('Almost sorted')
def almost_sorted(size=1000, shuffle_ratio=0.02):
    sorted_elements = list(range(0, size))

    def swap_random(elements):
        N = len(elements)
        i = randint(0, N-1)
        j = randint(0, N-1)

        elements[i], elements[j] = elements[j], elements[i]

    for i in range(int(size * shuffle_ratio)):
        swap_random(sorted_elements)

    return sorted_elements

@title('Sorted')
def sorted_list(size=1000):
    return list(range(0, size))

@title('Reversed')
def reversed_list(size=1000):
    return list(reversed(range(0, size)))

###################################################################
### Fonction pour mesurer le temps d'exécution d'un algorithme de tri
###################################################################

def bench(algo, sizes=None, distribution=random_list_alldifferent):
    sizes = sizes or default_sizes

    report = Report(headers=('N', 'times'))

    for N in sizes:
        elements = distribution(N, 0, N)
        t0 = time()
        algo(elements)
        t1 = time()

        report.insert([N, t1-t0])

    return report

def nb_ops(algo, elements, ops):
    comparisons.reset()
    swaps.reset()
    algo(elements)
    return sum([op.value for op in ops])


def count_ops(algo, sizes=None, list_types=None, ops=None):
    sizes = sizes or default_sizes
    list_types = list_types or all_list_types
    ops = ops or [comparisons, swaps]

    headers = ['N'] + [f.title for f in list_types]
    report = Report(headers=headers)

    for N in sizes:
        data = [N] + [nb_ops(algo, f(size=N), ops=ops) for f in list_types]
        report.insert(data)

    return report
