# L'entropie ne mesure pas le chaos

"Tu devrais l'appeler entropie, pour deux raisons. 
Tout d'abord, ta fonction d'incertitude a été utilisée en mécanique statistique sous ce nom, 
elle a donc déjà un nom. 
Deuxièmement, et surtout, personne ne sait vraiment ce qu'est l'entropie, 
de sorte que dans un débat, vous aurez toujours l'avantage."

Tel fut le conseil que le génie américano-hongrois John von Neumann donna à Claude Shannon,
lorsque le second proposa sa mesure de quantification de l'incertitude, dans les années 1940.
Enfin, pourrait-on croire, la nature profonde de l'entropie aura-t-elle été saisie.

Pourtant, 80 ans plus tard, force est de reconnaître que, 
si la science de l'entropie a énormément avancé,
très peu de gens savent aujourd'hui vraiment ce qu'est l'entropie.
En fait, même tout physicien sera bien embarrassé, 
lorsqu'on lui demandera de calculer l'entropie d'un ordinateur,
ou de tout objet complexe qui est très loin d'être un gaz à l'équilibre thermodynamique.

Là où il semble y avoir un paradoxe profond,
c'est que ce concept est au coeur du second principe de la thermodynamique,
l'une des théories les plus indéboulonnables de la science.
Tandis que les lois de la mécanique de Newton, les lois de l'électromagnétisme de Maxwell
et les lois de l'espace-temps de Galilée ont toutes été ébranlées par les sciences modernes,
et alors que le premier principe de conservation de l'énergie est aujourd'hui réinterprété
comme une simple conséquence de l'invariance dans le temps des lois de la physique,
ce second principe résiste encore obstinément à l'expérimentation et à l'entendement.

Plus encore que les bizarreries quantiques,
le second principe est à mes yeux le mystère ultime de la science.
Même si on est encore incapable de le définir précisément,
il gouverne nos sociétés, en imposant des limites strictes au champ des possibles.
Après tout, comme l'explique très bien David de Science Étonnante,
ce qui fait défaut à nos sociétés n'est absolument pas un manque d'énergie.
En fait, le changement climatique n'est autre qu'un excédent d'énergie sur terre.
Et en particulier, quand on dit que l'énergie est le moteur de la croissance,
on dit quelque chose de profondément erroné sur le plan scientifique.
Ce qui fait tourner nos machines, c'est en un sens davantage l'entropie que l'énergie.

Ceux qui le comprennent peuvent alors être tentés de se jeter sur le concept d'entropie,
et faire croire que, en vertu notamment du second principe de la thermodynamique,
nous traversons une crise de l'entropie.
Malheureusement, certains en vont même jusqu'à prétendre 
que le second principe garantit le désordre et le chaos,

"Personne ne sait vraiment ce qu'est l'entropie",
et visiblement, certains abusent de cette mécompréhension.

Aujourd'hui, je vais essayer de clarifier ce qu'est l'entropie, en tout cas au sens de Shannon,
pour mieux évaluer ce qu'il est raisonnable de dire de l'entropie,
ce qui est beaucoup plus discutable,
et ce qui est extrêmement trompeur.

Et plutôt que de suivre le tortilleux chemin historique pour en arriver là,
je vais suivre les pas de Shannon, et prendre la voie informationnelle.
Et oui, on va voir que les problèmes de pétrole et d'énergie renouvelable
sont réductibles à des problèmes informationnels ---
même si je ne suis pas sûr que ce réductionnisme informationnel soit vraiment utile en pratique...


## L'entropie de Shannon

Quelle est d'après vous l'information contenue dans le mot "Lê" ?
Et puis, comment quantifier cette information ?

Intuitivement, c'est un mot très informatif, puisqu'il permet d'identifier un objet,
à savoir moi, parmi l'ensemble de tous les objets de l'univers.
C'est quand même pas mal !
Mais alors, est-ce que l'information dans le mot "Lê" est très grand ?

L'idée de génie de Claude Shannon, 
c'est de supposer que information et incertitude doivent être les deux faces d'une même pièce.
Plus précisément, selon Shannon, l'information d'un message, 
c'est la quantité d'incertitude que la lecture de ce message fait disparaître.

Autrement dit, si un message était très attendu, il est peu informatif.
Hein, quoi ? Un nouveau scandale à OpenAI ?
Oui j'aurais pu le deviner. Ce n'est pas très informatif.

Dit autrement, plus je suis surpris par le message, plus il contient d'information.
Et plus je risque de devoir changer d'avis.
Et d'ailleurs, cette attention à la surprise, 
je vous en ai déjà parler au tout début de cette série sur le bayésianisme,
en l'an 1 avant le COVID.
L'information est intimement liée à la surprise.

