from benchmark import *
from counter import *

def least_element_index(elements, start_index=0):
    assert len(elements) > 0

    least_index = start_index

    for i in range(start_index+1, len(elements)):
        comparisons.incr()
        if elements[i] < elements[least_index]:
            least_index = i

    return least_index


def selection_sort_2(elements):
    N = len(elements)

    for i in range(N):
        index_of_least = least_element_index(elements, start_index=i)

        # échange du plus petit élément avec le premier du sous-tableau
        # actuellement en cours d'examen
        swaps.incr()
        elements[i], elements[index_of_least] = elements[index_of_least], elements[i]

    return elements


def test():
    assert selection_sort_2([4,5,2,3,1,6]) == [1,2,3,4,5,6]
    assert selection_sort_2([1,2,1,2,3,2,1]) == [1,1,1,2,2,2,3]
    assert selection_sort_2([6,5,4,3,2,1]) == [1,2,3,4,5,6]


def timeit():
    sizes = [500, 1000, 2000, 5000, 10000, 15000, 20000]
    bench(selection_sort_2, distribution=random_list_alldifferent, sizes=sizes, output="csv")


test()
timeit()
