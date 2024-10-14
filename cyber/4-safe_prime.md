# Les nombres premiers sûrs

La dernière fois, on a vu que la clé de la cryptographie,
c'était de générer des secrets $$w$$,
et de concevoir un problème difficile $$x$$ dont $$w$$ est la solution.
En particulier, idéalement résoudre $$x$$ doit être calculatoirement tellement difficile
qu'on peut être confiant que même les superintellygences de l'espace numérique,
comme Google, la NSA et le gouvernement chinois,
soient incapables de découvrir une solution au problème $$x$$,
comme le secret $$w$$ dont on a la connaissance.

Aujourd'hui, on va voir la solution qui est très largement la plus utilisée aujourd'hui
pour concevoir des problèmes difficiles $$x$$ à partir de secrets $$w$$.
Cette opération, c'est celle qui consiste à simplement calculer $$x = g^w$$,
où $$g$$ est un nombre un peu particulier, comme on le verra dans la suite.
Résoudre le problème $$x$$, c'est alors trouver un nombre $$v$$ tel que $$x = g^v$$.
Clairement, nous qui avons conçu le problème $$x$$ à partir de $$w$$,
on en connaît une solution, à savoir $$v = w$$.
Mais l'espoir, c'est que même une superintellygence ne saura pas trouver une solution $$v$$
à l'équation $$x = g^v$$.

