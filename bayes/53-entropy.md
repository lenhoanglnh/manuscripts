# L'entropie ne mesure pas le chaos

"Tu devrais l'appeler entropie, pour deux raisons. 
Tout d'abord, ta fonction d'incertitude a été utilisée en mécanique statistique sous ce nom, 
elle a donc déjà un nom. 
Deuxièmement, et surtout, personne ne sait vraiment ce qu'est l'entropie, 
de sorte que dans un débat, vous aurez toujours l'avantage."

Tel fut le conseil que le génie américano-hongrois John von Neumann donna à Claude Shannon,
lorsque le second proposa sa mesure de quantification de l'incertitude, dans les années 1940.
Enfin, pourrait-on croire, la nature profonde de l'entropie a-t-elle été saisie.

Pourtant, 80 ans plus tard, force est de reconnaître que, 
si la science de l'entropie a énormément avancé,
très peu de gens savent aujourd'hui vraiment ce qu'est l'entropie.
En fait, tout physicien sera même bien embarrassé, 
lorsqu'on lui demandera de calculer l'entropie d'un ordinateur,
ou de tout objet complexe qui est très loin d'être un gaz à l'équilibre thermodynamique.  
https://community.ams.org/journals/notices/199805/lieb.pdf  
https://www.mdpi.com/1099-4300/19/11/603

Là où il semble y avoir un paradoxe profond,
c'est que ce concept est au coeur du second principe de la thermodynamique,
l'une des théories les plus indéboulonnables de la science.
Tandis que les lois de la mécanique de Newton, les lois de l'électromagnétisme de Maxwell
et les lois de l'espace-temps de Galilée ont toutes été ébranlées par les sciences modernes,
et alors que le premier principe de conservation de l'énergie est aujourd'hui réinterprété
comme une simple conséquence de l'invariance dans le temps des lois de la physique,  
https://tournesol.app/entities/yt:CxlHLqJ9I0A  
ce second principe résiste encore obstinément à l'expérimentation et à l'entendement.

Plus encore que les bizarreries quantiques,
le second principe est à mes yeux le mystère ultime de la science.
Même si les physiciens sont en fait encore incapables de le définir précisément,
il gouverne nos sociétés, en imposant des limites strictes au champ des possibles.
Après tout, comme l'explique très bien David de Science Étonnante,  
https://tournesol.app/entities/yt:2Z9p_I3hhUc  
ce qui fait défaut à nos sociétés n'est absolument pas un manque d'énergie.
En fait, le changement climatique n'est autre qu'un excédent d'énergie sur terre.
Et en particulier, quand on dit que l'énergie est le moteur de la croissance,
on dit quelque chose de profondément erroné sur le plan scientifique.
Ce qui fait tourner nos machines, c'est davantage l'entropie que l'énergie.

Ceux qui le comprennent peuvent alors être tentés de se jeter sur le concept d'entropie,
et faire croire que, en vertu notamment du second principe de la thermodynamique,
nous traversons une crise de l'entropie.
Certains en vont même jusqu'à prétendre 
que le second principe garantit le désordre et le chaos,
et là ça commence à me faire sérieusement grincer des dents...

"Personne ne sait vraiment ce qu'est l'entropie",
et visiblement, certains abusent de cette mécompréhension,
en utilisant ce terme scientifique pour feutrer leurs discours poétiques, ou politiques.

Aujourd'hui, je vais essayer de clarifier au mieux ce qu'on comprend vraiment de l'entropie, 
pour mieux évaluer ce qu'il est raisonnable de dire de l'entropie,
ce qui est beaucoup plus discutable,
et ce qui relève du discours extrêmement trompeur, et très problématique.

Et plutôt que de suivre le tortilleux chemin de l'histoire des sciences pour en arriver là,
je vais suivre les pas de Shannon, et prendre la voie informationnelle.
Et oui, on va voir que, en un sens grossier, 
ce qu'on appelle "problèmes énergétiques" est en bonne partie une histoire d'information !


## L'entropie de Shannon

Quelle est d'après vous l'information contenue dans le mot "Lê" ?
Et puis, comment quantifier cette information ?

