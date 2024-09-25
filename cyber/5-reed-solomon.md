# Qui est-ce ? (avec un mensonge !)

Imaginez une partie un peu spéciale du jeu "qui est-ce ?"
où chaque joueur a le droit de mentir une seule fois.
Prenons le cas particulier où vous avez 4 personnages possibles.
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

Et pour les plus motivés d'entre vous, 
je vous invite à considérer le cas de 16 personnages, 
sur lequel on reviendra plus tard dans cette vidéo.

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

Appliquons maintenant tout cela au problème du Qui Est-Ce 
avec 16 personnages possibles et un mensonge.

J'ai choisi celui-là en particulier,
parce qu'il s'adapte particulièrement bien à un encodage de Reed Solomon.
En l'occurence, on va travailler non pas avec le corps F_256_, 
mais avec le corps fini F_4_ à quatre éléments.
Souvenez-vous, les éléments de ce corps s'écrivent a + bk,
où a et b et sont éléments de F_2_, c'est-à-dire des bits,
et où k est un nombre imaginaire qui vérifie k² = 1 + k.
Pour simplifier les notations, on notera parfois ab le nombre a + bk.
On a ainsi les quatre nombres de F_4_ qui s'écrivent
00, 01, 10 et 11.

Dans ce qui est-ce, comme il y a 16 personnages possibles,
on peut encoder l'identité du bon personnage par une suite de deux nombres de F_4_,
qu'on va appeler m_1_ et m_2_.
Mis bout à bout ces deux nombres forment alors une suite de 4 bits.
Par exemple, dans cette correspondance à l'écran,
Thibaut correspond au code binaire 01 11,
qui correspond aux nombres m_1_ = k et m_2_ = 1 + k.

Ainsi, si le bon personnage était Thibaut,
en suivant le code de Reed-Solomon,
il faudrait communiquer le polynôme P(X) = m_1_ + m_2_ X,
qui serait dans ce cas égal à P(X) = k + (1 + k) X.
Et pour y arriver, on va donner des valeurs de ce polynôme en 4 points,
qui vont être les 4 valeurs possibles de X, en tant que nombre de F_4_.

Ces quatre valeurs seront alors 
P(00) = P(0) = k = 01
P(10) = P(1) = k + (1 + k) = 1 + 2k, 
Ça, ça se simplifie. En effet, dans F_4_, 2 = 0, et donc 2k = 0k = 0.
Du coup P(10) = P(1) = 1 = 10.
Ensuite, P(01) = P(k) = k + (1+k) * k = k + (k + k²) = 2k + (1 + k) = 0 + 1 + k = 11.
Enfin, P(11) = P(1+k) = k + (1+k) * (1+k) = k + 1 + 2k + k² = 1 + k + (1 + k) = 00.
Du coup, le code associé à Thibaut sera 01 10 11 00.

On peut faire les mêmes opérations avec tout le monde.
Je vous épargne les calculs.
Mais in fine, on obtient alors le tableau des encodages de Reed-Solomon suivants :

 '00 00': '00 00 00 00'
 '00 10': '00 10 01 11'
 '00 01': '00 01 11 10'
 '00 11': '00 11 10 01'
 '10 00': '10 10 10 10'
 '10 10': '10 00 11 01'
 '10 01': '10 11 01 00'
 '10 11': '10 01 00 11'
 '01 00': '01 01 01 01'
 '01 10': '01 11 00 10'
 '01 01': '01 00 10 11'
 '01 11': '01 10 11 00'
 '11 00': '11 11 11 11'
 '11 10': '11 01 10 00'
 '11 01': '11 10 00 01'
 '11 11': '11 00 01 10'

Et je voulais vraiment vous montrer ça, 
parce qu'il y a quelque chose de magnifique dans la liste des codes obtenus.
Pour commencer, on peut remarquer que, dans chaque colonne,
il y a autant de 0 que de 1.
C'est un signe que l'encodage a bien été optimisé ;
chaque bit envoyé, s'il n'est pas corrompu, a bien un bit d'information.

