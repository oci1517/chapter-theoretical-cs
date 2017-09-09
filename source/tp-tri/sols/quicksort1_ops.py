from counter import comparisons, swaps

def findpivot(elements, i, j):
    '''

    Choisit un pivot dans la liste de nombres ``elements`` entre les bornes i et j

    '''
    return j
    #return (i + j) // 2

def swap(elements, i, j):
    '''

    Permute les éléments de la liste ``elements`` se trouvant aux positions
    ``i`` et ``j``.

    '''

    tmp = elements[i]
    elements[i] = elements[j]
    elements[j] = tmp
    swaps.incr()


def partition(elements, left, right, pivot):
    '''

    Effectue le partitionnement *in place* des éléments de ``elements`` situés
    entre la position ``left`` et la position ``right``. Compare les éléments
    par rapport à la valeur ``pivot`` du pivot choisi.

    Retourne la position finale du pivot au sein de la liste ``elements``

    '''
    # déplacer les bornes (left et right) vers l'intérieur jusqu'à ce qu'ils se
    # rencontrent
    while left <= right:
        while elements[left] < pivot:
            comparisons.incr()
            left += 1
        while (right >= left) and (elements[right] >= pivot):
            comparisons.incr()
            right -= 1

        # à ce stade, elements[left] et elements[right] sont tous deux du
        # mauvais côté de la position finale du pivot. On va donc les échanger
        # (swap) si les bornes ne se sont pas encore croisées
        if right > left:
            swap(elements, left, right)

    # retoure la position finale que prendra la pivot
    return left

def quicksort(elements, i=0, j=None):
    if j is None:
        j = len(elements) - 1

    # Choisir un pivot et le placer tout à la fin du tableau
    pivotindex = findpivot(elements, i, j)
    swap(elements, pivotindex, j)

    # Effectuer le partitionnement et déterminer la position finale du pivot
    k = partition(elements, i, j-1, elements[j])

    # déplace le pivot depuis la fin du tableau (position j) vers sa position
    # finale (position k)
    swap(elements, k, j)

    # si la partition de gauche contient plus que 1 élément
    if (k-i) > 1:
        # trier récursivement la partition à la gauche du pivot
        quicksort(elements, i, k-1)
    # si la partition de droite contient plus que 1 élément
    if (j-k) > 1:
        # trier récursivement la partition à la droite du pivot
        quicksort(elements, k+1, j)
