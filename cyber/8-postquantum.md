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
Ou même plus précisément, 
on va étudier l'astuce fondamentale des algorithmes,
qui s'appuient sur [l'article fondateur d'Oded Regev](https://dl.acm.org/doi/10.1145/1060590.1060603) 
publié en 2005.
Et accrochez-vous, tout ne va pas être ultra simple.
En fait, si vous n'êtes pas à l'aise avec les corps finis et les matrices,
je vous invite à sauter à la section suivante de cette vidéo...

Et oui, un autre gros défaut du post-quantique,
c'est que c'est beaucoup plus complexe à comprendre que la cryptographie classique,
et donc beaucoup plus coûteux en termes de ressources humaines ;
et c'est d'ailleurs aussi bien plus coûteux en termes de ressources calculatoires,
notamment en termes de tailles des clés et des signatures cryptographiques...

L'idée de Regev, c'est en gros de remplacer l'opération $x = g^w$
par l'opération $x = G w$, 
où le clé privée $w$ un vecteur aléatoire de $n$ nombres modulo un nombre premier $p$,
où $G$ est une matrice aléatoire $G$ de taille $m \times n$,
contenant elle aussi des nombres modulo $p$,
et où l'aggrégation de la clé privée $w$ 
et de la matrice $G$ se fait par multiplication matricielle.

Alors, il y a une petite subtilité :
alors qu'Alice va utiliser $x_A = G w_A$ avec sa clé privée $w_A$,
Bob va lui utiliser $x_B = G^T w_B$ avec sa clé privée $w_B$.
Comme dans Diffie-Hellmann, $x_A$ et $x_B$ vont alors être rendus publics.
Dès lors, Alice et Bob pourront concevoir un secret partagé,
sous la forme de $s = x_B^T w_A$ calculable par Alice, 
qui est aussi égal à $s = w_B^T x_A$.
Et oui, en développant ces expressions, on se rend compte que $s = w_B^T G w_A$.
Autrement dit, on a créé le secret partagé 
en exploitant l'associativité de la multiplication matricielle,
d'où on tire une sorte de quasi-commutativité de la fonction $x = Gw$.

Si maintenant Bob veut envoyer le bit $b \in \{ 0, 1 \}$ à Alice,
il va alors envoyer $z = s + b$,
qu'Alice pourra aisément déchiffrer en retranchant le secret partagé $s$.