Intuitivement, même si ce mot n'a que deux lettres,
c'est un mot très informatif, puisqu'il permet d'identifier un objet,
à savoir moi, parmi l'ensemble de tous les objets de l'univers.
C'est quand même pas mal !
Mais alors, est-ce que l'information dans le mot "Lê" est très grande ?

L'idée de génie de Claude Shannon, 
c'est de supposer que information et incertitude doivent être les deux faces d'une même pièce.
Plus précisément, selon Shannon, l'information d'un message, 
c'est la quantité d'incertitude que la lecture de ce message fait disparaître.

Autrement dit, si un message était très attendu, il est peu informatif.
Hein, quoi ? Un nouveau scandale impliquant Elon Musk ?
Oui j'aurais pu le deviner. Ce n'est pas très informatif.

Dit autrement, plus je suis surpris par le message, plus il contient d'information.
Et plus je risque de devoir changer d'avis.
Et d'ailleurs, cette attention à la surprise, 
je vous en ai déjà parler au tout début de cette série sur le bayésianisme,
en l'an 1 avant le COVID,
puisqu'elle est critique pour mettre à jour correctement notre état de connaissance du monde.
L'information est intimement liée à la surprise.

Mais alors, à quel point le mot "Lê" est-il surprenant ?

Eh bien, comme on l'a vu encore et encore dans cette série sur le bayésianisme,
la réponse à cette question est nécessairement contextuelle.
Si le mot "Lê" vient juste après "Le créateur de Science4All dont le prénom est ...",
alors vous qui suivez cette chaîne serez probablement aucunement surpris par ce mot.

À l'inverse, si vous entendez le mot "Lê" lors d'une réunion de travail dans votre entrepise,
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
mais je la trouve pédagogiquement extrêmement utile,
et assez conforme à notre intuition de ce qu'est l'intuition.

Mais donc, l'entropie, c'est quoi ?
Eh bien, l'entropie de Shannon, c'est la quantité d'information que je m'attend à recevoir,
qu'on appelle plus précisément l'espérance de l'information,
et qui est donnée explicitement par la somme des quantités d'information
des messages que je peux recevoir,
pondérée par les probabilités de ces messages.

Ou dit autrement, en utilisant la dualité information-incertitude,
l'entropie mesure l'incertitude qu'on a sur les messages qu'on va recevoir.
Par exemple, la position politique qu'adopteront les journalistes de CNews et de Blast
sur le sujet de l'immigration la semaine prochaine aura peu d'entropie pour moi,
car j'ai très peu d'incertitude sur l'angle journalistique qui sera choisi par ces médias.
À l'inverse, l'entropie sur le prochain lieu de conflit armé majeur est énorme à mes yeux,
car ça part un peu dans tous les sens en ce moment...

En tout cas, l'entropie est l'objet au coeur de la plus grande contribution de Claude Shannon,
retranscrite dans son article fabuleux de 1948 intitulé
"A mathematical theory of communication",
qui, pour les matheux parmi vous, est extrêmement lisible.
Vraiment, ce papier est un véritable bijou, non seulement mathématique,
mais aussi d'ingénierie, de linguistique et, je pense, de philosophie.
La lecture de cet article est vraiment l'un des plus grands bouleversements intellectuels de ma vie,
pas loin de Solomonoff 2009, Turing 1950 et Laplace 1814.

Laplaaaace !!!

Bon j'avoue, je met Laplace au-dessus des trois autres...


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

Patatra, l'entropie d'Omega a diminué !
Oui vous avez bien entendu.
L'entropie a diminué.

D'ailleurs, la réduction de l'entropie sera précisément égale 
à l'information espérée contenue dans X.

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

Souvenez-vous de l'exemple du mot "Lê".
Pour quelqu'un qui n'a jamais entendu parler de Science4All,
le mot "Lê" dans la phrase "Le créateur de Science4All dont le prénom est ..."
est très grande, puisqu'il sera surpris de ce prénom.
Mais ceux parmi vous qui me connaissez bien, ce mot ne contient presque aucune information.
Vous le saviez déjà.
L'entropie du mot Lê a été réduite par vos connaissances préalables.

