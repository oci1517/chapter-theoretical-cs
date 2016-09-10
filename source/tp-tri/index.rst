#################################
TP sur les algorithmes de tri
#################################

Introduction aux algorithmes de tri
===================================

En informatique, un algorithme de tri est une suite finie d’opérations
permettant d’organiser une collection d’objets selon un ordre déterminé. Les
objets à trier font donc partie d’un ensemble muni d’une relation d’ordre comme,
par exemple, l’ordre numérique ou lexicographique.

La principale caractéristique qui permet de différencier les algorithmes de tri
est leur complexité algorithmique. Cette analyse permet de prévoir les
ressources (i.e. la quantité de mémoire) nécessaires à l’algorithme et de
mesurer son temps d’exécution. Ce temps est calculé en estimant le nombre moyen
d’opérations exécutées pour trier un ensemble de n éléments.

En règle générale, les méthodes de tri élémentaires, comme le tri par sélection,
par insertion et par bulles, requièrent environ :math:`n^2` étapes pour trier
:math:`n` éléments choisis dans un ordre quelconque. Si :math:`n` est suffisamment petit
(:math:`n < 20`), ceci ne pose pas de problème et, si les éléments sont presque
ou déjà rangés, certaines de ces méthodes se montrent souvent bien meilleures
que d’autres plus complexes. Malgré tout, rappelons que ces méthodes ne
sauraient convenir pour des fichiers aléatoires de grande taille.

Différents algorithmes de tri
-----------------------------

..  only:: html

    ..  youtube:: ZZuD6iUe3Pc

..  only:: not html

    Visualiser la vidéo Youtube
    https://www.youtube.com/watch?v=ZZuD6iUe3Pc


..  admonition:: Visualisation de nombreux algorithmes de tri
    :class: tip

    https://www.youtube.com/playlist?annotation_id=annotation_3326900649&feature=iv&list=PLZh3kxyHrVp_AcOanN_jpuQbcMVdXbqei&src_vid=kPRA0W1kECg


Objectifs
=========

Au terme de cet exercice d'exploration, chaque étudiant devra être
capable de:

*	Expliquer le principe de chacun des algorithmes étudiés ;
*	Appliquer à la main chacun des algorithmes étudiés à une liste d’entiers (bouts de papiers numérotés);
*	Identifier le nombre moyen d’opérations à réaliser (comparaisons / copies / swaps) pour chacun des algorithmes étudiés;
*	Implémenter en Python chacun des algorithmes étudiés sur une liste d’entiers. Les implémentations doivent être *in-place*;
* Effectuer l'analyse de complexité expérimentale de chacun des algorithmes et comparer les algorithmes entre eux

Consignes du travail
====================

Étudier chacun des algorithmes de tri énoncés ci-dessous en suivant les étapes
ci-dessous :

#. Etudier le principe de tri de l’algorithme à l’aide de l’exemple introductif

#. Visualiser l’algorithme sur http://interstices.info/jcms/c_6973/les-algorithmes-de-tri

#. Décrire à la main la progression de l’algorithme sur la liste ``[91, 17, 2, 35, 54]`` et
   déterminer le nombre total de comparaisons nécessaires.

#.	Implémenter l’algorithme en Python sous la forme d’une fonction prenant en
   paramètre la liste d’entiers à trier.

#.	Testez votre algorithme avec une liste complètement mélangée, une liste
   décroissante, une liste croissante et une liste comprenant des doublons (Few
   uniques)

#. Chronométrer chacun des algorithmes et compter le nombre d'opérations de
   comparaisons / copies / swaps pour les tailles de tableaux ``sizes`` données
   par

   ::

      sizes = [1000*i for i in [1, 2, 5, 10, 15, 20]]

#. Représenter graphiquement le temps d'exécution de chaque algorithmes en
   fonction de la taille de la liste à trier. À cette fin, utiliser Excel ou
   Desmos (exemple : https://www.desmos.com/calculator/ka2cgp7aas)

#. Faire un rapport (Document LibreOffice) indiquant, pour chaque algorithme, sa
   classe de complexité ainsi que les mesures prises dans les points précédents

.. admonition:: Outils à disposition
   :class: tip

   Pour évaluer les performances des algorithmes à étudier, utiliser les modules
   suivants disponibles à l'adresse
   https://github.com/oci1517/chapter-theoretical-cs/tree/master/source/tp-tri/sols

   *  ``benchmark``
   *  ``counter``
   *  ``report``

   Un exemple d'utilisation de ces modules figure dans l'exemple d'analyse du
   tri par sélection (:ref:`sec-selection-sort-example`).

Les algorithmes à étudier
=========================

.. include:: selection-sort.rst
.. include:: insertion-sort.rst
.. include:: merge-sort.rst
.. include:: quick-sort.rst
