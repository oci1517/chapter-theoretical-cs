Tri fusion (merge sort)
-----------------------

Nous avons vu que les algorithmes de complexité quadratique en
:math:`\mathcal{O}(N^2)` ne sont pas exploitables en pratique sur de gros jeux de
données.

Le tri fusion est le premier tri que nous allons voir dont la complexité est
nettement meilleure. L'idée de l'algorithme consiste à séparer le tableau en
deux listes de longueur égale, à trier récursivement ces deux sous-tableaux avec
un tri fusion et à fusionner ces deux sous-tableaux triés pour n'en former plus
qu'un.

Implémentation OpenClassRooms
+++++++++++++++++++++++++++++

.. admonition:: Consigne
   :class: tip

   #. Lire le cours https://openclassrooms.com/courses/le-tri-fusion de
      OpenClassrooms qui présente le tri fusion.

   #. Déboguer le code erroné de OpenClassRooms (deux bugs) et tester le code sur de petites listes.

   #. Expliquer pourquoi l'implémentation de OpenClassrooms, une fois corrigée,
      se plante tout de même pour des listes de grande taille avec l'exception
      suivante :

      ::

        RuntimeError: maximum recursion depth exceeded in comparison

      Préciser quel appel récursif pose problème et pourquoi.

Implémentation avec fusion itérative
++++++++++++++++++++++++++++++++++++

.. admonition:: Consigne
   :class: tip

   #. Étudier le code ci-dessous pour le tri fusion qui procède à la fusion de
      manière itérative pour éviter de trop nombreux appels récursifs

   #. Chronométrer le temps d'exécution de l'algorithme sur des listes
      aléatoires de tailles ``sizes`` données par

      ::

         sizes = [1e3, 1e4, 2e4, 1e5, 5e5]

   #. Vérifier expérimentalement la complexité temporelle de l'algorithme du tri
      fusion en représentant les mesures du point précédent dans un graphique et
      en tentant de trouver une courbe d'ajustement correspondant au nuage de
      points obtenus (utiliser l'outil *table* de https://www.desmos.com/).

   #. Prédire le temps nécessaire pour trier ``1e6`` éléments aléatoires et vérifier cette prédiction expérimentalement.

   #. Compter expérimentalement le nombre moyen de comparaisons et d'insertions
      nécessaires sur les différents types de listes et pour les tailles de listes
      ``sizes`` indiquées au point précédent

   #. Exprimer la complexité mémoire de cet algorithme en fonction de la taille
      :math:`N` de la liste à trier

   #. Combien d'emplacements mémoire cette implémentation nécessite-t-elle pour les valeurs suivantes de :math:`N` :

      .. csv-table:: Taille mémoire nécessaire en fonction de :math:`N`
         :header: :math:`N`, taille mémoire
         :delim: ;

         :math:`10^3`;
         :math:`10^5`;
         :math:`10^7`;
         :math:`10^9`;

   #. Expliquer pourquoi le tri fusion est très rarement utilisé malgré sa très bonne complexité temporelle


Étudier le code suivant qui corrige le défaut rencontré dans le code du cours
OpenClassrooms et qui est une adaptation du code présenté dans le magnifique
ouvrage interactif "Problem Solving with Algorithms and Data Structures" de Miller et Rabin
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html.

.. literalinclude:: sols/merge_sort_2.py
   :language: python
   :linenos:

Visualisation dynamique
+++++++++++++++++++++++

..  only:: html

    ..  youtube:: ZRPoEKHXTJg

..  only:: not html

    Visualiser la vidéo Youtube
    https://www.youtube.com/watch?v=ZRPoEKHXTJg

Visualisation statique
++++++++++++++++++++++

..  figure:: figures/merge-static.png

    Visualisation statique du tri fusion (cf. https://corte.si/posts/code/visualisingsorting/index.html)