Mais alors, à quel point le mot "Lê" est-il surprenant ?

Eh bien, comme on l'a vu encore et encore dans cette série sur le bayésianisme,
la réponse à cette question est nécessairement contextuelle.
Si le mot "Lê" vient juste après "Le créateur de Science4All dont le prénom est ...",
alors vous qui suivez cette chaîne serez probablement aucunement surpris par ce mot.

À l'inverse, si vous entendez le mot "Lê" lors d'une réunion de travail dans votre entrerpise,
votre surprise sera probablement plus grande, et ce mot sera alors plus informatif.

"Sans conteste, sans contexte, c'est la mauvaise probabilité qu'on teste",
comme le dit le #ProverbeBayésien.

Formellement, l'information dans le mot "Lê" a été défini par Shannon 
comme le logarithme en base 2 de l'inverse de la probabilité du mot "Lê".
Je ne vais pas rentrer dans trop de détail ici,
mais cette formule garantit que l'information augmente avec la surprise.
Par ailleurs, le logarithme est utile pour garantir
que, conformément à l'intuition, l'information de deux messages indépendants
soit la somme des informations des deux messages.
Enfin, Shannon utilise la base 2 car cela permet de lier directement cette information
au nombre de bits nécessaire pour encoder le message.

OK, ça c'est l'information d'un message,
et d'ailleurs ce n'est pas vraiment une définition standard que je vous ai donnée ;
elle est surtout intéressante pédagogiquement.

Mais donc, l'entropie, c'est quoi ?
Eh bien, l'entropie de Shannon, c'est la quantité d'information que je m'attend à recevoir,
qu'on appelle plus précisément l'espérance de l'information,
et qui est donnée explicitement par la somme des quantités d'information
des messages que je peux recevoir,
pondérée par les probabilités de ces messages.

Voilà l'objet au coeur de la plus grande contribution de Claude Shannon,
retranscrite dans son article fabuleux de 1948 intitulé
"A mathematical theory of communication",
qui, pour les matheux parmi vous, est extrêmement lisible.

Vraiment, ce papier est un véritable bijou, non seulement mathématique,
mais aussi d'ingénierie et, je pense, de philosophie.
La lecture de cet article est vraiment l'un des plus grands bouleversements intellectuels de ma vie,
pas loin de Solomonoff 2009, Turing 1950 et Laplace 1814.


## Le théorème de la réduction de l'entropie

Appelons Omega l'ensemble de toutes les choses à savoir.
Omega est parfois appelé l'univers, et est très courant en probabilité.
A priori, on dispose d'une grande incertitude sur Omega,
qu'on peut appeler entropie d'Omega, et écrire H(Omega).

Maintenant, imaginons qu'on s'informe.
Appelons X ce qu'on découvre.
Alors l'entropie qu'il reste d'Omega, sera H(Omega|X),
c'est à l'incertitude qu'il reste sur Omega, 
conditionnellement à l'information X que l'on connaît désormais.

Je ne rentre pas dans les détails de ce que ça signifie,
mais sachez que c'est extrêmement standard en théorie de l'information.

Eh bien, un théorème assez simple à démontrer dit que H(Omega|X) est inférieur ou égal à H(Omega).
D'ailleurs, la réduction sera égale précisément à l'information contenue dans X.

Patatra, l'entropie d'Omega a diminué !
Oui vous avez bien entendu.
L'entropie a diminué.

Et là, on ne parle pas d'un principe de physicien,
qui ne sera considéré vrai que jusqu'au jour où on se rendra compte qu'il n'est pas si vrai.
On parle bien d'un théorème mathématique.
L'entropie du monde diminue.

Et bien sûr, ça, ça peut paraître complètement contradictoire 
avec le second principe de la thermodynammique,
qui affirme que l'entropie ne peut qu'augmenter.

Que se passe-t-il ? A-t-on enfin démontré la stupidité des physiciens ?
Qu'en pensez-vous ?

Prenez le temps de mettre pause pour bien essayer de comprendre ce qu'il se passe...

"Sans conteste, sans contexte, c'est la mauvaise probabilité qu'on teste".
En particulier, il ne faut pas perdre de vue que la notion d'entropie est contextuelle.
Elle dépend des informations auxquelles on a accès.

Et clairement, ça, ce n'est pas du tout ce que la physique cherche à décrire.
L'entropie thermodynamique vise à décrire quelque chose qui ne dépend pas de l'observateur.

