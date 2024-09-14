# Qui est-ce ? (avec un mensonge !)

Imaginez une partie un peu spéciale du jeu "qui est-ce ?"
où chaque joueur a le droit de mentir une seule fois.
Prenons le cas particulier où vous avez 4 personnages possibles,
et vous devez identifier le personnage que l'autre joueur a dans la main,
en posant uniquement des questions binaires.
Par exemple, vous pouvez demander : "le personnage est-il une fille ?"
Ou "le personnage a-t-il un micro ?".
Et l'autre joueur doit répondre par oui ou par non,
avec un droit unique au mensonge.
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


## L'interpolation de Lagrange

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
L'idée de Reed-Solomon est d'effectuer une autre transformation,
en remplaçant la suite m_1_, m_2_, m_3_ par le polynôme
P(X) = m_1_ + m_2_ X + m_3_ X².

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



## Le cas des corps finis



## Résolution du Qui Est-Ce ?

n=F3

1 -> 00000
2 -> 00111
3 -> 11100
4 -> 11011

Distance de Hamming


## Reed-Muller


## Conclusion

