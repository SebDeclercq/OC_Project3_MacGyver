# ANALYSE
Le présent document contient mon analyse relative au cahier des charges décrivant l'attendu pour le projet 3 du parcours "[DA Python][url_parcours]", à savoir *"Aidez MacGyver à s'échapper !"*.

## Modélisation

### Identification des classes
Afin de mener à bien le développement, plusieurs classes ont été repérées :
1. `Game` : le jeu en lui-même
2. `GameBoard` : le plateau du jeu
3. `BoardElement` : les éléments présents sur le plateau

Ces éléments seront considérés comme des classes filles de `BoardElement`, à savoir :
1. `Pawn` : le pion
2. `Tool` : un objet présent sur le plateau

Deux autres classes "de soutien" seront potentiellement présentes, à utiliser comme classes uniquement (i.e. ne pas instancier) :
1. `Config` : la configuration globale du programme
2. `Constants` : la liste des constantes

#### `Game`
La classe `Game` doit permettre de démarrer le jeu, de jouer et de quitter en fin de partie.

Pour débuter le jeu, elle doit créer un nouveau plateau grâce à la configuration fournie, un pion et les trois objets. Ces quatre derniers devront être placés aléatoirement sur le plateau.

Durant la phase de jeu, le programme doit prendre en entrée un input utilisateur demandant de déplacer le pion sur le plateau, vérifier l'autorisation d'accès et mener les actions liées à la case (présence d'un objet, case de sortie, etc.).

Pour quitter le jeu, elle doit vérifier si le pion a bien l'autorisation de sortir (i.e. s'il a bien collecté tous les objets attendus et qu'il se trouve sur la case de sortie). Le cas échéant, le joueur gagne. A l'inverse, il perd.

#### `GameBoard`
Le plateau de jeu sera créé sur base d'un fichier *modèle* complété par l'utilisateur final. Le format du fichier sera spécifié dans les attributs de la classe `Config` ; plusieurs méthodes de *parsing* devront être développées.

Lors de son instanciation, il positionnera aléatoirement les trois `Tool` demandés.

Afin de permettre la jouabilité du programme, il sera nécessaire que soient connues la liste des cases autorisées pour le pion et de celles non-autorisées. De même, il faut garder trace de la cellule de sortie.

#### `BoardElement`
Chaque élément présent sur le plateau héritera de cette classe abstraite qui sert à spécifier une fois pour toute que chaque élément du jeu a sa propre position, définie par une paire abscisse/ordonnée.

##### `Tool`
Chaque objet (*aiguille*, *tube* et *éther*) aura une position.

##### `Pawn`
Le pion sera défini par sa position. Il devra se déplacer sur le plateau et ramasser les objets sur son passage. Ces objets seront stockés dans un attribut.

#### `Config`
Cette configuration sera fournie par une classe `Config`, sous forme d'attributs de classe.

*Idéalement*, il faudrait trouver un moyen pour charger automatiquement le contenu d'un fichier de configuration de type YAML ou JSON dans les attributs de classe.

#### `Constants`
Proposera une liste de constantes utiles au programme, sous forme d'attributs de classe.

## Déroulement du programme
Le déroulement du programme peut se définir comme suit :
1. Initialisation du `Game`
    1. Création du `GameBoard` (composition d'objet)
        1. *Parser* le fichier modèle et constituer le plateau
    2. Création du `Pawn`
    3. Création des trois `Tool` (aiguille, tube, éther)
    4. Placer aléatoirement le `Pawn` et les trois `Tool` sur le plateau
2. Déroulement du `Game`
    1. Attente de l'input
    2. À la réception de l'input
        1. Déplacer le `Pawn`

          > Si le déplacement n'est pas autorisé (i.e. mur ou sortie du plateau) : retour à 2.1.
          >
          > Sinon, continuer au 2.2.2

        2. Contrôler si un `Tool` est dans la case de destination

           > Si non, continuer au 2.2.3
           >
           > Si oui, récupérer l'objet pour le `Pawn` et continuer au 2.2.3

        3. Contrôler si la case de destination est la case de sortie

           > Si non, retour à 2.1
           >
           > Si oui

            1. Contrôler si le `Pawn` a bien les trois `Tool` en sa possession

               > Si oui, c'est **gagné :-)**
               >
               > Si non, c'est **perdu :-(**


### UML
Voici la représentation UML (v. 2):

![UML v2][uml_v2]

*À noter que les constructeurs ont été volontairement omis.*

[url_parcours]: https://openclassrooms.com/fr/paths/68-developpeur-dapplication-python
[uml_v2]: ./oc-project-3-uml-2.jpg
