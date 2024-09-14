# Qui est-ce ? (avec un mensonge !)

Imaginez une partie un peu spéciale du jeu "qui est-ce ?"
où chaque joueur a le droit de mentir une seule fois.
Prenons le cas particulier où vous avez 4 personnages possibles,
Sabine, Victor, Valentine et Jean-Lou.
L'autre joueur a l'un de ces personnages dans la main,
mais vous ne savez pas lequel.
Vous devez le déterminer, en posant uniquement des questions binaires.
Par exemple, vous pouvez demander : "le personnage est-il une fille ?"
Ou "le personnage a-t-il un micro ?".
Et l'autre joueur doit répondre par oui ou par non.

Sauf que contrairement au jeu classique,
le joueur adverse a un droit unique au mensonge.
Quel est le nombre minimal de question à poser
pour identifier avec certitude le personnage que l'autre joueur a dans la main ?
Je vous invite à mettre pause, et à essayer de répondre vous même à cette question.

En pratique, plutôt qu'un mensonge potentiellement malveillant,
les informaticiens doivent préserver l'intégrité de toutes sortes d'informations,
notamment lors de communications via la 4G qui ne passent pas toujours parfaitement,
lors du stockage à long terme des données sur des CD, des DVD ou des disques durs,
malgré des rayures ou des démagnétisations,
ou lorsqu'un QR Code imprimé est en partie arraché.

Le mensonge est ici davantage un accident.
Cependant, l'enjeu de préservation des données est parfois existentiel,
notamment pour des notaires, mais aussi des banques, des assurances ou des huissiers.
Dès lors il faut absolument envisager les pires cas,
et protéger les données autant que possible même dans ces cas.

Alors, si vous traînez sur le YouTube mathématique anglophone,
vous avez sans doute vu l'excellente vidéo de 3Blue1Brown
sur l'une des meilleures solutions de robustesse à la corruption des données,
puisqu'il a notamment traité le code de Hamming.
Mais aujourd'hui, on va voir un meilleur code encore,
un code même optimal,
à savoir le code de Reed-Solomon ;
même si le code de Hamming suffit amplement à résoudre le problème
du qui est-ce à 4 personnage et 1 mensonge...


## Exemple quadratique

Commençons par numériser l'information ;
il paraît qu'on fait souvent cela en informatique...
Imaginons par exemple qu'on cherche à encoder une message.
Le numériser revient à le transformer en une suite de nombres.
Les détails vont dépendre de l'encodage,
mais par exemple, en utilisant l'UTF-8,
tout message textuel peut être transformé en une suite de nombres
entre 0 et 255.

Par exemple, le mot "Lê" est encodé en UTF-8 par
la suite de 3 nombres m_1_ = 76, m_2_ = 195 et m_3_ = 170.
Comment maintenant puis-je encoder cette suite de 3 nombres,
de sorte que le code que j'obtiens soit résilient à des erreurs ?
Une solution naïve serait d'envoyer 3 fois chaque nombre.
Et donc, j'envoie (76, 76, 76, 195, 195, 195, 170, 170, 170).
Ça me fait 9 octets à envoyer ;
et en effet, s'il y a un octet erroné,
je saurai le détecter, et identifier sa bonne valeur.
Mais cet encodage est très coûteux.
Il requiert de tripler la quantité d'information envoyée.
Ne pourrait-on pas faire mieux ?

L'idée de Reed-Solomon est d'effectuer une autre transformation,
en remplaçant la suite m_1_, m_2_, m_3_ par le polynôme
P(X) = m_1_ + m_2_ X + m_3_ X²,
qui va donc ici être 
P(X) = 76 + 195 X + 170 X².

Si vous vous souvenez de vos cours de lycée,
on aime représenter par une courbe,
dont les points ont les coordonnées (X, P(X)), pour les réels X.
Et comme P(X) est un polynôme du second degré,
cette courbe est une parabole.
Mais surtout, on peut facilement se convaincre,
par exemple en jouant sur le site Desmos.com,
que deux courbes paraboliques sont identiques,
si et sulement si, 
elles sont définies par les mêmes nombres m_1_, m_2_ et m_3_.

Or une courbe parabolique peut être définie tout autrement aussi.
Prenez trois points de l'espace,
alors il existe en fait une et une seule parabole 
qui passe par ces trois points.
Et bien, on tient là l'astuce pour définir le code de Reed-Solomon.

L'idée va être de choisir non pas 3, mais 5 points désormais sur cette parabole,
par exemple les points (1, P(1)), (2, P(2)), (3, P(3)), (4, P(4)) et (5, P(5)).
En fait, si on se met d'accord au préalable qu'on enverra
les points dont les abscisses sont 1, 2, 3, 4 et 5,
il me suffit d'envoyer P(1), P(2), P(3), P(4) et P(5).

