# Le postquantique

Dans les vidéos précédentes, 
on a vu que la cryptographie moderne s'appuie à foison 
sur la création d'un secret $w$,
suivie de celle d'un problème $x$ dont $w$ est la solution.
Typiquement, dans le cas de l'exponentiation modulaire,
le problème $x$ est défini comme étant $x = g^w$ modulo $p$,
pour un grand nombre premier sûr $p$
et un nombre $g$ entre $2$ et $p-2$.
Dans le cas des courbes elliptiques, 
le problème $x$ est le point $X = w G$,
où $G$ est un point de la courbe elliptique 
et l'opération sous-jacente est l'opération de groupe commutatif
des points de la courbe elliptique.

Et si ces créations de problème sont si utiles à la cryptographie,
c'est avant tout parce que, dans les deux cas,
le calcul de $x$ est une fonction à sens unique :
il est facile à faire par n'importe quel citoyen muni d'un téléphone,
mais même la NSA et son réseau d'espions et de machines ne saura pas le défaire.
Mais ce n'est pas tout.
Ces fonctions à sens unique a de jolies propriétés algébriques,
comme le fait que $g^w \cdot g^v = g^{w+v}$,
ce qui revient à dire qu'on a là un morphisme de groupe,
ou le fait que $(g^w)^v = g^{wv}$,
qu'on appelle la quasi-commutativité.

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
c'est de détruire la cybersécurité qui s'appuie 
sur l'opération $x = g^w [p]$ ou sur l'opération $X = w G$.

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
et à cause de la publication scientifique des découvertes 
qui peuvent être récupérées par des superpuissances autoritaires,
ce n'est probablement qu'une question de temps, et peut-être même d'années,
avant que nos systèmes informatiques actuels ne soient plus protégés.

