# Prouver un savoir sans le révéler

Comme on l'a vu la dernière fois,
les passeports biométriques sont des solutions
qui peuvent être utilisées par toute plateforme en ligne
pour garantir qu'un compte appartienne à un citoyen,
et que ce citoyen ne possède qu'un seul compte sur la plateforme.
Cependant, avant de déployer de telles solutions,
il est important d'évaluer les risques que cela implique
notamment pour l'anonymat en ligne et la liberté d'expression.

L'une des découvertes les plus spectaculaires 
de la science de l'information moderne
est qu'il est tout à fait possible 
de combiner authentification et anonymat.
En fait, nos démocraties n'ont pas attendu l'informatique
pour développer une telle solution :
le vote à l'urne, 
avec insertion du bulletin de vote dans une enveloppe,
authentification du votant au moment de l'insertion de l'enveloppe dans l'urne
et mélange des enveloppes dans l'urne,
est une solution remarquablement sécurisée
pour combiner authentification et anonymat.

Mais est-ce vraiment possible d'obtenir ces mêmes propriétés
pour toute opération d'authentification anonyme en ligne ?
Comment fournir des preuves de citoyenneté à usage unique
sans que ces preuves ne révèlent quoi que ce soit de l'identité du citoyen,
y compris aux yeux de superintellygences comme les gouvernements
qui certifient l'authenticité de ces preuves ?

Aujourd'hui, on va voir la brique fondamental de telles preuves,
à savoir une solution pour prouver 
qu'on connaît une solution 
à une équation polynomiale difficile à résoudre,
sans révéler cette solution.
Par exemple, imaginons que je connaisse une solution
à l'équation `X^3^ + Y^3^ = Z^3^ + 5`
dans le corps fini à 2^255^ - 19 éléments.
Comment pourrais-je vous prouver que je connais la solution,
sans vous la révéler ?


## Le 3-coloriage de graphe

Avant d'attaquer pleinement le problème des équations polynomiales,
faisons un petit détour historique vers un autre problème,
qui est vraiment la grande découverte qui a initié tout un champ de recherche.
Et ce qui est cool, c'est que cette solution est assez simple à expliquer.

Considérez un graphe, c'est-à-dire un ensemble de noeud,
avec des arêtes entre certaines paires de noeud.
Colorier le graphe consiste à colorier chaque noeud du graphe avec une couleur,
de sorte que deux noeuds liés par une arête ne soit jamais coloriés
avec une même couleur.

Imaginons que le prouveur connaît un coloriage du graphe en 3 couleurs.
Comment le prouveur peut-il démontrer cette connaissance,
sans permettre au vérificateur d'apprendre quoi que ce soit
à propos la solution que le prouveur a en tête,
à part le fait que c'est une solution correct ?

Imaginons le prouveur connaisse un coloriage, 
avec les trois couleurs rouge, bleu et vert.
Alors, il connaît en fait 6 coloriages différents ;
s'il échange les rouges et les bleus,
ou les rouges et les verts,
ou les bleus et les verts,
ou s'il remplace les rouges par les bleus par les verts par les rouges,
ou les rouges par les verts par les bleus par les rouges,
il obtient à chaque fois un nouveau coloriage correct.

Eh bien, ce que le vérificateur va faire,
c'est demander au prouver de prendre une feuille et de dessiner l'un de ces coloriages.
Puis, il va lui cacher son dessin.
Maintenant, le vérificateur va choisir une arête du graphe au hasard,
et il va demander au prouveur de révéler les couleurs des noeuds que l'arête relie.
Si les couleurs sont identiques, c'est clairement que le coloriage était incorrect,
et que le prouveur a bluffé :
le vérificateur pourra conclure que le prouveur ne connais en fait pas un coloriage.
À l'inverse, si les couleurs ne sont pas identiques,
c'est un signe que le coloriage était correct, au moins vis-à-vis de cette arrête.
Mais bien sûr, cela ne prouve a priori pas que le coloriage était correct.

Cependant, ce qui est intéressant, c'est que si le coloriage était incorrect,
alors il y a forcément au moins une arête dont les deux noeuds reliés sont de la même couleur.
Et donc pour tout coloriage incorrect,
la probabilité que le test du vérificateur révèle la supercherie
sera au moins 1 divisé par A, où A est le nombre d'arêtes.
Eh bien, l'astuce c'est de répéter un grand nombre de fois le défi.
Après n défis, pour un coloriage incorrect,
la probabilité qu'aucun défi ne conduise à un rejet du prouveur par le vérificateur
sera au moins (1-1/A)^n^.
En particulier, quand n est plusieurs fois A,
cette probabilité (1-1/A)^kA^ < e^-jk décroît exponentiellement vite vers 0,
et on peut donc rendre la probabilité d'un échec à rejeter une supercherie très négligeable.

Ainsi, en répétant 100A fois le test, 
on est essentiellement garanti d'approuver des prouveurs corrects,
et de rejeter des prouveurs incorrects.
Le protocole interactif permet donc très bien de déterminer
sir le prouveur connaît un coloriage correct.

Mais la magie de ce protocole, bien sûr,
c'est surtout qu'il ne révèle rien au vérificateur.
Parce que les couleurs qu'il s'attend à observer sont une paire
uniformément aléatoire de couleurs distinctes,
et parce que c'est ce qu'il observe avec le prouveur correct,
il n'observe rien d'autre que ce qui correpond à une vérification d'un coloriage correct.
En particulier, ces informations ne permettent aucunement
de reconstruire un coloriage correct.

Prenez le temps d'y réfléchir. C'est quand même vraiment fou !

Mieux encore, le problème du coloriage de graphe à 3 couleurs
est un problème qu'on sait être NP-complet,
c'est-à-dire qu'il fait partie des problèmes les plus difficiles,
parmi ceux dont la validité d'une solution est vérifiable rapidement
suite à la révélation complète de la solution.
En particulier, ça veut dire que tout problème de la sorte,
y compris la vérification que des nombres sont solutions d'une équation polynomiale, 
tout ça peut être reformulé comme un problème de coloriage de graphe.

Cependant, cette reformulation est très complexe ;
et elle est surtout sous-optimale.
Et dans la suite, on va surtout voir une meilleure solution pour notre problème initial.


## L'algorithme de Schnorr


## L'engagement de Pedersen


## L'engagement polynomial


## Formalisation des preuves à divulgation nulle


## Conclusion

Fiat-Shamir
