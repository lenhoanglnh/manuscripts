# Les nombres imaginaires de l'informatique

La dernière fois, on a vu que les nombres modulo un nombre premier p
pouvaient être efficacement additionnés, soustraits, multipliés et divisés,
ce qui donne à chaque fois des nombres modulo ce même nombre premier p.
Ils ne sont bien sûr pas les seuls.
Il y a bien sûr aussi les nombres réels, les plus courants en mathématiques ;
mais dont l'existence physique est 
[discutable et discutée](https://tournesol.app/entities/yt:gqLIfCkorRc).
Mais bon, ne nous écartons pas du sujet.

Dans le jargon mathématique, 
on dit que ces nombres qui peuvent être manipulées avec les 4 opérations fondamentales 
forment ce qu'on appelle un corps.
Un autre exemple est le corps des fractions.
Ajoutez, soustrayez, multipliez ou divisez deux fractions,
et vous obtiendrez encore une fraction.
À l'école, vous avez peut-être aussi vu le corps des nombres complexes.
Si vous ne connaissez pas les nombres complexes, ne vous en faites pas.
Ça ne nous sera d'aucune utilité.

Aujourd'hui, on va s'intéresser en particulier aux corps finis,
c'est-à-dire aux ensembles finis de nombres 
qui peuvent être combinés par les 4 opérations fondamentales,
à l'instar du corps des nombres modulo un nombre premier p.
On va voir que la liste des corps finis est remarquablement simple et structurée.
Mais surtout, ces corps finis forment aujourd'hui 
le socle d'un grand nombre de solution de cybersécurité,
non seulement pour le chiffrement des données,
mais aussi pour l'authentification des sources des données
et pour l'intégrité de ces données.
Mais tout ça, on prendra le temps d'en parler dans de futures vidéos.


## Le corps fini à 3 éléments

Pour définir un corps fini, il suffit de définir un ensemble fini d'objets,
et de définir comment ils se combinent à travers l'addition et la multiplication.
Je vous propose de commencer par prendre l'exemple concret du corps fini à 3 éléments,
communément appelé F<sub>3</sub>.
Ce corps a uniquement trois nombres, qu'on va appeler 0, 1 et a.
Et pour définir l'addition et la multiplication,
je vais simplement vous donner leurs tables d'addition et de multiplication.
Voici ce que ça nous donne :

| + | 0 | 1 | a |
| - | - | - | - |
| 0 | 0 | 1 | a |
| 1 | 1 | a | 0 |
| a | a | 0 | 1 |

| * | 0 | 1 | a |
| - | - | - | - |
| 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | a |
| a | 0 | a | 1 |

Ainsi, si je vous donne à calculer `(0+1)*(1+a+0)`,
vous pouvez vérifier que `0+1`, ça nous fait 1,
que `1+a` font 0, et donc que `1+a+0` font `0+0`, ce qui fait la tête à toto,
enfin, je voulais dire 0.
et que le résultat est donc `1 * 0`, qui est égal à 0.
Voilà, vous venez peut-être d'avoir fait vos premiers calculs
dans le corps fini F<sub>3</sub>.

Alors, si on regarde de plus prêt les deux tables d'addition et de multiplication,
on peut faire quelques remarques assez profondes sur les corps finis.
D'abord, les deux tableaux sont symétrique par rapport à la diagonale principale,
qui va d'en haut à gauche à en bas à droite.
Ça revient à dire que, par exemple, 1+a est nécessairement égal à a+1.
De même `0*a = a*0`.
On dit que l'addition et la multiplication sont commutatives.
Et bien, en 1905, Joseph Wedderburn a démontré que dans tout corps fini,
c'était nécessairement le cas.
Et donc, que toutes les tables d'addition et de multiplication d'un corps fini
doivent nécessairement avoir une symétrie selon la diagonale principale.

Maintenant, notez que la ligne du 0 de la table d'addition est identique
à la suite des éléments de l'ensemble.
Autrement dit, 0 + n'importe quoi est égal à n'importe quoi.
On dit que 0 est l'élément neutre de l'addition,
puisqu'il n'a aucun effet quand on l'additionne aux autres éléments du corps.
De même, la ligne du 1 dans la table de multiplication 
est identique à la suite des éléments de l'ensemble ;
et du coup, 1 est appelé élément neutre de la multiplication.
Dans tout corps, on exige l'existence de ces deux nombres particuliers.

Notez par ailleurs que la ligne de multiplication de zéro
est identiquement égale à zéro.
Ça, c'est parce que `1 - 1 = 0`.
Et donc, calculer `0 * a`, ça revient à calculer `(1 - 1) * a`.
Par la propriété fondamentale de distributivité de la multiplication,
ça nous donne `1*a - 1*a`, qui est égal à `a - a`, qui fait zéro.
De même `0 * 1 = (1-1) * 1 = 1*1 - 1*1 = 1 - 1 = 0`.
Multiplier par 0 fait donc toujours 0.

Une troisième remarque à faire, c'est que, à l'image d'un sudoku,
dans les tables d'addition et de multiplication,
à l'exception de la ligne multiplicative du 0,
chaque ligne et chaque colonne contient tous les éléments du corps finis
une et une seule fois.
Ça, ça vient vraiment du fait qu'on veut pouvoir soustraire et diviser.
En effet, on veut pouvoir calculer des quantités comme `1 - a`.
Et pour cela, il faut que, dans la ligne du a de la table d'addition, 
il y ait une case dont la valeur est 1.
Dans notre cas, cette case correspond à la colonne du a.
Et ça, ça nous dit que `a + a = 1`, 
ce qu'on peut réécrire `a = 1 - a`, en soustrayant a des deux côtés.
De même, dans la ligne du a de la table de multiplication, 
il y a une case égale à 1, 
qui correspond à la colonne du a.
Et ça, ça nous dit que `a * a = 1`, et donc que `1/a = a`.
On peut donc bien diviser 1 par a.

Comme `1/a` est tel que `a * (1/a)` est égal à l'élément neutre de la multiplication,
à savoir 1,
on dit que `1/a` est l'inverse de `a`.
Dans les livres sur les corps finis, vous le verrez davantage noté a<sup>-1</sup>.
De même la quantité `0 - a` est souvent appelée l'opposé de a.
On pourrait aussi l'appeler l'inverse additif de a.


## Les corps finis à 4 éléments

OK. Sachant tout ce qu'on a vu, 
est-ce que vous sauriez définir un corps fini à 4 éléments ?
Pour rappel pour cela, il faut définir 4 objets, qu'on peut appeler 0, 1, a et b.
Et surtout il faut définir comment ces objets interagissent,
ce qui revient à dresser des tables d'addition et de multiplication,
qui doivent être symétriques selon la diagonale principale,
avec la neutralité de l'addition par 0 et la multiplication par 1,
et l'apparition de tous les éléments une et une seule fois dans chaque ligne et colonne,
à l'exception de la ligne et de la colonne multiplicative du 0.

| + | 0 | 1 | a | b |
| - | - | - | - | - |
| 0 | 0 | 1 | a | b |
| 1 | 1 |   |   |   |
| a | a |   |   |   |
| b | b |   |   |   |

| * | 0 | 1 | a | b |
| - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | a | b |
| a | 0 | a |   |   |
| b | 0 | b |   |   |

On peut commencer par la table de multiplication,
qui a moins de cases à remplir.
Dans la ligne du a, il manque le 1 et le b.
Mais le b ne peut pas aller tout au bout, 
car il y a déjà un b dans la dernière colonne.
Du coup, il faut mettre le b dans la colonne du a,
ce qui revient à dire que `a*a = b`.
Mais du coup, il faut mettre un 1 dans la dernière case de la ligne du a,
c'est-à-dire qu'il faut avoir `a*b = 1`.
Par commutativité, on sait que, du coup, `b*a = 1`.
Et la dernière case à remplir doit du coup l'être par un a,
pour qu'il y ait au moins un a dans la dernière ligne.

| * | 0 | 1 | a | b |
| - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | a | b |
| a | 0 | a | b | 1 |
| b | 0 | b | 1 | a |

Passons maintenant à l'addition, 
qui va être un peu plus compliquée à définir.
Je vous invite vraiment à mettre pause,
et à prendre le temps de tester différentes combinaisons.
Si vous galérez un peu, c'est normal, ce n'est pas si facile.
Allez, mettez pause, pour essayer...

Vous avez trouvé ?

Alors, je vais introduire une astuce, 
qui va nous être très utile pour comprendre tous les corps finis.
Cette astuce, c'est l'observation que 1 + 1 + 1 + 1 doit être égal à 0.
Alors, la démonstration n'est pas suffisamment simple pour que je vous la donne ici
sans rendre la vidéo indigeste pour beaucoup,
mais sachez que c'est une conséquence du théorème de Lagrange.
Et c'est généralisable à tout corps fini.
Si ce corps a q éléments, alors la somme de q éléments tous égaux à 1 est égale à 0.

Maintenant, dans notre cas, remarquez que `(1 + 1) * (1 + 1) = 1 + 1 + 1 + 1`,
par la distributivité de la multiplication sur l'addition.
Et donc, on sait que `(1+1) * (1+1) = 0`.
Ou dit autrement, 1+1 est un nombre dont la multiplication par lui-même vaut 0.
Maintenant, lorsqu'on regarde la table de multiplication,
la multiplication par soi-même correspond à la diagonale principale ;
et il n'y a qu'un seul cas où elle est égale à 0 :
c'est lorsque le nombre est déjà égal à 0.
Là encore, il s'agit d'un théorème plus général sur les corps :
si une multiplication de deux nombres vaut zéro,
alors au moins l'un des deux nombres doit lui-même être zéro.
Quoi qu'il en soit, comme `(1+1) * (1+1) = 0`,
on conclut que `1 + 1` doit être égal à 0.

| + | 0 | 1 | a | b |
| - | - | - | - | - |
| 0 | 0 | 1 | a | b |
| 1 | 1 | 0 |   |   |
| a | a |   |   |   |
| b | b |   |   |   |

Mais du coup, comme il faut un a et un b par ligne et colonne,
on peut remplir la ligne et la colone du 1.

| + | 0 | 1 | a | b |
| - | - | - | - | - |
| 0 | 0 | 1 | a | b |
| 1 | 1 | 0 | b | a |
| a | a | b |   |   |
| b | b | a |   |   |

Comment maintenant déterminer a + a ?
On peut faire la remarque que 
a + a = a * (1 + 1) = a * 0 = 0.
Et donc, la diagonale principale est en fait égale à 0.
Puisqu'il faut au moins un 1 dans chaque ligne et colonne,
on en déduit que les deux cases restantes doivent être des 1.

| + | 0 | 1 | a | b |
| - | - | - | - | - |
| 0 | 0 | 1 | a | b |
| 1 | 1 | 0 | b | a |
| a | a | b | 0 | 1 |
| b | b | a | 1 | 0 |

Ça y est ! On a réussi à définir notre corps fini F<sub>4</sub> à 4 éléments !


## Les corps finis

On a vu que dans tout corps fini à q éléments,
la somme `1 + 1 + 1 + ... + 1` avec q termes est égale à 0.
OK, mais comme on l'a vu dans notre exemple, 
ce n'est pas nécessairement la plus petite somme de 1 qui s'annule.
On avait ainsi vu que pour q = 4, la somme 1+1 s'annulait déjà.
Appelons p le plus petit nombre de 1 tel que leur somme s'annule.
Ce nombre p est aussi connu sous le nom de "caractéristique" du corps.

On peut faire la remarque que p est forcément premier.
En effet, sinon, la somme de p termes égaux à 1 pourrait se factoriser
en `(1 + 1 + ... + 1) * (1 + 1 + ... + 1) = 0`.
Or on a vu que le produit de deux nombres ne peut être nul 
que si au moins un des termes est nul ;
or dans chaque terme, le nombre de terme est strictement inférieur à p.
Ainsi la charactéristique des corps finis est toujours un nombre premier ---
et c'est ça qui rend les nombres premiers si centraux à la théorie des corps finis,
et à la cryptographie qui en fait abondamment usage.

En fait, l'ensemble des éléments qu'on construit avec une somme de 1
forme lui-même un sous-corps de corps à q éléments, 
c'est-à-dire un sous-ensemble de nombres qui se combinent via les 4 opérations de base.
En effet, lorsqu'on multiplie deux éléments qui sont des sommes de 1,
alors par distributivité de la multiplication, on obtient encore une somme de 1.
De plus, on vient de montrer qu'il contient exactement p éléments ;
la somme de p éléments rebouclant alors avec la valeur 0.
On dit que le sous-corps engendré par (0, 1) est un corps fini à p éléments.

En fait, chaque élément de ce sous-corps est directement identifié par le nombre de 1
qui compose son écriture en somme de 1.
C'est juste que quand ce nombre excède p, alors on peut lui retirer p termes,
car la somme de ces p termes est égale à 1.
Vous le voyez peut-être venir, ce corps fini à p éléments n'est autre
que l'ensemble des nombres dits "modulo p",
c'est-à-dire l'ensemble des nombres entiers avec l'égalité "forcée" p = 0.

On a d'ailleurs déjà vu un exemple de tel corps, à savoir le corps à 3 éléments.
Et oui, p = 3 est un nombre premier !
On peut de même détailler 
les tables d'addition et de multiplication du corps à 5 éléments,
qui correspondent aux opérations modul 5.

| + | 0 | 1 | 2 | 3 | 4 |
| - | - | - | - | - | - |
| 0 | 0 | 1 | 2 | 3 | 4 |
| 1 | 1 | 2 | 3 | 4 | 0 |
| 2 | 2 | 3 | 4 | 0 | 1 |
| 3 | 3 | 4 | 0 | 1 | 2 |
| 4 | 4 | 0 | 1 | 2 | 3 |

| * | 0 | 1 | 2 | 3 | 4 |
| - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 | 4 |
| 2 | 0 | 2 | 4 | 1 | 3 |
| 3 | 0 | 3 | 1 | 4 | 2 |
| 4 | 0 | 4 | 3 | 2 | 1 |

Cependant, le corps à q éléments n'a pas forcément un nombre premier d'éléments,
à l'instar du corps à 4 éléments qu'on a vu plus tôt.

Je vous épargne d'autres justifications mathématiques,
mais on peut montrer que ce corps doit nécessairement introduire 
des espèces de "nombres imaginaires",
comme la racine carrée de -1 pour construire les nombres complexes à partir des réels.

Appelons par exemple k le "nombre imaginaire" du corps à q éléments.
Alors les nombres du corps à q éléments doivent pouvoir s'écrire :
a<sub>0</sub> + a<sub>1</sub> k + a<sub>2</sub> k² + ... + a<sub>n-1</sub> k<sup>n-1</sup>,
pour un certain nombre entier naturel n,
avec des coefficients a<sub>0</sub>, a<sub>1</sub>, ..., a<sub>n-1</sub> qui sont des éléments du corps fini à p éléments.
On dit dans le jargon que F<sub>q</sub> a une structure de F<sub>p</sub>-espace vectoriel.
Mais alors le nombre d'éléments de F<sub>q</sub>,
c'est le nombre de façon de choisir a<sub>0</sub>, fois celui de choisir a<sub>1</sub>, et ainsi de suite.
Cela fait p<sup>n</sup> choix possibles. 
Voilà qui force q = p<sup>n</sup> : 
autrement dit le nombre d'éléments de tout corps fini doit être une puissance 
d'un nombre premier p.


## Construire des corps finis à p<sup>n</sup> éléments

En cryptographie, on a souvent besoin de construction explicite de corps finis à p<sup>n</sup> éléments.
Pour effectuer cette construction, il nous faut définir comment le nombre imaginaire k
se réduit à un nombre du corps,
lorsqu'on le met à une trop grande puissance.

C'est exactement ce qui a été fait pour les nombres complexes.
En effet, pour définir ces nombres, on a forcé le nombre imaginaire i
à avoir une puissance 2 qui s'écrit entièrement en tant que nombre réel,
à savoir i² = -1.
Mais du coup, quand on multiplie des nombres complexes et qu'un terme i⁷ apparaît,
on peut le réduire à un nombre complexe usuel,
en faisant la remarque que `i⁷ = i² * i² * i² * i = (-1) * (-1) * (-1) * i = -i`.

Eh bien, on va faire exactement pareil pour k, 
mais en se permettant des expressions plus complexes de k<sup>n</sup>.
Pour illustrer, prenons le cas du corps fini à 2 éléments,
qui correspond donc aux nombres modulo 2,
et dont les tables d'addition et de multiplication sont les suivantes : 

| + | 0 | 1 |
| - | - | - |
| 0 | 0 | 1 |
| 1 | 1 | 0 |

| * | 0 | 1 |
| - | - | - |
| 0 | 0 | 0 |
| 1 | 0 | 1 |

Et ajoutons le nombre imaginaire k avec k² = k + 1
au corps fini à 2 éléments.
On a alors 4 valeurs possibles : `0 + 0k`, `1 + 0k`, `0 + 1k`, `1+1k`,
qu'on peut réécrire 0, 1, k et k+1.

Notez que 0 et 1 se combine comme avant,
tandis que `k+k = 0 + (1+1)k = 0 + 0k = 0`.
Du coup, on obtient la table d'addition suivante :

|  +  |  0  |  1  |  k  | k+1 |
| --- | --- | --- | --- | --- |
|  0  |  0  |  1  |  k  | k+1 |
|  1  |  1  |  0  | k+1 |  k  |
|  k  |  k  | k+1 |  0  |  1  |
| k+1 | k+1 |  k  |  1  |  0  |

On peut également calculer la table de multiplication,
en utilisant `k² = k + 1`,
qui implique `k(k+1) = k² + k = (k+k) + 1 = 1`
et `(k+1)² = k² + k + k + 1 = k+1 + k+k + 1 = k`.
Ceci donne

|  *  |  0  |  1  |  k  | k+1 |
| --- | --- | --- | --- | --- |
|  0  |  0  |  0  |  0  |  0  |
|  1  |  0  |  1  |  k  | k+1 |
|  k  |  0  |  k  | k+1 |  1  |
| k+1 |  0  | k+1 |  1  |  k  |

On obtient exactement les mêmes tables que celles qu'on a construites précédemment,
avec k à la place de a et k+1 à la place de b... Laplaaaaace !!!
Désolé. C'était hors-sujet...


## Polynomes irréductibles

Alors, il y a quand même une difficulté que j'ai sauté,
au moment de définir l'équation du nombre imaginaire k.
Et oui, si j'ai choisi `k² = k + 1`, et pas k² = -1,
ce n'est en fait pas par hasard.

En effet, si j'étais parti avec k² = -1, 
j'aurai obtenu la table de multiplication suivante : 

|  *  |  0  |  1  |  k  | k+1 |
| --- | --- | --- | --- | --- |
|  0  |  0  |  0  |  0  |  0  |
|  1  |  0  |  1  |  k  | k+1 |
|  k  |  0  |  k  |  1  |  0  |
| k+1 |  0  | k+1 |  0  |  1  |

Vous voyez le drame ? 
Le 0 apparaît maintenant plusieurs fois dans une même ligne !
Et ça, ça implique que les opérations définies ne composent plus un corps.

Mais, donc, pourquoi est-ce que `k² = k+1` est un bon choix,
mais `k² = -1` en est un mauvais ?

Eh bien, ça vient du fait que l'équation `X² = -1` a déjà une solution dans F<sub>2</sub>.
Vous vous souvenez peut-être que, si on a introduire le nombre imaginaire i,
c'est parce qu'on ne pouvait pas prendre la racine carrée de -1 dans le corps des nombres réels.
L'équation `X² = -1` n'a pas de solution réelle.
Et bien, c'est ça qui fait que ajouter une solution i à cette équation
renforce le corps des nombres réels, en un corps plus grands, à savoir celui des complexes.

Et bien, il en va de même pour les corps finis.
Toute extension de corps finis requiert l'identification d'une équation en `X<sup>n</sup>`
qui n'a pas de solution dans le corps fini.
Les expressions comme `X<sup>n</sup> - X - 1` qui n'ont pas de solutions `X<sup>n</sup> - X - 1 = 0`
sont appelées des polynomes irréductibles.
Et en pratique, les informaticiens identifient de telles expressions 
pour ensuite concevoir des corps finis.

Par exemple, le corps fini à 2⁴ = 16 éléments peut se construire à partir de F<sub>2</sub>,
en s'appuyant sur le nombre imaginaire k défini par `k⁴ = k + 1`.
Et ça, ça marche, parce que le polynome `X⁴ - X - 1` est irréductible dans F<sub>2</sub>,
et qu'il est de degré 4, c'est-à-dire que la plus grande puissance est 4.
En pratique, les informaticiens utilisent particulièrement le corps fini à 2⁸ = 256 éléments,
notamment car ils regroupent souvent les bits par paquets de 8,
qui forment alors un octet.
On utilise alors le nombre imaginaire k défini par `k⁸ = k⁴ + k³ + k² + 1`,
qui correspond à un polynome irréductible.
Comme on le verra la prochaine fois,
c'est ce nombre imaginaire qui est utilisé dans les QR Codes.

D'ailleurs on peut noter que, de façon plus générale, 
l'encodage des corps F<sub>2<sup>n</sup></sub> est particulièrement naturel en informatique.
En effet, tout élément de F<sub>2<sup>n</sup></sub> s'écrit
a<sub>0</sub> + a<sub>1</sub> k + a<sub>2</sub> k² + ... + a<sub>n-1</sub> k<sup>n-1</sup>,
puisque les puissances supérieures sont réduites par la définition du nombre imaginaire $k$.
Et donc, on peut l'encoder, en ne retenant que les coefficients a<sub>n-1</sub>, a<sub>n-2</sub>, ..., a<sub>0</sub>.
Or chaque terme a<sub>n-1</sub>, a<sub>n-2</sub>, ..., a<sub>0</sub> doit appartenir à F<sub>2,
le corps à 2 éléments, dont on sait qu'ils sont 0 ou 1.
Et donc l'encodage a<sub>n-1</sub>, a<sub>n-2</sub>, ..., a<sub>0</sub>$ est naturellement binaire :
il s'agit d'une suite de n bits !

L'addition dans F<sub>2<sup>n</sup></sub> correspond alors naturellement à une addition terme à terme sans retenue.
Par exemple dans F<sub>2⁴</sub>, les nombres `k³ + k + 1` et `k² + 1` 
sont respectivement encodés par `1011` et `0101`.
Leur addition donne `k³ + k² + k + (1+1)`.
Et comme 1+1 = 0 dans F<sub>2</sub>, ça nous fait juste `k³ + k² + k`.
Et comme vous le sentez peut-être venir, 
l'addition se fait indépendamment pour chaque puissance de k.
Et ça, ça revient à pauser l'addition, 
mais sans invoquer de retenues qui feraient interagir les différentes puissancse de k.
Autrement dit, on peut poser l'addition

  1011  
+ 0101  
  ----  
  1110

Quant à la multiplication, 
il est amusant de voir qu'elle correspond pas mal à la multiplication classique,
à ceci près qu'il ne faut pas oublier de réduire les termes de "memory overflow".
Illustrons cela en multipliant par exemple `1101` et `1010`.
En posant la multiplication comme à l'école, on obtient

    1101

Test

--------
    0000
+  1101
+ 0000
+1101
--------
 1110010
 
Ce résultat est juste en un certain sens, 
mais il est insatisfaisant car 1110010 ne correspond pas à l'encodage des nombres de F<sub>2⁴</sub>
comme on l'a défini, car cet encodage doit être une suite de 4 bits.

L'astuce est maintenant de réduire ce résultat,
à l'aide de l'équation fondamentale du nombre imaginaire k,
qu'on a défini comme `k⁴ = k+1`.
En notation binaire, ça veut dire que `10000 = 0011`.
Utilisons cela pour réduire `1110010`:

   1110010
----------
   1000000
+   110010
----------
    001100
+   110010
----------
    111110
----------
    100000
+    11110
----------
     00110
+    11110
----------
     11000
----------
     10000
+     1000
----------
      0011
+     1000
----------
      1011

Ça y est, on y est parvenu, on a obtenu le résultat de notre multiplication.


## Calculs dans les corps finis de (quasi)-Mersenne

Notez qu'il y a également d'autres astuces de calculs remarquables 
pour certains autres corps finis,
notamment les corps à p éléments, 
où p est un nombre premier de Mersenne.
Un tel nombre premier s'écrit p = 2<sup>r</sup> - 1, où r est lui aussi premier.

Illustrons le avec r = 3, qui donne le nombre premier de Mersenne 2³ - 1 = 7
Les nombres de 0 à 6 du corps F<sub>7</sub> sont simplement représentés 
par leurs représentations binaires à 3 bits,
ce qui donne la suite de nombres 000, 001, 010, 011, 100, 101 et 110.
Cependant, on sait que dans F<sub>7</sub>, le 7e nombre est intuitivement 0.
on a donc 111 = 000.

On peut alors considérer des opérations classiques de multiplication et d'addition,
mais avec la retenue cette fois, 
puisqu'on travaille avec les représentation binaires des nombres entiers,
et non pas des nombres d'un corps F<sub>2<sup>n</sup></sub> de caractéristique 2.
Il faut juste prêter attention
à bien effectuer une réduction de 111 en 000 
à chaque fois qu'on atteint ou qu'on dépasse 111.

Illustrons cela en faisant `100 * 100`. 
On obtient alors 100000, qui se décompose en
10000 = 10000 - 1110 = 10.

Plus généralement tous les nombres premiers de la forme 2<sup>r</sup> - c,
avec un petit nombre impair c,
définissent des corps finis F<sub>2<sup>r</sup> - c</sub> particulièrement intéressants pour la cryptographie,
notamment car ils facilitent les calculs par ordinateur,
en réduisant des opérations d'addition et de multiplication à des manipulations de bits.
Ça paraît anecdotique dit comme ça,
mais quand il s'agit de produire un grand nombre de preuves cryptographiques,
ça fait rapidement des économies pas si négligeables de temps et d'énergie !


## Conclusion

Clairement, aujourd'hui, je ne vous ai donné qu'une introduction aux corps finis.
Il y aurait clairement beaucoup de choses à dire,
notamment en reliant tout cela aux travaux génialissimes 
d'un jeune révolutionnaire mort beaucoup trop tôt,
un certain [Évariste Galois](https://tournesol.app/entities/yt:OjIdGsts_RA), 
qui mériterait plusieurs films dédiés à son histoire rocambolesque.

En particulier, la construction que je vous ai montrée 
fait partie d'une recherche plus générale
sur l'études des solutions des équations polynomiales,
et sur les structures algébriques des nombres.
Les mathématiciens plus purs s'intéressent ainsi à l'ajout de nombres "imaginaires"
qui aident à résoudre des équations que les nombres rationnels ne permettent pas de résoudre ;
et il faut que je fasse un peu attention à la terminologie ici,
car par nombres "imaginaires", 
je ne pense pas forcément à la racine carrée de -1.

Par exemple, quand on cherche des solutions rationnelles,
on peut vouloir ajouter des nombres "imaginaires" comme la racine carrée de 2,
qui correspond à l'équation k² = 2.
Et ça marche très bien, car en effet,
l'équation X² = 2 n'a pas de solution rationnelle.

En particulier, les mathématiciens qui suivent les pas de Galois 
aiment réfléchir aux corps infinis conçus par ajouts 
de tous les nombres "imaginaires" utiles à la résolution des équations polynomiales.
Voilà qui conduit typiquement au corps des nombres complexes si on part des nombres réels,
ou au corps des nombres algébriques, si on part des nombres rationnels.
On parle alors de "clôture algébrique".
Il est par ailleurs aussi possible de le faire à partir des corps finis,
voire de garantir l'existence et l'unicité d'une clôture algébrique pour tout corps,
à isomorphisme près.
Mais ceci requiert de basculer dans le monde des maths non-constructives,
ce qui nous éloigne drastiquement des applications.

Mais tout ça, en cryptographie, en tout cas dans les protocoles les plus standards,
il n'y a pas lieu de se soucier de ces aspects.
L'ensemble des corps finis à p<sup>n</sup> éléments est un espace déjà suffisamment riche,
et surtout suffisamment calculable,
pour nous fournir des billes précieuses pour sécuriser nos systèmes d'information,
dont je suis impatient de vous parler.