Et j'insiste sur le fait qu'on ne parle pas de jeu vidéo ici.
On parle de la cybersécurité de toute l'infrastructure informatique mondiale,
sur laquelle repose toute l'économie moderne,
mais aussi des [technologies de guerre comme des avions de chasse](https://tournesol.app/entities/yt:pCeRpEs9CJE),
et dont une paralysie prolongée ou ciblée serait une catastrophe.
Bref. Arrêtons de parler des calculateurs quantiques 
comme d'un truc aussi cool que Candy Crush.
On parle là d'une menace pour la sécurité nationale,
dans un contexte géopolitique déjà extrêmement tendu.

Bien sûr, ce constat, je suis très loin d'être le seul,
ou d'être même le premier, à l'effectuer.
En particulier, face à l'urgence de sécuriser le cyberespace 
contre les calculateurs quantiques,
les cryptographes se sont organisés.
Ils ont notamment développé la [cryptographie quantique](https://tournesol.app/entities/yt:kJFfleuDHrU).
Cependant, celle-ci requiert du matériel spécialisé,
et risque de ne pas être simple à déployer, surtout sur le court terme.

En tout cas, le National Institute of Standards and Technology,
le NIST, aux États-Unis, envisage une autre solution, 
qui repose sur le même principe que la cryptographie classique :
générer une clé privée $w$ et publier un problème difficile $x$ dont $w$ est solution.
Mais cette fois, bien sûr, il faut que le problème $x$ soit si difficile
que même une superpuissance armée de calculateurs quantiques
ne pourra pas le résoudre avant la fin de l'univers.

En août dernier 2024, le NIST a fait un énorme pas vers cet objectif,
en approuvant [un nouveau standard cryptographique](https://csrc.nist.gov/News/2024/postquantum-cryptography-fips-approved).
Ce standard, habituellement qualifié de post-quantique,
est un chiffrement qu'on espère être sécurisé contre les calculateurs quantiques.
Et je dis bien "on espère", car on ne dispose pas de garanties de sécurité.
En particulier, les cryptographes restent bien moins confiants vis-à-vis de la sécurité
de la cryptographie post-quantique contre les ordinateurs quantiques,
qu'ils ne sont confiants de la sécurité de la cryptographie pré-quantique 
contre les ordinateurs classiques.
Ou dit plus simplement, l'avènement des ordinateurs quantiques augmente
nos préoccupations de cybersécurité,
même dans l'hypothèse où on parviendrait à tout basculer au post-quantique du jour au lendemain ;
ce qui est également très loin d'être gagné !

En fait, quand, en avril 2024, 
un [chercheur chinois](https://eprint.iacr.org/2024/555.pdf) a partagé en preprint
un article intitulé "quantum algorithms for lattice problems",
la réaction n'a pas été un dédain pour un n+1-ième crack.
J'ai des amis à la Direction Générale de l'Armement qui m'ont raconté
avoir vécu une semaine très difficile,
occupée à rechercher une erreur quelque part dans les 60 pages de preuves de l'article.
Le risque, c'est que les solutions les plus prometteuses pour la cryptographie post-quantique
venaient d'être balayées d'un revers de la main.
Fort heureusement, 8 jours plus tard, une erreur fatale fut trouvée ;
enfin, quand je dis fort heureusement, c'est pour la cybersécurité post-quantique,
pas forcément pour le chercheur en question,
qui aura connu un sort qui n'est pas sans rappeler celui 
du [génial Gottlob Frege](tournesol.app/entities/yt:xqSKawORrPo).

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
et même si j'ai pas mal lu sur ce sujet récemment,
je dois dire que je ne maîtrise absolument pas les subtilités de ces protocoles.

Aujourd'hui, je vais me concentrer uniquement 
sur les propriétés fondamentales et les grands principes 
des protocoles de créations de secrets partagés
et de signatures cryptographiques à base de réseaux,
ou lattice-based cryptography en anglais,
qui ont été sélectionnés par le NIST.
Ou même plus précisément, 
on va étudier l'astuce fondamentale des algorithmes
qui s'appuient sur [l'article fondateur d'Oded Regev](https://dl.acm.org/doi/10.1145/1060590.1060603) 
publié en 2005.
Et accrochez-vous, tout ne va pas être ultra simple.
En particulier, si vous n'êtes pas à l'aise avec les corps finis et les matrices,
n'hésitez pas à prendre le temps de regarder ces quelques vidéos 
avant de prendre la suite de la celle-ci...

Et oui, un autre gros défaut du post-quantique,
c'est que c'est beaucoup plus complexe à comprendre que la cryptographie classique,
et donc beaucoup plus coûteux en termes de ressources humaines ;
et c'est d'ailleurs aussi bien plus coûteux en termes de tailles mémoires,
notamment en termes de tailles des clés et des signatures cryptographiques,
même si à l'inverse on a réussi à avoir des chiffrements rapides en temps de calcul...

L'idée de Regev, c'est en gros de remplacer les opérations $x = g^w$ et $X = w G$
par l'opération $x = G w$, 
où le clé privée $w$ est un vecteur secret de $n$ nombres modulo un nombre premier $p$,
où $G$ est une matrice publique $G$ de taille $m \times n$,
contenant elle aussi des nombres modulo $p$,
et où l'aggrégation de la clé privée $w$ et de la matrice publique $G$ 
se fait par multiplication matricielle.

La beauté de cette opération, 
c'est que le calcul de $x = G w$ reste un morphisme de groupe,
dans le sens où le problème associé à la somme des clés privées $w$ et $v$
est la somme des problèmes associées à ces clés,
c'est-à-dire $G(w+v) = Gw + Gv$.
On a donc l'une des trois propriétés nécessaires
pour concevoir des secrets partagés et des signatures cryptographiques.

Par contre, la quasi-commutativité, elle, ne tient pas.
Il n'est pas claire a priori de voir comment utiliser $x = Gw$ 
pour créer un problème à partir d'une autre clé $v$.
En particulier, l'expression $(Gw)v$ n'a pas de sens,
car $Gw$ n'est pas une matrice comme $G$.

Cependant, si vous connaissez l'algèbre linéaire, 
vous voyez peut-être une astuce pour néanmoins combiner $Gw$ et $v$.
Et oui, si $(Gw)v$ n'a pas de sens, on peut en donner à $(Gw)^T v$,
à condition que $v$ soit un vecteur à $m$ coordonnées.
En particulier, on peut noter que $(Gw)^T v = w^T G^T v = w^T (G^T v)$,
qui va alors être un nombre modulo $p$.

Eh bien, c'est précisément cette astuce qui est utilisée 
pour adapter Diffie-Hellmann au post-quantique.
En particulier, Alice va créer le problème $x_A = G w_A$ avec sa clé privée $w_A$,
Bob va lui utiliser $x_B = G^T w_B$ avec sa clé privée $w_B$.
Comme dans Diffie-Hellmann, $x_A$ et $x_B$ vont alors être rendus publics.
Dès lors, Alice et Bob pourront concevoir un secret partagé,
sous la forme de $s = x_B^T w_A$ calculable par Alice, 
qui est aussi égal à $s = w_B^T x_A$.
Et oui, en développant ces expressions, on se rend compte que $s = w_B^T G w_A$.
Autrement dit, on a créé le secret partagé 
en exploitant l'associativité de la multiplication matricielle,
d'où on tire une sorte de quasi-commutativité de la fonction $x = Gw$.

On a donc en gros maintenant 2 des 3 propriétés nécessaires 
pour concevoir un socle d'une cryptographie.
Il reste toutefois une 3e propriété à garantir, et qui est aussi la plus importante,
à savoir garantir que le calcul de $x = Gw$ est à sens unique,
si possible y compris contre des calculateurs quantiques.
Et là, en fait, clairement, ça ne marche pas.
La fonction qui calcule $x = Gw$ à partir de $w$
ne semble pas vraiment être à sens unique :
sachant $x$, on semble pouvoir récupérer $w$, 
en calculant $w = G^{-1} x$.
Pour cela, il faut bien sûr réussir à inverser la matrice $G$,
mais ça, c'est en fait très simple, 
par exemple via [l'algorithme de Gauss-Jordan](https://www.youtube.com/watch?v=Da7p1zWm5lM).
Et clairement, Regev s'en est bien rendu compte.
Mais alors, quelle astuce a-t-il introduit pour sécuriser ce protocole ?

> $G$ est même en général surdimensionné, 
de sorte que même l'observation partielle de $x$ suffit à reconstruire $w$ !

Eh bien l'astuce, c'est d'ajouter volontairement des erreurs dans les calculs de $x_A$.
Ainsi, la vraie opération à sens unique, 
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
comme j'en ai parlé dans une [vieille vidéo](https://tournesol.app/entities/yt:Ee8gLwVCPxg),
c'est tout bêtement le problème de la régression linéaire,
que Laplace avait déjà étudié il y a deux siècles et demi ! #Laplaaaaace

Il y a toutefois un détail important :
les solutions qu'on cherchent doivent être des nombres entiers modulo $p$.
Ça, ça fait en particulier que les méthodes classiques,
qui s'appuient sur la minimisation de la somme des carrés des erreurs,
vont ici échouer, 
notamment parce que la somme des carrés des erreurs n'est plus une fonction convexe.

Bref. Certes il y a des ressemblances avec la régression linéaire,
mais on pense néanmoins que, contrairement à la régression linéaire,
le problème LWE est lui difficile.
Et surtout, on pense, ou en tout cas on espère, 
qu'il demeurera difficile y compris pour les superpuissances 
qui disposent de calculateurs quantiques.
C'est en tout cas ce que sous-entend Regev 
dans son [article original](https://cims.nyu.edu/~regev/papers/qcrypto.pdf),
avec une note de bas de page qui dit 
"Si on me forçait à effectuer un pari, je dirais que la conjecture est vraie".

OK... admettons que LWE soit difficile.
Il reste toutefois un problème : 
parce qu'on a introduit des erreurs dans les calculs des données publiques $x_A$ et $x_B$,
les calculs $s_A = x_B^T w_A$ et $s_B = w_B^T x_A$ ne vont plus coïncider,
car $x_B$ n'est plus exactement $G^T w_B$, 
et surtout l'erreur qui y a été introduite ne coïncide pas 
avec celle ajoutée à $G w_A$ pour obtenir $x_A$.
Les secrets sont maintenant bien secrets, mais ils ne sont plus partagés !

Néanmoins, en développant les expressions,
on se rend compte que 
$s_A = w_B^T G w_A + w_A^T erreur_B$
$s_B = w_B^T G w_A + w_B^T erreur_A$,
et donc que la différence entre les deux est
$w_A^T erreur_B - w_B^T erreur_A$.
Si les erreurs sont suffisamment faibles,
même si $s_A$ et $s_B$ ne coïncident pas,
il y a de bonnes chances pour que $s_A$ soit proche de $s_B$.

Petit détail, pour garantir que le bruit $w_B^T erreur$ soit petit,
en plus d'exiger que les erreurs soient de petites tailles,
il faut que le $w_B$ soit petit lui aussi.
Rappelons que $w_B$ est un vecteur à $m$ coordonnées modulo $p$.
Pour garantir un petit $w_B$, 
Regev propose d'exiger que les coordonnées de $w_B$ soient égales à 0 ou 1,
et de prendre ces décisions entre 0 et 1 au hasard.

Cependant, même en réduisant l'erreur entre $s_A$ et $s_B$,
par conception même de ces valeurs à base d'erreurs pour garantir la protection des secrets,
Alice et Bob auront échoué à créer un secret vraiment partagé.
Est-ce que notre construction est un échec ?

Eh bien, l'astuce de Regev, 
c'est d'être moins ambitieux qu'un partage d'un secret partagé complexe.
En fait, on va simplement chercher à communiquer un seul bit secret, 
et faire en sorte qu'il sera très probablement partagé.
On va même faire plus simple encore,
et permettre à Bob de choisir le bit secret partagé,
puis à exploiter $x_A$ et $x_B$ pour l'envoyer à Alice.

Reprenons le protocole.
Cette fois, Alice et Bob tirent aléatoirement des secrets $w_A$ et $w_B$.
Puis il vont calculer et publier $x_A = G w_A + erreur_A$
et $x_B = G^T w_B + erreur_B$.
Bob va alors calculer $s_B = x_A^T w_B$,
et il sait qu'Alice (et seule Alice) saura calculer un nombre $s_A$ proche de $s_B$.
Maintenant, pour envoyer le bit secret $b=0$, 
Bob peut juste envoyer à Alice le nombre $z_B = s_B$.

Et à l'inverse pour envoyer le bit secret $b=1$,
Bob va envoyer un nombre $z_B$ le plus éloigné possible de $s_A$,
qui selon Bob, doit être environ $s_B$.
Quel est le nombre modulo $p$ le plus éloigné possible ?
Vous le voyez peut-être venir.
Pour envoyer le bit secret $b=1$, Bob va calculer $z_B = s_B + (p/2) [p]$,
puisque le nombre le plus éloigné de $s_B$ modulo $p$ est à distance $p/2$.
Alors, bien sûr, si $p$ est un grand nombre premier,
il n'est clairement pas pair,
et du coup $p/2$ n'est pas un entier.
Pour éviter ça, Bob va simplement prendre la partie entière de $p/2$,
et Bob va donc en fait envoyer $z_B = s_B + \lfloor p/2 \rfloor [p]$.

Pour reconstruire le bit envoyé par Bob,
Alice va simplement calculer la distance entre $s_A$ et $z_B$.
Si cette distance est inférieure à $p/2$, 
elle va deviner que le bit $b$ était $b=0$.
Dans le cas contraire, elle va reconstruire $b=1$.

J'insiste à nouveau sur le fait que, à cause des erreurs aléatoires,
le protocole de Regev ne garantit pas que la communication de $b$ sera correcte.
Il y a une tension entre ajouter suffisamment d'erreurs 
pour garantir que la construction est bien à sens unique,
et donc protégée des attaquants qui auraient acquis la connaissance de $x_A$, $x_B$ et $z_B$,
et rajouter trop d'erreurs,
ce qui conduirait $s_B$ à trop souvent diverger de $s_A$, 
et donc à des communications erronées du bit secret.

Il faut malheureusement faire des mathématiques assez poussées 
pour bien comprendre et optimiser ces compromis inévitables,
en invoquant par exemple un nombre premier $p$ suffisamment grand,
mais pas trop pour ne pas trop ralentir les calculs.
Fort heureusement, on dispose de codes de correction d'erreur.

En particulier, en répétant le protocole de Regev, 
c'est-à-dire notamment en tirant d'autres secrets $w_A$ et $w_B$,
et en exploitant l'algorithme de Reed-Solomon dont on parlé 
dans une [vidéo précédente](https://tournesol.app/entities/yt:VvXfarnn0N4),
des secrets partagés plus complexes peuvent être communiqués
avec des probabilités d'erreur quasi-nulles,
et typiquement ensuite utilisés pour du chiffrement symétrique,
comme ceux dont on parlera la prochaine fois.

On l'a fait !
On vient de comprendre comment communiquer de manière secrète
à l'aide d'un chiffrement asymétrique résilient aux calculateurs quantiques.

Alors, en pratique, on peut obtenir des solutions plus efficaces, 
en remplaçant les entiers modulo $p$
par des polynômes à coefficients modulo $p$,
et avec des propriétés comme $X^n$ qui se décompose en un polynôme de moindre degré,
on peut adapter l'algorithme de Regev
pour permettre l'envoi de plusieurs bits.
Lorsque $p$ est premier, l'ensemble de ces polynômes forme ce qu'on appelle un anneau fini.
Et si $p$ n'est pas premier, il forme un module ;
et cela suffit en fait à définir une méthode de chiffrement sécurisé.
On parle alors de Module-LWE, à la place du problème LWE défini initialement par Regev.

Et comme Regev a lui même démontré des liens très proches entre LWE
et les réseaux Euclidiens, qu'on appelle lattice en anglais,
on parle souvent de lattice-based cryptography,
ou cryptographie à base de réseaux Euclidiens.
Je ne vais pas rentrer dans plus de détails,
et je vais juste vous renvoyer vers cette [vidéo](https://www.youtube.com/watch?v=G23kfRJGH0k)
pour en savoir plus.

Quoi qu'il en soit, 
en utilisant Module-LWE pour permettre à Bob 
d'envoyer à Alice une clé partagée de chiffrement symétrique,
on obtient un mécanisme d'encapsulation de clé à base de LWE avec module,
qui est intimement lié aux réseaux euclidiens.
Et bien, c'est pour ça que le nom du protocole retenu par le NIST
n'est autre que "Module-Lattice-Based Key-Encapsulation Mechanism Standard".


## Signature post-quantique

Des protocoles de signature ont aussi été proposés.
Rappelons qu'Alice peut émettre la clé publique $x = G w + erreur$ à partir d'une clé privée $w$.
On va toutefois complexifier légèrement l'équation,
en considérant une clé privée $W$ qui est maintenant une matrice de taille $n \times k$,
ce qui donne une clé publique $X$ qui est de taille $m \times k$.
On a donc maintenant $X = G W + erreurs$, avec tout en majuscule.

Pour signer un message $m$,
Alice commence par prendre une fonction de hachage, et par calculer $c = H(m)$.
Le hash $c$ est ensuite transformé en un vecteur $C$ de dimension $k$ modulo $p$.
Ce qui est important, c'est que $C$ se calcule directement de $m$ par une fonction à sens unique.
Puis Alice peut signer le message $m$ en publiant $S = W C$.
N'importe qui peut alors vérifier la validité de la signature,
en calculant $G S - X C = G W C - G W C - erreurs = - erreurs$.
La signature sera alors considérée valide si $G S - X C$ est un petit vecteur.

Alors, là je n'ai donné qu'une idée très grossière de la signature cryptographique post-quantique,
qui s'appuie encore une fois sur l'associativité de la multiplication
dans le calcul de $G W C$.
En particulier, le secret $W$ peut être utilisé un coup à gauche pour révéler $X- erreurs = GW$,
et un coup à droite pour révéler $S = W C$.

Mais bien sûr, dans la version que j'ai présentée,
le protocole n'est pas sécurisé :
à partir de $S$ et $C$ en particulier, 
il peut être possible reconstruire $W$,
au moins en partie.

Pour sécuriser la signature post-quantique, 
il faut ajouter de nombreuses autres astuces,
comme une erreur dans le calcul de $S$.
En fait, le protocole Module-Lattice-Based Digital Signature Algorithm
retenu par le NIST pour la signature post-quantique
est nettement plus complexe que ce que j'ai présenté ;
même si son astuce fondamentale est bien l'associativité du calcul de $GWC$.

On peut toutefois souligner le coût en espace mémoire de cette solution.
Pour signer un message, 
Alice doit ainsi publier $G$ et $X$, qui sont maintenant des matrices,
ainsi que la signature $S$ qui est un vecteur.
Et dans le cas de l'algorithme ML-DSA approuvé par le NIST,
les coordonnées de ces objets doivent eux-mêmes être des polynômes
dont les coefficients sont pris modulo le nombre premier 8 380 417.
Là encore, il y a en fait d'autres astuces pour réduire la taille des signatures,
mais on obtient néanmoins des signatures de plusieurs kilo-octets,
ce qui est beaucoup plus gros que les signatures comme El Gamal ou EC-DSA,
qui sont typiquement une paire de nombres à 256 bits,
ce qui fait seulement 64 octets.

Notez enfin que le NIST a approuvé un troisième protocole postquantique,
appelée "StateLess Hash-Based Digital Signature Algorithm" ou SLH-DSA,
qui est une solution alternative de signature cryptographique,
cette fois fondée sur les arbres Merkel dont on reparlera plus tard dans cette série,
mais la taille des signatures générées est alors plus grande encore,
et excède rapidement les dizaines de kilo-octets.

Et en pratique, cette inflation de la taille des signatures,
ça peut être extrêmement coûteux quand il faut valider beaucoup d'authentifications de messages,
comme c'est le cas dans un de mes projets...


## Conclusion

Les calculateurs quantiques représentent une menace majeure pour la cybersécurité d'aujourd'hui,
et plus il y aura une hype injustifiée à leur sujet,
plus on verra des milliards de dollars d'investissement dans leur développement,
et plus on rapprochera le fameux Q-day,
ce jour où ces calculateurs quantiques pourront s'attaquer à l'état de sécurité 
des systèmes d'information déployés à très grande échelle.
Alors, bien sûr, il faut se méfier des effets d'annonce.
Non, contrairement à ce qui a pu être rapporté maladroitement dans certains médias,
la Chine n'a pas du tout réussi à "casser RSA" ;
des chercheurs prétendent uniquement avoir cassé des versions ridiculement simplistes
de la cryptographie.

Cependant, il ne faut pas non plus tomber dans le travers inverse,
qui consiste à fermer les yeux devant le développement technologique,
et imaginer que les calculateurs quantiques ne sont qu'une fantaisie de science-fiction.
Leur développement ne cesse de progresser.
Dès lors, il faut se préparer dès aujourd'hui 
pour éviter une catastrophe de cybersécurité dans le futur.
D'autant que les attaquants collectent déjà massivement des données chiffrées
par les protocoles actuels,
avec l'objectif de les déchiffrer aussi tôt 
qu'un calculateur quantique suffisamment grand et fiable leur sera accessible.
En particulier, ceci implique que, 
même si on parvient à déployer la cryptographie post-quantique à grande échelle à temps,
et même si cette cryptographie post-quantique 
est effectivement résiliente aux calculateur quantiques,
promouvoir l'informatique quantique,
c'est avancer le jour où des secrets industriels d'aujourd'hui seront découverts,
à une date où leur révélation aura davantage de conséquence,
que si cette révélation avait lieu dans un siècle.
Il me semble y avoir quelque chose de profondément immoral dans la recherche
sur le calcul quantique...

Et d'ailleurs, les conséquences négatives de cette recherche ne sont pas la seule raison
pour laquelle un excès d'investissement dans ce domaine serait éthiquement très discutable.
Nous vivons depuis une décennie déjà une période de l'histoire
où les technologies de l'information ont acquis un pouvoir monumental sur la santé des démocraties,
avec des conséquences déjà tragiques dans de nombreux pays 
comme le Myanmar, l'Éthiopie et le Soudan,
et des dégradations terrifiantes de l'intégrité de nombreux états démocratiques.

Dans ce contexte, donner de l'argent public à de la recherche 
qui n'est clairement pas vouée à protéger la population,
c'est exactement comme ignorer volontairement des urgences sociétales comme le changement climatique.
Pour protéger les démocraties, nous avons désespérément besoin
d'une recherche publique qui soit au service des démocraties ;
or les chercheurs d'aujourd'hui, y compris dans la fonction publique,
sont encore sous une pression terrible à suivre la hype,
plutôt qu'à travailler sur ce qui aura le plus de chance d'être d'intérêt général.

Si vous pensez que la recherche publique doit être beaucoup plus alignée avec l'intérêt général,
je vous invite en particulier à participer à notre projet Tournesol,
cette plateforme collaborative qui vise à encourager la recherche sur une démocratie numérique.
Que ce soit en promouvant le projet autour de vous,
en appelant les journalistes, les conférenciers et les chercheurs à s'y intéresser,
en contribuant vous-mêmes à la recherche ou au développement de la plateforme,
en fournissant des jugements sur la plateforme pour identifier plus de vidéos d'intérêt général,
ou en effectuant des dons à l'Association Tournesol,
vous pouvez nous aider à mettre des sujets démocratiques 
au centre des préoccupation de la recherche publique.

Merci beaucoup d'avance.

