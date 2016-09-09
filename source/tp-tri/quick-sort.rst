Tri rapide (Quick sort)
-----------------------

Le tri rapide est, comme son nom l'indique, un algorithme de tri très rapide et
utilisé dans la plupart des langages. Il présente par rapport au tri fusion
l'avantage de ne pas utiliser de mémoire supplémentaire. Il s'agit donc d'un tri
*in-place* qui présente des performances temporelles similaires au tri fusion.

.. admonition:: Consigne
   :class: tip

   #. Visionner la vidéo https://www.youtube.com/watch?v=B4URnLNITgw présentant
      le fonctionnement du tri rapide (en anglais)

   #. Définir les notions de pivot et de partition (gauche et droite) utilisées dans l'algorithme du tri rapide

   #. Développer une implémentation complètement *in-place* de l'algorithme du
      tri rapide selon l'explication donnée dans la vidéo YouTube ci-dessus.

   #. Chronométrer le temps d'exécution de l'algorithme sur des listes
      aléatoires de tailles ``sizes`` données par

      ::

         sizes = [1e3, 1e4, 2e4, 1e5, 5e5]

   #. Vérifier expérimentalement la complexité temporelle de l'algorithme du tri
      rapide en représentant les mesures du point précédent dans un graphique et
      en tentant de trouver une courbe d'ajustement correspondant au nuage de
      points obtenus (utiliser l'outil *table* de https://www.desmos.com/).

   #. Prédire le temps nécessaire pour trier ``1e6`` éléments aléatoires et vérifier cette prédiction expérimentalement.

   #. Compter expérimentalement le nombre moyen de comparaisons et de
      permutations (swaps) nécessaires sur les différents types de listes et pour
      les tailles de listes ``sizes`` indiquées au point précédent. Pour ce faire,
      utiliser le module ``counter`` en insérant dans le code des appels à
      ``comparisons.incr()`` et ``swaps.incr()``

   #. Exprimer la complexité mémoire de cet algorithme en fonction de la taille
      :math:`N` de la liste à trier


.. comment : cette notion de simulation présentée dans la pythonnerie n''est pas
            évidente, ne ne vois pas  #. Compléter le programme suivant permettant simuler,
            sans l'effectuer, le nombre de comparaisons nécessaires pour effectuer un tri
            rapide sur une liste de nombres de longueur $N$

      .. literalinclude:: sols/simul_quick_sort_nbcmp.py
         :language: python
         :linenos:

La vidéo suivante constitue une bonne introduction à l'algorithme du tri rapide

..  only:: html

    ..  youtube:: B4URnLNITgw

..  only:: not html

    Visualiser la vidéo Youtube
    https://www.youtube.com/watch?v=B4URnLNITgw


Visualisation dynamique
+++++++++++++++++++++++

..  only:: html

    ..  youtube:: 8hEyhs3OV1w

..  only:: not html

    Visualiser la vidéo Youtube
    https://www.youtube.com/watch?v=8hEyhs3OV1w

Visualisation statique
++++++++++++++++++++++

..  figure:: figures/quick-static.png

    Visualisation statique du tri rapide (cf. https://corte.si/posts/code/visualisingsorting/index.html)