En l'occurence, en utilisant mon polynôme P(X) = 76 + 195 X + 170 X²,
ça me donne 441, 1146, 2191, 3576 et 5301.
Vous voyez pourquoi c'est génial ?

Imaginons qu'il y ait une erreur de transmission sur le point P(2),
Au lieu de recevoir 1146, je reçois 114. 
Le 6 est mal passé...

Si j'essaie de tracer la parabole qui passe par mes trois premiers points,
vous pouvez voir visuellement qu'elle va échouer à intersecter les 4e et 5e points.
En supposant qu'il y a au plus une erreur parmi les 5 points reçus,
et donc que le 4e ou le 5e point est forcément correct,
cela montre que j'ai reçu une erreur parmi les 3 premiers points.

On peut donc envisager 3 cas :
- interpoler les points 1, 2 et 4, et voir si ça coupe le point 5. C'est raté...
- interpoler 2, 3 et 4, et voir si ça coupe 5. C'est raté...
- interpoler 1, 3 et 4, et voir si ça coupe 5. Bingo, c'est gagné !
Grâce à l'envoi de 5 points, on a réussi à identifier l'erreur et à la corriger.


## Le cas plus général

Dans un cadre plus général, 
si on veut encoder un message (m_1_, m_2_, ..., m_k_) de longueur k,
on peut encoder le message par le polynôme
P(X) = m_1_ + m_2_ X + m_3_ X² + ... + m_k_ X^k-1^.
Mieux encore, si on veut s'autoriser t erreurs,
on peut envoyer k+2t valeurs du polynôme,
comme la suite P(1), P(2), ..., P(k+2t).
Grâce à l'ajout de 2t redondances,
on va pouvoir tolérer t erreurs.

Cette fois, étant donné les points P(1), P(2), ..., P(k+2t),
pour trouver le bon polynôme,
il faut en trouver un de la forme P(X) = m_1_ + m_2_ X + m_3_ X² + ... + m_k_ X^k-1^
qui passe par au moins k+t de ces points ;
un peu comme dans le cas k = 3 et t = 1 qu'on a traité plus tôt,
il nous fallait trouver une parabole qui passe par 4 points.

Par ailleurs, et c'est aussi très utile en pratique,
on va pouvoir tolérer la disparition de 2t données.
Typiquement, si vous avez laissé votre doigt sur le QrCode,
certaines information du QrCode auront disparu ;
et bien, si la fraction disparue est 2t/(k+2t), 
alors vous pourrez néanmoins lire le QrCode sans erreur !

OK, mais les plus perspicaces d'entre vous ont peut-être toutefois noté un problème.
Dans l'exemple que je vous ai donné, 
j'ai dû envoyer les nombres 441, 1146, 2191, 3576 et 5301,
qui sont en fait tous trop grands pour être inscrit dans un octet.
Et la situation risque d'être bien pire, 
si j'utilise des plus grandes valeurs de k.

Si vous avez vu la vidéo précédente,
vous devinez sans doute l'astuce à venir.
Il suffit d'effectuer les calculs de P(1), P(2), ..., P(k+2t),
non pas avec des nombres entiers,
mais avec des nombres d'un corps fini,
typiquement le corps fini F_2⁸_ à 256 éléments,
qui est particulièrement adapté à manipuler des octets.

En fait non, dans F_256_, comme dans tout corps fini à 2^n^ éléments, 
on a vu que 1 + 1 = 0.
Et donc P(2) = P(4) = P(0).
Donc ça ne marche pas de prendre les valeurs de P pour les valeurs 1, 2, 3...
Mais il suffit d'utiliser des éléments distincts du corps F_256_.
En pratique, il y a même de nombreuses autres astuces 
notamment pour faciliter les opérations de décodage ;
mais le principe global est le même... même si l'interprétation géométrique devient bancale.

Et oui, je vous ai expliqué Reed-Solomon de manière géométrique,
parce que c'est quand même plus sympa, et ça aide vraiment à comprendre ;
mais en fait, l'intuition géométrique ne tient que pour les nombres réels !
Fort heureusement, grâce à la géométrie algébrique,
qui est une sorte de dictionnaire de traduction entre la géométrie et l'algèbre,
toutes mes illustrations correspondent à des calculs très clairement définis.

En particulier, le mathématicien français Lagrange --- #Laplaaaace 
Non... non... Lagrange pas Laplace.
Ah ok...
Lagrange, donc, a résolu l'algèbre nécessaire pour identifier la parabole 
qui passe par n'importe quel triplets de points.
Ses solutions sont aujourd'hui appelés polynômes de Lagrange.

