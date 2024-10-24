# Le postquantique

Dans les vidéos précédentes, 
on a vu que la cryptographie moderne s'appuie à foison 
sur la création d'un secret $w,
suivie de celle d'un problème $x = g^w$ dont $w$ est la solution.
Et si cette approche est si utile à la cryptographie,
c'est avant tout parce qu'on pense que le calcul de $x = g^w$
est une fonction à sens unique :
il est facile à faire par n'importe quel citoyen muni d'un téléphone,
mais même la NSA et son réseau d'espions et de machines ne saura pas le défaire.

Mieux encore, on a vu que l'on pouvait calculer $x = g^w$
non seulement avec des nombres modulo un nombre premier sûr,
mais aussi dans le groupe des points d'une courbe elliptique.
Qui plus est, cette fonction à sens unique a de jolies propriétés algébriques,
comme le fait que $(g^w)^v = g^{wv}$,
qu'on appelle la quasi-commutativité,
ou le fait que $g^w \cdot g^v = g^{w+v}$,
ce qui revient à dire qu'on a là un morphisme de groupe.

Toutes ces merveilleuses propriétés ont conduit à un déploiement massif
de nombreuses technologies de chiffrements 
qui s'appuient sur cette fonction à sens unique,
de la création de secret partagé par Diffie-Hellman à la signature électronique,
en passant par d'autres applications plus sophistiquées,
comme la preuve à divulgation nulle de connaissance et le chiffrement homomorphe,
dont on reparlera plus tard dans cette série.
Et on aurait même pu considérer que 
la cryptographie sécurisée était un enjeu majeur de société résolu,
au moins pour un très grand nombre de cas d'usage.

Sauf que...


## Le danger quantique

Sauf que des armées de physiciens ont investi des milliards de dollars
pour que tout l'édifice cryptographique conçu jusque là
puisse être balayé d'un revers de la main.
Je parle bien sûr de la recherche sur la conception de calculateurs quantiques,
souvent présentée comme une gloire de l'intellect humain
dépassant les limites de la connaissance,
voire parfois comme un nouveau jeu vidéo qu'il serait insensé de ne pas vouloir développer,
alors qu'on sait très bien que, de très loin,
la principale application de ces calculateurs,
c'est de détruire la cybersécurité qui s'appuie sur l'opération $x = g^w$.

Et oui, parce que si l'on pense toujours que cette opération est à sens unique,
même vis-à-vis des plus puissants supercalculateurs d'aujourd'hui,
on sait malheureusement depuis 1994
que l'algorithme de Shor permet aux calculateurs quantiques
d'inverser cette fonction.
C'est ainsi sans doute une opération à sens unique pour les calculateurs classiques ;
mais on est sûr qu'elle ne l'est pas pour les calculateurs quantiques.

Alors, jusque là, les calculateurs quantiques ne parviennent pas encore
à intriquer suffisamment de qubits pour être en mesure de s'attaquer
aux protocoles de cryptographie qui sont abondamment utilisés sur le web.
Mais à cause des milliards de dollars d'investissement public et privé
dans cette technologie,
et à cause de la publication des découvertes qui peuvent être récupérées 
par des superpuissances autoritaires,
ce n'est probablement qu'une question de temps, et peut-être même d'années,
avant que nos systèmes informatiques actuels ne soient plus protégés.

Et j'insiste sur le fait qu'on ne parle pas de jeu vidéo ici.
On parle de la cybersécurité de toute l'infrastructure informatique mondiale,
sur laquelle repose toute l'économie moderne,
et dont une paralysie prolongée serait une catastrophe.
Bref. Arrêtons de parler des calculateurs quantiques 
comme d'un truc aussi cool que Candy Crush.
On parle là d'une menace pour la sécurité nationale.

Bien sûr, ce constat, je suis très loin d'être le seul,
ou d'être même le premier, à l'effectuer.
En particulier, face à l'urgence de sécuriser le cyberespace 
contre les calculateurs quantiques,
les cryptographes se sont organisés,
sous la coupole notamment du National Institute of Standards and Technology,
le NIST, aux États-Unis.
En août dernier, le NIST a en particulier approuvé 
[un nouveau standard cryptographique](https://csrc.nist.gov/News/2024/postquantum-cryptography-fips-approved).

Ce standard, habituellement qualifié de post-quantique,
est un chiffrement qu'on espère être sécurisé contre les calculateurs quantiques.
Et je dis bien "on espère", car on ne dispose pas de garanties de sécurité.
En particulier, de ce que je comprends, 
les cryptographes restent bien moins confiants vis-à-vis de la sécurité
de la cryptographie post-quantique contre les ordinateurs quantiques,
qu'ils ne sont confiants de la sécurité de la cryptographie pré-quantique 
contre les ordinateurs classiques.
Ou dit plus simplement, l'avènement des ordinateurs quantiques augmente
nos préoccupations de cybersécurité,
même dans l'hypothèse où on parviendrait à tout basculer au post-quantique du jour au lendemain ;
ce qui est également très loin d'être gagné !

Ainsi quand, en avril 2024, 
un [chercheur chinois](https://eprint.iacr.org/2024/555.pdf) a partagé en preprint
un article intitulé "quantum algorithms for lattice problems",
la réaction n'a pas été un dédain pour un n+1-ième crack.
J'ai des amis à la Direction Générale de l'Armement qui m'ont raconté
avoir vécu une semaine très difficile,
occupée à rechercher une erreur quelque part dans les 60 pages de preuves de l'article.
Le risque, c'est que les solutions les plus prometteuses pour la cryptographie post-quantique
venaient d'être balayées d'un revers de la main.
Fort heureusement, 8 jours plus tard, une erreur fatale fut prouvée ;
enfin, quand je dis fort heureusement, c'est pour la cybersécurité post-quantique,
pas forcément pour le chercheur en question 
dont l'oeuvre a été balayée d'un revers de la main.

Toujours est-il que, aujourd'hui, faute de mieux,
le NIST a approuvé la cryptographie post-quantique,
que je vais donc pouvoir vous présenter.


## La cryptographie post-quantique

Alors, en fait non.
La cryptographie post-quantique est malheureusement beaucoup plus complexe
que la simple opération $x = g^w$,
ce qui fait que je ne vais pas pouvoir vous la décrire pleinement
dans une vidéo Science4All.
En fait, il existe même de nombreux protocoles différents de cryptographie post-quantique,
et même si j'ai pas mal lu à ce sujet récemment,
je dois dire que je ne maîtrise absolument pas les subtilités de ces protocoles.

Aujourd'hui, je vais me concentrer uniquement 
sur les propriétés fondamentales et les grands principes 
des protocoles de créations de secrets partagés
et de signatures cryptographiques à base de réseaux,
ou lattice-based cryptography en anglais,
qui ont été sélectionnés par le NIST.
Ou même plus précisément, on va étudier des versions simplifiées de ces protocoles.

Et oui, un autre gros défaut du post-quantique,
c'est que c'est beaucoup plus complexe à comprendre que la cryptographie classique,
et donc beaucoup plus coûteux en termes de ressources humaines ;
et c'est d'ailleurs aussi bien plus coûteux en termes de ressources calculatoires,
notamment en termes de tailles des clés et des signatures cryptographiques...





