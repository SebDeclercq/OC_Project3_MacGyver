# ANALYSE
Le présent document contient mon analyse relative au cahier des charges décrivant l'attendu pour le projet 3 du parcours "[DA Python][url_parcours]", à savoir *"Aidez MacGyver à s'échapper !"*.

## Modélisation

### Identification des classes
Afin de mener à bien le développement, plusieurs classes ont été repérées :
1. `Game` : le jeu en lui-même
2. `Config` : la configuration
3. `GameBoard` : le plateau du jeu
4. `BoardElement` : les éléments présents sur le plateau

Ces éléments seront considérés comme des classes filles de `BoardElement`, à savoir :
1. `Cell` : une cellule sur le plateau
2. `Pawn` : le pion
3. `Tool` : un objet présent sur le plateau

#### `Game`
La classe `Game` doit permettre de démarrer le jeu, de jouer et de quitter en fin de partie.

Pour débuter le jeu, elle doit créer un nouveau plateau grâce à la configuration fournie.

Pour quitter le jeu, elle doit vérifier si le pion a bien l'autorisation de sortir (i.e. s'il a bien collecté tous les objets attendus et qu'il se trouve sur la case de sortie).

#### `Config`
Cette configuration sera fournie par une classe `Config`, qui *parsera* un fichier de configuration type JSON, YAML ou assimilé qui contiendra l'ensemble des valeurs utiles à chaque classe du programme.

#### `GameBoard`
Le plateau de jeu sera créé sur base d'un fichier *modèle* complété par l'utilisateur final (format à définir).

Lors de son instanciation, il positionnera aléatoirement les trois `Tool` demandés.

Afin de permettre la jouabilité du programme, il sera nécessaire que soient connues la liste des cases autorisées pour le pion et de celles non-autorisées. De même, il faut garder trace de la cellule de sortie.

#### `BoardElement`
Chaque élément présent sur le plateau héritera de cette classe abstraite qui sert à spécifier une fois pour toute que chaque élément du jeu a sa propre position, définie par une paire abscisse/ordonnée.

##### `Cell`
Chaque cellule du plateau sera définie par sa position ainsi qu'une notion d'autorisation (`True`, `False`).

##### `Tool`
Chaque objet (*aiguille*, *tube* et *éther*) aura un type (son "nom") et une position.

##### `Pawn`
Le pion sera défini par sa position. Il devra se déplacer sur le plateau et ramasser les objets sur son passage. Ces objets seront stockés dans un attribut.

### UML
Voici la représentation UML (v. 1):

![UML v1][uml_v1]

*À noter que les constructeurs ont été volontairement omis.*

[url_parcours]: https://openclassrooms.com/fr/paths/68-developpeur-dapplication-python
[uml_v1]: ./oc-project-3-uml-1.jpg