Eh bien, les polynômes de Lagrange, introduits 
pour calculer les polynômes qui passent par certains points
lorsqu'on considère des nombres réels,
sont algébriquement exactement les mêmes,
si on considère maintenant des nombres de corps finis.

Bref, pourvu qu'on sait multiplier et additionner correctement des octets,
en utilisant notamment les règles du nombre imaginaire k du corps F_256_,
on est capable de calculer des espèces de courbes de ces corps finis,
et de chercher en particulier une courbe associée à un polynôme,
qui intersecte k+t points parmis ceux qui nous ont été envoyés !


## Résolution du Qui Est-Ce ?

Appliquons maintenant tout cela au problème du Qui Est-Ce avec un mensonge.
Pour le résoudre, on va adapter une solution basée sur Reed Solomon.
En l'occurence, on va travailler non pas avec le corps F_256_, 
mais avec le corps fini F_3_ à trois éléments,
qui n'est autre que l'ensemble des entiers, 
avec l'égalité imposée 3 = 0.
Du coup, les trois éléments de F_3_ sont 0, 1 et 2.

Dans ce qui est-ce, comme il y a 4 personnages possibles,
on peut encoder l'identité du bon personnage par une suite de 2 bits.
Disons que Sabine est 00, Victor 01, Valentine 10 et Jean-Lou 11.
En particulier, chaque bit peut être vu comme un élément de F_3_ ;
donc le message à encoyer est ici une suite (m_1_, m_2_),
où m_1_ et m_2_ sont des éléments de F_3_,
dont on sait de surcroît qu'ils ne sont pas égaux à 2.

On peut alors construire le polynôme P(X) = m_1_ + m_2_ X.
Et on peut envoyer les valeurs P(1), P(2) et P(3).
Bon comme 3 = 0, ça revient à envoyer P(1), P(2) et P(0),
qui sont respectivement égaux à m_1_ + m_2_, m_1_ + 2 m_2_ et m_1_.
Notez que ces trois éléments sont des éléments de F_3_,
donc a priori il faut 2 bits pour les représenter.

En effet, on peut encoder l'élément 0 de F_3_ par 00,
l'élément 1 par 01 et l'élément 2 par 10.
Mais on va utiliser une astuce :
on sait que m_1_ est un élément de F_3_ forcément égal à 0 ou 1 ;
donc on peut convenir du fait qu'il sera envoyé par 1 bit.

Du coup, le nombre de bits envoyés sera égal à 2 bits pour m_1_ + m_2_,
2 bits pour m_1_ + 2m_2_ et 1 bit pour m_1_,
soit un total de 5 bits d'information.

On peut même être plus précis que cela.
À moins d'un mensonge, 
le premier bit sera égal à 1 si et seulement si m_1_ + m_2_ = 2,
ce qui revient à dire que m_1_ = 1 et m_2_ = 1,
ou dit autrement, ce sera le cas si et seulement si le bon personnage est Jean-Lou.
Donc il correspond à la question "As-tu Jean-Lou ?".

Le second bit sera égal à 1 si et seulement si m_1_ + m_2_ = 1,
ce qui sera le cas si le bon personage le code 01 ou 10 ;
ou dit autrement s'il s'agit de Victor ou Valentine.
Donc il correspond à la question 
"La première lettre du prénom du personnage est-il le V ?"

Le troisième bit sera égal à 1 si m_1_ + 2m_2_ = 2,
ce qui ne peut arriver que si m_1_ = 0 et m_2_ = 1.
Il correspond donc à la question
"Le personnage est-il Victor ?"

Le quatrième bit sera égal à 1 si m_1_ + 2m_2_ = 1,
ce qui ne peut arriver que si m_1_ = 1 et m_2_ = 0.
Il correspond donc à la question
"Le personnage est-il Valentine ?"

Enfin, le cinquième bit est égal à 1 si m_1_ = 1,
ce qui correspond à demander si
le personnage est Valentine ou Jean-Lou.

Telles sont les 5 questions binaires qu'on peut poser
pour récupérer exactement le code de Reed-Solomon.
Or on sait que s'il y a au plus une erreur parmi les 5 réponses,
ça va impliquer au plus une erreur 
dans la suite (P(1), P(2), P(3)),
ce qui ne nous empêchera pas de reconstruire le message initial.

En effet, il suffira de trouver la droite définie par 2 points

Et ça, ça veut dire

00 -> 00000
01 -> 01100
10 -> 01011
11 -> 10001

1 -> 00000
2 -> 00111
3 -> 11100
4 -> 11011

Distance de Hamming


## Reed-Muller


## Conclusion

