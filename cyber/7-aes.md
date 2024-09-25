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
Cette fonction doit être par ailleurs inversible,
autrement dit, elle doit définir une permutation de l'ensemble des suites de n bits.

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

En effet, l'idée est de décomposer les 128 bits du bloc à chiffrer
en 16 sous-blocs de 8 bits.
Une suite de 8 bits, c'est aussi ce qu'on appelle un octet,
ou *byte* en anglais.

> Techniquement, un *byte* n'est pas nécessairement un octet,
> mais c'est le cas le plus souvent.

On va même placer les 16 octets sous la forme d'un tableau,
qu'on appelle aussi une *matrice*.
Cette représentation est utile pour comprendre les opérations 
qui vont être effectuées pour modifier les bits du bloc.


## Davies-Meyer


## Merkle-Darmgard (SHA-2)


## Le chiffrement par chaîne de blocs (CBC)


## Le chiffrement par compteur (CTR)


## Le code d'authentification de message


## Le chiffrement symétrique standard AES-CCM


## Le générateur AES-CTR_DBRG


## Conclusion


