##############
Files (Queues)
##############

Introduction
============

En guise d'introduction, référez-vous à la `présentation PowerPoint faite en classe <https://www.dropbox.com/s/5aobgi6pqn1glud/stacks-queues.pptx?dl=0>`_

Implémentation naïve
====================

.. literalinclude:: scripts/simple_queue.py
   :language: python
   :linenos:


.. admonition:: Remarque
   :class: attention

   L'implémentation ci-dessus présente l'avantage d'être très simple et très
   rapidement codée. Elle permet de comprendre le fonctionnement de base des
   files. Cependant, elle est loin d'être satisfaisante du point de vue des
   performances car l'insertion a une complexité en :math:`\mathcal{O}(N)` puisque
   l'on insère les nouveaux éléments en tête de liste dans une simple liste
   Python

Implémentation à l'aide de tableaux
===================================

Pour obtenir une insertion en :math:`\mathcal{O}(1)`, on peut par exemple
utiliser un tableau "qui se mord la queue" en incrémentant les indices ``front``
et ``rear`` modulo la longueur du tableau.

.. literalinclude:: scripts/array_queue.py
   :language: python
   :linenos:

Tests unitaires
---------------

Pour s'assurer du bon fonctionnement du code de l'implémentation avec les
tableaux, on peut mettre en place des tests unitaires qui simulent l'utilisation
de la classe et qui testent systématiquement les conditions de la file après
chaque opérations d'addition ou de suppression d'éléments. Ceci présente
plusieurs avantages

*  Il est possible de comprendre le fonctionnement attendu de la classe en
   lisant les tests, ce qui sert à la fois de spécification pour la classe.

*  Les tests unitaires constituent une sorte de documentation dont la lectur
   est utile pour comprendre le fonctionnement de la classe

*  On peut sans problème modifier ou corriger le code sans craindre d'ajouter
   des bugs qui n'étaient pas présents au préalable.

Voici le fichier de test utilisable pour tester le classe ``ArrayQueue`` :


.. literalinclude:: scripts/array_queue_test.py
   :language: python
   :linenos:

.. admonition:: Remarque
   :class: tip

   Vous aurez sans doute remarqué que les tests comportent plus de lignes de
   code que la classe elle-même. Ceci est un phénomène courant lorsque l'on
   teste sérieusement son code.



Exercices
=========

#. Comparer les performances des deux implémentations des files en mesurant le
   temps nécessaire pour insérer le nombre suivant d'éléments dans la file :

   ::

      num_inserts = [1e3, 1e4, 5e4, 1e5, 5e5, 1e6, 1e7]


   Pour chacune des implémentations, représenter dans un graphique le temps
   nécessaire pour l'insertion en fonction du nombre d'éléments à insérer.

   .. admonition:: Indication
      :class: tip

      Exporter les données au format CSV et importez-les dans le grapheur
      http://www.desmos.com.
