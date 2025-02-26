# Cette équation est une backdoor de la NSA

Dans notre monde extrêmement numérisé, 
maîtriser les mathématiques est devenu une sorte de superpouvoir.
Et celui-ci peut être utilisé pour le bien du plus grand nombre, ou non.
Aujourd'hui, on va voir que, il y a deux décennies,
la NSA semble assez clairement avoir exploité ce superpouvoir,
pour faciliter la cybersurveillance de masse de l'ensemble de la planète,
mais aussi la prise de contrôle des objets électroniques.

Heureusement, dans le cas de la cyber-attaque de la NSA dont on va parler,
d'un côté les mathématiciens de la NSA n'ont pas été particulièrement brillants ;
et surtout, la même maîtrise des mathématiques par des membres de la société civile
a permis d'identifier et de contre-carrer les plans de la NSA ---
NSA qui, rappelons-le, est sous l'autorité du Président des États-Unis d'Amérique,
auquel il est sans doute raisonnable de n'avoir qu'une confiance très limitée.

Bizarrement, 
pour comprendre comment la NSA a failli réussir à piéger tous nos systèmes d'information,
il va nous falloir faire un détour vers les courbes elliptiques,
qui sont des objets remarquables de la géométrie algébrique,
et des composants essentiels de la cryptographie moderne.
En fait, pour regarder la vidéo que vous regardez,
et en particulier pour certifier qu'elle est bien une vidéo envoyée par YouTube,
votre smartphone ou votre ordinateur a dû effectué des opérations sur des courbes elliptiques.


## Les courbes elliptiques

De façon générale, une courbe elliptique est définie
comme l'ensemble des solutions (x,y) de l'équation 
$y^2 = x^3 + ax + b$.

> Pour éviter les singularités, on suppose $4a^3 + 27b^2 \neq 0$.

Le cas suspicieux de la NSA considérait le cas `a = -3` et 
`b = 41058363725152142129326129780047268409114441015993725554835256314039467401291`.
Bon, déjà, ce choix de la valeur de `b` paraît étrange.

Par opposition, l'une des courbes les plus standards aujourd'hui
est l'équation $y^2 = x^3 + 486662 x^2 + x$,
qui définit Curve25519.
Bon, ce n'est pas tout à fait une courbe elliptique en forme standard,
ce qui facilite certains calculs,
mais ce que je veux vous montrer, 
c'est surtout que ses constantes sont beaucoup plus simples,
et plus justifiées, que celles de la NSA.

Mais oublions ces détails pour l'instant.
Ce qui est intéressant à voir, 
c'est que si on trace la courbe $y^2 = x^3 + ax + b$ dans un logiciel comme Desmos,
par exemple ici pour `a = 1` et `b = 1`,
on obtient cette figure assez caractéristique.

