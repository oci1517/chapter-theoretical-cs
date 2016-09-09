def merge_sort(elements):

    # ancrage de la récursion : lorsqu'il n'y a plus qu'un seul élément à trier,
    # il n'y a plus rien à faire
    if len(elements) > 1:

        # découpage en deux sous-listes de taille égale (plus ou moins 1 élément
        # pour les listes de taille impaire)
        mid = len(elements) // 2
        lefthalf = elements[:mid]
        righthalf = elements[mid:]

        # appels récursifs
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # fusion des deux sous-listes ``lefthalf`` et ``righthalf``
        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                elements[k]=lefthalf[i]
                i=i+1
            else:
                elements[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            elements[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            elements[k]=righthalf[j]
            j=j+1
            k=k+1

    return elements