En particulier, on peut maintenant transformer les codes de 8 bits de Reed-Solomon
en une suite d 8 questions binaires.
Pour cela, pour le premier bit,
il suffit d'identifier toutes les lignes où le bit est égal à 1.
Ces lignes correspondent à une moitié des personnages.
Et bien, pour récolter l'information sur la valeur du premier bit du code de Reed-Solomon,
il suffit de demander si le personnage que l'autre joueur a en main
fait partie de cette moitié des personnages.
Si la réponse est oui, c'est que le premier bit du code de Reed-Solomon est égal à 1.
Sinon, il est égal à 0.
Et en faisant cela pour chaque bit du code de Reed-Solomon,
on peut alors récupérer ce code après 8 questions binaires.

Par ailleurs, à l'exception des codes de 00 00 et 11 11,
tous les codes obtenus ont exactement 4 valeurs 0, et 4 valeurs 1.
Mais surtout, le plus fou, 
c'est vraiment ce qu'il se passe quand on compare n'importe quelle paire de codes.
Prenons par exemple des codes associés à 01 10 et 11 01.
Ça nous donne les codes
01 11 00 10 et
11 10 00 01.
On peut alors compter le nombre de bits pour lesquels ses codes diffèrent.
On obtient 4.
On dit que la distance de Hamming entre les deux codes est égale à 4.

Et bien, ce chiffre n'est pas spécifique aux deux codes qu'on a sélectionnés.
Si on prend n'importe quelle paire de codes,
le nombre de bits dont ils diffèrent va toujours être 4 ;
à moins que les codes sont complètement opposés,
comme celui de 00 00 et celui de 11 00.

Dans le jargon, on dit que la distance de Hamming 
entre n'importe quelle paire de codes est supérieure ou égale à 4.
Et bien, je vous mets au défi de concevoir une liste de 16 codes de longueur 8
telle que la distance entre chaque paire est supérieure ou égale à 4,
sans invoquer la théorie des corps fini et le code de Reed-Solomon !
C'est assez fou ce qu'on a réussi.

Et d'ailleurs, cette distance de Hamming qui permet d'avoir un code robuste.
En effet, s'il y a une erreur sur un bit,
alors obtiendra le code corrompu ne sera qu'à une distance de Hamming de 1 
de l'un des codes valides de Hamming ; celui qu'il était avant l'erreur.
Mais il sera en revanche à une distance de Hamming au moins 3 de n'importe quel autre code !
Et oui, à la base il était à une distance 4,
et un changement d'un bit ne peut réduire cette distance que de 1.

D'ailleurs, on peut faire la remarque qu'il aurait suffi d'avoir des codes de Hamming
dont la distance de Hamming entre n'importe quelle paire de code est supérieure égale à 3,
pour garantir une reconstruction correcte avec au plus une erreur sur un bit.
Dans notre cas, avec une distance de Hamming d'au moins 4,
n peut faire la remarque que le code reste robuste malgré un changement de bit
et une perte de bit,
ce qui est un peu plus résilient encore !

D'ailleurs, si vous n'avez pas résolu le problème du Qui Est-Ce avec 4 personnage,
je vous invite à réfléchir à ces notions de codes de Hamming...

Allez, si vous êtes vraiment, vraiment en galère,
je vous ai mis un indice dans le script de cette vidéo,
dont le lien est en description :

Hint:
00000
00111
11100
11011


## Reed-Muller

Avant de conclure, j'aimerais vous dire quelques mots d'une variante du code de Reed-Solomon,
appelé le code de Reed-Muller.
L'idée, c'est qu'au lieu d'encoder un message m par un polynôme P à une variable,
le code de Reed-Muller va l'encoder dans un polynôme multilinéaire Q à plusieurs variables.
Autrement dit, Q doit avoir plusieurs variables, 
qu'on peut noter Z_1_, Z_2_, et ainsi de suite,
et quand on fixe toutes les variables sauf une,
on doit obtenir un polynôme de degré 1.

Si Q a q variables, alors il doit s'écrire comme une somme de termes
Z^h^ = Z_1_^h_1^ Z_2_^h_2^ Z_3_^h_3^ ... Z_q_^h_q^,
où h est une suite binaire de q bits.
Eh bien, l'idée est d'associer à chacun des termes de la sortes 
un coefficient m_h_ qui dépend du message m à encoder.
AUtrement dit, m est encodé par le polynôme multilinéaire à plusieurs variables
qui est la somme des m_h_ Z^h^.

