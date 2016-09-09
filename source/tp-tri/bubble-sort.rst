..  Ce fichier n'est pas inséré dans le toctree (pas très utile)

..  comment:: je ne vois pas très bien ce que le tri à bulles apporte de plus
    Tri à bulles
    ------------

    Cette méthode consiste à traverser plusieurs fois la liste en échangeant à
    chaque passage des éléments adjacents placés dans un mauvais ordre relatif. Plus
    précisément, dès que l’élément de plus grande valeur est rencontré lors de la
    première traversée, il est échangé avec chacun des éléments situés à sa droite
    jusqu’à ce qu’il trouve sa place définitive, à l’extrémité droite de la liste. A
    la deuxième traversée, c’est l’élément ayant la deuxième plus grande valeur qui
    est successivement poussé vers sa place définitive et ainsi de suite, comme
    l’illustre la figure ci-dessous :

    ..  figure:: figures/bubble-sort-visu.png
        :width: 50%
        :align: center

    Chaque traversée permet de placer un élément à sa place définitive en commençant
    par celui ayant la plus grande valeur. Dès lors, les éléments situés à droite de
    l’indice ``i`` sont à leur position.

    Visualisation dynamique
    +++++++++++++++++++++++

    ..  only:: html

        ..  youtube:: Cq7SMsQBEU

    ..  only:: not html

        Visualiser la vidéo Youtube
        https://www.youtube.com/watch?v=Cq7SMsQBEU

    Visualisation statique
    ++++++++++++++++++++++

    ..  figure:: figures/bubble-static.png

        Visualisation statique du tri à bulles (cf. https://corte.si/posts/code/visualisingsorting/index.html)