Or, l'entropie de Shannon est fondamentalement subjective :
elle dépend des informations auxquelles un sujet a accès.
En un sens, on pourrait parler d'entropie anthropique,
puisqu'elle se réfère à une personne, qu'on peut généralement supposer humaine.
Et parce que ça me fait marrer de dire "entropie anthropique",
même si ça serait un peu trop flatteur pour les humains.

En fait, pour que le concept d'entropie de Shannon s'applique rigoureusement à un sujet,
il faut que ce sujet soit bayésien,
dans le sens où ce sujet doit être constamment en mesure d'appliquer les lois des probabilités...

Dit autrement, il ne s'applique vraiment qu'à une forme de superintelligence,
qui, dans mon livre La Formule du Savoir, est appelée le démon de Solomonoff.
Le démon de Solomonoff est cette entité imaginaire qui collecte cumulativement de l'information,
et a le faculté d'appliquer systématiquement la formule de Bayes pour améliorer son modèle du monde.

En pratique, l'entropie anthropique, c'est-à-dire l'incertitude des humains sur le monde,
peut en fait augmenter, lorsque nous autres humains finissiont par perdre de la mémoire,
ou quand nos biais cognitifs nous poussent à mal raisonner sur notre incertitude sur le monde.


## L'entropie thermodynamique

Mais donc, qu'est-ce que l'entropie thermodynamique ?
A-t-elle vraiment à voir avec la théorie de l'information de Shannon ?
Pourquoi von Neumann conseillait-il à Shannon d'appeler sa mesure d'information "entropie" ?
Et si oui, de quel sujet dépend cette entropie thermodynamique ?

Alors, c'est là qu'on rentre en zone instable,
puisqu'on est très loin aujourd'hui encore d'avoir une définition consensuelle 
sur la définition de l'entropie thermodynamique,
pour des systèmes qui ne sont pas ultra-simplifiés 
comme des gaz parfaits à l'équilibre thermodynamique.

Cependant, une interprétation que je vous propose, 
et qui colle pas mal avec les théories les plus standards,
c'est d'introduire un être un peu spécial, que je vais appeler le démon de Boltzmann,
en référence aux démons de Laplace et de Maxwell.

Pour rappel, le démon de Laplace, c'est un être omniscient,
qui connaît toutes les positions et toutes les vitesses de toutes les particules de l'univers.
Autrement dit sa connaissance de l'univers va jusqu'aux échelles microscopiques.

A contrario, le démon de Boltzmann, c'est un être que je définis comme macroscopiquement omniscient.
Il connaît tous les "macro-états", c'est-à-dire les descriptions de tous les objets du monde,
ainsi que leurs positions, leurs vitesses, leurs températures et leurs pressions,
mais ne connaît pas les positions et les vitesses des particules qui composent ces objets.

Eh bien, l'entropie thermodynamique, au moins dans le cas des gaz à l'équilibre thermodynamique,
on peut vraiment la voir comme l'incertitude du démon de Boltzmann
sur les positions et les vitesses des particules,
malgré son omniscience macroscopique.
Dit autrement, elle quantifie les informations du démon de Laplace 
auxquelles le démon de Boltzmann n'a pas accès.
L'entropie thermodynamique quantifie la différence de connaissance entre les deux démons.

Encore une fois, je vous présente là une interprétation, qui vient vraiment de mon chapeau, 
qui colle parfaitement avec la thermodynamique à l'équilibre,
et qui me semble être quelque chose de très profond, 
ou en tout cas de pédagogiquement très utile...
mais qui est très loin de faire consensus chez les physiciens.

Ceci dit, dans tous les mécanismes d'irréversibilité,
il semble y avoir une mécanique de la sorte en jeu.
De l'information semble échapper au démon de Boltzmann, 
lorsque celle-ci passe du monde macroscopique au monde microscopique,
et cette perte d'information semble irréversible.

Quoi qu'il en soit, avec cette interprétation, 
on a une nouvelle compréhension du second principe de la thermodynamique.
Celui-ci affirme que le différentiel de connaissance entre les démons de Laplace et de Boltzmann
ne peut que croître avec le temps.
Au fur et à mesure que des actions irréversibles ont lieu,
le démon de Boltzmann perdra de l'information sur les positions et les vitesses des particules,
et deviendra davantage ignorant, 
comparativement au démon de Laplace qui lui ne perd pas ses informations.

Alors, quelques précisions techniques :
le démon de Boltzmann doit être supposé être un omniscient du présent uniquement.
Ou dit autrement, il n'a pas de mémoire,
ce qui le distingue du démon de Solomonoff.

