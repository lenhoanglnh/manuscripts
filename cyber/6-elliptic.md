# Cette équation est une backdoor de la NSA

Dans notre monde extrêmement numérisé, 
maîtriser les mathématiques est devenu une sorte de superpouvoir.
Et celui-ci peut être utilisé pour le bien du plus grand nombre, ou non.
Aujourd'hui, on va voir que, il y a deux décennies,
la NSA semble assez clairement avoir exploité ce superpouvoir,
pour faciliter la cybersurveillance de masse de l'ensemble de la planète,
mais aussi la prise de contrôle des objets électroniques ;
et l'attaque récente des bipeurs au Liban montre bien toute l'ampleur d'un tel pouvoir.

Heureusement, dans ce cas, 
d'un côté les mathématiciens de la NSA n'ont pas été particulièrement brillants ;
et surtout, la même maîtrise des mathématiques par des membres de la société civile
a permis d'identifier ce qui peut bien sembler être une cyberattaque mondialisée de la NSA.
Et quand on voit certains dirigeants politiques de premier plan outre-Atlantique,
il y a de quoi y voir une menace globale sur l'ensemble de la planète...

Mais bizarrement, pour comprendre tout ceci,
il va nous falloir faire un détour vers les courbes elliptiques,
qui sont des objets remarquables de la géométrie algébrique,
et des composants essentiels de la cryptographie moderne.
En fait, pour regarder la vidéo que vous regardez,
et en particulier pour certifier qu'elle est bien une vidéo envoyée par YouTube,
votre machine a dû effectué des opérations sur des courbes elliptiques.


## Les courbes elliptiques

De façon générale, une courbe elliptique est définie
comme l'ensemble des solutions (x,y) de l'équation 
`y² = x³ + ax + b`.

> Pour éviter les singularités, on suppose `4a³ + 27b² ≠ 0`.

Le cas suspicieux de la NSA considérait le cas `a = -3` et 
`b = 41058363725152142129326129780047268409114441015993725554835256314039467401291`.
Bon, déjà, ce choix de la valeur de `b` paraît étrange.

Par opposition, l'une des courbes les plus standards aujourd'hui
est l'équation `y² = x³ + 486662 x² + x`,
qui définit Curve25519.
Bon, ce n'est pas tout à fait une courbe elliptique en forme standard,
ce qui facilite certains calculs,
mais ce que je veux vous montrer, 
c'est surtout que ses constantes sont beaucoup plus simples,
et plus justifiées, que celles de la NSA.

Mais oublions ces détails pour l'instant.
Ce qui est intéressant à voir, 
c'est que si on trace la courbe `y² = x³ + ax + b` dans un logiciel comme Desmos,
par exemple ici pour `a = -3` et `b = 5`,
on obtient cette figure assez caractéristique.