Mais ça, ça correspond aux solutions $(x,y)$ pour le corps des nombres réels.
Les mathématiciens se sont amusés à explorer des solutions 
dans d'autres classes de nombres.
Si on considère les solutions dans le corps des nombres complexes,
on obtient alors une surface fermée, mais avec un trou ;
on parle de tore, un peu comme celui qu'on avait vu dans cette 
[vieille vidéo](https://tournesol.app/entities/yt:8v2JxCUDW6M).

Et ça, c'est joli. 
Mais visiblement, pour les mathématiciens, ce n'est pas encore assez joli.
Et ils s'intéressent en fait souvent bien plus aux solutions 
dans le corps des nombres rationnels, c'est-à-dire les fractions d'entiers.
Et d'ailleurs El Jj a fait 
une [excellente vidéo](https://tournesol.app/entities/yt:NEVapv8c-SM) à ce sujet,
où on voit que ces "courbes" sont en fait plein de points discrets.

Mais ce n'est pas tout.
Les mathématiciens vont aussi chercher 
à identifier les solutions des courbes elliptiques 
dans d'autres corps de nombres, 
comme le corps des nombres [p-adiques](https://tournesol.app/entities/yt:tRaq4aYPzCc),
qui ont notamment été utile 
pour [prouver le fameux dernier théorème de Fermat](https://tournesol.app/entities/yt:grzFM5XciAY).

Mais si vous avez suivi cette série,
vous savez désormais que, en cryptographie, 
les solutions qui vont nous intéresser,
ce sont les solutions dans les corps finis,
comme celui des nombres modulo un grand nombre premier p.
Dans le cas de l'équation de la NSA, 
qui définit un protocole appelé Dual\_EC\_DRBG,
ce nombre est `p = 115792089210356248762697446949407573529996955224135760342422259061068512044369`.
Pour la courbe Curve25519, 
qui pour rappel est la plus standard et la plus sécurisée aujourd'hui,
on a $p = 2^{255} - 19$.
C'est beaucoup plus propre que le choix étrange de la NSA !

C'est d'ailleurs de cette valeur du nombre premier 
que vient le nom de Curve25519.
Et en plus d'être une expression relativement naturelle,
les nombres peuvent être écrits du corps peuvent être écrits avec 256 bits,
et que les calculs peuvent être optimisés 
car $p = 2^{255} - 19$ est un quasi-nombre premier de Mersenne,
comme on en a parlé dans une [vidéo précédente](https://tournesol.app/entities/yt:kkU8u6IWrVs).


## Une courbe elliptique est un groupe

La propriété fondamentale des courbes elliptiques, 
quels que soient le corps des nombres qu'on considère,
c'est que l'ensemble de ses points peuvent être combiné algébriquement.
Autrement dit, étant donné n'importe quels points P et Q déjà sur la courbe,
je peux combiner P et Q pour fabriquer un troisième point R sur la courbe.

Et la manière la plus simple de voir 
comment cette composition des points d'une courbe elliptique opère
consiste à revenir au cas le plus visuel,
à savoir celui du ces nombres réels,
puisqu'on a alors une courbe elliptique 
qui ressemble vraiment à ce qu'on pense, quand on entend le mot "courbe".

Considérons deux points P et Q sur cette courbe.
Je peux alors construire un troisième point R sur cette courbe,
en traçant la droite qui passe par P et Q,
en observant qu'elle coupe la courbe elliptique à un 3e point,
et en prenant le symétrique de ce point selon l'axe des abscisses.

Et si je vous décris ces opérations géométriquement,
on peux très bien en avoir une description algébrique aussi,
grâce à la magie de la géométrie algébrique.
Allez, on va se faire une petite minute de calculs,
que vous pouvez sauter sans perdre le fil de la vidéo.

Appelons ainsi $y^2 = x^3 + ax + b$ la courbe elliptique,
et $y = cx + d$ la droite qui passe par P et Q.
Déterminer les intersections entre la courbe elliptique et la droite,
ça revient à résoudre ces deux équations à la fois.
En injectant l'expression y selon l'équation de la droite
dans l'équation de la courbe elliptique,
on obtient $(cx + d)^2 = x^3 + ax + b$,
qu'on peut réécrire $c^2 x^2 + 2cd x + d^2 = x^3 + ax + b$.
En mettant tout à droite de l'équation, on obtient
$x^3 - c^2 x^2 + (a - 2cd) x + (b-d)^2 = 0$,
ce qui est une équation de degré 3 en $x$.

Et là, on pourrait vouloir sortir la calculatrice,
mais il y a en fait une remarque plus maligne à faire.
En effet, on sait que parmi les points d'intersection 
entre la courbe elliptique et la droite, il y a les points P, Q et R.
Mais donc, on sait que les abscisses de ces points sont solution de l'équation.
Appelons $x_P$, $x_Q$ et $x_R$ ces points d'intersection.
Alors, d'après la théorie des polynômes, 
on sait que toute équation de degré 3 qui s'annule en ces 3 points doit s'écrire
$(x-x_P)(x-x_Q)(x-x_R)$.
Comme c'est le cas de notre équation de l'intersection 
entre la courbe elliptique et la droite,
on sait donc que
$x^3 - c^2 x^2 + (a - 2cd) x + (b-d)^2 = (x-x_P)(x-x_Q)(x-x_R)$.

Ok, on y presque !
Maintenant, on va développer le terme de droite, ce qui donne
$(x-x_P)(x-x_Q)(x-x_R) = x^3 - (x_P + x_Q + x_R) x^2 + autres$.
Ce qui va m'intéresser maintenant, c'est d'identifier les coefficients de degrés 2.
En effet, par égalité des polynômes, 
on sait qu'on doit avoir
$c^2 = x_P + x_Q + x_R$.
Mais donc, $x_R = c² - x_P - x_Q$.
Notez qu'on peut estimer la pente $c$ de la droite 
en calculant le taux d'accroissement entre les points $P$ et $Q$, 
ce qui donne $c = (y_P - y_Q) / (x_P - x_Q)$,
et donc on a $x_R = (y_P - y_Q)^2 / (x_P - x_Q)^2 - x_P - x_Q$.
On peut ensuite en déduire $y_R$ en utilisant le fait que R est sur la droite,
ce qui donne $y_R = c x_R + d = (y_P - y_Q) (x_R - x_P) / (x_P - x_Q) + y_P$.

Si vous n'avez pas suivi tous les calculs, ne vous en faites pas.
Ce que je veux vraiment vous montrer,
c'est que les coordonnées du point R peuvent se calculer algébriquement,
en combinant les coordonnées des points P et Q à l'aide uniquement 
d'additions, de soustractions, de multiplications et de divisions.
Et c'est ça qui rend la géométrie algébrique si puissante.
En effet, désormais, on peut oublier complètement l'interprétation géométrique,
et utiliser ces relations pour d'autres classes de nombres.

En particulier, la construction se généralise aux nombres complexes, rationnels et p-adiques,
mais aussi et surtout aux corps finis.
Pour les corps finis aussi,
n'importe quelle paire de points d'une courbe elliptique peut se combiner,
et nous fournir un troisième de la courbe elliptique ;
qui rappellons-le, est en fait un ensemble fini de points $(x,y)$
où $x$ et $y$ sont des nombres d'un corps fini.

Enfin, ce n'est pas tout à fait exact.
Et oui, dans nos équations, on a une division par $x_P - x_Q$.
Or si $x_P = x_Q$, alors $x_P = x_Q$, et on a donc une division par zéro.
Or ça, c'est vraiment ultra-interdit, non seulement dans le corps des nombres réels,
mais aussi dans tous les autres corps,
y compris donc dans le corps des nombres finis.

En fait, si on regarde notamment la courbe elliptique pour les nombres réels, 
il y a exactement 2 cas où $P$ et $Q$ sont sur la courbe et où ils ont la même abscisse :
soit $P = Q$, soit $P$ est le symétrique de $Q$ selon l'axe des abscisses.
Dans le premier cas, l'astuce est de dire que $Q$ est un point limite 
d'une suite $Q_1$, $Q_2$, ... qui tend vers $P$.
On va alors exiger que la combinaison de $P$ et $Q$ est 
la limite des combinaisons de $P$ et $Q_n$.
Formellement, ceci revient à considérer la tangente à la courbe elliptique qui passe par $P$,
et à définir $R$ comme le symétrique de l'autre intersection 
de la tangente avec la courbe elliptique.

Dans le second cas, on va considérer et la combinaison de $P$ avec $Q$,
qui est donc la combinaison de $P$ avec lui-même, 
est égal à un point fictif,
qu'on va appeler $0$, 
et qu'on va considérer être un point un peu spécial de la courbe elliptique.
Ce point fictif aura par ailleurs la propriété de n'avoir aucun effet,
quand on le combine à n'importe quel autre point de la courbe.
Autrement dit, combiner $0$ et $P$ fait $P$.

Et voilà, on a notre façon de combiner toutes les paires de points
de notre courbe elliptique étendue.
On dit que l'opération qu'on a définie est une loi de composition interne,
et on peut la noter `R = Compo(P, Q)`.
Et on peut même faire la remarque que cette loi de composition a de très belles propriétés :
1. Il y a un élément "neutre", dans le sens où il a un effet nul sur tout point.
Autrement dit, pour tout point P de la courbe elliptique, on a `Compo(P, 0) = P`.
2. Pour tout point P de la courbe elliptique, il existe un point Q de la courbe elliptique, 
qui est son symétrique par rapport à l'axe des abscisses, 
tel que combiner `Compo(P, Q) = 0`.
On dit que la loi de composition est inversible, et que `Q` est l'inverse de `P`.
3. Si P, Q et R sont des points de la courbe elliptique, 
alors on peut démontrer `Compo(Compo(P, Q), R) = Compo(P, Compo(Q, R))`.
Bon, ça requiert des calculs pour le vérifier.
Mais du coup, on dit que la loi de composition est associative.
4. Si P et Q sont des points de la courbe elliptique,
alors `Compo(P, Q) = Compo(Q, P)`.
Ça, ça vient simplement du fait que la droite qui passe par P et Q,
et bah, c'est la même que celle qui passe par Q et P ;
ces deux points jouent un rôle symétrique dans la définition géométrique
de la loi de composition des points de la courbe elliptique.
On dit cette loi de composition interne est commutative.

Grâce à ces 4 propriétés, 
la courbe elliptique, étendue avec un 0, et munie de sa loi de composition interne
forme alors ce qu'on appelle un groupe commutatif.

> on dit parfois abélien.

Et de façon remarquable, ce sera le cas,
quel que soit le corps des nombres sur lequel la courbe elliptique est définie.
Dès lors, on va simplifier les notations, 
et remplace l'opérateur `Compo` par un signe usuel pour les groupes commutatifs.
Dans cette vidéo, je vais utiliser le signe $\oplus$,
pour montrer que ça ressemble à l'addition sans être l'addition usuelle ;
mais beaucoup de ressources, y compris Wikipedia, utilisent le signe usuel de l'addition $+$.
En tout cas, grâce à cette opération $\oplus$,
on peut maintenant ajouter des points de la courbe elliptique.
Faites très attention toutefois,
l'addition des points de la courbe elliptique n'est pas du tout une addition usuelle ;
en particulier, elle ne correspond absolument pas à l'addition des coordonnées.
C'est une opération plus complexe ;
mais cela reste une opération algébrique, 
conformément aux équations qu'on a identifiées plus haut.

$x_R = (y_P - y_Q)^2 / (x_P - x_Q)^2 - x_P - x_Q$,
$y_R = (y_P - y_Q) (x_R - x_P) / (x_P - x_Q) + y_P$.

Bien sûr, en cryptographie, le cas qui nous intéresse particulièrement,
c'est celui des corps finis.
Et en fait, ce qui nous intéresse même particulièrement en cryptographie,
ça va être le groupe cyclique engendré par un point de la courbe...


## Visualisation des courbes elliptiques sur des corps finis

Pour bien se rendre compte de la magie des courbes elliptiques,
j'ai développé une petite application web,
accessible à [ellipticcurve.science4all.org](https://ellipticcurve.science4all.org).
Vous pouvez rentrer vos paramètres de la courbe elliptique,
à savoir les coefficients $a$ et $b$ de l'équation $y^2 = x^3 + ax + b$,
et le nombre $p$ modulo lequel on va effectuer les calculs.

Pour $a = 1$, $b = 1$ et $p = 5$ par exemple,
c'est-à-dire la courbe $y^2 = x^3 + x + 1 [5]$,
on peut tracer un quadrillage 
dont les intersections sont les points $(x, y)$ qui sont des entiers modulo $p$,
et on peut ensuite placer explicitement ceux qui sont solutions de l'équation modulo $p$.
L'ensemble des points à l'écran correspond exactement à la courbe elliptique...
ou presque ! N'oublions pas le point à l'infini qui n'est pas représenté ici.
Ça nous fait donc une courbe composée de 1, 2, 3, 4, 5, 6, 7, 8 et 9 points.

Ainsi le point $(x = 0, y = 1)$ est bien un point de la courbe elliptique, 
puisqu'il vérifie bien l'équation $y^2 = x^3 + x + 1$.
En effet, si je remplace $y$ par 1, j'obtiens 1 à gauche,
et si remplace $x$ par 0, j'obtiens $0 + 0 + 1 = 1$ à droite.
De même, le point $(2, 1)$ est aussi solution,
puisque $y^2$ est alors égal à $1^2 = 1 [5]$, 
et $x^3 + x + 1$ est égal à $2^3 + 2 + 1 = 8 + 2 + 1 = 11 = 5 + 5 + 1 = 1 [5]$.

Sur le corps fini des nombres modulo $5$,
clairement, notre courbe elliptique ne ressemble plus trop à une courbe.
Néanmoins, l'ensemble de ses points n'a rien d'aléatoire !
Au contraire, il dispose de nombreuses propriétés fascinantes.

On peut commencer par observer une symétrie par rapport à l'axe des abscisses,
qui vient tout simplement du fait que $y$ doit être une racine carrée de $x^3 + x + 1$.
Et bien sûr, si $y$ est une racine carrée, alors $-y$ le sera aussi.

De façon plus spectaculaire, si je prends deux points de la courbe elliptique,
ils couperont un troisième point de la courbe.
Par exemple, si je prends les points $(0, 1)$ et $(2, 1)$,
alors la droite qui passe par ces points coupera un troisième point, à savoir $(-2, 1)$.
D'ailleurs, ça, ça implique que la somme $(0, 1) \oplus (2, 1)$ dans la courbe elliptique
va donner comme résultat l'image du troisième point $(-2, 1)$ par l'axe des abscisses,
à savoir $(-2, -1)$.
On a l'égalité $(0, 1) \oplus (-2, 1) = (-2, -1)$.

De même, la droite qui passe par $(-1, -2)$ et $(0, -1)$ passe aussi par $(2, 1)$,
ce qui revient à dire que $(-1, -2) \oplus (0, -1) = (2, -1)$.

Mais il y a plus vicieux.
Si je prends la droite qui passe par $(-1, -2)$ et $(2, -1)$,
on pourrait croire dans un premier temps qu'elle ne passe pas 
par un troisième point de la courbe elliptique,
comme le suggère ce dessin.
Sauf qu'il ne faut pas oublier qu'on travaille modulo un nombre premier $p$.
Et donc, en fait, le point tout à droite, en $(2.5, -0.67)$,
c'est en fait le même que le point à gauche, en $(-2.5, -0.67)$.
En fait, l'ensemble des coordonnées modulo $p$, 
ça correspond en fait au monde de Pacman, où les côtés opposés sont en fait collés.
Dans le jargon, on parle en fait de tore carré,
comme celui dont je vous avais parlé 
dans une [vieille vidéo](https://tournesol.app/entities/yt:8v2JxCUDW6M).

Bref. Du coup, la droite qui sort à droite doit réapparaître à gauche.
Et quand elle sort en haut, elle doit réapparaître en bas.
Et c'est ainsi que cette droite finit bel et bien par couper un troisième point,
à savoir (-2, 1).
Magique, non ?

Et bien, sur l'application que j'ai développé, 
vous pourrez tester cela avec toutes sortes de paires de points,
et vous verrez qu'il y a toujours une troisième intersection.
Et c'est quand même fou ! 
A priori, ça n'a absolument rien d'évident que de placer des points dans l'espace
avec cette propriété remarquable.
Mais comme vous voyez, cela marche en fait toujours...

Ou presque. Voici un cas où ça ne marche pas.
Si je prends deux points avec la même abscisse, comme (0, 1) et (0, -1),
je n'ai pas de 3e intersection.
Mais vous voyez pourquoi ce n'est pas un problème ?
En fait, on a introduit le $0$ des courbes elliptiques précisément pour résoudre ce problème.
La droite qui passe par deux points symétriques par l'axe des abscisses
va être défini comme étant égal à un point infini tout en haut,
qu'on appelle le $0$.
Et d'ailleurs, on voit que cela implique bien que les points symétriques
selon l'axe des abscisses sont bien opposé selon l'opération des courbes elliptiques.
En effet, comme $(0, 1) \oplus (0, -1) = 0$,
ce qu'on pourrait écrire $(0, 1) = \ominus (0, -1)$.

Enfin, si vous testez bien toutes les possibilités,
vous finirez peut-être par tomber sur une autre exception.
Par exemple, la droite qui passe par $(-2, -1)$ et $(0, 1)$
ne semble couper aucun autre point.
Bizarre, non ?

Si vous regardez l'application, 
vous verrez qu'elle dit toutefois que leur combinaison est censée donner le point $(-2, 1)$.
Vous voyez ce qu'il se passe ?
On semble avoir $(-2, 1) \oplus (0, 1) = (-2, 1) = \ominus (-2, -1)$.
Mais donc, on a en fait $(-2, 1) \oplus (0, 1) \oplus (-2, 1) = 0$.
En fait, la droite qui passe par $(-2, 1)$ et $(0, 1)$ passe deux fois par $(-2, 1)$.
C'est une droite qui est en fait tangente à la courbe elliptique en $(-2, 1)$.
Vous pouvez le vérifier sur l'application 
en traçant la droite qui passe par $(-2, 1)$ et $(-2, 1)$ :
elle passe bien par $(0, 1)$.
Voici la seule exception à la règle des trois intersections,
lorsqu'on tient bien compte du point à l'infini en haut.

Bref, je vous laisse explorer l'application, 
si vous voulez bien sentir les courbes elliptiques sur les corps finis.
Mais gardez toutefois en tête que ce que vous pourrez visualiser,
ce sera inéluctablement restreint à de petits nombres premiers $p$.
Ce qui rend les courbes elliptiques si utiles à la cryptographie,
c'est précisément leur complexité pour de grandes valeurs de $p$,
pour lesquelles tout effort de visualisation est peine perdue...


## Groupe cyclique et exponentiation

En pratique, en cryptographie, on va considérer un point G de la courbe elliptique,
et à tous les points qu'on peut obtenir en ajoutant G à lui-même un certain nombre de fois.
Appelons ainsi $w G$ le résultat de l'addition $G + G + ... + G$,
avec n copies du point G.
L'ensemble des points obtenus ainsi est appelé le groupe cyclique généré par le point G.

> Ceci correspond formellement à un morphisme de groupe `EntierRelatif -> CourbeElliptique`.

Prenons l'exemple de $G = (2, 1)$ de la courbe $y^2 = x^3 + x + 1 [5]$.
D'après l'application, on a alors $2G = G \oplus G = (2, -1)$.
Puis $3G = G \oplus 2G = (2, 1) \oplus (2, -1) = 0$.
On vient de retomber à 0 après 3 itérations.
Mais du coup, $4G = G \oplus 3G = G \oplus 0 = G$.
En fait le groupe généré par $G$ n'a ici que 3 éléments.
Et en particulier, on n'a absolument pas visité les 9 points
de la courbe elliptique $y^2 = x^3 + x + 1$ modulo $5$.
Si vous avez vu la vidéo sur les [nombres premiers sûrs](https://tournesol.app/entities/yt:gQAvq620lSI),
cela ne vous surprend peut-être pas.
En fait, $y^2 = x^3 + x + 1 [5]$ n'est pas une très bonne courbe elliptique,
car son nombre de points, à savoir 9, est un nombre friable,
c'est-à-dire qu'il s'écrit comme le produit de nombre premiers tous très petits.

À l'inverse, considérons la courbe $y^2 = x^3 + 2x + 1 [5]$.
Comme vous pouvez le voir dans l'application,
cette courbe a 6 points finis, plus le point $0$ à l'infini,
soit un total de 7 points.
Et 7, c'est beaucoup mieux que 9, puisque 7 est un nombre premier.
En particulier, peu importe votre point $G$ initial,
le groupe engendré par $G$ va lui bien passer par tous les points de la courbe elliptique.

Notez que Curve25519 lui n'a pas cette jolie propriété, mais elle l'a presque.
Son nombre de point est en effet égal à $8r$,
où $r = 2^{252} + 27742317777372353535851937790883648493$ est lui bel et bien un nombre premier,
dont la taille est cryptographiquement grande.
En particulier, en pratique, on a choisi un point $G$ de Curve25519
tel que le groupe engendré par ce point $G$ est d'ordre $r$ uniquement.
Notez que ce groupe est isomorphe au groupe additif des entiers modulo $r$ ;
mais de façon cruciale, cet isomorphisme est à sens unique :
c'est facile de calculer $w G$ étant donné un nombre $w$ modulo $r$,
mais c'est très difficile, étant donné un point $X$ du groupe engendré par $G$,
de déterminer une valeur de $w$ modulo $r$ telle que $X = w G$,
même pour une superpuissance numérique.

En fait, ce $X = w G$ des courbes elliptiques, 
c'est exactement l'équivalent du $x = g^w [p]$ dont on avait parlé 
dans une [vidéo précédente](https://tournesol.app/entities/yt:gQAvq620lSI).
En particulier, si $X = w G$ peut se calculer rapidement,
c'est grâce à l'astuce des carrés répétés.
Formellement, le nombre d'opérations nécessaires sera logarithmique en $r$.
Et de manière pratique, 
ça veut dire que $X = w G$ peut se calculer très rapidement,
même pour des valeurs cryptographiquement grandes de $w$.

Toutefois, à l'inverse, étant donné les coordonnées d'un point $X$ d'une courbe elliptique,
déterminer pour quelle valeur de $w$ on a $X = w G$,
eh bien, on ne sait pas faire.
Mieux encore, on suspecte que personne ne saura le faire,
à moins de lister une bonne partie des 
plus de $2^{252}$ valeurs possibles de $w G$,
jusqu'à en trouver une qui correspond à $X$.
Dit autrement, on pense
que le problème du logarithme discret pour les courbes elliptiques 
est essentiellement impossible pour les superpuissances numériques d'aujourd'hui...
même si on sait que celles qui auront un calculateur quantique dans le futur
pourront inverser ce composant fondamental de la cryptographie moderne.

Mais oublions les calculateurs quantiques pour aujourd'hui,
comme le font en gros presque toutes les entreprises de cybersécurité.
On pense donc que calculer $X = w G$ est aujourd'hui une fonction à sens unique.
D'autant que le nombre d'éléments qu'on peut ainsi construire, 
à savoir $2^{252} + 27742317777372353535851937790883648493$,
est un nombre premier,
ce qui empêche toute attaque à la Pohlig-Hellman 
dont on a parlé dans un épisode précédent.


## Mieux que RSA et l'exponentiation modulaire

Oui, parce que tout ça, mathématiquement, c'est super joli.
Mais en a-t-on vraiment besoin ?
Pourquoi a-t-il fallu utiliser ces mathématiques aussi complexes
pour pouvoir faire de la cryptographie ?
Est-ce que l'exponentiation modulaire qu'on a vu plus tôt dans cette série ne suffit pas ?
Et quid de RSA, dont je vous ai parlé sur la chaîne String Theory ?

Pour rappel, RSA est un autre chiffrement, 
qui s'appuie sur l'hypothèse selon laquelle multiplier 
deux très grands nombres premiers $p$ et $q$ pour obtenir $N = pq$
est une fonction à sens unique :
facile à faire, et extrêmement difficile à défaire.
De même, l'exponentiation modulaire s'appuie sur la fonction $x = g^w [p]$,
qu'on suppose aussi être à sens unique.

Et en gros, oui, ces opérations sont à sens unique,
contre les meilleurs calculateurs et les meilleurs algorithmes d'aujourd'hui.
Mais elles ne le sont en fait pas *maximalement*.

Plus précisément, [l'algorithme généralisé du crible de nombres](https://ntnuopen.ntnu.no/ntnu-xmlui/bitstream/handle/11250/2394427/14190_FULLTEXT.pdf) 
est capable de casser ces deux problèmes,
en un temps d'environ
$\exp \left( \sqrt[3]{\frac{64}{9}} (\ln p)^{1/3} (\ln \ln p)^{2/3} \right)$,
qui est sous-exponentiel en le nombre de chiffres du nombre premier $p$.
Alors, c'est sous-exponentiel, dans le sens où ça finit par être inférieur
à n'importe quelle fonction $\exp( c \ln p)$.
Mais qu'on soit clair, ça reste superpolynomial en le nombre de chiffre de $p$,
et en particulier infaisable par les supercalculateurs dès que $p$ a beaucoup de chiffres.

Pour quantifier la sécurité d'un nombre premier $p$,
comme on l'a vu dans un [épisode précédent](https://tournesol.app/entities/yt:v_sz0elq0eo),
on utilise la mesure en nombre de bits $b$ de sécurité calculatoire,
c'est-à-dire le nombre $b$ tel qu'un attaquant pourra casser le chiffrement
en effectuant $2^b$ opérations.
Je vous épargne des détails de calculs,
mais si on appelle $k$ le nombre de chiffres de $p$ en écriture binaire,
alors le nombre de bits de sécurité calculatoire sera donné par cette fonction
$b = \log_2 \exp \left( \sqrt[3]{\frac{64}{9}} (k \ln 2)^{1/3} (\ln (k \ln 2))^{2/3} \right)$.
Avec $1024$ bits de $p$, on obtient $b \approx 87$ bits de sécurité.

```
import numpy as np
b = lambda k: np.log2(np.exp(np.power(64/9, 1/3) * np.power(k * np.log(2), 1/3) * np.power(np.log(k*np.log(2)), 2/3)))
b(1024)
b(3072)
```

En pratique, on a tendance à viser $120$ bits de sécurité pour la plupart des applications,
ce qui peut s'obtenir avec $p = 3072$.
Plus précisément, pour des clés de $3072$ bits, 
on aura environ 139 bits de sécurité.

Cependant, cette vulnérabilité de l'exponentiation modulaire et de RSA
à l'algorithme généralisé du crible des nombres,
elle vient vraiment des propriétés des nombres,
sur lesquelles s'appuient fortement ces solutions cryptographiques.
En particulier, jusque là, personne n'a su généraliser cet algorithme
pour casser le chiffrement par courbes elliptiques --- 
sauf pour certaines courbes elliptiques avec des propriétés très particulières.

En fait, l'algorithme le plus rapide connu pour casser le chiffrement par Curve25519
est l'algorithme rho de Pollard,
qui requiert un temps de calcul de l'ordre de $\sqrt{p}$,
qui est bien exponentiel en le nombre de chiffre de $p$,
puisqu'on peut aussi l'écrire $2^(k/2)$,
où $k = \log2(p)$ est le nombre de chiffre de $p$.
Et du coup, en utilisant un $p = 2^255 - 19$ comme le fait Curve25519,
ce nombre de chiffre est $k = 254$,
et elle conduit à $b = k/2 = 127$ bits de sécurité !

Autrement dit, on a la même sécurité,
malgré des clés dix fois plus petites.
Voilà qui permet à la cryptographie par courbes elliptiques
d'être significativement moins coûteuse en temps de calculs,
pour un même niveau de sécurité calculatoire.


## Secret partagé et signature cryptographique

Comme la fonction $x = g^w [p]$ dont on a parlé dans une vidéo précédente,
la fonction $X = w G$ est une fonction à sens unique,
qui est de surcroît un isomorphisme de groupe et est quasi-commutative.
Et du coup, on peut utiliser les mêmes constructions que celles de la vidéo précédente,
pour concevoir des protocoles de Diffie-Hellman pour créer des secrets partagés,
ou à la El Gamal pour signer cryptographiquement des messages.

Dans Diffie-Hellman avec courbes elliptiques, ou ECDH en anglais,
Alice et Bob pense chacun à un grand nombre secret aléatoire $w_A$ et $w_B$.
Typiquement, s'ils utilisent Curve25519,
ils peuvent utiliser des nombres à 255 bits.

Chacun calcule les points $X_A = w_A G$ et $X_B = w_B G$, qu'ils rendent publics.
Alice calcule ensuite $w_A X_B$, et Bob calcule $w_B X_A$.
Et là, magie magie, on se rend compte 
qu'ils ont en fait calculé le même point $S$ sur la courbe elliptique.
En effet, $S = w_A X_B = w_A (w_B G) = (w_A w_B) G$,
qui est bien symétrique en A et B.

Et de manière cruciale, cette information partagée est bien secrète,
car même sachant $G$, $X_A$ et $X_B$,
on suppose qu'un attaquant sera incapable de deviner ni $w_A$, ni $w_B$ ni $S$,
en utilisant le fait que la fonction 
qui calcule $X_A = w_A G$ avec $w_A$ est à sens unique.

Ensuite, Alice et Bob vont typiquement appliquer une fonction de hachage
au secret partagé $S$,
pour obtenir une clé partagée `K = Hash(S)`
qui va être utilisée ensuite pour les communications chiffrées symétriquement,
comme on le verra dans une future vidéo.

Le cas de la signature cryptographique par courbe elliptique, ou ECDSA en anglais,
est similaire, en copiant cette fois le protocole d'El Gamal.
Appelons $q$ le nombre d'éléments de la courbe elliptique,
qui est donc $2^{252} + 27742317777372353535851937790883648493$ pour Curve25519,
et qui, rappelons-le, est dans ce cas premier.
On tire au hasard $k$ entre $1$ et $q-1$.
Puis on calcule $R = k G$ et $s = (H(m) - R_x w) / k [q]$,
où $H(m)$ est le hash du message $m$ à signer 
et $R_x$ est la coordonnée de $R$ selon $x$.
Encore une fois, l'intuition, c'est d'obtenir un $s$
qui mélange le message $m$, le clé privée $w$ et de la randomisation via $k$.
On publie alors $(R, s)$, qui forme la signature cryptographique.
La vérification s'effectue ensuite en vérifiant que $H(m) G = s R + R_x X$.

Alors, le protocole peut être davantage optimisé,
en publiant uniquement la coordonnée $R_x$ de $R$,
ce qui nécessite de diviser l'égalité de vérification par $s$,
et de regarder uniquement selon la coordonnée $x$, ce qui donne
$R_x = ((H(m)/s) G - (R_x/s) X)_x$.
Mais du coup, il faut que $s$ soit non nul :
si on obtient $s = 0$, on va simplement tirer un autre $k$ au hasard.
Enfin, dernière chose qui n'a aucune importance théorique,
l'algorithme standard remplace la soustraction dans le calcul de $s$ par une addition
$s = (H(m) + R_x w) / k [q]$,
ce qui donne ensuite la vérification $R_x = ((H(m)/s) G + (R_x/s) X)_x$.

Bref, les courbes elliptiques sont aujourd'hui abondamment utilisées 
pour chiffrer ou pour authentifier des messages.
Mais étrangement, c'est pour une autre application encore
que la NSA proposa Dual\_EC\_DRBG.


## La backdoor de la NSA

On y vient ! On va enfin parler de la probable backdoor de la NSA.
Pour commencer, parlons de ce que le protocole proposé est censé permettre :
il s'agit de produire des nombres aléatoires.
Alors, vous pourriez croire que c'est facile de créer des nombres aléatoires,
mais la difficulté, 
c'est en fait davantage de produire des nombres *imprévisibles*.
Autrement dit, ils doivent être aléatoires au sens de Laplace et du bayésianisme :
même en sachant tous les nombres aléatoires générés précédemment,
idéalement, même le [démon de Laplace](https://tournesol.app/entities/yt:H71WR50stm4),
ou disons plutôt le [démon de Solomonoff](https://tournesol.app/entities/yt:6N0dlorL0r8),
devrait être incapable de prédire le prochain nombre de la suite mieux que le hasard.

Voilà qui est indispensable pour de nombreuses applications cruciales de la cryptographie.
Par exemple, comme on l'a vu, 
le protocole Diffie-Hellman requiert la génération de nombres aléatoires.
Mais si vous avez un moyen de deviner le secret de Bob,
alors vous pourrez non seulement usurper l'identité Bob 
et dire à Alice des éléments trompeurs au nom de Bob ;
mais vous pourrez même usurper l'identité d'Alice et piéeger Bob !
Plus généralement, de nombreux systèmes modernes exploitent à foison 
ce qu'on appelle des tokens aléatoires,
à savoir des nombres qu'Alice peut typiquement envoyer à Bob,
et que Bob pourra réutiliser pour affirmer être Bob.
Rien à voir avec les tokens des algorithmes de langage...
Si ces tokens aléatoires peuvent être prédits, même uniquement de temps en temps,
alors l'attaquant pourra en fait régulièrement infiltrer de nombreux systèmes d'information.

Alors, en pratique, un hasard imprévisible par le démon de Solomonoff est trop coûteux à obtenir ;
du coup, on se contente de générer une suite de nombres,
en espérant qu'une superpuissance numérique soit incapable de la prolonger mieux que le hasard,
à cause de ses limites en puissance de calculs,
comme on en a parlé dans une [vidéo précédente](https://tournesol.app/entities/yt:Sbh3-EHgawI).
Et oui, pour rappel, 
toute superintellygence du monde physique est très inférieure au démon de Solomonoff,
qui lui-même est très inférieur au démon de Laplace.

Eh bien, la NSA a proposé un algorithme qui génère une suite de nombres,
en suggérant que toute superpuissance numérique sera incapable 
de prédire le suivant mieux que le hasard.
Enfin, pour être exact, c'est le NIST, 
le National Institute of Standards and Technology,
qui [a proposé ce standard](https://csrc.nist.gov/pubs/sp/800/90/a/final).

Et c'est là qu'on rentre dans une frontière fine et floue 
en théorie du complot et confiance justifiée en les institutions.
Clairement le NIST est proche de la NSA.
Mais ça ne veut pas dire que tout ce que dit le NIST est une backdoor ;
en tout cas, je vous assure ne pas avoir été contacté par le NIST
pour [leur rapport sur la sécurité de l'IA](https://csrc.nist.gov/pubs/ai/100/2/e2023/final),
même si le NIST cite un de mes algorithmes 
comme étant l'une des solutions à l'état de l'art à adopter
pour atténuer les risques d'empoisonnement des modèles d'IA.
Et plus généralement, quand le NIST justifie ses standards 
par des recherches scientifiques publiées par des chercheurs indépendants
dans des revues scientifiques de renom,
comme c'est davantage le cas de la cryptographie postquantique dont on reparlera,
il y a de quoi avoir raisonnablement confiance en ses recommandations.
Mais le cas de l'algorithme de génération de nombres aléatoires proposé par le NIST en 2012
est beaucoup plus louche...

Cet algorithme s'appuie sur une courbe elliptique,
à savoir $y^2 = x^3 - 3x + b$,
où `b = 41058363725152142129326129780047268409114441015993725554835256314039467401291`,
dans le corps fini à 
`p = 115792089210356248762697446949407573529996955224135760342422259061068512044369` éléments,
et sur deux points `P` et `Q` de la courbe,
dont les coordonnées sont... des grands nombres.
Ici, je donne leur écriture en hexadecimale, c'est-à-dire en base 16.

Pour générer la suite, 
NIST propose de commencer par prendre un nombre $w_0$ à 256 bits, 
qu'on appelle la graine, ou seed en anglais.
Puis l'algorithme calculs $P_1 = w_0 P$, avec l'exponentiation rapide.
Et il définit son nouvel état $w_1$ comme étant la coordonnée $x$ de $P_1$.
Autrement dit, il pose $w_1 = (w_0 P)_x$.
Notez que $w_1$ est alors bien un nombre à 256 bits.

Ce nombre est alors utilisé pour générer un nombre aléatoire,
en utilisant la même opération, mais cette fois à partir du point Q.
Autrement dit, on pose $r_1 = (w_1 Q)_x$, 
qui est lui aussi un nombre à 256 bits.
En fait, non, pour éviter de révéler trop d'information,
on va effacer les 16 premiers bits $(w_1 Q)_x$.
On pose donc $r_1 = Trim_{16}( (w_1 Q)_x )$,
où Trim est cette fonction qui efface les premiers bits.

Puis, on réeffectue les mêmes opérations, 
en partant de $w_1$ au lieu de $w_0$.
Autrement dit, la suite générée est définie par les équations
$w_k = (w_{k-1} P)_x$
et $r_k = Trim_{16} ( (w_k Q)_x)$.
Et ce que le NIST prétend,
c'est que sachant les observations $r_1$, $r_2$, $r_3$, ..., $r_k$,
il est impossible de deviner la valeur de $r_{k+1}$.

OK... mais présenté ainsi, c'est déjà étrange...
Est-ce qu'on a vraiment la garantie que cette suite paraît aléatoire ?
Est-ce que retirer 16 bits suffit vraiment ?
Et pourquoi avoir choisi ces deux points P et Q en particulier ?
Étonnamment, NIST ne justifie pas le choix de ces points.

Et c'est là que réside probablement la backdoor de la NSA.
Pour commencer, noter que si on connaît $r_1$,
alors il ne reste que 16 bits à deviner pour déterminer $(s_1 Q)_x$.
Sauf que 16 bits à deviner, ça fait $2^{16}$ possibilités,
soit seulement 65 536.
Or c'est complètement gérable d'explorer toutes ses possibilités avec une machine !
Étrange, étrange...

Passons maintenant à l'autre bizarrerie : les choix de P et Q,
qui sont très peu justifiés dans le rapport du NIST.s
Si la NSA est malicieuse,
alors elle a pu choisir un point Q de la courbe, 
choisir un nombre secret $e$ à 256 bits,
et calculer ensuite $P = e Q$.

Testons donc l'une des 65 536 valeurs possibles de $(s_1 Q)_x$ sachant $r_1$.
Si on connaît $(s_1 Q)_x$,
alors on peut déterminer $s_1 Q$;
il suffit de résoudre $y^2 = (s_1 Q)_x^3 - a (s_1 Q)_x + b [p]$,
ce qui revient à calculer une racine carrée module p.
Il y a par exemple l'algorithme de Tonelli-Shanks qui permet de le faire efficacement.

Maintenant, pour prédire $r_2$, ce serait bien de connaître $s_2$.
Est-ce possible ?
Et bien, on a $s_2 = (s_1 P)_x$.
Mais une NSA malicieuse peut alors avoir choisi $P = e Q$.
Dès lors, on aurait $s_2 = (s_1 e Q)_x = ( e (s_1 Q) )_x$.
Vous le voyez venir, sachant $(s_1 Q)_x$,
on peut en fait calculer le prochain état $s_2$ du générateur,
et donc le nombre aléatoire $r_2$ qu'il va générer.

Alors, bien sûr, en observant $r_1$, on n'apprend pas $(s_1 Q)_x$.
Mais on connaît 65 536 valeurs qu'il peut prendre.
Et donc, on connaît 65 536 valeurs que $r_2$ peut prendre.
L'observation de $r_2$ nous permttra alors quasi-assurément
de trancher sur la valeur de $(s_1 Q)_x$,
ce qui fait que le générateur de nombre aléatoire n'aura plus aucun secret pour nous ;
ou, plus précisément, pour quiconque connaîtrait le secret $e$
qui lie les points $P$ et $Q$ dont le choix est si peu justifié.

Alors bien sûr, le NIST prétend que
déterminer la solution $e$ à l'équation $P = e Q$
revient à inverser une fonction qu'on considère être à sens unique ;
mais le problème, c'est de savoir si le NIST a d'abord choisi $e$,
et a ensuite calculer $P$ pour que cette équation soit vérifiée.
Vu le peu d'explication sur le choix de ces points,
personnellement, j'ai mon bullshit alert rouge écarlate...


## Conclusion

Ce dont j'espère vous avoir convaincu aujourd'hui,
c'est que même les mathématiques les plus obscures comme la géométrie algébrique,
peuvent être des outils de contrôle, de chiffrement et de surveillance,
et donc de sécurité nationale.
En particulier, sans que 
Mais surtout, ce que j'aimerais que vous reteniez,
c'est que dès lors, les mathématiques et les mathématiciens
ne peuvent plus considérer qu'ils sont purs et loins de toute implication sociale.

En fait, de nos jours, le simple choix du sujet de recherche,
qu'il soit du côté de l'implantation de backdoors indétectables,
ou du côté de la recherche des backdoors et de solutions vraiment sécurisées,
est un choix fondamentalement politique.
Et ce que je dis là de la géométrie algébrique
est bien entendu encore plus pertinent pour des sciences
dont les applications à grande échelle et à court terme sont nombreuses ;
en commençant bien sûr par la recherche sur l'intelligence artificielle,
par opposition par exemple à celle sur la gouvernance démocratique des algorithmes.

Malheureusement, les tentations financières, y compris dans la recherche publique,
vont trop souvent dans le mauvais sens ;
de nos jours, tout informaticien sera beaucoup, beaucoup, beaucoup mieux payé,
en travaillant pour des géants de la tech,
dont les externalités négatives sur la société vont 
de l'affaiblissement des démocraties à des complicités de génocides,
qu'en travaillant au service de la cybersécurité et de la gouvernance algorithmique.

Dans un monde numérisé,
les mathématiciens parmi nous sont un peu devenus, qu'ils le veuillent ou non,
des super héros ou des super villains en puissance,
avec des trajectoires maléfiques toutes tracées par des multinationales privées.
Mais, comme le dirait l'oncle de Spiderman,
de grands pouvoirs impliquent de grandes responsabilités.

Les mathématiciens me semblent avoir une responsabilité immense
à rendre leurs mathématiques plus socialement responsables,
tout comme plus généralemet tous ceux parmi nous qui avons le luxe
de ne pas vivre dans le besoin grâce à la stabilité de nos démocraties,
qui est pourtant plus menacée aujourd'hui 
qu'elle ne l'a été au cours des 70 dernières années.
Si vous voulez davantage vous investir dans des sciences responsables,
je ne peux que vous encourager à vous intéresser de plus près à la cybersécurité,
mais aussi aux mathématiques de la gouvernance,
incarnée notamment dans notre projet Tournesol.
Et bien sûr, vous pouvez explicitement y contribuer,
notamment en créant un compte sur la plateforme
et en y évaluant les contenus de YouTube 
que vous pensez être le plus d'intérêt général.