Par ailleurs, contrairement aux démons de Solomonoff et de Laplace,
le démon de Boltzmann est un être mal défini.
En particulier, sa description dépend de la distinction 
entre le monde macroscopique et le monde microscopique.
Et ce n'est pas là une limite de mon analogie.
Je parle là d'un problème fondamental au coeur de la thermodynamique statistique,
qui dépend d'une distinction entre les "macro-états" et les "micro-états".

S'il est clair que les micro-états décrivent les positions et les vitesses de toutes les particules,
il n'est pas tout à fait clair ce que sont les macro-états.
Intuitivement, il s'agit des description à base de positions et vitesses de "gros objets",
ainsi que de leurs pressions, de leurs températures, de leurs états physiques,
de leurs champs électro-magnétiques et de leurs compositions chimiques.
Mais qu'est-ce qu'un gros objet ? Parle-t-on de l'échelle du milligramme ? Du nanogramme ?
Combien faut-il de particules, ou de volume d'espace, pour que l'objet soit "macroscopique" ?

Clairement, plus le seuil est petit, plus le démon de Boltzmann aura connaissance fine du monde,
et plus l'entropie thermodynamique, c'est-à-dire ce qu'il ne sait pas du monde microscopique,
sera faible,


## Le démon de Maxwell

En 1867, le génie écossais James Clerk Maxwell proposa une expérience de pensée,
pour montrer en quoi l'information microscopique est au coeur de la thermodynamique,
c'est-à-dire de la dynamique des échanges de chaleur.
Son expérience de pensée précède d'ailleurs les travaux de Boltzmann,
et ils ont certainement aidé Boltzmann à formaliser l'entropie thermodynamique
en tant qu'incertitude microscopique.

L'expérience de pensée de Maxwell fait intervenir un être puissant,
qu'il est désormais de coûtume d'appeler le démon de Maxwell.
De façon remarquable, en ne faisant que traiter de l'information,
ce démon était capable de violer le second principe de la thermodynamique,
en faissant baisser l'enthropie thermodynamique, au sens classique non-informationnel de Clausius.

Pour comprendre cela, imaginez deux cloisons complètement isolantes, 
avec une trappe qui les sépare.
Imaginez que, initialement, la cloison de gauche contient de l'air froid,
alors que la cloison de droite a de l'air chaud.
En 1855, Clausius fit la remarque que, lorsque la trappe était ouverte,
la chaleur allait nécessairement se déplacer du chaud vers le froid,
de sorte que les températures des deux cloisons finissent par s'homogénéiser.
Et il mathématisa cela en définissant l'entropie comme une grandeur additive,
qui augmentait nécessairement avec le temps.

La remarque de Maxwell, toutefois, 
c'est que si l'on considère que les gaz sont composés de particules,
et que la température est en gros la vitesse moyenne de ces particules,
alors on peut en fait réduire l'entropie en faisant simplement un tri.

[NB : Techniquement, la température est davantage liée à l'énergie cinétique des particules.
En fait cette énergie de chaque particule doit être en gros kT,
où k est la constante de Boltzmann, 
à un facteur multiplicatif prêt qui dépend du degré de liberté des particules.]

Pour cela, il suffit au démon de Maxwell d'ouvrir la trappe 
lorsqu'une particule rapide va de gauche à droite,
et en la fermant quand elle va de droite à gauche.
Ainsi, les particules à haute énergie cinétique vont se retrouver à droite,
tandis que les particules à faible énergie vont se retrouver à gauche.
Ce faisant la différence de température entre les cloisons va augmenter ;
ou dit autrement, l'entropie va diminuer.

En ouvrant et en fermant la trappe, ce qui est clairement une opération réversible,
mais en faisant cela aux bons moments,
le démon de Maxwell pouvait violer le second principe de l'entropie.
En particulier, ce faisant, il pouvait transformer de l'énergie thermique inutilisable,
en une différence de chaleur, qui peut être utilisée pour extraire du travail !

Dit autrement, la simple exploitation d'informations microscopiques suffit
à créer une capacité de travail,
et donc à résoudre les problèmes d'énergie dans nos sociétés.
En fait, tous les maux énergétiques de nos sociétés, 
ce ne sont pas des pénuries d'énergie ;
il s'agit avant tout d'une incapacité à exploiter des informations microscopiques,
comme le démon de Maxwell sait le faire.


## Des limites thermodynamiques au traitement informationnel ?

Principe de Landauer

Calcul réversible

Le réductionnisme énergétique est une erreur !


## L'entropie ne mesure pas le chaos social

Trier des pommes ne changera pas l'entropie thermodynamique.

C'est en cela que je dis que "l'entropie ne mesure pas le chaos".

En particulier, depuis 1789, la France a beaucoup gagné een structures. Mais l'entropie a augmenté !

On est extrêmement loin des limites thermodynamiques !



