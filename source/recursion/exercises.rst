##########################
Exercices sur la récursion
##########################


Exercice 1
==========

Faire les exercices 1 à 3 du manuel TigerJython, chapitre "Tortue graphique",
section "Fonctions récursives" (http://www.tigerjython.fr/franz/index.php?inhalt_links=navigation.inc.php&inhalt_mitte=turtle/rekursionen.inc.php)

Exercice 2
==========

#.  Développer une fonction récursive ``recursive_product(numbers : List[float]) -> float`` qui
    prend en argument une liste de nombres ``float`` et retourne la somme de cette
    liste. La fonction ne doit pas utiliser de boucle ``for`` ou ``while``.

    ..  code-block:: python

        def recursive_product(numbers):
            # type your code here ...  
            pass

    ..  admonition:: Exemple d'utilisation
        :class: note

        ::

            >>> recursive_product([1, 2, 3, 4, 5])
            120.0
            >>> recursive_product([])
            1.0


#.  Modifier la fonction ``recursive_product`` pour qu'elle lève une exception de type
    ``ValueError`` avec un message approprié si l'un des éléments de la liste n'est
    pas un nombre.

    ..  admonition:: Indication
        :class: tip

        Vous pouvez utiliser la fonction ``isinstance(object, classname)`` pour
        déterminer si ``object`` est une instance de la classe ``classname``. Il
        suffit donc de déterminer si l'élément est une instance de ``int`` ou de
        ``float`` et de lever l'exception si nécessaire.

        Documentation : https://docs.python.org/2/library/functions.html#isinstance

        ::

            >>> isinstance(1, int)
            True
            >>> isinstance(1.0, int)
            False
            >>> isinstance(1.0, float)
            True
            >>> isinstance("1", int)
            False

Exercice 3
==========


Développer une fonction récursive ``max_rec(numbers: float) -> float`` qui retourne
l'élément maximal d'une liste de nombres flottants. Si la liste est vide,
lever une exception de type ``ValueError``. Il est interdit d'utiliser une
boucle et la fonction prédéfinie ``max`` dans cet exercice.


..  admonition:: Indication
    :class: tip

    Commencer par définir une fonction ``max2(a: float, b: float) -> float`` qui
    retourne le maximum de deux éléments et utiliser cette fonction au sein de
    votre fonction récursive ``max_rec``.

    Prenez la peine de bien définir le cas de base (problème trivial) et la
    manière de réduire la taille du problème.

..  only:: corrige

    ..  admonition:: Corrigé
        :class: important

        ..  code-block:: python
            :linenos:

            def max2(a, b):
                if a > b:
                    return a
                else: 
                    return b

            def max_rec(numbers):
                if len(numbers) == 1:
                    return numbers[0]
                else:
                    return max2(numbers[0], max_rec(numbers[1:]))
                
            print(max_rec([1,4,8,3,10, 6]))


Exercice 4
==========

Définir une fonction ``is_palindrom(text: str) -> bool`` pour vérifier si la
chaine de caractères ``text`` est un palindrome. Une chaine de caractères est un
palindrome si elle est symétrique, à savoir qu'elle est égale à elle-même
lorsqu'on l'inverse. 

**Indication** : Ne pas utiliser de boucle ``for`` ou ``while`` mais uniquement
le principe de la récursion.

Exemples de palindromes : ``"<><>"``, ``"abccba"``, ``"engagelejeuquejelegagne"``

..  code-block:: python

    def is_palindrom(text):
        # type your code here ...  
        pass

..  admonition:: Exemple d'utilisation
    :class: note

    ::

        >>> is_palindrom("")
        True
        >>> is_palindrom("<><>")
        True
        >>> is_palindrom("abccba")
        True
        >>> is_palindrom("engagelejeuquejelegagne")
        True
        >>> is_palindrom("Hello world!")
        False

..  only:: corrige

    ..  admonition:: Corrigé
        :class: important

        ..  code-block:: python
            :linenos:

            def is_palindrom(text):
                if len(text) in [0, 1]:
                    return True
                elif len(text) == 2:
                    return text[0] == text[1]
                else:
                    return text[0] == text[-1] and is_palindrom(text[1:-1])
                    
            def test():
                assert is_palindrom("abba") == True
                assert is_palindrom("") == True
                assert is_palindrom("abcba") == True
                assert is_palindrom("abdcba") == False

            test()

Exercice 5
==========

Définir une fonction ``fibonacci_rec(n: int) -> List[int]`` qui retourne le
:math:`n`-ième terme de Fibonacci. La suite de Fibonacci joue un rôle important
dans de plusieurs domaines scientifiques. Elle est définie de la manière
suivante

..  math::  

    a_n = \begin{cases}
        1 &\text{si $n = 0$} \\
        1 &\text{si $n = 1$} \\
        a_{n-2} + a_{n-1} &\text{si $n > 1$}
    \end{cases}
        
Les premiers termes de la suite sont donc :math:`1, 1, 2, 3, 5, 8, 13, 21, 34, \ldots`

Consignes
---------

#.  Définir cette fonction de manière récursive en partant de la définition mathématique

    ..  admonition:: Exemple d'utilisation
        :class: important

        ::

            >>> fibonacci_rec(0)
            1
            >>> fibonacci_rec(1)
            1
            >>> fibonacci_rec(3)
            3
            >>> fibonacci_rec(6)
            13

    ..  only:: corrige

        ..  admonition:: Corrigé
            :class: important

            ..  code-block:: python
                :linenos:

                from __future__ import print_function
                from time import time

                def fibonacci_rec(n):
                    if n in [0, 1]:
                        return 1
                    else:
                        print("fib({})".format(n))
                        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

                for n in [1, 2, 5, 10, 15, 25, 30, 35]:
                    # measure algorithm running time
                    t0 = time()
                    print(fibonacci_rec(n))
                    t1 = time()
                    print("temps nécessaire pour le calcul : ", t1 - t0, "secondes")

#.  Après avoir sauvegardé votre code (rappelez-vous qu'une fonction récursive
    peut faire planter votre machine ...), tester votre fonction pour les
    valeurs suivantes de ``n`` : ``[1, 2, 5, 10, 15, 25, 30, 35, 40]`` et
    mesurer le temps d'exécution pour chacune des valeurs de ``n``. Que
    constatez-vous?

    ..  only:: corrige

        ..  admonition:: Corrigé
            :class: important

            L'appel ``fibonacci_rec(40)`` prend énormément de temps, même sur un
            ordinateur très rapide. 