Le code de Reed-Muller est obtenu en prenant les valeurs du polynôme Q
pour ses différentes entrées.
On peut ainsi vouloir travailler avec le corps fini F_2_ à deux éléments,
et donc considérer m_h_ égal à 0 ou à 1.
Le polynôme Q prend alors en entrée q variables binaires,
ce qui fait 2^q entrées possibles.
En publiant ses valeurs pour toutes ces entrées,
qui elles aussi seront binaires,
on obtient un code de Reed-Muller de longueur 2^q.

Il y a beaucoup de détails sur lequel je ne vais pas m'étendre pour aujourd'hui,
comme le fait de se restreindre au moment de la définition du polynôme Q
à un sous-ensemble des valeurs possibles de h 
typiquement en fonction du nombre de 1 dans la suite binaire h,
cependant ce que je veux simplement vous montrer aujourd'hui,
c'est qu'on peut naturellement généraliser les idées de Reed-Solomon 
pour les polynômes à une variable
à des solutions qui exploitent les polynômes à plusieurs variables.

Comme on le verra par la suite, ces polynômes à plusieurs variables,
dans lesquels résident tant de subtilités de la géométrie algébrique,
à l'instar du dernier théorème de Fermat,
sont des composants centraux de la cryptographie en général,
et des preuves à divulgation nulle de connaissance en particulier ;
notamment parce que la distance de Hamming entre les codes qu'ils génèrent
est souvent garantie d'être grande.


## Conclusion

J'aimerais conclure avec un semi mea culpa.
Face à l'urgence à résoudre les problèmes de nos sociétés,
en particulier l'amplification algorithmique de la désinformation et de la haine,
il m'arrive souvent de prendre à partie les sujets 
qui me semblent banaliser l'inattention à ces problèmes,
et qui me semblent donc dangereusement ralentir la mobilisation nécessaire
pour les résoudre, et protéger des vies et nos démocraties.
Et la géométrie algébrique est un exemple que je prends souvent
pour mettre en évidence l'énorme gachis d'intellects humains,
indispensables pour relever les grands défis d'aujourd'hui,
mais trop occupés à s'adonner à leurs passions artistiques.

Même si je savais déjà que cette géométrie algébrique avait des applications en cryptographie,
notamment pour concevoir des codes de correction d'erreur comme Reed-Solomon et Reed-Muller,
j'ai quand même pris une claque il y a quelques mois,
en découvrant à quel point elle est essentielle 
pour des solutions plus avancées de cryptographie
qui me semblent essentielles pour fermer l'espace informationnel européen 
contre les ingérences des entreprises et des gouvernements étrangers,
tout en permettant aux citoyens européens de profiter de ce cyberespace en toute sécurité,
et en particulier en toute confidentialité vis-à-vis de forces politiques internes
que ces citoyens devraient pouvoir ouvertement critiquer sans représailles.
On aura le temps d'y venir, mais oui, 
ces solutions semblent clé pour fournir des preuves de citoyenneté
avec divulgation nulle de connaissance,
capables de mimiquer les propriétés du vote à l'isoloir 
pour de nombreuses applications sur le web.
Décidément, les mathématiques ne cessent de me surprendre
par leurs nombreuses applications souvent inattendues.

Néanmoins, le fait que certaines parties de la géométrie algébrique 
aient des applications qui me semblent essentielles 
pour la protection des démocraties
ne signifie pas que toutes les recherches dans le domaine lui soit utiles.
Vu l'urgence démocratique,
il me semble en fait au contraire plus urgent que jamais
que les chercheurs qui ont les facultés mathématiques 
pour comprendre cette géométrie algébrique 
et pour l'appliquer à la protection des systèmes démocratiques le fassent.

En un sens, ces mathématiciens sont les Spiderman de l'âge moderne de l'information.
Leur faculté rare est un véritable superpouvoir,
ou du moins un pouvoir que beaucoup de militants pour la démocratie adoreraient avoir.
À ces mathématiciens, j'aimerais relayer la remarque de l'oncle de Spiderman :
"de grands pouvoirs impliquent de grandes responsabilités".

Nous avons désespérément besoin de sécuriser notre cyberespace.
Aidez-nous à y parvenir, pour le bien des démocraties.