Pour ceux qui ont vu 
la chouette [vidéo](https://tournesol.app/entities/yt:1Yv8m398Fv0) de Science Étonnante,
cette astuce qui consiste à cacher $$w$$ et à révéler $$x = g^w$$ est au coeur
de l'algorithme de Diffie-Hellman,
une solution au centre de la sécurité du web.
David explique en particulier l'utilité de cette expression
si $$g$$ et $$w$$ sont des nombres entiers 
et si $$x = g^w$$ est calculé modulo un nombre premier $$p$$,
c'est-à-dire en forçant l'égalité $$p = 0$$,
un peu comme je vous ai expliqué comment forcer l'égalité $$12 = 0$$
dans [cette vidéo sur String Theory](https://tournesol.app/entities/yt:PalsAMRgU3A).
Ne vous enfuyez pas tout de suite, j'y reviendrai.

Dans le jargon, si cette opération est si utile en cybersécurité,
c'est parce qu'on a des bonnes raisons de penser 
qu'elle est une fonction à sens unique.
Autrement dit, calculer le problème $$x = g^w$$ à partir de $$g$$ et $$w$$, c'est facile.
Mais il peut être extrêmement difficile de reconstruire $$w$$ à partir de $$g$$ et $$x$$.
C'est donc une opération facile à faire, et extrêmement difficile à défaire ;
ou dit avec le langage de la vidéo précédente :
étant donné un secret $$w$$, c'est facile de trouver un problème $$x$$ dont $$w$$ est la solution,
mais dont la résolution est extrêmement difficile.

Eh bien, ça, ce sont des opérations qu'on adore en cryptographie !
En effet, ça permet à un citoyen lambda de faire des choses
que même une superintellygence sera incapable de défaire,
comme se connecter à un site web d'une manière si sécurisée
qu'elle sera incassable même par la NSA.

Et alors, David est allé un peu vite sur quelques petits aspects fascinants,
que je vais le prendre aujourd'hui le temps d'explorer,
en faisant notamment un détour par l'une des plus grandes mathématiciennes de l'Histoire,
une certaine Sophie Germain...


## L'arithmétique modulo p (avec un angle algorithmique!)

Commençons par quelques bases de l'arithmétique modulaire,
c'est-à-dire les opérations sur les nombres entiers
lorsque l'égalité $$p = 0$$ est imposée.
Et illustrons tout cela avec le nombre premier $$p = 13$$.

Si on impose $$13 = 0$$, 
alors on obtient des égalités qui peuvent vous paraître surprenantes
comme $$14 = 13 + 1 = 0 + 1 = 1$$.
Pour bien préciser le fait qu'on a cette égalité modulo 13,
et pas une égalité pour des nombres entiers naturels usuels,
je vous propose d'écrire cela 
$$14 =_{13} 1$$.
On peut ainsi se rendre compte que tout nombre entier
sera égal modulo 13 à un nombre entier entre 0 et 12.
En effet, $$37 =_{13} 13 + 13 + 11 =_{13} 0 + 0 + 11 =_{13} 11$$, qui est bien entre 0 et 12.
Plutôt qu'une décomposition en somme de 13,
on peut même utiliser une décomposition en 13 fois un entier plus un reste.
Ainsi $$37 =_{13} (13 \times  2) + 11 =_{13} (0 \times  2) + 11 =_{13} 11$$.

Cette écriture de 37 en tant que $$13 \times 2 + 11$$
est aussi appelée le reste de la division euclidienne de 37 par 13.
Une première observation qu'on peut faire,
c'est que cette division euclidienne, et en particulier le calcul de 11,
est très rapide.
Il suffit en effet de poser une division, 
comme vous l'aviez appris à l'école.
Et en gros, il suffit de faire autant d'opération que le nombre à diviser a de chiffres.
On dit que le temps de calcul est linéaire en la description des nombres.
Ainsi, même si on manipule avec des nombres cryptographiques avec des milliers de chiffres,
il suffira d'effectuer des milliers d'opérations ;
à la main, c'est très long, mais pour les machines du premier citoyen venu,
ce sera virtuellement immédiat.
Bref. Réduire un nombre modulo 13, c'est très facile.
En python, il suffit de taper par exemple 37 % 13, et la réponse est immédiate.

Et ça, ça va impliquer que faire 
des additions, des soustractions et des multiplications modulo 13,
c'est aussi très facile.
Si je veux multiplier 3151 par 46825 modulo 13 par exemple,
je peux commencer par réduire chacun de ces nombres modulo 13,
ce qui me donnent 5 fois 12 modulo 13.
Maintenant 5 fois 12 se calcule rapidement aussi, avec la multiplication classique ;
le nombre d'opérations nécessaires sera proportionnels au nombre de chiffres du nombre 13.
On obtient en l'occurence 60,
qu'on va réduire modulo 13 pour obtenir 8.

OK. Qu'en est-il de la division ?
Peut-on calculer 3151 / 46825 modulo 13 ?

On peut commencer par clarifier la question.
Le résultat de cette division doit être un nombre n tel que
n =<sub>13</sub> 3151 / 46825.
En multipliant par 46825 des deux côtés,
cette égalité devient 46825 * n =<sub>13</sub> 3151.
Alors, on peut déjà remarquer que cette égalité doit se simplifier modulo 13,
en remplaçant 46825 par sont modulo 13 et 3151 aussi.
Ça nous donne 12 \* n =<sub>13</sub> 5.
Et enfin, on peut remarquer que si on sait résoudre 12 \* m =<sub>13</sub> 1,
alors il suffira de poser n =<sub>13</sub> 5 \* m pour résoudre notre division.

OK. Mais donc, peut-on trouver m tel que 12 \* m =<sub>13</sub> 1 ?
Peut-on, en un sens, calculer 1 douzième modulo 13 ?
Un tel nombre m est appelé l'inverse de 12 modulo 13.
Et on peut remarquer que cette égalité modulo 13
revient à dire qu'il existe un autre nombre entier k
tel que 12 \* m - 13 \* k = 1, ce qu'on appelle une identité de Bézout.
Je vais passer sous silence des détails,
mais parce que 13 est un nombre premier,
on sait que m et k sont garantis d'exister,
et même qu'on peut les calculer efficacement, en passant par le calcul du pgcd.
J'invite d'ailleurs les plus motivés parmi vous 
à écrire explicitement un algorithme pour y parvenir,
et à calculer le nombres d'opérations requises par cet algorithme.

Ce qu'il faut retenir de cette discussion,
c'est surtout que, dans l'arithmétique modulo p,
l'addition, la soustraction, la multiplication et la division sont non seulement bien définies ;
ces opérations sont aussi et surtout extrêmement rapides à effectuer ---
leur temps de calcul va être dans tous ces cas proportionnels au nombre de chiffres de p.

Et c'est en particulier le fait que la division marche aussi bien modulo p
que l'idée lancée par David d'utiliser la multiplication pour créer un secret partagé
ne fonctionne pas :
si Eve observe une multiplication$$x$$ =<sub>p</sub> gw de deux nombres entiers g et$$w$$modulo p,
et si elle connaît aussi g et p,
alors elle pourra reconstruire s en calculant$$w$$=<sub>p</sub> x/g.
On dit que la multiplication modulo p n'est pas une fonction à sens unique.
C'est une opération qu'il est simple de défaire.

> Dit autrement, le logarithme discret dans le groupe additif Z/pZ est facile,
> à cause de l'algorithme d'Euclide de calcul du pgcd.


##$$x$$ =<sub>p</sub> g<sup>w</sup>

Voilà qui nous amène tout doucement à$$x$$ = g<sup>w</sup> modulo p.
Est-ce là bien une opération à sens unique ?

D'abord, précisons que g<sup>w</sup> consiste à multiplier g par g par g et ainsi de suite$$w$$fois.
Et donc$$w$$en particulier doit être une entier naturel.
Qui plus est, même modulo 13, g<sup>13</sup> n'est pas g<sup>0</sup>.
On ne peut pas remplacer le 13 dans les exposants par un 0,
car l'exposant n'est pas lui-même un nombre modulo 13.
Le nombre g lui, l'est, mais pas l'exposant.
OK. Mais donc, si p, g et s sont grands, 
le calcul de$$x$$ = g<sup>w</sup> modulo p est-il une opération à sens unique,
comme David le suggère dans sa vidéo ?

Eh bien, avant de montrer que c'est une opération difficile à défaire,
encore faut-il montrer qu'elle est facile à faire.
Comment pourriez-vous calculer rapidement g<sup>1'050'625</sup> modulo p ?
Alors, bien sûr, on pourrait prendre g, le multiplier par g,
puis multiplier le résultat par g,
puis multiplier le résultat par g,
et ainsi de suite 1'050'625 de fois.
Ça commence à faire vraiment beaucoup, même pour votre machine.
Or en pratique, on remplace 1'050'625 par des nombres cryptographiques,
c'est-à-dire avec plusieurs dizaines de chiffres, voire des centaines.
Et là, ça représente des calculs que même votre machine ne pourra pas effectuer ;
en fait on compte justement sur ça quand on affirme que l'opération est difficile à défaire.
Clairement, il va falloir faire mieux.

Eh bien, j'en avais parlé sur [String Theory](https://tournesol.app/entities/yt:PalsAMRgU3A).
L'idée c'est de décomposer 1'050'625 en une somme de puissances de 2.
Cela nous donne 1'050'625 = 2<sup>20</sup> + 2<sup>12</sup> + 2<sup>0</sup>.
En fait, cette décomposition n'est autre que l'écriture du nombre en base 2 ;
et le nombre de terme est exactement le nombre de chiffres égaux à 1 en base 2.

Maintenant, pour calculer g<sup>2<sup>20</sup></sup>, on va calculer la suite des carrés
g, g², (g²)², ((g²)²)², et ainsi de suite jusqu'à la combinaison de 20 opérations.
De manière cruciale, pour arriver jusqu'à 2<sup>20</sup>,
il suffit en fait de prendre 20 fois des carrés.
C'est beaucoup mieux que 1'050'625 de fois !
De même on peut aisément calculer g puissance 2<sup>12</sup>.
On obtient g<sup>1'050'625</sup> ensuite 
en multipliant g puissance 2<sup>20</sup> par g puissance 2<sup>12</sup>,
puis en multipliant ça par g puissance 2⁰, qui n'est autre que g lui-même.
Voilà qui nous permet de calculer le résultat avec un petit nombre d'opérations ;
en fait cette astuce des carrés répétés permet de calculer$$x$$ = g<sup>w</sup> modulo p
en un nombre d'opérations qui est proportionnel au nombre de chiffres de s.

L'opération est donc facile à faire.
Mais est-elle difficile à défaire ?

Eh bien, comme l'explique David, ce n'est pas toujours le cas.
Typiquement, un mauvais choix de g, comme g = 5 quand p = 13, 
alors le logarithme discret peut être trivial à défaire,
parce que la suite des$$x$$ = g<sup>w</sup> boucle très vite.
Mais donc, comment choisir g et p ?


## L'algorithme de Pohlig-Hellman

Quand p est un nombre premier,
l'ensemble des nombres modulo p qui ne sont pas égaux à zéro
forme ce qu'on appelle le groupe multiplicatif modulo p.
Cet ensemble contient p-1 nombres, à savoir les nombres de 1 à p-1 modulo p.
Tous ces nombres peuvent être multipliés et divisés entre eux,
et ça donnera toujours des nombres entre 1 et p-1 modulo p.

On peut alors démontrer l'existence de racines de primitive,
c'est-à-dire que pour tout p,
il existe des nombres g tels que les$$x$$ = g<sup>w</sup> prennent toutes les valeurs
entre 1 et p-1 modulo p avant de reboucler.
On dit que le groupe multiplicatif est monogène :
tout élément du groupe multiplicatif s'écrit g<sup>w</sup> pour un entier$$w$$.

D'ailleurs, vu que g<sup>w</sup> \* g<sup>v</sup> = g<sup>w+v</sup>,
on voit que multiplier deux éléments du groupes
revient à ajouter leurs exposants, 
dans l'écriture sous forme de puissance de g.
En fait, ça revient à dire que l'application 
qui à$$w$$associe g<sup>w</sup> est un morphisme de groupe.

Mieux encore, on peut remarquer que le p-ième élément de la suite des g<sup>w</sup>
doit forcément reboucler, et donc que g<sup>p</sup> =<sub>p</sub> g.
C'est ce qu'on appelle d'ailleurs le petit théorème de Fermat.
Mais donc g<sup>p-1</sup> est tel que g<sup>p-1</sup> g =<sub>p</sub> g.
En divisant par g des deux côtés, on conclut que g<sup>p-1</sup> =<sub>p</sub> 1.
Or on peut aussi écrire 1 =<sub>p</sub> g⁰.
Donc g<sup>p-1</sup> =<sub>p</sub> g⁰.
Et donc en termes d'exposants cette fois, on a l'égalité p-1 = 0.

En fait, quand g est une racine primitive de p, 
les exposants des g<sup>w</sup> modulo p se comportent comme des nombres modulo p-1.
On dit que le groupe multiplicatif modulo p est isomorphe au groupe additif modulo p-1,
ou encore que la fonction qui à$$w$$associe g<sup>w</sup> est un isomorphisme de groupe,
entre le groupe multiplicatif modulo p et le groupe additif modulo p-1.

Mais alors, le logarithme discret modulo p, 
c'est finalement la division dans le groupe modulo p-1.
En général, on espère que cette division est difficile,
surtout quand on n'a pas accès directement à$$w$$, et qu'on ne connaît que g<sup>w</sup>.
Mais ce ne sera pas toujours le cas, notamment en fonction des diviseurs de p-1.

OK, on va aborder maintenant la partie la plus difficile de la vidéo,
donc asseyez-vous bien au fond de votre siège, respirez un bon coup...
et n'hésitez pas à passer à la section suivante de la vidéo si vous ne le sentez pas !

Prenons l'exemple du nombre premier p = 31, avec g = 3.
On peut vérifier que la suite des g<sup>w</sup> modulo p couvre toutes les valeurs entre 1 et 30,
et donc que g est une racine primitive de p.
Sauf que p-1 s'écrit p-1 = 30 = 2 \* 3 \* 5.
Autremet dit, 30 se décompose comme un produit de petits nombres premiers.
Eh bien, ça, c'est une vulnérabilité majeure du nombre premier p.

En particulier, regardez ce qu'il se passe 
quand j'étudie le groupe engendré par g<sub>2</sub> =<sub>p</sub> g<sup>3\*5</sup>,
c'est-à-dire par g à la puissance des facteurs premiers de p qui ne sont pas 2.
On a alors g<sub>2</sub><sup>2</sup> 
=<sub>p</sub> (g²)<sup>3\*5</sup> =<sub>p</sub> g<sup>2\*3\*5</sup> 
= <sub>p</sub> g<sup>30</sup> =<sub>p</sub> g<sup>p-1</sup> = 1.
Et du coup la suite des g<sub>2</sub><sup>w</sup> va osciller entre 1 et g<sub>2</sub>.

De même on peut voir que le groupe engendré par g<sub>3</sub> =<sub>p</sub> g<sup>2\*5</sup>
va osciller entre trois valeurs, à savoir 1, g<sub>3</sub> et g<sub>3</sub>².
Enfin, le groupe engendré par g<sub>5</sub> =<sub>p</sub> g<sup>2\*3</sup> va osciller entre 5 valeurs,
à savoir 1, g<sub>5</sub>, g<sub>5</sub>², g<sub>5</sub>³ et g<sub>5</sub>⁴.

Comme on n'a que des petits facteurs premiers,
tous ces éléments peuvent être calculés explicitement en assez peu de temps.
Mieux encore, les trois éléments (g<sub>2</sub>, g<sub>3</sub>, g<sub>5</sub>) forment une sorte de base
de l'ensemble des éléments du groupe multiplicatif modulo p,
dans le sens où tout terme de ce groupe s'écrit de manière unique
h =<sub>p</sub> g<sub>2</sub><sup>w<sub>2</sub></sup> g<sub>3</sub><sup>w<sub>3</sub></sup> g<sub>5</sub><sup>w<sub>5</sub></sup>,
où (s<sub>2</sub>, s<sub>3</sub>, s<sub>5</sub>) sont des sortes de coordonnées de$$x$$ dans cette base,
qui sont respectivement des nombres modulo 2, 3 et 5.

Pour résoudre$$x$$ =<sub>p</sub> g<sub>2</sub><sup>w<sub>2</sub></sup> g<sub>3</sub><sup>w<sub>3</sub></sup> g<sub>5</sub><sup>w<sub>5</sub></sup>,
on peut en particulier, précisder les valeurs 
g<sub>2</sub> =<sub>p</sub> g<sup>3\*5</sup> =<sub>p</sub> 30, 
g<sub>3</sub> =<sub>p</sub> g<sup>2\*5</sup> =<sub>p</sub> 25, et 
g<sub>5</sub> =<sub>p</sub> g<sup>2\*3</sup> =<sub>p</sub> 16
et surtout calculer des termes similaires pour x,
ce qui va définir 
x<sub>2</sub> =<sub>p</sub> x<sup>3\*5</sup> =<sub>p</sub> 30, 
x<sub>3</sub> =<sub>p</sub> x<sup>2\*5</sup> =<sub>p</sub> 5 et 
x<sub>5</sub> =<sub>p</sub> x<sup>2\*3</sup> =<sub>p</sub> 1.

Pour chaque facteur premier q de p-1,
on va s'intéresser en particulier à résoudre l'équation
x<sub>q</sub> =<sub>p</sub> g<sub>q</sub><sup>w<sub>q</sub></sup>.
Dans notre cas, on obtient les équations
30 =<sub>p</sub> 30<sup>w<sub>2</sub></sup>,
5 = <sub>p</sub> 25<sup>w<sub>3</sub></sup> et
1 =<sub>p</sub> 16<sup>w<sub>5</sub></sup>.
En évaluant toutes les puissances de g<sub>q</sub><sup>w</sup>, 
vu qu'il y en a peu pour des petits nombres premiers q,
on peut alors obtenir 
w<sub>2</sub> =<sub>2</sub> 1, 
w<sub>3</sub> =<sub>3</sub> 2 et 
w<sub>5</sub> =<sub>5</sub> 4.

Pour conclure, il reste à trouver un nombre entier s
tel que si on écrit 
g<sup>w</sup> =<sub>p</sub> g<sub>2</sub><sup>w<sub>2</sub></sup> g<sub>3</sub><sup>w<sub>3</sub></sup> g<sub>5</sub><sup>w<sub>5</sub></sup>,
alors les s<sub>2</sub> =<sub>2</sub> 1, s<sub>3</sub> =<sub>3</sub> 2 et s<sub>5</sub> =<sub>5</sub> 4.
Eh bien, ça, ça correspond au théorème des restes chinois :
si on connais tous les restes de s modulo des facteurs premiers q,
alors on peut reconstruire efficacement s modulo le produit des facteurs premiers q.

Bref. Je saute ici encore quelques détails pour ne pas perdre le fil de la vidéo,
mais toujours est-il que, 
parce que p-1 pouvait se factoriser en un produit de plein de petits nombres premiers,
on peut factoriser le problème du logarithme discret,
et le résoudre beaucoup plus efficacement.
L'algorithme que je vous ai présenté peut en fait être généralisé au cas
où certains facteurs premiers apparaissent plusieurs fois,
et davantage optimisés pour résoudre le logarithme discret pour des petits nombres premiers.
On obtient alors [l'algorithme de Pohlig-Hellman](https://fr.wikipedia.org/wiki/Algorithme_de_Pohlig-Hellman).
Et oui, c'est le même Hellman que dans Diffie-Hellman.

Le temps de calcul de Pohlig-Hellman être de l'ordre
de la racine carrée du plus grand facteur premier de p-1.

> Techniquement la complexity sera O(\sum<sub>q</sub> k<sub>q</sub> (log(n) + sqrt(q)), 
> si p-1 = \prod q<sup>k<sub>q</sub></sup>.

Si ce plus grand facteur premier reste un nombre cryptographique, ça reste déraisonnable.
Mais s'il est de l'ordre du million de milliards seulement,
la fonction qui à s associe g<sup>w</sup> modulo p ne pourra plus être considérée être à sens unique.

> En pratique, il reste le problème de la factorisation de p-1,
> que l'on considère être un problème difficile.
> L'un des dangers toutefois est davantage l'implantation de porte dérobée :
> une superintellygence pourrait choisir des petits nombres premiers,
> et les multiplier entre eux, en espérant obtenir un nombre N
> tel que N+1 est un nombre premier.
> Il pourrait alors recommander d'utiliser p = N+1 dans les chiffrements.
> Ça peut paraître étrange comme cyber-attaques, 
> mais on verra bientôt un exemple de porte dérobée pas si différente,
> que la NSA semble avoir voulu encourager dans les solutions cyrptographiques...


## Les nombres premiers de Germain

Pour éviter d'être cassé par Pohlig-Hellman,
les cryptographes favorisent désormais l'adoption de grands nombres premiers p
tels que p-1 a le plus grand facteur premier possible.
Et comme p est impair, sauf pour p = 2 dont on peut difficilement dire qu'il est grand,
on sait que p-1 est pair,
et donc s'écrit p-1 = 2q.
Idéalement donc, q n'est pas lui-même décomposable ;
ce doit être un nombre premier.
Un tel nombre premier p, qui est donc tel que (p-1)/2 est aussi premier,
est ce qu'on appelle un *nombre premier sûr*.

Clairement, ces nombres premiers sûrs sont maximalement résilients contre Pohlig-Hellman ;
et donc pour ces nombres premiers sûrs p et pour une racine primitive g de p,
la fonction qui à$$w$$associe g<sup>w</sup> modulo aura de meilleures chances d'être à sens unique :
facile à faire, difficile à défaire.

Et bien sûr, les cryptographes ne sont pas les premiers 
à s'intéresser à ces nombres premiers sûrs.
T'es sûr ? Oui bien sûr, j'en suis sûr.

Il y a deux siècles, une brillante mathématicienne du nom de Sophie Germain
avait déjà étudié de tels nombres premiers.
Alors, techniquement, Germain a plus étudié 
les nombres premiers q tels que p = 2q + 1 est premier.
q est alors appelé nombre premier de Germain,
alors que p un le nombre premier sûr.
Une paire Germain-sûr est une paire (q, p)

J'en profite pour vous recommander cette excellente vidéo de Mathador
sur [Sophie Germain](https://tournesol.app/entities/yt:lvB5uTwry9c).

Les premières paires de nombres premiers de Germain-sûr sont ainsi
(2, 5), (3, 7), (5, 11), (11, 23), (23, 47), et ainsi de suite.
Notez que 13 n'est pas dans cette liste ;
et oui, 13 - 1 = 12 = 2² \* 3, ce qui est même un nombre très friable,
c'est-à-dire composé de facteurs premiers tous très petits.
Donc le choix de p de David n'était pas tout à fait optimal ;
même si bon, il a un défaut de sécurité nettement plus important, 
à savoir sa petite taille de base,
mais c'est bien sûr le cadet des soucis d'une vulgarisation de Diffie-Hellman !

Et si Sophie Germain s'y intéressait, 
c'était pour tenter de résoudre l'autre théorème de Fermat,
le fameux grand théorème de Fermat,
à savoir démontrer que l'équation x<sup>n</sup> + y<sup>n</sup> = z<sup>n</sup>
n'a aucune solution pour n entier supérieur ou égal à 3,
et x, y, z entiers.
À son époque très peu de progrès avaient été effectués sur cette question.
Mais la stratégie est toujours la même :
montrer que si (x, y, z, n) est solution de l'équation,
alors ils doivent satisfaire des propriétés tellement bizarres
qu'elles ne peuvent pas être vérifiées en même temps.

Avant Sophie Germain, on savait de plus qu'il suffisait d'étudier
le cas où n est un nombre premier.
L'avancée de Sophie Germain, c'est de montrer que si n est un nombre premier de Germain,
et si (x, y, z, n) forme une solution,
alors x, y ou z doit être divisible par p².
Malheureusement, l'approche globale de Germain n'a pas été couronnée de succès ;
et pour cause, il aura fallu 1994 et des outils mathématiquement diablement plus sophistiqués
pour qu'une preuve du théorème par Andrew Wiles soit enfin complète et validée.

Ces nombres premiers de Germain sont encore bourrés de mystères.
Par exemple, à l'instar de la conjecture des nombres premiers jumeaux,
on ne sait toujours pas s'il existe un nombre infini de nombres premiers de Germain,
même si on le suspecte.
De même, on peut s'intéresser aux suites telles p<sub>1</sub> est premier,
p<sub>2</sub> = 2 p<sub>1</sub> + 1 est premier,
p<sub>3</sub> = 2 p<sub>2</sub> + 1 est premier, et ainsi de suite.
Autrement dit, aux suites de nombres premiers, 
tels que chaque nombre premier de la suite est le nombre premier sûr
du nombre premier qui le précède.
De telles suites sont appelées chaînes de Cunningham.

On a démontré qu'il n'existe pas de chaînes de Cunningham infinies.
Cependant, certaines qu'on a trouvé sont très longues.
La plus longue connue a été découverte en 2014 et contient 19 nombres premiers 
(et donc 18 nombres premiers de Germain).
On pense qu'il existe des chaînes de Cunningham arbitrairement longues ;
mais là encore, c'est avant tout une conjecture ouverte.

Enfin, on peut noter que la génération de grands nombres premiers de Germain
peut être effectuée efficacement,
ce qui fait que vous n'avez aucune excuse à ne pas faire de la cryptographie 
modulo un nombre premier sûr,
plutôt que modulo un nombre premier friable.


## La menace des calculateurs quantiques

Si l'on pense que la fonction qui calcule g<sup>w</sup> modulo p
est une fonction à sens unique pour les superintellygences d'aujourd'hui,
en tout cas pour les nombres premiers sûrs,
on imagine toutefois qu'elle ne le sera plus pour certaines superintellygences de demain,
notamment celles qui auront accès à des calculateurs quantiques.

On avait déjà vu dans deux vidéos de String Theory,
d'une part [comment ces calculateurs fonctionnent](https://tournesol.app/entities/yt:plgQgJ4obTg),
et d'autre part comment les exploiter 
pour [factoriser des très grands nombres](https://tournesol.app/entities/yt:azXt6-098dU),
et malheureusement, c'est-à-déjà très problématique,
parce que la sécurité des certains protocoles cryptographiques très utilisés, 
comme le [protocole RSA](https://tournesol.app/entities/yt:Y2bsLRdVBP8),
repose fortement sur l'hypothèse selon laquelle 
multiplier des nombres cryptographiques est à sens unique.

En bref, ces calculateurs quantiques disposent de nombres cryptographiques d'espèces de jauge,
qu'ils peuvent manipuler de concert à l'aide d'opérations très spécifiques,
et en général très restreintes ;
en général ces calculateurs seront très lents et inefficaces.
Cependant, pour une poignée de problèmes, 
mais vraiment une toute poignée, genre 2 selon Wikipedia,
ces calculateurs peuvent exploiter des bizarreries quantiques
pour court-circuiter certains calculs.

L'un de ces deux problèmes, c'est le problèmes de la transformée de Fourier,
pour lequel il existe donc une transformée de Fourier quantique
exponentiellement plus efficace.
Or une transformée de Fourier, 
c'est particulièrement utile pour identifier des périodes dans un signal ;
et c'est vraiment pour ça qui permet 
la [factorisation des nombres](https://tournesol.app/entities/yt:azXt6-098dU).

Eh bien malheureusement, cette même astuce peut être utilisée 
pour résoudre le problème du logarithme discret,
c'est-à-dire identifier un$$w$$tel que$$x$$ =<sub>p</sub> g<sup>w</sup> modulo p, sachant x, g et p.
L'idée en gros c'est d'étudier la suite g<sup>a</sup> x<sup>-b</sup> modulo p,
et en particulier les moments où elle devient égale à 1.
Typiquement on sait que a =$$w$$et b = 1 doit être solution, 
mais aussi a = 2w et b = 2, 
ainsi que a = 3w et b = 3, et ainsi de suite.
Ainsi (w, 1) correspond à une sorte de fréquence du signal.

Eh bien, je vous épargne bien des détails,
mais trouver la fréquence fondamentale peut être en gros effectué 
par la transformée de Fourier quantique,
et celle-ci peut ensuite être utilisée pour trouver$$w$$.
Et voilà pourquoi toute superintellygence 
qui aura conçu ou accédé à un calculateur quantique
pourra inverser la fonction à sens unique qui calcule g<sup>w</sup> à partir de$$w$$,
sur laquelle repose tant la sécurité de notre espace informationnel.

Dès lors, je ne vois vraiment pas comment on peut moralement justifier
la poursuite effrénée de la conception de calculateurs quantiques,
surtout quand cette course à la conception est publiée dans des journaux
auxquels des armées cyber de toutes sortes de pays ont aisément accès,
y compris des pays de moins en moins démocratiques,
et des pays qui ne l'ont jamais été.


## Conclusion

Aujourd'hui, c'était une vidéo nettement plus technique que les précédentes.
Mais il n'y a nul besoin de retenir tous les détails techniques.
S'il y a une chose à retenir, 
c'est surtout qu'une grosse partie de la cybersécurité moderne
s'appuie sur l'hypothèse selon laquelle le calcul de$$x$$ = g<sup>w</sup> à partir de w
est une fonction à sens unique,
c'est-à-dire facile à faire par n'importe quel citoyen sur son téléphone,
mais extrêmement difficile à défaire par n'importe quel superintellygence.

Mais il y a mieux encore. 
Cette fonction possède de nombreuses propriétés mathématiques très utiles en pratique,
notamment le fait que (g<sup>w</sup>)<sup>v</sup> = g<sup>wv</sup>, comme c'est utilisé dans Diffie-Hellman,
ou encore que g<sup>w</sup> g<sup>v</sup> = g<sup>w+v</sup>, 
qui est le socle de nombreuses applications avancées 
comme le chiffrement homomorphe et la divulgation nulle de connaissance.
On dit que la fonction à sens unique est de surcroît quasi-commutative,
et définit un isomorphisme de groupe.

Pour toutes ces raisons,
on s'est énormément appuyé sur cette fonction,
quitte à trouver des astuces pour toujours mieux la sécuriser,
en cherchant typiquement à le faire modulo des nombres premiers sûrs.
En fait, aujourd'hui, on utilise d'autres solutions encore,
comme effectuer le calcul dans des courbes elliptiques,
dont on aura l'occasion de reparler plus tard dans cette série.

Malheureusement, on sait depuis 1994, soit 30 ans déjà,
qu'il va nous falloir abandonner tout ça, et adopter des alternatives,
souvent malheureusement beaucoup plus complexes encore à comprendre,
et donc à rendre intelligibles y compris pour des docteurs en mathématiques comme moi,
parce qu'on sait déjà 
que les calculateurs quantiques vont être capables d'inverser la fonction, 
et qu'elle ne sera donc plus à sens unique face à certaines superintellygence.
Dans ce contexte, en plus de la recherche et développement de cryptographies alternatives,
qu'on appelle post-quantique,
il y a une urgence à ralentir celle des calculateurs quantiques,
dont les applications extrêmement limitées ne contre-balancent absolument pas,
en tout cas à mes yeux,
la menace existentielle qu'ils font peser 
sur l'espace informationnel déjà très mal en point d'aujourd'hui ;
et pourrait-on dire même d'hier, 
puisque les superintellygences malveillantes collectent déjà massivement
des données chiffrées par g<sup>w</sup>, directement ou non,
pour pouvoir les lire le jour où un elles auront accès à un calculateur quantique.
Je vous renvoie à cette excellente 
[vidéo de Veritasium](https://tournesol.app/entities/yt:-UrdExQW0cs)
sur le "harvest now, decrypt later".

L'ordinateur quantique, ce n'est vraiment pas un nouveau jeu vidéo.
C'est une menace de plus pour notre espace informationnel,
qui a déjà propulsé les partis d'extrême-droite au pouvoir depuis une décennie,
alimenté la haine et la volonté de meurtres de populations étrangères
et réduit au silence les sujets les plus vitaux pour notre futur.

D'ailleurs j'en profite pour vous appeler à l'aide.
Si on veut construire un futur beaucoup plus sécurisé,
il va falloir qu'on rende rapidement le web beaucoup plus démocratique ;
mais au préalable, il va falloir montrer qu'un tel web est possible.
C'est vraiment tout l'objet du projet non-lucratif Tournesol.
Plus vous participerez à ce projet, 
plus il nous sera facile de trouver des soutiens, financiers, humains et institutionnels,
pour ensuite défendre beaucoup plus efficacement le projet d'un numérique démocratique.
S'il-vous-plaît, prenez le temps de créer un compte sur Tournesol,
et d'y évaluer les meilleures vidéos de YouTube,
pour que l'algorithme de recommandation collaboratif de Tournesol
puisse correspondre mieux aux jugements humains sur la bonne priorisation 
des sujets d'attention de notre société.
Du fond du coeur, je vous en remercie d'avance.


