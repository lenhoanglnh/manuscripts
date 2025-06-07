# Prévisiblement imprévisible

La cybersécurité repose sur l'incapacité de cybercriminels puissants
à prédire des informations secrètes de nos systèmes d'information.
En particulier, comme on l'a vu dans la dernière vidéo,
de nombreuses solutions cryptographiques exigent de générer des nombres que 
même une superpuissance comme la NSA sera incapable de prédire.
Idéalement, il faudrait être mathématiquement assuré 
de l'incapacité de toute superintellygence à prédire les nombres aléatoires qu'on génère.
Dans le jargon, on parle de génération de nombres aléatoires cryptographiquement sécurisés.
Ces nombres doivent non seulement être imprévisibles pour nous ;
il doit surtout être prévisible qu'ils seront imprévisibles pour les superintellygences aussi.
Ils doivent être prévisiblement imprévisibles.

A priori, on pourrait se dire que c'est facile.
En tout cas nous autres humains,
on semble capable de dire des nombres que 
même notre moi du passé ne saurait pas prédire, non ?
Eh bien, ce n'est pas si évident.
En particulier, comme le montre 
cette [excellente vidéo de Veritasium](https://tournesol.app/entities/yt:d6iQrh2TK98),
nous autres humains avons tendance à prédire certains nombres 
qui nous paraissent plus aléatoires,
lorsqu'on nous dit de dire un nombre au hasard,
comme 7 s'il faut dire un nombre entre 0 et 9,
ou 37 quand il faut dire un nombre entre 0 et 99.
Ainsi s'il fallait casser un protocole qui utilise un nombre aléatoire généré par un humain,
alors on pourrait commencer par tester le cas où ce nombre est 7 ou 37,
et on aurait plus de chances de réussir,
que si on utilisait à la place un meilleur générateur de nombre aléatoire.
Nous autres humains sommes prévisiblement pas si imprévisibles...

En fait, être prévisiblement imprévisible, ce n'est vraiment pas évident.
En pratique, beaucoup de générateurs de nombres aléatoires
ne sont en fait pas *cryptographiquement* sécurisés.
Par exemple, le module `random` de python n'est pas cryptographiquement sécurisé,
comme vous pouvez vous en rendre compte en lisant 
la [documentation du module](https://docs.python.org/3/library/random.html).
Autrement dit, si vous utilisez le module `random` de python,
un attaquant qui observe les nombres que vous générez pourra finir
par deviner les prochains nombres générés, 
qui n'auront alors plus aucune prévisibilité pour lui.
L'aléatoire `random` de python est en fait prévisiblement prévisible.

En pratique, dans certains protocoles à haut enjeu,
on va exploiter des capteurs de température ou des mesures de lampes lava,
et en particulier la théorie du chaos dans des systèmes physiques complexes,
pour être aussi prévisiblement imprévisible que possible.
Mais même là, on va généralement combiner cette graine d'aléatoire
pour ensuite générer d'autres nombres aléatoires, 
sans avoir accès à des capteurs extérieurs.
Comment fait-on pour être alors algorithmiquement prévisiblement imprévisible ?
N'est-ce pas là un oxymore ?
N'y a-t-il pas là une contradiction dans les termes ?

Aujourd'hui, on va voir les solutions aujourd'hui considérées standards,
notamment AES-CTR\_DBRG et SHA-256,
qu'on pense être des algorithmes prévisibles imprévisibles,
y compris selon les standards élevés de la cryptographie.
Et comme on va le voir, 
les applications de cette faculté à être prévisiblement imprévisible 
sont nombreuses ;
on retrouve ces algorithmes aussi bien 
dans le calcul d'empreintes cryptographiques
que dans le chiffrement symétrique, parmi de nombreux autres exemples.
En fait, le coeur de la cybersécurité aujourd'hui,
ce sont vraiment ces opérations prévisiblement imprévisibles.

> Étymologiquement, le mot cybersécurité vient du grec kubernân,
> qui signifie « gouverner ».
> D'une certaine manière, la cybersécurité, 
> c'est vérifier que l'espace informationnel est gouverné
> tel que nous souhaiterions qu'il le soit.
> Sauf que, en pratique, dans tous les pays francophones, 
> on peut considérer qu'il y a énormément de défauts de gouvernance
> de notre espace numérique,
> comme le montre d'ailleurs très bien la [commission d'enquête](https://www.senat.fr/travaux-parlementaires/structures-temporaires/commissions-denquete/commission-denquete-sur-les-couts-et-les-modalites-effectifs-de-la-commande-publique-et-la-mesure-de-leur-effet-dentrainement-sur-leconomie-francaise.html)
> sur la commande publique présidée par le sénateur Simon Uzenat en France.
> Sachant que la loi FISA et le Patriot Act en vigueur outre-Atlantique
> permettent aux autorités américaines d'accéder à des données de non-américains
> stockées sur le territoire étatsuniens, 
> il y a urgence à investir dans une autonomie numérique.
> Et c'est justement ce que vous propose Infomaniak, le sponsor de cette vidéo.
> Je vous invite en particulier à vous intéresser à kDrive, 
> la solution de stockage en ligne d'Infomaniak, 
> une entreprise suisse 100% indépendante
> qui fait un effort majeur pour tout développer de manière souveraine. 
> Vous pouvez profitez de my kSuite, 
> leur offre gratuite qui inclus une adresse email ainsi que kDrive,
> qui sont des alternatives souveraines à Gmail et Google Drive.
> Je vous encourage à tester leur offre gratuite et si vous êtes convaincu, 
> j'ai pour vous le code promo SCIENCE80 pour passer à la mise à niveau payante,
> et profiter d'un rabais de 80% sur l'offre 1 To pendant la première année.
> Retrouvez le lien en description.
> Pour chaque vidéo où je les promeus, ce que je fais avec grand plaisir, 
> Infomaniak reverse un don à l'Association Tournesol. 
> Merci beaucoup à eux pour ce partenariat.


## Le chiffrement de bloc

L'ingrédient de base 
de nombreuses solutions cryptographiques est le chiffrement de bloc,
ou *bloc cipher* en anglais.
L'idée est de définir une fonction qui prend en entrée 
une suite de bits de longueur fixée, qu'on appelle aussi un bloc,
et qui sort un bloc de même longueur.
De plus, la transformation va être paramétrée par une clé secrète.

On exige généralement que, pour n'importe quelle clé,
deux blocs différents en entrée
soient transformés en deux blocs différents en sortie.
Autrement dit, on évite les collisions en sortie,
pour éviter que certaines sorties soient plus fréquentes que d'autres.
En termes techniques, pour toute clé, 
le chiffrement de bloc doit définir une permutation 
de l'ensemble des blocs.
Cette propriété très utile pour maximiser 
de manière prévisible l'imprévisibilité de la sortie
sera d'ailleurs *essentielle* pour le chiffrement symétrique.

Dans les années 1970, un chiffrement de bloc appelé DES a été proposé, 
et a ensuite été érigé en standard ;
mais la sécurité de cette solution fut montrée insuffisante,
à la fois parce qu'elle utilisait des clés de chiffrement à seulement 56 bits,
ce qui ne fait que $2^{56} ≈ 10^{17}$ clés possibles seulement,
mais aussi parce qu'il y avait des moyens de court-circuiter une partie du calcul.
En 1999, [la *Electronic Frontier Foundation* a ainsi montré comment casser un chiffrement DES en à peine 22 heures](https://w2.eff.org/Privacy/Crypto/Crypto_misc/DESCracker/HTML/19980716_eff_des_faq.html).

Bref. On pourrait croire qu'il suffit de faire un peu n'importe quoi 
avec les blocs de bits pour générer du hasard ;
mais être prévisiblement imprévisible n'est pas si évident !
Cet exemple montre par ailleurs ce qu'on entend vraiment par "imprévisibilité" :
on ne cherche en fait pas à être imprévisible au sens de 
[Solomonoff et du bayésianisme](https://tournesol.app/entities/yt:t4X6BWjr_do).
Il s'agit d'être imprévisible contre des 
["bayésiens pragmatiques"](https://tournesol.app/entities/yt:lXRVZP-tUzw),
c'est-à-dire contre des algorithmes limités en puissances de calcul.
Autrement dit, il s'agit d'être sécurisé contre 
des [la NSA](https://tournesol.app/entities/yt:v_sz0elq0eo),
mais pas contre le [démon de Solomonoff](https://tournesol.app/entities/yt:6N0dlorL0r8).

De nos jours, le chiffrement de bloc le plus standard est AES avec 256 bits,
qui opère sur des blocs de 128 bits, avec une clé qui fait également 256 bits.
Les détails d'AES ne sont pas particulièrement passionnants,
mais je vais quand même vous en dire quelques mots,
notamment parce que ses opérations sont un peu analogues 
aux calculs des réseaux de neurones.

> Il y a en fait 3 modes de fonctionnements d'AES,
avec respectivement 128, 192 et 256 bits.
Mais ici je ne parlerai uniquement que du cas avec 256 bits.

Pour comprendre la construction d'AES, 
il est utile de voir les suites de 128 bits en entrée
comme des suites de 16 paquets de 8 bits.
Chaque paquet de 8 bit est alors appelé un octet.
On parle aussi de *byte* en anglais.

> Techniquement, un *byte* n'est pas nécessairement un octet,
mais ce sera généralement le cas en pratique.

Mieux encore, chaque octet définit un nombre du corps fini à $2^8 = 256$ éléments.
J'ai parlé de ces corps finis dans une [vidéo précédente](https://tournesol.app/entities/yt:kkU8u6IWrVs).
Mais tout ce que vous avez besoin de savoir pour aujourd'hui,
c'est qu'on peut définir des opérations d'additions et de multiplications
entre les octets,
et que ces opérations sont inversibles,
dans le sens où on peut aussi effectuer des soustractions et des divisions,
à l'exception de la multiplication et de la division par zéro.
Du coup, on peut remarquer que toute fonction affine $P(x) = ax + b$,
où $a$ et $b$ sont constantes dans le corps fini avec $a$ non nul,
définit une permutation de l'ensemble des octets.
C'est donc a priori un très bon candidat pour être un chiffrement de bloc.

Alors, pas tout à fait, car on a vu que le bloc AES prenait en entrée,
non pas un octet, mais 16 octets.
Bien sûr, on pourrait effectuer une transformation affine différente à chaque
octet du bloc d'entrée d'AES.
Mais si vous connaissez l'algèbre linéaire, 
vous voyez peut-être comment faire mieux.
Si on voit la suite de 128 bits comme un vecteur de 16 octets,
on peut définir des fonctions linéaires à l'aide de matrices.
Formellement, si on définit $f(X) = AX + B$,
où $A$ est une matrice de 16 x 16 octets,
où $B$ est une suite de 16 octets,
et où $X$ représente les 16 octets qui forment le bloc en entrée,
pourvu que $A$ est ce qu'on appelle une *matrice inversible*,
alors $f$ définit ainsi une permutation des suite de 128 bits.

> Le cas où on fait des transformations affines par octet
correspond au cas où $A$ est une matrice diagonale
à coefficients diagonaux non nuls.

Bingo ! En construisant $A$ et $B$ à partir de la clé secrète,
on semble tenir là une solution à notre sélection d'une permutation aléatoire, non ?

Eh bien, il y a un petit problème avec les fonctions linéaires.
En effet, pour déterminer la fonction $f$,
il suffit de connaître sa valeur en un petit nombre de points.
Ainsi, si un attaquant parvient à connaître à la fois $X$ et $f(X)$,
alors il saura que $AX + B = f(X)$,
ce qui correspond à une équation linéaire en les coefficients secrets $A$ et $B$.
On peut même dire que c'est un système de 16 équations,
puisqu'il s'agit d'une égalité entre des vecteurs de 16 octets ;
et qu'il a au plus $16 \times 16 + 16 = 272$ inconnues.
En particulier, il suffit de 17 observations $(X, f(X))$
pour garantir une reconstruction des secrets $A$ et $B$,
via des algorithmes très rapides 
comme le [pivot de Gauss-Jordan](https://tournesol.app/entities/yt:17UAULAknyQ).
Autrement dit, si une superintellygence observe environ 17 nombres générés,
alors le chiffrement linéaire sera cassé.

> Si ces coefficients sont eux même des fonctions linéaire 
> d'une clé secrète `K` à 256 bits, soit 32 octets,
> alors on peut même écrire l'équation sous la forme $X^T A_0 K + B_0 K = f(X)$.
> C'est un système linéaire à 16 équations à 32 inconnues.
> Si on observe maintenant $X_1$, $f(X_1)$, $X_2$ et $f(X_2)$,
> alors on a déjà de quoi permettre reconstruire $K$ après 2 observations !

Mais donc, comment augmenter la sécurité de notre génération de blocs ?
Alors, vous pourriez vouloir échanger des octets,
et les additionner entre eux ;
mais toutes ces opérations sont en fait elles aussi linéaires.
Et qui plus est, combiner tout plein d'opérations linéaires,
eh bien, ça reste une opération linéaire.
Non, si on veut aller au-delà du $AX+B$, il va falloir une autre astuce.
Vous l'avez trouvée ?

Eh bien, une autre permutation qu'on peut définir pour un octet,
c'est celle qui consiste à remplacer tout octet $x$ par son inverse $1/x$,
à l'exception du $0$ qu'on laisse inchangé.
Cette opération est bien une permutation,
puisqu'on peut l'inverser en réeffectuant la même opération ;
et oui, $1/(1/x)) = x$.
Eh bien, AES, en gros c'est ça.
C'est une succession de 14 transformations linéaires définies par la clé secrète,
avec des inversions des octets intercalées entre ces transformations linéaires.
Alors, en pratique, ce ne sont pas exactement des inversions,
notamment pour éviter des points, mais c'est en gros des inversions.
Par ailleurs, dans AES, la clé secrète suit elle aussi des transformations linéaires
et des opérations d'inversions d'octets,
pour définir la suite des matrices $A$ et des vecteurs $B$
qui seront appliqués aux 16 octets ;
de sorte que même une superintellygence 
qui parviendrait à accéder à des millions d'observations $(X, f(X))$
aura le plus grand mal à identifier les clés secrètes du chiffrement AES,
et donc à reconstruire la fonction de permutation utilisée.

Si vous avez vu ma vidéo sur les transformeurs,
ou si vous connaissez les réseaux de neurones,
il y a là une analogie évidente avec ces solutions au machine learning.
Dans les deux cas, il s'agit de bidouilles non-linéaires,
avec entre chaque bidouille non-linéaire une transformation linéaire.
En particulier, ces opérations ont le don d'être largement parallélisables,
[sans l'être complètement](https://tournesol.app/entities/yt:g_u8YWpe4BM).

Ainsi, AES définit ainsi une opération qui prend en entrée un bloc $X$ de 128 bits
et une clé $K$ de 256 bits, et qui sort un bloc $Y$ de 128 bits.
On peut ainsi écrire $Y = AES(X, K)$.
Et si on prend une clé `K` parfaitement inconnue d'une superintelligence,
alors aux yeux de celle-ci, 
AES effectue une permutation essentiellement imprévisble
de l'ensemble des blocs de 128 bits,
surtout si on suppose de surcroît 
que la superintellygence reste calculatoirement limitée.

Enfin, plus exactement, c'est ce qu'on suspecte fortement.
Malheureusement, démontrer mathématiquement la sécurité d'AES reste un problème ouvert ;
en fait on n'arrive même pas à démontrer qu'il existe des fonctions
de hachage cryptographiques,
c'est-à-dire des solutions au problème de la conception d'algorithmes prévisiblement imprévisibles,
notamment parce que c'est un problème plus dur en quoi mathématiquement
que de prouver que P est différent de NP,
pour lequel il y a un prix d'un million de dollars du Clay Math Institute,
dont aucun mathématicien n'a encore su se saisir.
Eh oui, quand on dit être prévisiblement imprévisible,
c'est vis-à-vis de supercalculateurs dont la puissance de calcul est limitée,
ce qui est très proche des considérations de 
[P versus NP](https://tournesol.app/entities/yt:AgtOCNCejQ8).

Néanmoins la sécurité d'AES, y compris contre les calculateurs quantiques,
c'est peut-être la conjecture non démontrée la plus fiable de la cybersécurité,
ne serait-ce que parce que cela fait désormais un quart de siècle
qu'on échoue à la casser.
Voilà pourquoi on s'est appuyé sur AES depuis pour 
le hachage, le chiffrement symétrique et la génération de nombres aléatoires.


## Les fonctions de hachage SHA-2

Voyons comment utiliser AES pour définir 
des fonctions de hachage cryptographiquement sécurisées,
dont je vous avais parlé dans une 
[vieille vidéo sur String Theory FR](https://tournesol.app/entities/yt:rO5aQzgKOs0).
Souvenez qu'une propriété fondamentale de telles fonctions de hachage,
c'est d'être des fonctions à sens unique en un sens fort :
autrement dit, sachant la sortie,
il doit être impossible pour une superintellygence 
de deviner quoi que ce soit à propos de l'entrée mieux que le hasard,
à cause de ses limites en puissances de calcul.

Pour garantir cette propriété, le bloc AES a un léger défaut :
si on connaît la clé $K$ et le bloc de sortie,
alors on peut reconstruire le bloc en entrée.
Ainsi, quand la clé parvient à être identifiée, 
AES génère une sortie informative vis-à-vis de son entrée.
Pour être davantage prévisiblement imprévisible,
les informaticiens Merkle et Damgård ont proposé d'utiliser 
des clés K beaucoup plus longues.
On va ensuite décomposer K en une suite de blocs $K_1, K_2, ..., K_N$,
chacun étant de longueur 256 bits.
Puis, l'idée est de partir d'un bloc initial $X_0$ à encoder,
et de les ré-encoder itérativement par les clés $K_1, K_2, ..., K_N$.
Autrement dit, on pose $X_{n+1} = AES(X_n, K_n)$.
En bout de ligne, $X_{N+1} = MerkleDamgård (AES, X_0, K)$ 
sera le résultat du hachage
par construction de Merkle-Damgård.

Eh bien, c'est en gros sur ce principe qu'est fondé
l'un standard qu'on considère être le plus sécurisé,
à savoir les fonctions de hachage de la famille SHA-2,
et en particulier une fonction comme SHA-256.
Et pour cause, c'est elle qui est utilisée pour le Bitcoin,
de sorte que, en cassant SHA-256, 
vous pouvez "légalement" gagner des milliards de dollars.
Bon, je mets "légalement" entre guillement,
car ce sera légal selon les normes du Bitcoin ;
mais le statut légal du Bitcoin est une autre et vaste question.
Bref, vu les incitatifs monumentaux à casser SHA-256,
l'absence de hacks effectifs est un indicateur très convaincant
de l'absence de hacks tout court.

Notez que d'autres fonctions de hachage ont été introduites,
notamment la famille de fonctions SHA-3.
Cependant, leur vocation n'est pas nécessairement de remplacer SHA-2.
IL s'agissait plus de proposer une solution fondée 
sur des principes radicalement distincts,
pour anticiper l'éventualité où SHA-2 serait cassée.
On n'oublie surtout pas le principe de défense en profondeur en cryptographie !

Alors, pour être plus précis, 
SHA-256 utilise un autre chiffrement de bloc que AES,
qui est composée de 64 opérations linéaires plutôt que 14,
avec bien sûr là encore des opérations non-linéaires intercalées.
Par ailleurs, les blocs de SHA-256 sont constitués de 512 bits plutôt que 128.
Enfin, l'opération non-linéaire utilisée est davantage la rotation,
c'est-à-dire remplacer par exemple la suite de bits 1000 par 0001,
en faisant glisser le bit à gaucher vers la droite.
Et il y a par ailleurs d'autres précautions à prendre,
notamment vis-à-vis du choix des constantes des transformations linéaires,
ou vis-à-vis du préformatage des données à hacher
pour qu'elles se décomposent bien en suites de 512 bits.

> La fonction de chiffrement de bloc de SHA-256
fait en fait intervenir deux sortes différentes d'addition,
une addition dans le corps F_2^32^_ qui revient à prendre le XOR,
et une addition dans l'anneau Z_2^32^_ qui requiert des retenues.
Dans les deux cas, l'addition d'une constante définit une permutation
des suites de 32 bits.

> En pratique, SHA-256 utilise la transformation de Davies-Meyer
pour définir le chiffrement de bloc,
qui a pourtant le défaut de ne pas conduire à une permutation.
Ceci dit, personne jusque là n'a su exploiter les mauvaises propriétés
de cette transformation pour casser SHA-256.

Quoi qu'il en soit, ce faisant,
SHA-256 prend n'importe quelle suite de bits de n'importe quelle taille en entrée,
et ressort ensuite une suite de 256 bits,
qui même pour une superintellygence,
sont aucunement informative sur la nature de l'entrée,
bien que l'entrée détermine entièrement cette sortie.

Et en fait, en pratique, la sécurité de nombreux protocoles 
dépend beaucoup plus encore de la sécurité de SHA-256,
et en particulier la difficulté d'inverser cet algorithme,
que des autres aspects dont on a parlé dans cette série de vidéos,
tout simplement parce que SHA-256 est vraiment beaucoup utilisé.
Et pour le coup, on pense que SHA-256 est post-quantique,
dans le sens où même les superpuissances dotées de calculateurs quantiques
seront incapables d'inverser cette fonction de hachage.

Plus formellement, la sécurité de SHA-256 dépend de 2 propriétés légèrement distinctes.
La première, c'est qu'étant donné un hash $h$ pris au hasard,
aucun algorithme ne doit pouvoir trouver un message $m$
dont le hash est $SHA256(m) = h$ en temps raisonnable.
On parle de résistance aux attaques par préimage.

La seconde, c'est qu'aucun algorithme ne doit pouvoir trouver
deux messages différents $m_1$ et $m_2$ qui ont le même hash,
c'est-à-dire tels que $SHA256(m_1) = SHA256(m_2)$,
à moins d'y passer un temps complètement déraisonnable.
On parle de résistance aux attaques par collision.

> NB: Formellement, on doit admettre que l'algorithme adversaire 
peut avoir des énormes coups de chance, 
mais ces coups de chance doivent avoir une probabilité extrêmement faible.
Par ailleurs, plutôt que de SHA256, on formalise habituellement
ces propriétés de manière asymptotiques :
on considère plutôt une famille de fonction de hachage 
$f_k : \{0, 1\}^* \to \{0,1\}^k$.
Le temps de calculs des adversaires doit alors être polynomial en $k$,
et la probabilité de coups de chance inférieure à toute fonction polynomiale de $k$.

Et si, en théorie, on ne dispose pas de preuves de résistance de SHA256
contre les attaques par préimage et par collision,
deux décennies et demi de pratique ont convaincu les cryptographes
que cette résistance était suffisamment probable
pour que toute l'économie mondiale repose dessus.
En tout cas, les experts sont tous convaincus que 
les principales vulnérabilités des systèmes d'information ne résident pas
dans SHA256.


## Le chiffrement symétrique CBC

Passons maintenant au chiffrement symétrique.
Vous vous souvenez peut-être que, dans la vidéo précédente,
on avait vu comment les courbes elliptiques permettent 
à deux interlocuteurs Alice et Bob de constituer un secret partagé $S$,
sans qu'aucune superintellygence ne soit capable de deviner ce secret $S$,
y compris après avoir intercepté tous les échanges
qui ont permis à Alice et Bob de constituer ce secret.
Cette solution est appelée algorithme de Diffie-Hellman,
et si vous ne vous rendez pas compte de la magie qu'il opère,
je vous invite à aller voir la vidéo de Science Étonnante qui l'explique très bien.

OK, mais avoir un secret partagé $S$,
ce n'est pas tout à fait l'objectif d'Alice et Bob.
Ce qu'ils veulent, c'est surtout pouvoir envoyer des messages
sans que la superintellygence ne puisse les lire.
Eh bien, pour y arriver, 
on va d'abord transformer le secret partagé $S$ 
en une clé de chiffrement $K$,
à l'aide d'une fonction de hachage ;
comme typiquement SHA-256.
D'ailleurs avec SHA-256, Alice et Bob obtiendront une clé de 256 bits,
ce qui correspond exactement à la longueur nécessaire pour AES.

Maintenant, imaginons qu'Alice souhaite envoyer un message $M$ à Bob,
en chiffrant le message avec la clé de chiffrement partagée $K$.
Comment peut-elle s'y prendre ?
Bien sûr, on peut commencer en transformant $M$ en une suite de bits,
comme vos machines le font à longueur de journée.
Cependant, cette suite peut avoir un nombre arbitraire de bits,
alors que AES ne peut avoir en entrée que 128 bits.
Clairement, il va nous falloir découper $M$ en une suite de blocs de 128 bits.
Supposons que $M$ est un énorme fichier,
de sorte que son code binaire est une suite d'un million de blocs de 128 bits.
Comment utiliser la clé $K$ à 256 bits 
pour chiffrer cette énorme suite de blocs ?

Si on y va bêtement, en utilisant AES indépendamment pour chaque bloc,
alors on va risquer malheureusement de révéler des informations.
Par exemple, s'il s'agit d'un chiffrement de textes, ou de pixels dans une image,
alors il arrive souvent que des blocs de 128 bits sont en fait identiques,
et ils vont alors être transformés en codes chiffrés identiques.
Voilà des indices intrusifs que pourra utiliser la superintellygence,
un peu comme ceux utilisés par Turing pour casser les codes Nazis
pendant la seconde guerre mondiale.

Une solution pour mieux chiffrer les données est le chiffrement pas chaîne de blocs,
appelé *cipher block chaining* ou CBC en anglais.
Et non ce n'est pas vraiment lié à la fameuse Blockchain.
L'idée, c'est qu'au lieu d'utiliser en entrée le bloc de 128 bits à chiffrer,
on va utiliser sa somme avec la sortie du bloc précédent.
Comme le chiffrement de chaque bloc est difficilement prévisible,
l'entrée du chiffrement du bloc suivant le sera aussi,
ce qui rendra sa sortie tout aussi imprévisible, et ainsi de suite.
En particulier, désormais deux blocs initialement identiques
seront chiffrés différemment.

> Pour rendre le chiffrement encore un peu imprévisible,
Alice et Bob peuvent aussi ajouter une suite de 128 bits au premier bloc à chiffrer.
Cette suite peut tout à fait être publique.
Son but est uniquement de garantir que deux messages identiques
seront chiffrés différemment.
De telles données publiques à usage unique 
qui viennent en support du chiffrement
sont appelés des nonces.

De façon cruciale, toutes ses opérations sont facilement inversibles,
pour Bob qui connaît le code chiffré et la clé $K$.
En effet, le déchiffrement de chaque bloc s'obtient
en effectuant les opérations d'inversion du chiffrement de bloc AES,
et en ajoutant ce résultat au bloc chiffré précédent.

Ce chiffrement symétrique CBC a toutefois quelques défauts,
qui font qu'on lui préfère d'autre solutions.
Est-ce que vous saurez identifier ces défauts ?

En premier lieu, le chiffrement chaîné fait que toute erreur
est propagée à l'entièreté du chiffrement du message.
En particulier, s'il y a un bit erroné parmi les premiers bits du message chiffré
qu'Alice envoie à Bob,
alors Bob ne pourra quasiment rien comprendre même après déchiffrement.
En pratique, on peut bien sûr atténuer ces risques avec de la redondance,
notamment l'algorithme de Reed-Solomon dont on a parlé précédemment.
Mais si des blocs précédents entiers n'ont pas été envoyés avec succès,
peut-être parce que Bob était en montagne et la 4G passait mal,
alors même cette redondance sera insuffisante.

En second lieu, un autre défaut de CBC,
c'est que les calculs de chiffrement et de déchiffrement 
ne peuvent pas être parallélisés.
S'il faut chiffrer de petits messages, cela ne pose pas de gros problèmes.
Mais s'il s'agit de chiffrer des peta-octets de données 
pour les sauvegarder dans un disque dur externe qui sert de backup,
alors ces calculs peuvent être beaucoup plus longs.


## Le générateur AES-CTR_DBRG

Pour chiffrer de vastes quantités de données 
en exploitant la parallélisation du calcul,
la solution du chiffrement par compteur, ou CTR,
a été proposée... par Diffie et Hellman.
Et oui, le chiffrement symétrique CTR, 
c'est l'autre algorithme de Diffie-Hellman !

L'idée de CTR, c'est d'utiliser en entrée d'AES,
non pas le bloc à chiffrer, 
mais une suite publique de 64 bits d'apparence aléatoire appelée nonce,
suivie de l'écriture du numéro à chiffrer en base 2, en 64 bits.

> Le nonce permet de contrer les attaques par pré-calcul :
un attaquant peut faire plein de calculs en amont
pour construire une table d'inversion des messages chiffrés.
Mais si la construction de cette table prend plus de temps que l'âge de l'univers,
alors cette attaque par pré-calcul restera vaine.

Le résultat du chiffrement de cette entrée avec la clé $K$
donne alors 128 bits qui peuvent paraître aléatoires.
Eh bien, CTR propose d'ajouter ces 128 bits au bloc à chiffrer,
ce qui donne alors le bloc correspondant chiffré.
Cette fois, pas de dépendance inter-blocs dans le chiffrement ;
et donc aucune dépendance inter-blocs dans le déchiffrement non plus !
Voilà qui sont des opérations entièrement parallélisables.

Bien entendu, AES pourrait être remplacé par un autre chiffrement de bloc.
En fait, certains considèrent que la meilleure solution est désormais
ChaCha20, qui combine des solutions d'AES et de SHA-256.
Mais si l'on garde AES et si on le combine à CTR, on obtient alors AES-CTR.
Intuitivement, AES-CTR peut paraître moins sécurisé que AES-CBC,
car il y a moins l'effet d'avalanche qui fait que deux messages qui diffèrent d'un bit
auront des chiffrements radicalement différents.
Cependant, jusque là, AES-CTR reste considéré pleinement sécurisé.

En pratique, AES-CTR, AES-CBC et ChaCha20 sont généralement combinés à d'autres informations,
potentiellement publiques comme des méta-données sur le destinataire du message,
typiquement sous la forme d'une adresse IP.
Enfin, tout cela est souvent accompagné d'un hash du code chiffré
et des méta-données, pour authentifier le message.
Un tel hash est appelé *code d'authentification du message* ou MAC en anglais.
On parle alors de chiffrement symétrique authentifié.
ChaCha20 + MAC donne alors ChaCha20-Poly1305, ou ChaChaPoly pour les intimes,
que certains considèrent être la meilleure solution de communication sécurisée aujourd'hui.

Enfin, on peut parler du générateur de nombre aléatoire AES-CTR_DBRG.
Sa conception correspond tout simplement au chiffrement d'un message vide avec AES-CTR.
En pratique, plutôt qu'utiliser un nonce,
on encourage la personne qui utilise ce générateur 
à spécifier, en plus de la clé $K$ à 256 bits, 
un nombre aléatoire $V$ à 128 bits, qui sera l'entrée d'AES.
$V$ et $K$ sont alors appelées des *graines* du générateur.
Pour obtenir le n-ième nombre généré par AES-CTR_DBRG
à partir de la graine $(V, K)$,
il suffit alors de calculer $AES(V \oplus n, K)$,
où l'addition est ici un XOR.

En pratique, AES-CTR_DBRG est aujourd'hui considéré être 
l'un des générateurs de nombres aléatoires les plus sécurisés,
y compris contre des calculateurs quantiques.
Et oui, le quantique, ce n'est pas magique !
Comme l'explique très bien [3Blue1Brown](https://tournesol.app/entities/yt:RQWpF2Gb-gU),
le quantique n'est vraiment utile que pour une poignée de problèmes,
en particulier pour casser le chiffrement pré-quantique,
mais il ne permet absolument pas en général de casser le chiffrement.
En pratique, pour casser AES-CTR_DBRG,
on pense qu'un calculateur quantique nécessitera toujours un temps exponentiel
en la longueur des clés secrètes.

Et je dis bien "on pense", car, en théorie, 
il reste encore beaucoup de chemins à parcourir 
pour être pleinement rassuré pour la sécurité d'AES-CTR_DBRG.
En particulier, celle-ci dépend fortement de la conjecture
des générateurs de nombres pseudo-aléatoires.
Formellement, cette conjecture dit 
qu'à partir d'une graine aléatoire à $k$ bits,
on peut générer une suite deux fois plus longue
telle qu'aucun algorithme, 
dont le temps de calcul est raisonnable
et qui ne connaît pas la graine aléatoire,
ne pourra distinguer la suite de $2k$ bits d'une suite vraiment aléatoire.

> NB: Là encore, formellement, on doit admettre que l'algorithme adversaire 
peut avoir des énormes coups de chance, 
mais ces coups de chance doivent avoir une probabilité extrêmement faible.
Plus formellement, on considère un adversaire $A: \{0,1\}^{2k} \to \{0, 1\}$,
qui prédit si la suite vient du générateur ou est un vrai aléatoire.
Il faut alors que $P[A(AES-CTR_DBRG_{2k}(x))] \approx P[A(y)]$,
avec une erreur inférieure à toute fonction polynomiale de $k$.


## Conclusion

Honnêtement, la vidéo d'aujourd'hui n'était pas 
initialement prévue au programme de cette série.
C'est parce que, pendant longtemps, 
je préfèrais m'intéressais 
aux plus élégantes astuces mathématiques de la cryptographie.
Cependant, l'importance moderne de la cybersécurité m'a invité
à m'attarder sur ses composants les plus fondamentaux.
Rendez-vous bien compte.
S'il y a une faille dans les objets qu'on a présenté aujourd'hui,
alors c'est tout notre système d'information mondiale 
qui serait à la complète merci de la première superintellygence 
qui l'aura identifiée.

À l'inverse, on pourrait espérer réussir à prouver la sécurité de ces solutions.
Malheureusement, cette sécurité est encore plus difficile à prouver
que P différent de NP,
ce prestigieux problème ouvert à 1 million de dollars
dont on a parlé dans un épisode précédent.
Néanmoins, à défaut d'un résultat conclusif,
de nombreux théorèmes de sécurité ont été prouvés à propos des algorithmes,
lesquels s'appuient généralement sur des hypothèses 
comme un certain état d'ignorance des superintellygences sur les clés secrètes,
ou l'impossibilité de résoudre certains problèmes en temps raisonnable.

Mais surtout, les grands héros de la sécurisation de notre cyber espace,
dont je n'ai finalement pas vraiment parlé aujourd'hui,
ce sont les armées de *cryptanalystes*,
c'est-à-dire ces ingénieurs et ces chercheurs qui
ont passé des décennies à essayer de casser ces algorithmes,
en particulier SHA-256, AES, CBC et CTR,
à l'aide de machines très puissantes.
Si cette superintellygence bienveillante n'y est pas parvenue,
peut-être pont-on espérer que d'autres, moins bienveillantes,
n'y arriveront pas non plus.

À défaut de théorèmes mathématiques, 
c'est en tout cas le meilleur pari qu'on a trouvé
pour fournir des solutions pragmatiques 
pour être prévisiblement imprévisibles,
en ne s'appuyant que sur des opérations purement déterministes.

