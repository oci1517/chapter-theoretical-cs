from benchmark import *
from report import *
from counter import *

def least_element(elements):
    assert len(elements) > 0

    least = elements[0]

    for el in elements:
        if el < least:
            least = el

    return least


def selection_sort_1(elements):
    new_list = []

    while len(elements) > 0:
        least = least_element(elements)

        new_list.append(least)
        elements.remove(least)

    return new_list


def test():
    assert selection_sort_1([4,5,2,3,1,6]) == [1,2,3,4,5,6]
    assert selection_sort_1([1,2,1,2,3,2,1]) == [1,1,1,2,2,2,3]
    assert selection_sort_1([6,5,4,3,2,1]) == [1,2,3,4,5,6]


def timeit():
    sizes = [1000, 2000, 5000, 10000, 20000]
    # bench(selection_sort_1, distribution=random_list_alldifferent, sizes=sizes, output="csv")
    report = bench(selection_sort_1, distribution=random_list_alldifferent, sizes=sizes)
    report.add_formats([FormatCSV]).report().stdout()


if __name__ == '__main__':
    timeit()
    test()
