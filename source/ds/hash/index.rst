#################
Tables de hachage
#################

Pour calculer la clé de hachage d'un nombre entier, il suffit de 

.. code-block:: python

   bpython version 0.15 on top of Python 3.4.3 /usr/bin/python3.4m
   >>> ord('A')
   65
   >>> ord('B')
   66
   >>> ord('a')
   97
   >>> chr(35)
   '#'
   >>> chr(65)
   'A'
   >>> [ord(x) for x in 'salut']
   [115, 97, 108, 117, 116]
   >>> sum([ord(x) for x in 'salut'])
   553
   >>> sum([ord(x) for x in 'salut']) % 11
   3
   >>> sum([ord(x) for x in 'chien']) % 11
   2
   >>> sum([ord(x) for x in 'niche']) % 11
   2
   >>> sum([ord(x) * i for i, x in enumerate('niche')]) % 11
   7
   >>> sum([ord(x) * i for i, x in enumerate('niche')]) % 11
   7
   >>> sum([ord(x) * i for i, x in enumerate('chien')]) % 11
   1
   >>> list(enumerate('chien'))
   [(0, 'c'), (1, 'h'), (2, 'i'), (3, 'e'), (4, 'n')]
   >>> sum([ord(x) * i for i, x in enumerate('chien')]) % 11