Et clairement, ça, ce n'est pas du tout ce que la physique cherche à décrire.
L'entropie thermodynamique vise à décrire quelque chose qui ne dépend pas de l'observateur.

A contrario, l'entropie de Shannon est fondamentalement subjective :
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
Pour ce démon, l'entropie est une fonction décroissante du temps !

Et alors, en pratique, l'entropie anthropique, 
c'est-à-dire l'incertitude du monde pour nous autres Homo Sapiens,
peut en fait augmenter, 
lorsque nous autres humains finissiont par perdre de la mémoire,
ou quand nos biais cognitifs nous poussent à mal raisonner sur notre incertitude sur le monde.


## Le démon de Gibbs et l'entropie thermodynamique

Mais donc, qu'est-ce que l'entropie thermodynamique ?
A-t-elle vraiment à voir avec la théorie de l'information de Shannon ?
Pourquoi von Neumann conseillait-il à Shannon d'appeler sa mesure d'information "entropie" ?
Et si oui, de quel sujet dépend cette entropie thermodynamique ?

Alors, c'est là qu'on rentre en zone grise,
puisqu'on est très loin aujourd'hui encore d'avoir une définition consensuelle 
sur la définition de l'entropie thermodynamique,
pour des systèmes qui ne sont pas ultra-simplifiés 
comme des gaz parfaits à l'équilibre thermodynamique.

Cependant, une interprétation que je vous propose, 
et qui à ma connaissance colle parfaitement avec les théories les plus standards,
c'est d'introduire un être un peu spécial, 
que je vais appeler le démon de Gibbs,
du nom du physicien Josah William Gibbs,
reconnu aux côtés de Maxwell et Boltzmann comme le père de la physique statistique.
Et si je parle de démon de Gibbs,
c'est en partie en comparaions à d'autres démons, comme le démon de Laplace.

Pour rappel, le démon de Laplace, c'est un être omniscient,
qui connaît toutes les positions et toutes les vitesses de toutes les particules de l'univers.
Autrement dit sa connaissance de l'univers va jusqu'aux échelles microscopiques.

A contrario, le démon de Gibbs, c'est un être que je définis comme macroscopiquement omniscient.
Il connaît tous les "macro-états", c'est-à-dire les descriptions de tous les objets du monde,
ainsi que leurs positions, vitesses, volumes, températures et pressions,
mais ne connaît pas les positions et les vitesses des particules qui composent ces objets.

Eh bien, l'entropie thermodynamique, au moins dans le cas des gaz à l'équilibre thermodynamique,
on peut vraiment la voir comme l'incertitude du démon de Gibbs
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
Donc prenez-la avec des pincettes.

Ceci dit, dans tous les mécanismes d'irréversibilité,
il semble y avoir une mécanique de la sorte en jeu.
De l'information semble échapper au démon de Gibbs, 
lorsque celle-ci passe du monde macroscopique au monde microscopique,
et cette perte d'information semble irréversible.

Alors, petite note terminologique.
Le terme "démon de Gibbs", je l'ai vraiment inventé pour cette vidéo.
Initialement, j'étais tenté d'appeler ce démon le "démon de Boltzmann",
car l'interprétation macro versus micro-état est beaucoup plus associée à Boltzmann.
Malheureusement, la notion de "démon de Boltzmann" est déjà utilisée,
pour décrire un argument de "mélange aléatoire" dans les équations de Boltzmann.
Plus précisément, dans l'argument de Boltzmann, 
la perte d'information surgit vraiment des collisions entre deux particules élémentaires.
Intuitivement, ces deux particules vont avoir tendance à homogénéiser leurs vitesses respectives.
Typiquement, au billard, l'énergie cinétique de la boule blanche va se répartir à toutes les boules.
Bon ce n'est pas toujours vrai, puisque les équations de la physique sont réversibles,
et qu'il est en principe possible que les collisions mettent les autres boules à l'arrêt,
de sorte à concentrer l'énergie cinétique dans la boule blanche.
Mais ce second scénario semble extrêmement improbable.
Pour formuler cette uniformation de manière mathématique,
Boltzmann a supposer que la prochaine collision pouvait être décrite 
comme celle entre deux particules tirées au hasard.
C'est là qu'il y a un petit tour de passe-passe dans l'argument de Boltzmann,
et d'autres chercheurs ont souligné cette hypothèse en introduisant un "démon de Boltzmann",
qui choisit aléatoirement des prochaines particules qui entreront en collision.