#.  Tentez d'expliquer le phénomène expliqué dans le point précédent. 

    ..  admonition:: Indication
        :class: tip
        
        Utiliser ``print`` pour afficher un message à chaque appel récursif en
        précisant la valeur de l'argument ``n``.


    ..  only:: corrige

        ..  admonition:: Corrigé
            :class: important

            En rajoutant une instruction ``print`` lors de au début de la
            fonction, on se rend compte qu'il faut vite énormément d'appels
            récursifs. Ceci vient du fait que l'on recalcule plusieurs fois les
            mêmes valeurs, ce que l'on peut visualiser sous forme d'un arbre :

            ..  code-block:: python
                :linenos:

                from __future__ import print_function
                from time import time

                def fibonacci_rec(n, level=0):
                    print("    "*level + "fib({})".format(n))
                    if n in [0, 1]:
                        return 1
                    else:
                        return fibonacci_rec(n-1, level+1) + fibonacci_rec(n-2, level+1)

                fibonacci_rec(6)

            ..  figure:: figures/fib_rec_call_tree.png
                :align: center
                :width: 80%

                Appels récursifs de la fonction ``fibonacci_rec``

            ::

                >>> fibonacci_rec(6)
                fib(6)
                    fib(5)
                        fib(4)
                            fib(3)
                                fib(2)
                                    fib(1)
                                    fib(0)
                                fib(1)
                            fib(2)
                                fib(1)
                                fib(0)
                        fib(3)
                            fib(2)
                                fib(1)
                                fib(0)
                            fib(1)
                    fib(4)
                        fib(3)
                            fib(2)
                                fib(1)
                                fib(0)
                            fib(1)
                        fib(2)
                            fib(1)
                            fib(0)

Exercice 6 : Mémoïsation
========================

Dans cet exercice, nous allons utiliser une technique dite de mémoïsation (il
n'y a pas de faute d'orthographe !!!) permettant de surmonter les difficultés de
performance rencontrées dans l'algorithme récursif construisant la suite de
Fibonacci. Cette technique consiste à stocker le résultat de l'appel de la
fonction dans un dictionnaire afin d'éviter de devoir refaire de nombreuses fois
le même calcul.

Consigne
--------

Optimiser l'algorithme récursif de la suite de Fibonacci développé à l'exercice
précédent en utilisant le technique de mémoïsation. Développer une fonction
``fibonacci_rec_opt(n: int) -> int`` qui retourne le :math:`n`-ième terme de la
suite de Fibonacci avec une technique de mémoïsation. 
   
..  admonition:: Indication
    :class: tip

    Il faut utiliser un dictionnaire ``already_computed`` dans lequel les clés
    seront l'argument passé à la fonction. Avant de retourner la valeur, on la
    stocke dans le dictionnaire ``already_computed``. Avant de calculer la
    valeur, on vérifie dans le dictionnaire si la valeur n'a pas déjà été
    calculée précédemment. Si c'est le cas, on retourne simplement la valeur qui
    existe dans le dictionnaire au lieu de refaire le calcul.

    On devrait donc avoir le déroulement suivante

    ::

        >>> already_computed = {}
        >>> fibonacci_rec_opt(0)
        >>> already_computed
        {0: 1}
        >>> fibonacci_rec(2)
        >>> already_computed
        {0: 1, 1: 1, 2: 2}
        >>> fibonacci_rec(4)
        >>> already_computed
        {0: 1, 1: 1, 2: 2, 3: 3, 4: 5}




..  admonition:: Exemple d'utilisation
    :class: important

    ::

        >>> fibonacci_rec(0)
        1
        >>> fibonacci_rec(1)
        1
        >>> fibonacci_rec(3)
        3
        >>> fibonacci_rec(6)
        13

..  only:: corrige

    ..  admonition:: Corrigé
        :class: important

        ..  code-block:: python
            :linenos:

            already_computed = {}

            def fibonacci_rec(n):
                if n in [0, 1]:
                    return 1
                else:
                    if n in already_computed:
                        return already_computed[n]
                    else:
                        already_computed[n] = fibonacci_rec(n-1) + fibonacci_rec(n-2)
                        return already_computed[n]
                
            print(fibonacci_rec(40))
            print(fibonacci_rec(150))
            print(fibonacci_rec(1000))
            print(fibonacci_rec(1500))


Exercice 7
==========

Utiliser la fonction ``fibonacci_rec_opt`` développée dans l'exercice précédent
pour les valeurs suivantes de ``n`` dans ``[150, 500, 1000, 1500]``.

Que se passe-t-il pour :math:`n = 1500`? Donnée une explication détaillée de ce
qui se passe.

Exercice 8
==========

Développer une fonction itérative (sans récursion) ``fibonacci_iter(n: int) -> int``,   
à l'aide d'une boucle, pour calculer le :math:`n`-ième terme de la suite de Fibonacci.

Calculer ``fibonacci_iter(2000)``. Cela pose-t-il problème ?