Bref, cette solution de chiffrement garantit un secret partagé,
lequel est ensuite exploitable pour communiquer de manière chifffrée.
Mais présenté comme je l'ai fait, il ne paraît pas franchement être si secret.
En particulier, la fonction qui calcule $x = Gw$ à partir de $w$
ne semble pas vraiment être à sens unique :
sachant $x$, on semble pouvoir récupérer $w$, 
en calculant $w = G^{-1} x$.
Pour cela, il faut bien sûr réussir à inverser la matrice $G$,
mais ça, c'est en fait très simple, 
par exemple via [l'algorithme de Gauss-Jordan](https://www.youtube.com/watch?v=Da7p1zWm5lM).
Et clairement, Regev s'en est bien rendu compte.
Mais alors, quelle astuce a-t-il introduit pour sécuriser ce protocole ?

Eh bien l'astuce, c'est d'ajouter volontairement des erreurs dans les calculs de $x_A$.
Ainsi, la vrai opération à sens unique, 
c'est celle qui consiste à calculer $x = G w + erreur$,
où erreur est un vecteur tiré au hasard et dont les paramètres sont très petits.
En fait, récupérer $w$ à partir d'une telle équation avec des erreurs,
y compris n'y arriver qu'avec une petite probabilité, 
tant que cette probabilité n'est pas négligeable,
c'est l'équivalent du problème du logarithme discret,
mais pour de nombreux protocoles de cryptographie postquantique.

On l'appelle le problème de l'apprentissage avec des erreurs,
ou learning with errors (LWE) en anglais.
Et ce qui peut paraître très perturbant pour les statisticiens parmi vous,
c'est que résoudre l'équation $x = G w + erreur$,
c'est pourtant un problème de base du machine learning :
comme j'en ai parlé dans une vieille vidéo,
c'est tout bêtement le problème de la régression linéaire,
que Laplace avait déjà étudié il y a deux siècles et demi !

Il y a toutefois deux petits détails, et pas des moindres.
D'un côté, on cherche ici des solutions qui sont des nombres entiers modulo $q$.
Et surtout, de l'autre, on ne dispose que d'inégalités modulo $q$.
Ça, ça fait en particulier que les méthodes classiques,
qui s'appuient sur la minimisation de la somme des carrés des erreurs,
vont ici échouer, parce que la somme des carrés des erreurs n'est plus une fonction convexe.

Bref. Certes il y a des ressemblances avec la régression linéaire,
mais on pense néanmoins que, contrairement à la régression linéaire,
le problème LWE est lui difficile.
Et surtout, on pense, ou en tout cas on espère, 
qu'il demeurera difficile y compris pour les superpuissances 
qui disposent de calculateurs quantiques.

OK... admettons que LWE soit difficile.
Il reste toutefois un problème : 
parce qu'on a introduit des erreurs dans les calculs des données publiques $x_A$ et $x_B$,
les calculs $s_A = x_B^T w_A$ et $s_B = w_B^T x_A$ ne vont plus coïncider !
Les secrets sont maintenant bien secrets, mais ils ne sont plus partagés !

En particulier, maintenant, le message chiffré envoyé par Bob va être
$z = s_B + b$. 
En développant l'expression de $s_B$, 
et en particulier de $x_A$ qui intervient dans le calcul de $s_B$, 
on obtient $z = w_B^T G w_A + w_B^T erreur + b$.

Alors, a priori, Alice ne peut pas calculer cette expression exactement,
car elle ne connaît pas $w_B$.
Elle ne connaît que $x_B$.
Cependant, si maintenant on oublie l'objectif de créer un secret partagé,
et si au lieu de cela on s'intéresse uniquement à l'envoi d'un bit chiffré de Bob vers Alice,
alors Bob n'a lui aucun intérêt à cacher $w_B$.
En particulier, on va supposer qu'il envoie $x_B = G^T w_B$,
autrement dit qu'il encode $w_B$ sans ajouter de bruit.
On se rend compte que $z$ s'écrit alors $z = x_B^T w_A + w_B^T erreur + b$.
En retranchant $x_B^T w_A$, qu'Alice peut tout à fait calculer,
elle obtient $z - x_B^T w_A = w_B^T erreur + b$.

Vous voyez ce qu'il se passe ?
Alice a presque récupérer $b$, à des erreurs près dans le calcul.
Eh bien, l'astuce final de Regev,
c'est de considérer des petits bruits ; après tout erreurs est généré par Alice même !
Et surtout, Regev va amplifier le signal.
Au lieu de rajouter un bit égal à 0 et ou 1,
il va rajouter en gros $b \times \lfloor p/2 \rfloor$,
c'est-à-dire que le signal va être maximalement large,
sachant qu'il est contraint d'être un nombre modulo p.

Et bien, cette fois, on y est !
On vient de comprendre comment envoyer un bit chiffré
à l'aide d'un chiffrement asymétrique résilient aux calculateurs quantiques.

Alors, notez que même en prenant des erreurs assez faibles,
comme elles doivent néanmoins être suffisamment grandes pour rendre
la fonction $x = G w + erreur$ difficilement inversible,
il peut arriver que le bruit $w_B^T erreur$ soit plus grand 
que le signal $b \times \lfloor p/2 \rfloor$,
ce qui implique alors que le déchiffrement de $b$ sera erroné.
Toutefois, le taux d'erreur peut être adjusté pour être extrêmement faible,
de sorte que la sécurité informationnelle du protocole soit très grande.
Et bien entendu, la sécurité peut être renforcée en ajoutant de la redondance.

Ceci dit, clairement, l'envoi d'un unique bit d'information est coûteux,
et il serait déraisonnable d'utiliser l'algorithme de Regev
pour chiffrer de longs messages.
Mais on peut alors l'utiliser pour créer un secret partagé :
il suffit à Bob d'envoyer un secret à Alice,
et ils pourront ensuite l'utiliser comme secret partager
pour communiquer par chiffrement symétrique,
avec des techniques dont on reparlera la prochaine fois,
et qu'on pense être également résilients aux calculateurs quantiques.


## Signature post-quantique

Dernière chose : la signature.

