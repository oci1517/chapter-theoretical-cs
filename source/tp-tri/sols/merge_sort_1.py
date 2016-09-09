
def insert(element, elements):
    '''

    La fonction insert prend l'élément à insérer et une séquence triée en tant
    qu'arguments. Elle insère l'élement à la place correcte dans la séquence et
    retourne cette-dernière.

    '''

    if elements==[]:
        return [element]
    elif element<=elements[0]:
        return [element] + elements
    else:
        return [elements[0]] + insert(element, elements[1:len(elements)])


def merge(left,right):
    '''

    La fonction merge prend 2 séquences triées comme arguments. Elle retourne
    une fusion des 2 séquences telles que la séquence résultante est triée.

    '''

    if left==[]:
        return right
    elif right==[]:
        return left
    else:
        return merge(
            left[1:len(left)],
            insert(left[0], right)
        )


def merge_sort(elements):
    '''

    La fonction merge_sort prend la séquence à trier comme argument. La séquence
    d'entrée est supposée être une liste. Cette fonction retourne une
    permutation de la séquence d'entrée, triée par ordre croissant.

    '''

    n = len(elements)

    if n == 0 or n == 1:
        return elements
    else:
        subseq1 = elements[0:n//2]
        subseq2 = elements[n//2:n]
        return merge(merge_sort(subseq1),merge_sort(subseq2))
