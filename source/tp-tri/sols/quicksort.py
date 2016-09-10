def get_pivot(left, right):
    return right

def swap(elements, i, j):
    tmp = elements[i]
    elements[i] = elements[j]
    elements[j] = tmp


def partition(elements, left, right, pivot):
    '''

    Partitionne elements[left:right] en deux sous-tableaux tels que tous les
    éléments inférieurs à ``pivot`` se trouvent à sa gauche et tous les éléments
    supérieurs à ``pivot`` se trouvent à sa droite.

    retourne la position finale du pivot, ce qui permet de déterminer les bornes
    des partitions.

    '''
    # échange le pivot avec l'élément se trouvant tout à la fin du tableau (pour
    # placer le pivot à la fin)
    swap(elements, pivot, right)
    pivot = right

    print(left, right, pivot)

    i, j = left, right-1

    while i < j:

        if elements[i] <= elements[pivot]:
            i += 1
        elif elements[j] >= elements[pivot]:
            j -= 1
        else:
            # les i et les j ne peuvent plus être resserrés et il faut échanger les
            # éléments i et j
            swap(elements, i, j)
            print(elements)

    # le pivot va devoir se mettre à l'endroit où se trouve le pointeur i
    # on a forcément i == j et elements[i] == elements[j] est forcément plus
    # grand que le pivot. De ce fait, on échange cet élément avec le pivot
    swap(elements, i, pivot)

    pivot_end_pos = i

    return pivot_end_pos


def quicksort(elements, left=None, right=None):
    left = left or 0
    if right is None:
        right = len(elements) - 1

    if right - left <= 1:
        return

    pivot = get_pivot(left, right)
    final_pivot_pos = partition(elements, left, right, pivot)

    # tri de la partition de gauche
    quicksort(elements, left=left, right=final_pivot_pos-1)
    # tri de la partition de droite
    quicksort(elements, left=final_pivot_pos+1, right=right)

    return elements

if __name__ == '__main__':
    quicksort([5,4,6,2,4,8,6,2])
    # print(quicksort([1,4,2,6,7,8,3]))
    #print("ok")
    #print(quicksort([5,4,6,2,4,8,6,2]))