Mais ça, ça correspond aux solutions `(x,y)` pour des nombres réels.
Les mathématiciens se sont amusés à explorer des solutions 
dans d'autres classes de nombres.
Si on considère les solutions complexes,
on obtient alors une surface fermée, mais avec un trou ;
on parle de tore, un peu comme celui qu'on avait vu dans cette 
[vieille vidéo](https://tournesol.app/entities/yt:8v2JxCUDW6M).

Et ça, c'est joli. 
Mais visiblement, pour les mathématiciens, ce n'est pas encore assez joli.
Et ils s'intéressent en fait souvent bien plus
aux solutions rationnelles, c'est-à-dire aux fractions d'entiers.
Et d'ailleurs El Jj a fait 
une [excellente vidéo](https://tournesol.app/entities/yt:NEVapv8c-SM) à ce sujet,
où on voit que ces "courbes" sont en fait plein de points discrets.

Mais ce n'est pas tout.
Les mathématiciens vont aussi chercher 
à identifier les solutions des courbes elliptiques 
dans d'autres classes de nombres, 
comme celui des [p-adiques](https://tournesol.app/entities/yt:tRaq4aYPzCc),
qui ont notamment été utile 
pour [prouver le fameux dernier théorème de Fermat](https://tournesol.app/entities/yt:grzFM5XciAY).

Mais en cryptographie, les solutions qui vont nous intéresser,
comme vous vous y attendez peut-être si vous avez vu les dernières vidéos,
ce sont les solutions dans les corps finis,
comme celui des nombres modulo un nombre premier p.
Dans le cas de l'équation de la NSA, 
qui définit un protocole appelé Dual\_EC\_DRBG,
ce nombre est `p = 115792089210356248762697446949407573529996955224135760342422259061068512044369`.
Pour la courbe Curve25519,
on a `p = 2^255^ - 19`.
C'est d'ailleurs de là que vient son nom d'ailleurs.
Notez que dans ce second cas, 
les nombres peuvent être écrits du corps peuvent être écrits avec 256 bits.
Ce qui est très utile...


## Une courbe elliptique est un groupe

La propriété fondamentale des courbes elliptiques, 
quel que soit les nombres qu'on considère,
c'est que l'ensemble de ses points peuvent être combiné algébriquement.
Autrement dit, étant donné n'importe quels points P et Q déjà sur la courbe,
je peux combiner P et Q pour fabriquer un troisième point R sur la courbe.

Et la manière la plus simple de voir 
comment cette composition des points d'une courbe elliptique opère
consiste à revenir au cas le plus visuel,
à savoir celui du ces nombres réels,
puisqu'on a alors une courbe elliptique 
qui ressemble vraiment à ce qu'on pense, quand on entend parler de courbe.

Considérons deux points P et Q sur cette courbe.
Je peux alors construire un troisième point R sur cette courbe,
en traçant la droite qui passe par P et Q,
en observant qu'elle coupe la courbe elliptique à un 3e point,
et en prenant le symétrique de ce point selon l'axe des abscisses.

Et si je vous décris ces opérations géométriquement,
on peux très bien en avoir une description algébrique aussi,
grâce à la magie de la géométrie algébrique.
Appelons ainsi `y² = x³ + ax + b` la courbe elliptique,
et `y = cx + d` la droite qui passe par P et Q.

Déterminer les intersection entre la courbe elliptique et la droite,
ça revient à résoudre ces deux équations à la fois.
En injectant l'expression y selon l'équation de la droite
dans l'équation de la courbe elliptique,
on obtient `(cx + d)² = x³ + ax + b`,
qu'on peut réécrire `c²x² + 2cd x + d² = x³ + ax + b`.
En mettant tout à droite de l'équation, on obtient
`x³ - c² x² + (a - 2cd) x + (b-d)² = 0`,
ce qui est une équation de degré 3 en `x`.

Et là, on pourrait vouloir sortir la calculatrice,
mais il y a en fait une remarque plus maligne à faire.
En effet, on sait que parmi les points d'intersection 
entre la courbe elliptique et la droite, il y a les points P, Q et R.
Mais donc, on sait que les abscisses de ces points sont solution de l'équation.
Appelons `x_P_`, `x_Q_` et `x_R_` ces points d'intersection.
Alors, d'après la théorie des polynômes, 
on sait que toute équation de degré 3 qui s'annule en ces 3 points doit s'écrire
`(x-x_P_)(x-x_Q_)(x-x_R)`.
Comme c'est le cas de notre équation de l'intersection 
entre la courbe elliptique et la droite,
on sait donc que
`x³ - c² x² + (a - 2cd) x + (b-d)² = (x-x_P_)(x-x_Q_)(x-x_R)`.

Ok, on y presque !
Maintenant, on va développer le terme de droite, ce qui donne
`(x-x_P_)(x-x_Q_)(x-x_R) = x³ - (x_P_ + x_Q_ + x_R_) x² + autres`.
Ce qui va m'intéresser maintenant, c'est d'identifier les coefficients de degrés 2.
En effet, par égalité des polynômes, 
on sait qu'on doit avoir
`c² = x_P_ + x_Q_ + x_R_`.
Mais donc, `x_R_ = c² - x_P_ - x_Q_`.
Notez qu'on peut estimer la pente `c` de la droite 
en calculant le taux d'accroissement entre les points `P` et `Q`, 
ce qui donne `c = (y_P_ - y_Q_) / (x_P_ - x_Q_)`,
et donc on a `x_R_ = (y_P_ - y_Q_)^2^ / (x_P_ - x_Q_)^2^ - x_P_ - x_Q_`.
On peut ensuite en déduire `y_R_` en utilisant le fait que R est sur la droite,
ce qui donne `y_R_ = c x_R_ + d = (y_P_ - y_Q_) (x_R_ - x_P_) / (x_P_ - x_Q_) + y_P_`.

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
qui rappellons-le, est en fait un ensemble fini de points `(x,y)` 
où `x` et `y` sont des nombres d'un corps fini.

Enfin, ce n'est pas tout à fait exact, 
en tout cas avec uniquement les opérations dont je vous ai parlé jusque là.
Et oui, dans nos équations, on a une division par `x_P_ - x_Q_`.
Or si `x_P_ = x_Q_`, alors `x_P_ = x_Q_`, et on a donc une division par zéro.
Or ça, c'est vraiment ultra-interdit, non seulement pour les nombres réels,
mais aussi dans le corps des nombres finis.

En fait, si on regarde notamment la courbe elliptique pour les nombres réels, 
il y a exactement 2 cas où P et Q sont sur la courbe et où ils ont la même abscisse :
soit `P = Q`, soit `P` est le symétrique de `Q` selon l'axe des abscisses.
Dans le premier cas, l'astuce est de dire que `Q` est un point limite 
d'une suite `Q_1_, Q_2_, ...` qui tend vers `P`.
On va alors exiger que la combinaison de P et Q est 
la limite des combinaisons de P et Q_n_.
Formellement, ceci revient à considérer la tangente à la courbe elliptique qui passe par `P`,
et à définir `R` comme le symétrique de l'autre intersection 
de la tangente avec la courbe elliptique.

Dans le second cas, on va considérer et la combinaison de P avec Q,
qui est donc la combinaison de P avec lui-même, 
est égal à un point fictif,
qu'on va appeler `0`, 
et qu'on va considérer être un point un peu spécial de la courbe elliptique.
Ce point fictif aura par ailleurs la propriété de n'avoir aucun effet,
quand on le combine à n'importe quel autre point de la courbe.
Autrement dit, combiner `0` et `P` fait `P`.

Et voilà, on a notre façon de combiner toutes les paires de points
de notre courbe elliptique étendue.
On dit que l'opération qu'on a définie est une loi de composition interne,
et on peut la noter `R = Compo(P, Q)`.
Et on peut même remarque que cette loi de composition a de très belles propriétés :
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
et remplace l'opérateur `Compo` par un signe usuel pour les groupes commutatifs,
à savoir le signe `+`.
Et oui, on va dire qu'on peut ajouter des points de la courbe elliptique.
Faites très attention toutefois,
l'addition des points de la courbe elliptique n'est pas du tout une addition usuelle ;
en particulier, elle ne correspond absolument pas à l'addition des coordonnées.
C'est une opération plus complexe ;
mais cela reste une opération algébrique, 
conformément aux équations qu'on a identifiées plus haut.

`x_R_ = (y_P_ - y_Q_)^2^ / (x_P_ - x_Q_)^2^ - x_P_ - x_Q_`,
`y_R_ = (y_P_ - y_Q_) (x_R_ - x_P_) / (x_P_ - x_Q_) + y_P_`.

Bien sûr, en cryptographie, le cas qui nous intéresse particulièrement,
c'est celui des corps finis.
Et en fait, ce qui nous intéresse même particulièrement en cryptographie,
ça va être le groupe cyclique engendré par un point de la courbe...


## Groupe cyclique et exponentiation

En pratique, en cryptographie, on va considérer un point G de la courbe elliptique,
et à tous les points qu'on peut obtenir en ajoutant G à lui-même un certain nombre de fois.
Appelons ainsi `n G` le résultat de l'addition `G + G + ... + G`,
avec n copies du point G.
L'ensemble des points obtenus ainsi est appelé le groupe cyclique généré par le point G.

> Ceci correspond formellement à un morphisme de groupe `EntierRelatif -> CourbeElliptique`.

Sur un corps fini, on sait qu'il y a un nombre fini de points sur la courbe elliptique,
ne serait-ce parce qu'il y a un nombre fini de paires (x,y),
où x et y sont des nombres du corps fini.
Du coup, on sait que la suite `n G` doit finir par boucler,
et en fait, 
on peut montrer qu'elle revient au point fictif `0` ajouté à la courbe elliptique.
En pratique, toutefois, la première valeur de `n > 0` telle que `n G = 0`
est cryptographiquement grande.
Pour Curve25519, ce nombre est `2^252^ + 27742317777372353535851937790883648493`,
soit approximativement le nombre de particules dans l'univers.
Même une superintelligence serait très incapable de lister tous les points
de la courbe elliptique Curve25519.

Heureusement, il existe une solution remarquable
pour rapidement un trouver le n-ième point de la courbe elliptique,
qui s'appuie sur des doublements successifs.
Ainsi, définissons `G_1_ = 2G =  G + G`.
Puis `G_2_ = 2G_1_ = G_1_ + G_1_`, et ainsi de suite.
Calculer `G_k+1` à partir de `G_k_` est très simple :
il suffit d'ajouter `G_k_` à lui-même.
Cela peut se faire en une opération sur les courbes elliptiques.
Mais du coup, on peut calculer `G_k_` à partir de G en seulement k opérations.
Cependant, de manière remarquable, `G_k_ = 2^k^ G`,
ce qui permet donc de calculer le 2^k^-ième élément de la suite en seulement k opérations.

Quid maintenant du n-ième élément, s'il n'est pas une puissance de 2 ?
Et bien, si on nous donne le nombre n en écriture binaire,
c'est très simple.
Par exemple, `n = 100` en base 10 s'écrit `n = 1100100` en base de 2,
ça veut dire qu'il a des bits 1 uniquement aux positions 3, 6 et 7 en partant de la droite,
alors il se décompose forcément en
`n = 2^3-1^ + 2^6-1^ + 2^7-1^ = 2² + 2⁵ + 2⁶`.
On a alors `G_n_ = 2² G + 2⁵ G + 2⁶ G = G_2_ + G_5_ + G_6`.
On peut en fait calculer `G_2_`, `G_5_` et `G_6_` en 6 opérations sur les courbes elliptiques.
Et on peut calculer leur somme avec 3 opérations de plus.
Voilà comment on a pu accéder au 100-ième élément de la suite des `n G`
avec seulement 9 opérations sur les courbes elliptiques !

Formellement, le nombre d'opérations nécessaires sera logarithmiques en `n`.
Et de manière pratique, 
ça veut dire que `P = n G` peut se calculer très rapidement,
même pour des valeurs cryptographiquement grandes de `n`.

Toutefois, à l'inverse, étant donné un point `P` d'une courbe elliptique,
déterminer pour quelle valeur de `n` on a `P = n G`,
eh bien, on ne sait pas faire.
Mieux encore, on suspecte que personne ne saura le faire,
à moins de lister une bonne partie des 
plus de `2^252^` valeurs possibles de `n G`,
jusqu'à en trouver une qui correspond à `P`.

Ainsi, on dit que la fonction qui a un nombre `n` associe `n G`
est une fonction à sens unique,
dans la mesure où on peut facilement la calculer,
mais on suppose qu'il est essentiellement impossible de l'inverser,
même pour une superintelligence,
pourvue qu'elle soit contrainte par les puissances de calculs aujourd'hui accessibles.

> En fait, si la superintelligence a accès à une machine quantique,
> alors on sait qu'elle pourra inverser cette fonction...
> On dit que le problème du *logarithme discret* est polynomialement soluble
> par un algorithme quantique.
> J'ai parlé d'un cas similaire dans la série 
> sur [String Theory](https://tournesol.app/entities/yt:plgQgJ4obTg).

Et c'est vraiment cette propriété des groupes cycliques,
qui n'est d'ailleurs pas du tout spécifiques aux courbes elliptiques,
qui fait que ces groupes sont d'une très utilité à la cryptographie.


## Comparaison avec RSA

Oui, parce que tout ça, mathématiquement, c'est super joli.
Mais en a-t-on vraiment besoin ?
Pourquoi a-t-il fallu utiliser ces mathématiques aussi complexes
pour pouvoir faire de la cryptographie ?
N'y a-t-il pas plein d'autres groupes cycliques beaucoup plus simples
qu'on aurait pu utiliser pour avoir cette même propriété ?

Eh bien, il y a vraiment eu un besoin à un moment donné.
En fait, pendant longtemps, les mathématiciens ont davantage exploité un autre groupe, 
à savoir le groupe multiplicatif des nombres inversibles modulo N,
où N est un nombre entier qui s'écrit `N = pq` pour deux nombres premiers `p`,
pour définir une cryptographie appelée RSA,
ou le groupe multiplicatif des nombres inversibles modulo un nombre p ;
pas besoin de comprendre les détails, 
mais si vous les voulez, 
j'ai une [vidéo](https://tournesol.app/entities/yt:Y2bsLRdVBP8) sur String Theory à ce sujet.

Cependant la sécurité de ces systèmes est extrêmement dépendante
de la difficulté à trouver les facteurs premiers d'un grand nombre entier N.
Et malheureusement, les mathématiciens et les informaticiens ont été brillants.
Même s'ils n'ont pas réussi à trouver un algorithme très rapide pour y arriver,
ils ont trouvé des algorithmes bien meilleurs que l'approche naïve,
dont le temps est typiquement exponentiel en la moitié du nombre de chiffres utilisés,
ce qui est nettement moins bien qu'être exponentiel en le nombre de chiffres utilisés.

En fait, on estime aujourd'hui que RSA requiert 
des nombres N avec environ 3000 bits,
soit environ 1000 chiffres en écriture décimale,
pour offrir un même niveau de sécurité 
que la cryptographie par courbes elliptiques avec des corps finis à environ 2^256^ éléments,
comme Curve25519,
qui ne requièrent que 256 bits.
Voilà qui permet à la cryptographie par courbes elliptiques
d'être significativement moins coûteuse en temps de calculs,
pour un même niveau de sécurité calculatoire.


## Diffie-Hellman

Même si j'en ai déjà parlé sur [String Theory](https://tournesol.app/entities/yt:jcQXNMuqhFU),
j'aimerais vous rappeler comment une communication sécurisée peut être établie,
en utilisant le fait qu'on pense que 
la fonction qui calcule `n G` à partir de `n` est à sens unique.

L'idée est la stratégie du double cadenas.
Alice et Bob pense chacun à un grand nombre secret aléatoire s_A_ et s_B_.
Typiquement, s'ils utilisent Curve25519,
ils peuvent utiliser des nombres à 255 bits.

Chacun calcule les points `P_A_ = s_A_ G` et `P_B_ = s_B_ G`, qu'ils rendent publics.
Alice calcule ensuite `s_A_ P_B_`, et Bob calcule `s_B_ P_A_`.
Et là, magie magie, on se rend compte 
qu'ils ont en fait calculé le même point `S` sur la courbe elliptique.
En effet, `S = s_A_ P_B_ = s_A_ (s_B_ G) = (s_A_ s_B_) G`,
qui est bien symétrique en A et B.

Et de manière cruciale, cette information partagée est bien secrète,
car même sachant `G`, `P_A_` et `P_B`,
on suppose qu'un attaquant sera incapable de deviner `s_A_` ou `s_B_` ou `S`,
en utilisant le fait que que la fonction qui calcule `P_A_` avec `s_A_` est à sens unique.

Ensuite, Alice et Bob vont typiquement appliquer une fonction de hachage
au secret partagé S,
pour obtenir une clé partagée `K = Hash(S)`
qui va être utilisée ensuite pour les communications chiffrées symétriquement.

Notez que les courbes elliptiques peuvent aussi être utilisées 
pour d'autres opérations cryptographiques,
comme le chiffrement à clé publique ou la signature crytographique.
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
Plus généralement, de nombreux systèmes modernes exploitent à foison des tokens aléatoires,
qui sont des nombres qu'Alice peut typiquement envoyer à Bob,
et que Bob pourra réutiliser pour affirmer être Bob.
Si ces tokens aléatoires peuvent être prédits, même uniquement de temps en temps,
alors l'attaquant pourra en fait régulièrement infiltrer de nombreux systèmes d'information.

Alors, en pratique, un hasard imprévisible par le démon de Solomonoff est trop coûteux à obtenir ;
du coup, on se contente de générer une suite de nombres,
en espérant qu'une superintelligence soit incapable de la prolonger mieux que le hasard,
à cause de ses limites en puissance de calculs,
comme on en a parlé dans une [vidéo précédente](TBD).
Et oui, pour rappel, 
toute superintelligence du monde physique est très inférieure au démon de Solomonoff,
qui lui-même est très inférieur au démon de Laplace.

Eh bien, la NSA a proposé un algorithme qui génère une suite de nombres,
en suggérant que toute superintelligence sera incapable 
de prédire le suivant mieux que le hasard.
Enfin, pour être exact, c'est le NIST, 
le National Institute of Standards and Technology,
qui [a proposé ce standard](https://csrc.nist.gov/pubs/sp/800/90/a/final).
Mais c'est évident que cet institut américain est proche de la NSA.

Bon, après, ça ne veut absolument pas dire que tout ce que dit le NIST est une backdoor ;
en tout cas, je vous assure ne pas avoir été contacté par le NIST
pour [leur rapport sur la sécurité de l'IA](https://csrc.nist.gov/pubs/ai/100/2/e2023/final),
même si le NIST cite un de mes algorithmes comme solution à adopter.

Bref. Revenons-en à l'algorithme de génération de nombres aléatoires
proposé par le NIST en 2012.
Cet algorithme s'appuie sur une courbe elliptique,
à savoir `y² = x³ - 3x + b`,
où `b = 41058363725152142129326129780047268409114441015993725554835256314039467401291`,
dans le corps fini à 
`p = 115792089210356248762697446949407573529996955224135760342422259061068512044369` éléments,
et sur deux points `P` et `Q` de la courbe,
dont les coordonnées sont... des grands nombres.
Ici, je donne leur écriture en hexadecimale, c'est-à-dire en base 16.

Pour générer la suite, 
NIST propose de commencer par prendre un nombre `s_0_` à 256 bits, 
qu'on appelle la graine, ou seed en anglais.
Puis l'algorithme calculs `P_1_ = s_0_ P`, avec l'exponentiation rapide.
Et il définit son nouvel état `s_1_` comme étant la coordonnée x de `P_1_`.
Autrement dit, il pose `s_1_ = (s_0_ P)_x_`.
Notez que `s_1_` est alors bien un nombre à 256 bits.

Ce nombre est alors utilisé pour générer un nombre aléatoire,
en utilisant la même opération, mais cette fois à partir du point Q.
Autrement dit, on pose `r_1_ = (s_1_ Q)_x_`, qui est lui aussi un nombre à 256 bits.
En fait, non, pour éviter de révéler trop d'information,
on va effacer les 16 premiers bits `(s_1_ Q)_x_`.
On pose donc `r_1_ = Trim_16_((s_1_ Q)_x_)`,
où Trim est cette fonction qui efface les premiers bits.

Puis, on réeffectue les mêmes opérations, en partant de `s_1_` au lieu de `s_0_`.
Autrement dit, la suite générée est définie par les équations
`s_k_ = (s_k-1_ P)_x_` et `r_k_ = Trim_16_((s_k_ Q)_x_)`.
Et ce que le NIST prétend,
c'est que sachant les observations `r_1_, r_2_, r_3_, ..., r_k_`,
il est impossible de deviner la valeur de `r_k+1_`.

OK... mais présenté ainsi, c'est déjà étrange...
Est-ce qu'on a vraiment la garantie que cette suite paraît aléatoire ?
Est-ce que retirer 16 bits suffit vraiment ?
Et pourquoi avoir choisi ces deux points P et Q en particulier.
Étonnamment, NIST ne justifie pas le choix de ces points.

Et c'est là que réside probablement la backdoor de la NSA.
Pour commencer, noter que si on connaît `r_1_`,
alors il ne reste que 16 bits à deviner pour déterminer `(s_1_ Q)_x_`.
Sauf que 16 bits à deviner, ça fait `2^16^` possibilités,
soit seulement 65 536.
Or c'est complètement gérable d'explorer toutes ses possibilités avec une machine !
Étrange, étrange...

Passons maintenant à l'autre bizarrerie : les choix de P et Q.
Si la NSA est malicieuse,
alors elle a pu choisir un point Q de la courbe, 
choisir un nombre secret `e` à 256 bits,
et calculer ensuite `P = e Q`.

Testons donc l'une des 65 536 valeurs possibles de `(s_1_ Q)_x_` sachant `r_1_`.
Si on connaît `(s_1_ Q)_x_`,
alors on peut déterminer `s_1_ Q`;
il suffit de résoudre `y² = (s_1_ Q)_x_³ - a (s_1_ Q)_x_ + b` modulo p,
ce qui revient à calculer une racine carrée module p.
Il y a par exemple l'algorithme de Tonelli-Shanks qui permet de le faire efficacement.

Maintenant, pour prédire `r_2_`, ce serait bien de connaître `s_2_`.
Est-ce possible ?
Et bien, on a `s_2_ = (s_1_ P)_x_`.
Mais une NSA malicieuse peut alors avoir choisi `P = e Q`.
Dès lors, on aurait `s_2_ = (s_1_ e Q)_x_ = ( e (s_1_ Q) )_x_`.
Vous le voyez venir, sachant `(s_1_ Q)_x_`,
on peut en fait calculer le prochain état `s_2_` du générateur,
et donc le nombre aléatoire `r_2_` qu'il va générer.

Alors, bien sûr, en observant `r_1_`, on n'apprend pas `(s_1_ Q)_x_`.
Mais on connaît 65 536 valeurs qu'il peut prendre.
Et donc, on connaît 65 536 valeurs que `r_2_` peut prendre.
L'observation de `r_2_` nous permttra alors quasi-assurément
de trancher sur la valeur de `(s_1_ Q)_x_`,
ce qui fait que le générateur de nombre aléatoire n'aura plus aucun secret pour nous ;
ou, plus précisément, pour quiconque connaîtrait le secret `e`
qui lie les points `P` et `Q` dont le choix est si peu justifié.

Alors bien sûr, le NIST prétend que
déterminer la solution `e` à l'équation `P = e Q` 
revient à inverser une fonction qu'on considère être à sens unique ;
mais le problème, c'est de savoir si le NIST a d'abord choisi `e`,
et a ensuite calculer `P` pour que cette équation soit vérifiée.
Vu le peu d'explication sur le choix de ces points,
personnellement, j'ai mon bullshit alert rouge écarlate...


## Conclusion

Ce dont j'espère vous avoir convaincu aujourd'hui,
c'est que même les mathématiques les plus obscures comme la géométrie algébrique,
peuvent être des outils de contrôle et de surveillance,
et donc de sécurité nationale.
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
à rendre leurs mathématiques plus socialement responsables.

