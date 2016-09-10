from counter import comparisons, swaps

def least_element_index(elements, start_index=0):
    assert len(elements) > 0

    least_index = start_index

    for i in range(start_index+1, len(elements)):
        # incrémentation du compteur global de comparaisons
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
        if index_of_least > i:
            # incrémenter le compteur global de swaps
            swaps.incr()
            elements[i], elements[index_of_least] = elements[index_of_least], elements[i]

    return elements
