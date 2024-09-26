# L'art d'être prévisiblement imprévisible

La cybersécurité repose sur l'incapacité de cybercriminels puissants
à prédire des informations secrètes de nos systèmes d'information.
En particulier, comme on l'a vu dans la dernière vidéo,
de nombreuses solutions cryptographiques exigent de générer des nombres que 
même une superintellygence comme la NSA sera incapable de prédire.
On parle parfois de générateurs de nombres pseudo-aléatoires cryptographiquement sécurisés.

Et notez que tous les générateurs ne sont pas cryptographiquement sécurisés.
Par exemple, le module `random` de python n'est pas cryptographiquement sécurisé,
comme vous pouvez vous en rendre compte en lisant 
la [documentation du module](https://docs.python.org/3/library/random.html).

Et idéalement, il faudrait être mathématiquement assuré 
de l'incapacité de toute superintellygence à prédire les nombres aléatoires qu'on génère.
Dans le jargon, on parle de génération de nombres aléatoires cryptographiquement sécurisés.
Ces nombres doivent non seulement être imprévisibles pour nous ;
il doit surtout être prévisible qu'ils seront imprévisibles pour les superintellygences aussi.
Ils doivent être prévisiblement imprévisibles.

Et a priori, on pourrait se dire que c'est facile.
En tout cas nous autres humains,
on semble capable de dire des nombres que même notre moi du passé ne saurait pas prédire, non ?
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

Mais surtout, en cryptographie, 
il nous faut générer beaucoup de nombres aléatoires,
parfois des milliers, des millions, voire des milliards de nombres aléatoires.
Et pour cette tâche, nos cerveaux de primate sont en fait très limités,
car ils sont dépassés par la quantité de travail que cela exige.

Alors, en pratique, dans certains protocoles,
on va exploiter des capteurs de température ou des mesures de lampes lava,
pour générer toujours plus de hasard.
Mais aujourd'hui, on va se demander comment nos machines sont programmées,
pour générer des nombres prévisiblement imprévisibles,
sans avoir accès à des capteurs extérieurs.

Et spoiler alert, on évite aujourd'hui d'utiliser la suggestion de la NSA de 2012,
appelée DUAL\_EC\_DRBG, car on se doute que celle-ci est backdoorée,
comme on l'a vu la dernière fois.
Non, la solution aujourd'hui considérée la plus standard,
c'est d'utiliser un algorithme appelé AES-CTR\_DBRG.
Et comme on va le voir, il s'appuie sur des concepts 
dont l'application va en fait bien au-delà 
de la génération de nombres prévisiblement imprévisibles ;
on les retrouve aussi dans le chiffrement symétrique 
et le calcul d'empreintes cryptographiques.


## Le chiffrement de bloc

L'ingrédient de base de nombreuses solutions cryptographiques est le chiffrement de bloc,
ou *bloc cipher* en anglais.
L'idée est de définir une fonction qui prend en entrée un bloc,
et sort un bloc de bits avec le même nombre n de bits,
et dont la transformation est paramétrée par une clé secrète.
Cette fonction doit être par ailleurs maximalement inversible.
En particulier, pour n'importe quelle clé,
il faut éviter que deux blocs différents en entrée
soient transformés soit transformés en deux blocs identiques en sortie,
puisque ça impliquerait que d'autres blocs en sortie sont garantis de ne pas être générés.
Autrement dit, pour toute clé, 
le chiffrement de bloc doit définir une permutation de l'ensemble des suites de n bits ;
et cette propriété sera par ailleurs essentielle pour le chiffrement symétrique aussi.

Dans les années 1970, un chiffrement de bloc appelé DES a été proposé, 
et a ensuite été érigé en standard ;
mais la sécurité de cette solution fut montrée insuffisante,
à la fois parce qu'elle utilisait des clés de chiffrement à seulement 56 bits,
ce qui ne fait que 2^56^ ≈ 10^17^ clés possibles seulement,
mais aussi parce qu'il y avait des moyens de court-circuiter une partie du calcul.
En 1999, la *Electronic Frontier Foundation* a ainsi montré comment casser 
un chiffrement DES en à peine 22 heures.

Bref. On pourrait croire qu'il suffit de faire un peu n'importe quoi 
avec les blocs de bits pour générer du hasard ;
mais être prévisiblement imprévisible n'est pas si évident !

De nos jours, le chiffrement de bloc le plus standard est AES avec 256 bits,
qui opère sur des blocs de 128 bits, avec une clé qui fait également 256 bits.
Les détails d'AES ne sont pas particulièrement passionnants,
mais je vais quand même vous en dire quelques mots,
notamment parce que ses opérations sont un peu analogues 
aux calculs des réseaux de neurones.

!> Il y a en fait 3 modes de fonctionnements d'AES,
avec respectivement 128, 192 et 256 bits.
Mais ici je ne parlerai uniquement que du cas avec 256 bits.

Pour comprendre la construction d'AES, 
il est utile de voir les suites de 128 bits en entrée
comme des suites de 16 paquets de 8 bits.
Chaque paquet de 8 bit est alors appelé un octet.
On parle aussi de *byte* en anglais.

!> Techniquement, un *byte* n'est pas nécessairement un octet,
mais ce sera généralement le cas en pratique.

Mieux encore, chaque octet définit un nombre du corps fini à 2⁸ éléments.
Je vous renvoie à une vidéo précédente pour comprendre ce que j'entends par là.
Et si ça, c'est très pratique,
c'est notamment parce qu'on a défini des additions et des multiplications
qui fonctionnent extrêmement bien pour les octets de la sorte.
En particulier, on peut remarquer que toute polynôme de degré 1,
c'est-à-dire toute fonction affine `P(x) = ax + b`,
où `a` et `b` sont constantes dans le corps fini avec `a` non nul,
définit bien une permutation de l'ensemble des octets.
En effet, on peut aisément résoudre toute équation `y = ax + b`,
en retranchant `b` puis en divisant par `a`,
ce qui nous donne `x = (y-b)/a`.

Mieux encore, si on voir la suite de 128 bits comme un vecteur de 16 octets,
on peut définir des fonctions linéaires à l'aide de matrices.
Formellement, si on définit `f(X) = AX + B`,
où `A` est une matrice de 16 x 16 octets,
où `B` est une suite de 16 octets,
et où `X` représente les 16 octets qui forment le bloc en entrée,
pourvu que `A` est ce qu'on appelle une *matrice inversible*,
alors `f` définit ainsi une permutation des suite de 128 bits.

Bingo ! En construisant `A` et `B` à partir de la clé secrète,
on semble tenir là une solution à notre sélection d'une permutation aléatoire, non ?

Eh bien, en tout cas, les cryptographes n'ont pas souhaité 
se restreindre uniquement à des opérations linéaires.
Et ça veut dire qu'il faut une autre manière 
de définir des permutations des suites de 16 octets.

Alors, vous pourriez vouloir échanger des octets,
et les additionner entre eux ;
mais toutes ces opérations sont en fait elles aussi linéaires.
Et qui plus est, combiner tout plein d'opérations linéaires,
eh bien, ça reste une opération linéaire.
Non, si on veut aller au-delà du `AX+B`, il va falloir une autre astuce.
Vous l'avez trouvée ?

Eh bien, une autre permutation qu'on peut définir pour un octet,
c'est celle qui consiste à remplacer tout octet `x` par son inverse `1/x`,
à l'exception du `0` qu'on laisse inchangé.
Cette opération est bien une permutation,
puisqu'on peut l'inverser en réeffectuant la même opération ;
et oui, `1/(1/x)) = x`.

Eh bien, AES, en gros c'est ça.
C'est une succession de 14 transformations linéaires définies par la clé secrète,
avec des inversions des octets intercalées entre ces transformations linéaires.
Mieux encore, la clé secrète suit elle aussi des transformations linéaires
et des opérations d'inversions d'octets,
pour définir la suite des matrices `A` et des vecteurs `B` 
qui seront appliqués aux 16 octets.

Si vous avez vu ma vidéo sur les transformeurs,
ou si vous connaissez les réseaux de neurones,
il y a là une analogie évidente avec ces solutions au machine learning.
Dans les deux cas, il s'agit de bidouilles non-linéaires,
avec entre chaque bidouille non-linéaire une transformation linéaire.
En particulier, ces opérations ont le don d'être largement parallélisables,
[sans l'être complètement](https://tournesol.app/entities/yt:g_u8YWpe4BM).

Ainsi, AES définit ainsi une opération qui prend en entrée un bloc `X` de 128 bits
et une clé `K` de 256 bits, et qui sort un bloc `Y` de 128 bits.
On peut ainsi écrire `Y = AES(X, K)`.
Et si on prend une clé `K` parfaitement inconnue d'une superintelligence,
alors aux yeux de celle-ci, 
AES effectue une permutation essentiellement imprévisble
de l'ensemble des blocs de 128 bits.
D'ailleurs, ce que je décris là, à savoir un a priori uniforme sur la valeur de `K`,
c'est ce qu'on appelle le modèle du chiffrement de bloc idéal ;
et il est très utilisé pour étudier théoriquement les garanties d'AES.

Et en particulier la sécurité de l'utilisation d'AES
pour le hachage, le chiffrement et la génération de nombres aléatoires.


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

Pour garantir cette propriété, le bloc AES a un défaut :
si on connaît la clé `K` et le bloc de sortie,
alors on peut reconstruire le bloc en entrée.
Ainsi, quand la clé parvient à être identifiée, 
AES génère une sortie informative vis-à-vis de son entrée.
Or on a vu dans la vidéo sur les courbes elliptiques
que la backdoor probable de la NSA s'appuyait sur une propriété de ce genre.

Pour être plus prévisiblement imprévisible,
les informaticiens Davies et Meyer ont simplement proposé
d'ajouter à `Y` le bloc `X` en entrée.
Ils définissent ainsi `Z = X + AES(X, K)`.
Enfin, pour agréger des longues suites de blocs `X_1_, _X_2_, ...`,
on va simplement réutiliser les sorties `Z_1_, Z_2_, ...`
des blocs précédents, 
combinés avec les blocs `X_1_, X_2_, ...` en tant que clés,
pour générer les sorties suivantes.
Ainsi, on va poser `Z_n+1_ = Z_n_ + AES(Z_n_, X_n_)`.
Cette construction est appelée construction de Merkle–Damgård,
du nom des deux informaticiens 
qui ont indépendamment montré des propriétés de sécurité de la construction.

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
Cependant, leur vocation n'est pas nécessairement de rremplacer SHA-2.
IL s'agissait plus de proposer une solution fondée 
sur des principes radicalement distincts,
pour anticiper l'éventualité où SHA-2 serait cassé.

Alors, pour être plus précis, 
SHA-256 utilise un autre chiffrement de bloc que AES,
qui est composée de 64 opérations linéaires plutôt que 14,
et qui agit sur des suites de 512 bits plutôt que 128.
Enfin, l'opération non-linéaire utilisée est davantage la rotation,
c'est-à-dire remplacer par exemple la suite de bits 1000 par 0001,
en faisant glisser le bit à gaucher vers la droite.
Et il y a par ailleurs d'autres précautions à prendre,
notamment vis-à-vis du choix des constantes des transformations linéaires,
ou vis-à-vis du préformatage des données à hacher
pour qu'elles se décomposent bien en suites de 512 bits.

!> Notez que la fonction de chiffrement de bloc de SHA-256
fait en fait intervenir deux sortes différentes d'addition,
une addition dans le corps F_2^32^_ qui revient à prendre le XOR,
et une addition dans l'anneau Z_2^32^_ qui requiert des retenues.
Dans les deux cas, l'addition d'une constante définit une permutation
des suites de 32 bits.

Quoi qu'il en soit, ce faisant,
SHA-256 prend n'importe quelle suite de bits de n'importe quelle taille en entrée,
et ressort ensuite une suite de 256 bits,
qui même pour une superintellygence,
sont aucunement informative sur la nature de l'entrée,
bien que l'entrée détermine entièrement cette sortie.


## Le chiffrement symétrique CBC

Passons maintenant au chiffrement symétrique.
Vous vous souvenez peut-être que, dans la vidéo précédente,
on avait vu comment les courbes elliptiques permettent 
à deux interlocuteurs Alice et Bob de constituer un secret partagé `S`,
sans qu'aucune superintellygence ne soit capable de deviner ce secret `S`,
y compris après avoir intercepté tous les échanges
qui ont permis à Alice et Bob de constituer ce secret.
Cette solution est appelée algorithme de Diffie-Hellman,
et si vous ne vous rendez pas compte de la magie qu'il opère,
je vous invite à aller voir la vidéo de Science Étonnante qui l'explique très bien.

OK, mais avoir un secret partagé `S`,
ce n'est pas tout à fait l'objectif d'Alice et Bob.
Ce qu'ils veulent, c'est surtout pouvoir envoyer des messages
sans que la superintellygence ne puisse les lire.
Eh bien, pour y arriver, 
AES propose de d'abord transformer le secret partagé `S` 
en une clé de chiffrement `K`,
à l'aide d'une fonction de hachage ;
comme typiquement SHA-256.
D'ailleurs avec SHA-256, Alice et Bob obtiendront une clé de 256 bits,
ce qui correspond exactement à la longueur nécessaire pour AES.

Maintenant, imaginons qu'Alice souhaite envoyer un message `M` à Bob,
en chiffrant le message avec la clé de chiffrement partagée `K`.
Comment peut-elle s'y prendre ?
Bien sûr, on peut commencer en transformant `M` en une suite de bits.
Cependant, cette suite peut avoir un nombre arbitraire de bits,
mais AES ne peut avoir en entrée que 128 bits.
Clairement, il va nous falloir découper `M` en une suite de blocs de 128 bits.
Supposons que `M` est un énorme fichier,
de sorte que son code binaire est une suite d'un million de blocs de 128 bits.
Comment utiliser `K` pour chiffrer cette suite de blocs ?

Si on y va bêtement, en utilisant AES indépendamment pour chaque bloc,
alors on va risque malheureusement de révéler des informations.
Par exemple, s'il s'agit d'un chiffrement de textes, ou de pixels dans une image,
alors il arrive souvent que des blocs de 128 bits sont en fait identiques,
et ils vont alors être transformés en codes chiffrés identiques.
Voilà des indices intrusifs que pourra utiliser la superintellygence.

Une solution pour mieux chiffrer les données est le chiffrement pas chaîne de blocs,
appelé *cipher block chaining* ou CBC en anglais.
Et non ce n'est pas directement lié à la fameuse Blockchain.
L'idée, c'est qu'au lieu d'utiliser en entrée le bloc de 128 bits à chiffrer,
on va utiliser sa somme avec la sortie du bloc précédent.
Comme le chiffrement de chaque bloc est difficilement prévisible,
l'entrée du chiffrement du bloc suivant le sera aussi,
ce qui rendra sa sortie tout aussi imprévisible, et ainsi de suite.
En particulier, désormais deux blocs initialement identiques
seront chiffrés différemment.

!> Pour rendre le chiffrement encore un peu imprévisible,
Alice et Bob peuvent aussi ajouter une suite de 128 bits au premier bloc à chiffrer.
Cette suite peut tout à fait être publique.
Son but est uniquement de garantir que deux messages identiques
seront chiffrés différemment.
De telles données publiques à usage unique 
qui viennent en support du chiffrement
sont appelés des nonces.

De façon cruciale, toutes ses opérations sont facilement inversibles,
pour Bob qui connaît le code chiffré et la clé `K`.
En effet, le déchiffrement de chaque bloc s'obtient
en effectuant les opérations d'inversion du chiffrement de bloc AES,
et d'ajouter ce résultat au bloc chiffré précédent.

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
Et oui, le chiffrement symétrique CTR, c'est l'autre algorithme de Diffie-Helmman !

L'idée de CTR, c'est d'utiliser en entrée d'AES,
non pas le bloc à chiffrer, mais un nonce de 64 bits,
suivi de l'écriture du numéro à chiffrer en base 2, en 64 bits.

!> Cela implique qu'il y ait au plus 2^64^ blocs,
soit environ 10 milliards de milliards,
ce qui correspond à environ 300 exaoctets.

Le résultat du chiffrement de cette entrée avec la clé `K`
donne alors 128 bits qui peuvent paraître aléatoires.
Eh bien, CTR propose d'ajouter ces 128 bits au bloc à chiffrer,
ce qui donne alors le bloc correspondant chiffré.
Cette fois, pas de dépendance inter-blocs dans le chiffrement ;
et donc aucune dépendance inter-blocs dans le déchiffrement non plus !
Voilà qui sont des opérations entièrement parallélisables.

Bien entendu, AES pourrait être remplacé par un autre chiffrement de bloc,
comme cela a été proposé pour SHA-256.
Mais si l'on garde AES et si on le combine à CTR, on obtient alors AES-CTR.
Intuitivement, AES-CTR peut paraître moins sécurisé que AES-CBC,
car il y a moins l'effet d'avalanche qui fait que deux messages qui diffèrent d'un bit
auront des chiffrements radicalement différents.
Cependant, jusque là, AES-CTR reste considéré pleinement sécurisé.

En pratique, AES-CTR et AES-CBC sont généralement combinés à d'autres informations,
potentiellement publiques comme des méta-données sur le destinataire du message,
typiquement sous la forme d'une adresse IP.
Enfin, tout cela est souvent accompagné d'un hash du code chiffré
et des méta-données, pour authentifier le message.
Un tel hash est appelé *code d'authentification du message* ou MAC en anglais.
On parle alors de chiffrement symétrique authentifié.

Par ailleurs, on peut enfin au générateur de nombre aléatoire AES-CTR_DBRG.
Sa conception correspond tout simplement au chiffrement d'un message vide avec AES-CTR.
En pratique, plutôt qu'utiliser un nonce,
on encourage la personne qui utilise ce générateur 
à spécifier, en plus de la clé `K` à 256 bits, 
un nombre aléatoire `V` à 128 bits, qui sera l'entrée d'AES.
`V` et `K` sont alors appelées des *graines* du générateur.
Pour obtenir le n-ième nombre généré par AES-CTR_DBRG
à partir de la graine `(V, K)`,
il suffit alors de calculer `AES(V + n, K)`,
où l'addition est ici une addition modulo 2^128^.

> En particulier, il ne s'agit pas de l'addition dans le corps fini F_2^128_.
Après tout, dans ce corps fini, on aurait V + 2 = V...

AES-CTR_DBRG est aujourd'hui considéré être 
l'un des générateurs de nombres aléatoires les plus sécurisés.
Après tout, sa sécurité est intimement lié au chiffrement symétrique AES-CTR,
qui est lui omniprésent, et pour l'instant au moins, est considéré sécurisé,
grâce notamment aux échecs à le casser,
malgré des incitatifs énormes à y parvenir.
En tout cas, je vous invite à le privilégier à DUAL\_EC\_DBRG,
si vous voyez ce que je veux dire...


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

