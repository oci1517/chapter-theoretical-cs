
Tri par sélection
-----------------

.. admonition:: Consigne
   :class: warning

   Cet algorithme sera étudié en classe avec le professeur et le développement
   de la correction se trouve dans la section :ref:`sec-selection-sort-example`.

   Il faut néanmoins lire cette section attentivement et maîtriser cet
   algorithme de tri.

   #. Développer une implémentation *in-place* de l'algorithme de tri par insertion dans un fichier ``selection_sort.py``

   #. Chronométrer le temps d'exécution de l'algorithme sur des listes
      aléatoires de tailles ``sizes`` données par

      ::

         sizes = [1000, 2000, 5000, 10000, 20000]

   #. Vérifier expérimentalement la complexité temporelle de l'algorithme du tri
      fusion en représentant les mesures du point précédent dans un graphique et
      en tentant de trouver une courbe d'ajustement correspondant au nuage de
      points obtenus (utiliser l'outil *table* de https://www.desmos.com/).

   #. Prédire le temps nécessaire pour trier 25000 éléments aléatoires et vérifier cette prédiction expérimentalement.

   #. Compter expérimentalement le nombre moyen de comparaisons et de
      permutations nécessaires sur les différents types de listes et pour les
      tailles de listes ``sizes`` indiquées au point précédent. Utiliser à cet
      effet le module ``counter`` qui définit les compteurs globaux
      ``comparisons`` et ``swaps``. La classe ``Counter`` possède une méthode
      ``incr()`` permettant d'incrémenter le compteur et une méthode ``reset()``
      permettant de le réinitialiser. Il ne faut en principe pas utiliser la
      méthode ``reset()`` depuis l'intérieur des algorithmes dont on compte le
      nombre d'opérations.



Cette méthode de tri commence par rechercher l’élément ayant la plus petite
valeur de la liste pour l’échanger avec celui situé en première position, puis
elle recherche l’élément ayant la deuxième plus petite valeur pour l’échanger
avec celui situé en deuxième position et elle recommence ainsi jusqu’à atteindre
le dernier élément de la liste. Cette méthode porte le nom de tri par sélection
car elle procède à la « sélection » successive de l’élément minimal parmi ceux
restants, comme le montre la figure ci-dessous :

.. figure:: figures/selection-sort-visu.png
   :width: 50%
   :align: center


À mesure que l’indice ``i`` progresse vers la droite de la liste, les éléments
situés à sa gauche ont pris leur position définitive et la liste est triée
lorsque l’indice atteint l’extrémité droite. Remarquons que l’algorithme peut
également se dérouler en triant la liste depuis la droite, c’est-à-dire en
sélectionnant à chaque passe le prochain plus grand élément.


Visualisation dynamique
+++++++++++++++++++++++

..  only:: html

    ..  youtube:: 92BfuxHn2XE

..  only:: not html

    Visualiser la vidéo Youtube
    https://www.youtube.com/watch?v=92BfuxHn2XE&index=11

Visualisation statique
++++++++++++++++++++++

Dans les visualisations statiques d'algorithmes de tri présentées dans ce
chapitre, les lignes correspondent au "trajet" des éléments au sein de la liste
durant le déroulement de l'algorithme. Plus une ligne est foncée, plus la taille
de l'élément qu'il représente est importante. À la fin du tri, les éléments sont
donc disposés du plus clair au plus foncé en partant du haut vers le bas.

..  figure:: figures/selection-static.png

    Visualisation statique du tri par sélection (cf. https://corte.si/posts/code/visualisingsorting/index.html)