Bon après, "démon de Gibbs" ce n'est pas si mal, 
puisque Gibbs a énormément contribué à consolider les idées parfois floues de Boltzmann.
Selon Henri Poincaré, 
"celui qui a vu le plus clairement [l'irréversibilité de processsus physiques macroscopiques en termes probabilistes], 
dans un livre trop peu lu car un peu difficile à lire, 
c'est Gibbs, dans ses Principes élémentaires de mécanique statistique".
D'ailleurs, un cours que Gibbs enseignait à Yale s'intitulait très clairement
"Sur la déduction a priori des principes de la thermodynamiques de la théorie des probabilités".
Et oui, selon Gibbs, la thermodynamique ne serait qu'une conséquence des lois des probabilités !
(Bon je nuancerais un peu cela, 
mais ça reste une perspective déficiente aujourd'hui, 
venant de l'un des plus grands experts de l'entropie de l'histoire !)  
https://terpconnect.umd.edu/~cjarzyns/CHEM-CHPH-PHYS_703_Spr_20/resources/Physics-of-Gibbs-in-his-time.pdf

Quoi qu'il en soit, avec l'interprétation via le démon de Gibbs, 
on a une nouvelle compréhension du second principe de la thermodynamique.
Celui-ci affirme que le différentiel de connaissance entre les démons de Laplace et de Gibbs
ne peut que croître avec le temps.
Au fur et à mesure que des opérations thermodynamiques irréversibles ont lieu,
le démon de Gibbs perdra de l'information sur les positions et les vitesses des particules,
et deviendra davantage ignorant, 
comparativement au démon de Laplace qui lui ne perd pas ses informations.

Alors, quelques précisions techniques :
le démon de Gibbs doit être supposé être un omniscient du présent uniquement.
Ou dit autrement, il n'a pas de mémoire,
ce qui le distingue du démon de Solomonoff.

Par ailleurs, malgré les énormes efforts de Gibbs pour combler aux manquements de sa théorie,
le démon de Gibbs reste nettement moins bien défini que ceux de Laplace et Solomonoff.
En particulier, sa description dépend de la distinction 
entre le monde macroscopique et le monde microscopique.
Et ce n'est pas là une limite de mon analogie.
Je parle là d'un problème fondamental au coeur de la thermodynamique statistique,
qui dépend d'une distinction entre les "macro-états" et les "micro-états".  
https://terpconnect.umd.edu/~cjarzyns/CHEM-CHPH-PHYS_703_Spr_20/resources/Physics-of-Gibbs-in-his-time.pdf

S'il est clair que les micro-états décrivent les positions et les vitesses de toutes les particules,
il n'est pas tout à fait clair ce que sont les macro-états.
Intuitivement, il s'agit des descriptions à base de positions et vitesses de "gros objets",
ainsi que de leurs pressions, de leurs températures, de leurs volumes, de leurs états physiques,
de leurs champs électro-magnétiques et de leurs compositions chimiques.
Mais qu'est-ce qu'un gros objet ? Parle-t-on de l'échelle du milligramme ? Du nanogramme ?
Combien faut-il de particules, ou de volume d'espace, pour que l'objet soit "macroscopique" ?

Est-ce qu'un atome qu'on manipulerait individuellement, 
et dont on connaît assez précisément la position et la vitesse,
forme un objet macroscopique ?  
https://en.wikipedia.org/wiki/IBM_%28atoms%29

Clairement, plus le seuil est petit, 
plus le démon de Gibbs aura une connaissance fine du monde,
et plus l'entropie thermodynamique, 
c'est-à-dire ce qu'il ne sait pas du monde microscopique, sera faible.
Sa mesure dépend ainsi fondamentalement de la granularité du monde macroscopique.

Or, de tout ce que j'ai lu, 
bien définir les contours de la frontière entre états macroscopiques et états microscopiques
reste une limite des connaissances actuelles de la recherche en thermodynamique statistique.
Surtout pour les systèmes hors-équilibre, 
les physiciens ne savent par encore vraiment comment définir l'entropie.  
https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.4.L012034  
https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.125.110601  
https://www.research.unipd.it/handle/11577/3425920  
https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.201912223?casa_token=mBbRVJ6vPbUAAAAA:JurERxLa-TdnddIKwKrPnONqQAbTqK6DfEZi3ommcUu3OGi5j9tmk7TtNhCaN-ZvqkH8w6v3EkrWvAE

D'ailleurs, selon le physicien et historien de la physique Martin Klein,
si Gibbs a procrastiné pendant plus d'une décennie la publication de son ouvrage fondateur
sur la physique statistique,
c'est probablement à cause de son incapacité à répondre à la question
"Quelle est l'entropie d'un système hors équilibre ?" ---
une question absolument fascinante dont je suis très loin d'avoir un iota de réponse satisfaisante !  
https://terpconnect.umd.edu/~cjarzyns/CHEM-CHPH-PHYS_703_Spr_20/resources/Physics-of-Gibbs-in-his-time.pdf


## Le démon de Maxwell

Plusieurs décennies avant la publication de l'ouvrage de Gibbs, en 1867, 
le génie écossais James Clerk Maxwell proposa une expérience de pensée,
pour montrer en quoi l'information microscopique est au coeur de la thermodynamique,
c'est-à-dire de la dynamique des échanges de chaleur.
Son expérience de pensée précède d'ailleurs aussi les travaux de Boltzmann,
et ils ont certainement aidé Boltzmann, puis Gibbs,
à formaliser l'entropie thermodynamique en tant qu'incertitude microscopique.

L'expérience de pensée de Maxwell fait intervenir un être puissant,
qu'il est désormais de coûtume d'appeler le démon de Maxwell.
Et oui, il y a beaucoup de démons dans ces histoires de physiques statistiques !
De façon remarquable, en ne faisant que traiter de l'information,
ce démon était capable de violer le second principe de la thermodynamique,
en faissant baisser l'enthropie thermodynamique, 
au sens classique non-informationnel de Clausius.

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

D'ailleurs le démon de Maxwell peut ainsi créer non seulement un différentiel de pression, 
mais aussi un différentiel de pression, en mettant toutes les particules d'un seul côté...
Vraiment, il y a quelques chose de profond dans le traitement des informations microscopiques.


## Des limites thermodynamiques au traitement informationnel ?

L'expérience de pensée du démon de Maxwell a en fait troubler les physiciens 
pendant plus d'un siècle.
En 1960, le physicien Rolf Landauer en a fournit une interprétation,
qui fait un pont entre information cédée au monde microscopique 
et énergie dissipée en énergie thermique non récupérable.

Et oui, on va enfin parler de ce mystérieux Landauer,
qui a gagné par ailleurs le droit d'être le nom du groupe Signal,
où Rodolphe, Jean-Lou et moi avons échangé pour préparer nos vidéos sur l'entropie !

Pour comprendre Landauer, il suffit de considérer le problème des deux cloisons,
avec cette fois une seule particule, dont on sait qu'elle se trouve à gauche.
Ou plus précisément, on va supposer 
que le fait que la particule se trouve à gauche est une information macroscopique,
et donc connue du démon de Gibbs.

En ouvrant la trappe, la particule va maintenant naviguer de gauche à droite et de droite à gauche,
de sorte que l'information sur la cloison qui contient la particule sera inconnue,
en tout cas dans le monde macroscopique.
Cette information sera perdue par le démon de Gibbs.
En particulier, à la question "la particule se trouve-t-elle à gauche ?",
le démon de Gibbs doit maintenant répondre
"il y a une probabilité 1/2 que ce soit le cas ?"
(en supposant les deux cloisons macroscopiquement identique).

En particulier, l'information avant ouverture de la trappe correspond 
à une information au sens de Shannon et relativement au démon de Gibbs
égale au logarithme en base de 2 de l'inverse de 1/2, qui est égale à 1 bit.
En ouvrant la trappe, le démon de Gibbs a perdu 1 bit d'information ;
ou dit autrement, l'entropie thermodynamique a augmenté d'un bit.

Gibbs montra que cette description informationnelle est équivalente à dire 
que l'entropie thermodynamique a augmenté de k ln 2 Joules par Kelvin.
De plus, si l'expérience a lieu à température ambiante T,
alors cette augmentation de l'entropie correspond à une dissipation de kT ln 2 Joules.

Aujourd'hui ce principe dit de Gibbs est souvent exprimé sous la forme d'un coût énergétique
à l'effacement de l'information.
Pour être plus précis, toutefois, il faut bien voir qu'il s'agit 
de la destruction d'une information macroscopique uniquement,
c'est-à-dire une destruction informationnelle pour l'observateur qu'est le démon de Gibbs.

Cependant, le démon de Laplace, qui a lui accès à l'information microscopique,
lui ne perd pas cette information.
Il n'y a en tout cas pas de perte d'information fondamentale dans l'univers.

Petite aparté mécanique quantique, 
parce que je sens qu'il y en a qui font le lien avec le hasard de l'interprétation de Copenhague,
en très bref, il existe plusieurs interprétations complètement déterministes de la mécanique quantique,
parfaitement conformes avec l'existence d'un démon de Laplace,
et selon lesquelles il n'y a pas de perte d'information microscopique.  
https://tournesol.app/entities/yt:OpOcGoGRslQ

En particulier, j'entends parfois dire que le traitement de l'information 
nécessite forcément un coût énergétique.
Alors, bon, d'abord, l'énergie est une grandeur qui se conserve.
Donc bon, la terminologie "coût énergétique" est trompeuse ;
il serait plus juste de parler de "coût entropique", 
et donc d'un coup en termes de perte d'information macroscopique.

Par ailleurs, ce coût inéluctable, selon le principe de Landauer, dépend de la température.
Et donc, en principe, on pourrait faire énormément de calculs
avec une très faible dissipation en énergie thermique,
si ces calculs sont effectués à des températures proches du zéro absolu.

Mais surtout, le principe de Landauer concerne uniquement l'effacement de l'information.
Or, effacer une information, on conviendra qu'il ne s'agit que d'une opération particulière,
parmi l'ensemble des opérations utiles au traitement de l'information.

Par exemple, s'il s'agit de trier les informations du web pour recommander les plus pertinentes,
comme cherche à le faire Tournesol notamment,
alors en principe ces opérations ne nécessitent pas de destruction informationnelle.
Il est donc possible en principe de faire Tournesol 
sans dissipation d'énergie en énergie thermique !

De façon générale, il y a toute une théorie à l'interface entre la physique et l'informatique,
qui étudie le calcul dit réversible,
et qui repose justement sur le non-effacement des informations macroscopiques.
Et comme tout thermodynamicien vous le dira, si une opération est réversible,
c'est qu'elle n'augmente pas l'entropie thermodynamique.

Bref. Dire que l'information nécessite de l'énergie est en fait une erreur.
Alors que dire les problèmes d'énergie sont avant tout 
des histoires de pertes d'informations microscopiques,
bon c'est très très loin d'être juste, hein, évitez de le dire,
mais c'est plus cohérent avec les lois fondamentales de la physique.

Bon ceci dit, bien sûr qu'en pratique et de facto, 
nos machines à traiter l'information dissipent énormément d'énergie en énergie thermique.
Mais premièrement, cette énergie dissipée est beaucoup, beaucoup, beaucoup plus faible 
que dans le cas du transport, de l'agriculture et du chauffage.
Et deuxièmement, réduire les problèmes d'information à cette dissipation énergétique,
c'est précisément faire un réductionnisme énergétique très malencontreux,
car il omet toutes les préoccupations majeures à avoir 
dans le traitement et la diffusion actuels de l'information,
qui échouent complètement à être décrites par ce réductionnisme énergétique.

C'est amusant que dans une vidéo où j'explique que Monsieur Jancovici tombe dans ce travers,
j'ai énormément de commentaires de ses fans qui, justement, illustrent ce travers...


## L'entropie ne mesure pas le chaos social

Pour vulgariser l'entropie, 
il est courant de la définir comme étant une mesure du désorder ou du chaos,
en prenant l'exemple d'une chambre mal rangée ou d'un mouvement social.
Ces analogies peuvent être utiles en première approximation
pour avoir une intuition de ce concept.

Après tout, si une chambre est mal rangée, 
c'est qu'il y a sans doute beaucoup d'incertitudes
sur les positions des chaussettes de la chambre.
Pour un observateur humain, on peut ainsi dire que 
l'entropie au sens de Shannon de la chambre mal rangée sera plus grande
que celle d'une chambre bien rangée, avec des étiquettes un peu partout.

Cependant, il ne faut pas confondre cette entropie de l'observateur humain
avec l'entropie thermodynamique, qui est vue via les lentilles du démon de Gibbs.
Ne l'oubliez pas.
Le démon de Gibbs est omniscient vis-à-vis de l'information macroscopique.
Or les chausssettes sont des objets macroscopiques ;
il n'a donc clairement aucune incertitude vis-à-vis de leurs positions.

En fait, il n'est pas clair que, pour le démon de Gibbs,
l'entropie de la chambre mal rangée est plus grande que celle de la chambre bien rangée.

De même ce n'est pas en triant des pommes que vous diminuerez l'entropie thermodynamique.
Encore une fois, le tri de pomme est une opération qui peut être effectuée de manière réversible.
Ce tri ne peut pas avoir réduit l'entropie thermodynamique.

C'est en cela que je dis que "l'entropie ne mesure pas le chaos".
Pour être moins erroné, on pourrait dire qu'elle mesure davantage le chaos microscopique,
mais je pense que là encore, si on balance ça juste au détour d'une phrase,
on risque d'induire en erreur car le mot "microscopique" peut facilement être mal compris.

En particulier, affirmer que le second principe de la thermodynamique 
prédit un effondrement civilisationnel,
ou qu'on court à notre perte en dissipant de l'énergie en chaleur,
c'est effectuer un grave contresens vis-à-vis des lois de la physique.

Du reste, depuis 1789, la France a beaucoup gagné en structures,
avec l'instauration de l'éducation populaire, la liberté de la presse et l'indépendance de la justice,
mais aussi en créant de nombreuses institutions publiques
pour permettre à la démocratie de fonctionner de manière stable, durable et satisfaisante.
À l'échelle macroscopique, 
si on regarde l'évolution des sociétés au cours des trois derniers siècles,
on est très loin d'assister à une amplification inéluctable du chaos.

Et pourtant, bien entendu, pendant ce temps, l'entropie thermodynamique de l'univers a augmenté !
Même si on n'inclut que le soleil est la terre,
et les rayonnements perdus dans l'espace pour obtenir un système fermé,
il y a eu une structuration macroscopique,
même si une partie de l'information macroscopique a été dissipée et perdue dans les échelles microscopiques.

Enfin, on peut insister sur le fait qu'on est encore extrêmement loin des limites thermodynamiques.
Après tout, une entropie maximale, 
ça correspond à un monde où le démon de Gibbs ne sait plus rien du tout !
Autrement dit, il s'agirait d'un énorme néant homogène de particules indiscernables macroscopiquement.
Il n'y aurait pas certaines particules qu'on peut associer à une chaussette, une chambre ou un humain.

Invoquer les limites thermodynamiques pour parler d'urgence écologique aujourd'hui,
c'est en fait beaucoup plus erronée que d'affirmer que la planète terre va brûler,
à cause de la transformation inéluctable de notre soleil en géante rouge.
C'est non seulement être complètement à côté de la plaque,
mais aussi révéler sa profonde confusion sur l'état des crises actuelles.

S'il-vous-plaît, évitez absolument d'invoquer l'entropie pour parler de chaos social.
Il y a déjà suffisamment de problèmes civilisationnels qui nous menacent au 21e siècle.
Concentrons-nous sur eux, plutôt que de détourner l'attention de tous 
vers des considérations injustifiées.



