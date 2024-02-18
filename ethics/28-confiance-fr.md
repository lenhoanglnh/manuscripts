# À qui faire confiance ?

De façon plus précise, l'idéal que l'on se fixe est celui de la démocratie,
à savoir un humain un droit de vote unitaire.
Mais pour cela, il nous faut donner à chaque humain une et une seule carte électorale.
En informatique, on parle de "Proof of Personhood", 
comme j'en ai récemment parlé au Conseil National du Numérique.
Notez qu'il ne s'agit pas uniquement de vérifier qu'un compte est contrôlé par un humain ;
il faut aussi garantir que ledit humain ne peut pas contrôler un autre compte validé sur Tournesol.  
https://cnnumerique.fr/paroles-de/les-grands-modeles-de-langage-quels-risques-echange-avec-le-nguyen-hoang

Pour assigner des Proof of Personhood,
Tournesol s'appuie sur la vérifications d'adresses emails
dont le nom de domaine paraît, d'après l'Association Tournesol, résilient aux attaques Sybil.
Ainsi, les adresses @epfl.ch ou @inria.fr sont considérées résilientes aux attaques Sybil par Tournesol,
car nous considérons qu'il est difficile pour des entités malveillantes 
de contrôler un grand nombre de messageries électroniques avec ces noms de domaines.
Et ça, c'est bien sûr par opposition à @gmail.com ou @proton.me,
puisqu'il suffit de quelques clics pour créer une messagerie de la sorte.

Bien entendu, cette solution est insatisfaisante, 
puisqu'elle discrimine tous ceux qui n'ont pas d'adresses emails 
rattachées à un nom de domaine Sybil-résilient.
Pour augmenter l'inclusivité de Tournesol,
la plateforme dispose également d'un système de parrainage :
chaque utilisateur peut ainsi se porter garant 
pour le fait qu'un autre compte est bien détenu par un humain 
qui n'utilise que ce compte de manière active sur Tournesol.

On peut ainsi voir les données de certification comme un graphe orienté de parrainnage,
avec une confiance initiale donnée à certains comptes.
Il s'agit ensuite intuitivement de faire diffuser la confiance à travers le réseau.

De façon plus précise, pour ce faire, 
Tournesol s'appuie sur un nouvel algorithme inspiré du fameux algorithme PageRank de Google.
Cet algorithme a une interprétation amusante :
imaginez un surfeur aléatoire se balader dans le réseau,
en prenant à chaque instant au hasard un arc sortant du noeud où il se trouve.
Avec une certaine probabilité, par ailleurs, il se téléporte au hasard
dans l'un des noeuds initialement de confiance.
La confiance d'un noeud correspondra alors à la fréquence à laquelle il aura été visité par le surfeur aléatoire.
https://tournesol.app/entities/yt:6jK9bFWE--g

Si PageRank a fait la fortune de Google, il possède toutefois un défaut de sécurité :
un noeud peut avoir une confiance disproportionné, si tout le monde lui fait confiance.
Mais alors, si ce noeud se fait tout à corrompre, il peut rediriger beaucoup de confiance
dans des parties obscures du réseau.
Pour limiter l'influence maximale de tout compte sur la confiance reçue par les autres,
Tournesol propose tout bêtement de limiter la fréquence de visite du noeud.
C'est comme si, lorsqu'un noeud est trop souvent visiter,
au lieu de le visiter, le surfeur se téléportait au hasard dans un noeud initialement de confiance.
L'algorithme qu'on obtient ainsi, qu'on a appelé LipschiTrust,
dispose alors d'une garantie de sécurité,
qui borne l'impact maximal d'un compte sur les confiances acquises par les autres comptes.
C'est ainsi que Tournesol associe à chaque compte une confiance, 
de manière assez robuste et sécurisée.

Pour chaque vidéo, chaque contributeur acquiert ensuite un droit de vote, de la manière suivante.
Tout d'abord Tournesol calcule la somme des confiances des contributeurs à la vidéo.
Puis, on va s'autoriser à assigner un nombre total de droits de votes,
de sorte que celui-ci ne dépasse pas trop la confiance maximale.
En gros, le delta entre la somme des confiances et la somme des droits de votes allouable
est ensuite répartie entre les comptes qui manquent de confiance.
Voilà qui limite leur impact conjoint, 
tout en permettant de les intégrer autant que n'importe qui d'autres,
si ces comptes qui manquent de confiance sont en fait peu nombreux.

Je vous renvoie vers notre article pour les détails plus précis autour de ces répartitions des droits de votes.


