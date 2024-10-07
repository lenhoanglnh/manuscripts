# Vérifier une superintelligence ? (P vs NP vs IP vs SNARK)

Comme on l'a vu la dernière fois,
l'un des grands enjeux de la cybersécurité,
c'est de pouvoir se protéger de "superintelligences",
c'est-à-dire de systèmes d'informations beaucoup plus puissants que nous-mêmes.
Par exemple, est-ce qu'une start-up de 3 personnes avec un unique serveur
peut empêcher toute l'armée numérique chinoise et la NSA
de compromettre les opérations de la start-up ?
Ou mieux encore, est-ce que la Commission Européenne
peut mettre en place des dispositifs pour vérifier 
que Google respecte les lois européennes ?
Autrement dit, un vérificateur peu puissant peut-il vérifier 
la conformité d'une superintelligence avec
les principes définis par le vérificateurs ?

Aujourd'hui, on va voir que ces questions sont au coeur
du problème le plus prestigieux de la science de l'information,
à savoir le problème P versus NP,
mais aussi au coeur de nombreuses de ses variantes,
notamment le problème NP versus IP.

Bien souvent, 
comme l'ont d'ailleurs très bien fait Passe Science et Science Étonnante,
on présente ainsi le problème P versus NP
comme une question sur la capacité des machines à résoudre des problèmes difficiles ;
mais on peut en fait aussi l'interpréter
comme une question sur la faculté d'un vérificateur faible
à déléguer des tâches à une sorte de superintelligence, 
sans que la superintelligence ne puisse tromper le vérificateur.

Et comme on va le voir, il existe des réponses positives à cette question.
Cec qui signifie que, 
si on prend le temps de développer des systèmes cryptographiques sécurisés,
il y a tout à fait moyen de garder des suyperintelligences sous contrôles,
au moins dans le contexte de certaines applications.


## Le problème P versus NP

Pour comprendre ce qu'on entend pas "vérificateur faible",
il faut d'abord que je vous dise quelques mots de la notion de temps de calculs.
Intuitivement, on se rend bien compte que certaines tâches sont complexes,
au sens où, pour les résoudre, il faut beaucoup travailler ;
et même si on délègue le travail aux machines,
ces machines doivent elles aussi énormément travailler.
Plus précisément, elles devront effectuer un grand nombre d'opérations.
Eh bien, un vérificateur faible,
c'est tout simplement un vérificateur qui n'a qu'une puissance de calculs limitée.

A priori, il peut sembler 
que déléguer une tâche à une superintelligence ne soit pas d'un énorme intérêt :
comment vérifier en quelques milliards d'opérations seulement
les milliards de milliards d'opérations qu'aura effectué la superintelligence ?
Et bien, en gros, le problème P versus NP revient à répondre 
"oui, c'est possible" à cette question,
pour au moins une certain classe de problème.
Mieux encore, prouver que P est différent de NP,
c'est démontrer que, pour beaucoup de problèmes,
ce gain à déléguer est gigantesque.

Un exemple typique de l'intérêt d'exploiter une superintelligence, 
c'est le problème de prouver des théorèmes mathématiques.
Grâce à des langages formels comme Coq,
on peut maintenant représenter formellement les théorèmes et les preuves mathématiques.
Mieux encore, en encodant les axiomes des mathématiques et de la logique dans Coq,
on a conçu un algorithme capable de vérifier la validité des preuves mathématiques.
Formellement, l'algorithme de vérification s'écrit 
`Verifie(preuve, théorème)`
et accepte si la preuve est une preuve valide du théorème, et rejette sinon.
Bien entendu, cet algorithme n'est pas magique ;
il faudra travailler pour effectuer cette vérification.

Mais la question qu'on se pose, 
c'est si l'algorithme y gagnerait beaucoup à déléguer la *recherche* de preuve mathématique,
plutôt qu'à l'effectuer lui-même.
Plus précisément, étant donné un théorème `théorème`,
y a-t-il un intérêt à délaisser à d'autres
la tâche de trouver une preuve `preuve` tel que `Verifie(preuve, théorème) = accepte` ?
Et oui, parce que Coq n'est pas juste un vérificateur de preuves,
il est aussi capable de rechercher des preuves.
Après tout, puisque `preuve` n'est qu'une suite de symboles,
on peut lister toutes les possibles valeurs de `preuve`,
en commençant par celle de 1 symbole, puis celles de 2 symboles et ainsi de suite.
Si Coq veut trouver une preuve, il lui suffit de suivre cet algorithme pour y arriver.
Cependant, ceci nécessitera beaucoup plus de travail de sa part,
que la simple tâche de vérification de la validité d'une preuve.

Pour mesurer le gain à déléguer,
les informaticiens proposent de quantifier le travail nécessaire à la recherche,
relativement au travail nécessaire à la vérification.
En fait, les problèmes P, c'est en gros les problèmes de vérification.
Tandis que les problèmes NP, ce sont les problèmes de recherche.
La question P versus NP demande s'il existe des problèmes
pour lesquels la recherche est forcément exponentiellement plus longue
que la vérification.

NB: Pour prouver que P est différent de NP, 
il suffit de prouver que la recherche soit obligatoirement superpolynomiale 
en la vérification pour au moins un problème, 
i.e. chercher une solution dont la description est de longueur n prend un temps f(n) tel que, 
pour tout entier k, f(n) / n^k^ tende obligatoirement vers l'infini quand n tend vers l'infini,
et tel que par ailleurs la vérification puisse prendre un temps qui ne soit que polynomial en n.

Et on considère généralement qu'il s'agit du plus important problème ouvert de l'informatique,
et peut-être même de toutes les mathématiques, 
de toutes les sciences et de sécurité nationale.
En tout cas, le Clay Institute of Mathematics offre 1 million de dollars
à quiconque parviendrait à résoudre ce problème.

NB: La seule raison pour laquelle je ne pense pas qu'il soit si important,
c'est parce que je suspecte très fortement de connaître la réponse 
(à savoir, P différente de NP).
Dès lors d'autres questions pour lesquelles on n'a aucune idée de la réponse,
comme des questions autour de la gouvernance algorithmique,
me semble en fait plus importante aujourd'hui.

Considérons ainsi toutes les preuves d'un théorème donné
dont le temps de vérification est faible,
c'est-à-dire qui peut être effectué en n secondes par Coq,
sur un laptop de base.

NB: La définition implique d'exclure les théorèmes et les preuves 
dont le nombre de symboles ne peut pas être lu par le laptop en n secondes, 

On va considérer que si le temps qu'il aurait fallu pour trouver une preuve
parmi l'ensemble de ces preuves est de n^2^ secondes,
alors l'algorithme y aura gagner à externaliser la preuve.
Mais il n'y aura pas beaucoup gagné.
Idem si ce temps est de l'ordre de n^3^ secondes, ou n^100^ secondes.

Dans le cadre du problème P versus NP, 
le vérificateur y gagne énormément, 
si le temps qu'il lui aurait été nécessaire est quelque chose comme 2^n^,
c'est-à-dire exponentiel en n.
Et oui, parce que 2^n^ a une croissance exponentielle,
c'est-à-dire qu'elle dépasse très rapidement notre entendement,
et en particulier ce que le vérificateur pourrait imaginer effectuer.
Pour illustrer, si on prend n = 60 secondes,
c'est-à-dire les preuves et les théorèmes avec vérifiabilité en 1 minute,
alors 2^n^ = 10^18^ secondes, soit l'âge de l'univers !

Et c'est là qu'on se rend compte de la puissance de la vérification 
si P est différent de NP.
Si tel est le cas, il existe en fait de nombreux problèmes,
comme la vérification des preuves mathématiques,
qui nécessiterait des temps astronomiques à être résolus,
mais qu'on peut vérifier en une minute seulement !

Alors, il existe bel et bien des superintelligences numériques,
ou du moins des réseaux de machines, 
qui sont capables d'effectuer 10^18^ opérations en une seconde ;
on estime par exemple que l'ensemble des mineurs Bitcoin y parvient,
mais aussi les supercalculateurs modernes.
Et du coup, il y a vraient un intérêt à la délégation du calcul,
suivi d'une vérification peu coûteuse.

Cependant, dès qu'on passe à des problèmes un poil plus compliqués,
comme déterminer une preuve d'un théorème avec un temps de vérification de n = 2 minutes,
même la combinaison de tous les supercalculateurs sur Terre
nécessiterait l'âge de l'univers pour y parvenir.
Et si on passe à n = 3 minutes, on peut en fait être raisonnablement confiant
qu'aucune machine sur Terre ne parviendra jamais au bout des calculs nécessairse
à la recherche de ladite preuve du théorème.

En fait, si P est différent de NP, 
c'est que, d'une certaine manière,
un vérificateur peut même vérifier des travaux effectués par une hyperintelligence,
c'est-à-dire un système d'information 
qui transcende les limites calculatoires de l'univers.


## Preuve de connaissance

De façon plus générale,
beaucoup de problèmes en informatique peuvent s'écrire 
comme des fonctions f à deux variables w et x,
et qui disent si (w, x) est une paire valide.
On en a vu un exemple avec la pire `(preuve, théorème)`.
Une telle fonction est dite dans P,
si elle peut se calculer rapidement.
Plus précisément si n_w_ et n_x_ sont les longueurs de description
des messages w et x,
alors le temps de calcul de f doit être au plus (n_w_ + n_x_)^k^,
pour un certain entier k.

Le problème de vérification est alors associé à un problème de recherche :
étant donné une valeur de x, qu'on appelle souvent une instance,
existe-t-il une valeur de w, souvent appelée témoin,
telle que (w, x) est une paire valide ?
Le problème de recherche, qu'on écrit formellement
`∃w, f(w,x)`,
est alors une question binaire à propos de x,
qui répond par oui ou non à la question précédente.
Calculer cette fonction de x est en gros un problème dit NP.  
https://www.scottaaronson.com/papers/pnp.pdf

NB : Pour que le calcul de f soit polynomial,
la longueur de w doit aussi être polynomiale en x.
Donc la bonne formule est plus `∃w, |w| \leq poly(|x|) and f(w,x)`,
où |w| et |x| sont les longueurs de description de w et x
qui sont logarithmiques en le nombre de valeurs qu'ils peuvent prendre.
Par ailleurs, techniquement, 
tout ce qui importe, dans NP, c'est de trouver efficacement les réponses "oui",
c'est-à-dire effectuer efficacement la recherche lorsqu'il existe des solutions.
En particulier, lorsqu'il n'y a pas de bonne réponse,
on n'exige pas que le temps de calculs soit rapide.
Les problèmes où, à l'inverse, on exige une réponse négative rapide 
quand il n'y a pas de solution sont appelés co-NP ;
et être capables de toujours fournir rapidement une réponse 
correspond à la classe NP ∩ co-NP.

La question P versus NP consiste à se demander si tous les problèmes NP,
c'est-à-dire qui peuvent se formuler comme la recherche efficace,
pour toutes les instances, d'un témoin,
sont solubles en temps polynomial.
Et on suspecte fortement que ce n'est pas le cas.
Autrement dit, on suppose que certains problèmes de recherche de solution
nécessitent des temps de calculs supra-astronomiques ;
bien que toute solution qui serait trouvée pourrait être validée 
par un vérificateur peu puissant en quelques minutes seulement.

En particulier, de manière à la fois fascinante intellectuellement
et extrêmement utile dans la pratique surtout en cryptographie,
prouver P ≠ NP prouverait les limites du calculable en pratique,
quelles que soient les machines qu'on utilise.
Ce serait une preuve des limites de toute superintelligence du monde réel,
y compris celles qui sont une combinaisons d'intellects humains et de supercalculateurs.

Ah oui, petite note très rapide, en gros, non,
on ne pense pas que les machines quantiques permettront
de résoudre les problèmes NP.
Elles peuvent être beaucoup plus efficaces pour certains problèmes NP,
comme la factorisation des nombres,
mais elles ne le sont probablement pas pour tous les problèmes NP.

Et alors, P ≠ NP peut être vu comme une terrible nouvelle
pour ceux qui aspirent à l'accessibilité des connaissances par des vérificateurs faibles.
Cependant, on peut au contraire y voir une excellente nouvelle
pour les problèmes d'authentification.

Imaginons que nous soyons un vérificateur faible,
et qu'on ait face à nous un prouveur faible, comme un citoyen lambda avec un smartphone,
ainsi qu'une superintelligence, comme la NSA.
Est-ce que le prouveur faible peut néanmoins prouver son identité au vérificateur faible,
sans que même la superintelligence ne parvienne à l'usurper ?

L'astuce omniprésente de la cryptographie pour ce problème d'authentification,
c'est d'utiliser l'hypothèse P ≠ NP, et la création d'un secret.
On aura le temps de rentrer dans plus de détails mais en gros,
le prouveur faible va choisir un témoin secret w,
et il va générer une instance de problème x pour lequel w est solution.

Ça c'est généralement faisable très facilement.
Par exemple écrivons une expression complexe comme
w^5^ - 4 w^4^ + 2 w^3^ + 15 w^2^ - 64 w,
et en retranchons à cette expression sa valeur pour le nombre entier choisi.
Donc si w = 15,
ça nous fait w^5^ - 4 w^4^ + 2 w^3^ + 15 w^2^ - 64 w = 566040.
Et du coup, on a créé l'équation X^5^ - 4X^4^ + 2X^3^ + 15X^2^ - 64X - 566040 = 0,
dont on connaît une solution.
Bon ce n'est pas l'équation la plus sécurisée, 
on verra d'autres meilleures manières de créer des équations,
notamment à partir de mots de passe et de fonctions de hachage,
mais ça vous donne une idée de comment un prouveur faible
peut créer un problème difficile dont il connaît la solution.  
https://tournesol.app/entities/yt:rO5aQzgKOs0

Le prouveur faible peut alors publier son problème,
qui est ici le message `x = "X^5^ - 4X^4^ + 2X^3^ + 15X^2^ - 64X - 566040 = 0"`,
et affirmé qu'il connaît la solution.
Dès lors, le prouveur pourra être authentifié par sa connaissance de la solution.

En effet, si le vérificateur faible demande au prouveur faible de prouver son identité,
le prouveur faible pourra simplement lui envoyer la solution.
Cependant, et de façon cruciale, si la superintelligence prétend être le prouveur faible,
alors malgré toute sa supériorité en termes de ressources matérielles et humaines,
si le problème du prouveur faible est un problème difficile de la classe NP
et si P est différent de NP,
alors la superintelligence demeurera impuissante,
parce qu'il lui faudra beaucoup plus que l'âge de l'univers pour trouver une solution
au problème fabriqué par le prouveur faible.

Alors, bien sûr, un tel protocole a encore beaucoup de défauts,
et on verra par la suite de nombreuses solutions pour une authentification plus sécurisée.
Mais j'espère vous avoir aidé à comprendre
en quoi le problème P versus NP est au coeur de la cybersécurité,
et comment P ≠ NP peut aider les services juridiques d'un pays
à protéger des citoyens moins armés que des superintelligences,
malgré un rapport de forces humaines et matérielles très inégal.


## La classe IP

Les problèmes NP sont les problèmes 
dont les solutions sont vérifiables par un vérificateur faible.
Voilà qui peut être problématique 
si la solution est en fait trop longue pour être communiquée à un vérificateur faible,
ou si sa vérification requiert elle-même d'énormes calculs.

Les chercheurs en informatique se sont ainsi demandés 
si on ne pouvait pas généraliser la classe NP,
et envisager la vérification de solutions à des problèmes plus complexes encore,
en introduisant potentiellement plusieurs interactions entre le vérificateur et le prouveur,
et en s'autorisant des conclusions uniquement avec très grande probabilité,
plutôt que des réponses déterministes comme pour NP.

Voilà qui les a conduits à définir la classe des problèmes IP,
pour Interactive Proof, ou preuve par interaction.
Un problème est IP si un prouveur arbitrairement puissant 
qui a effectivement résolument le problème peut convaincre
le vérificateur faible que c'est le cas ;
et si un prouveur arbitrairement puissant 
qui n'a pas résolu le problème ne pourra pas y arriver.

Plus précisément, les deux conditions sont les suivantes :
1. Quand la réponse est "oui", 
un prouveur arbitrairement puissant est capable de convaincre 
avec grande probabilité le vérificateur que la réponse est oui,
après un nombre au plus polynomial d'échanges ;
2. Quand la réponse est "non", 
aucun prouveur, aussi puissant et malveillant soit-il,
ne pourra convaincre le vérificateur que la réponse est "non",
si ce n'est avec une très faible probabilité.

Comme on va le voir dans la suite de cette série,
les preuves IP sont en fait encore un peu plus 
au coeur des solutions les plus spectaculaires de la cryptographie moderne,
notamment quand il s'agit de fournir des preuves d'authentification
avec divulgation nulle de connaissance.
Et de manière remarquable, 
on suspecte qu'elles permettent au vérificateur de vérifier des problèmes
qui sont tellement complexes qu'ils ne sont pas NP,
à savoir des problèmes de recherche de témoins 
tels que prouver la validité d'un témoin ne peut pas se faire en temps polynomiale.

Plus précisément, on a démontré que les interactions multiples
permettent de résoudre des problèmes de la classe PSPACE,
c'est-à-dire les problèmes résolubles avec une place mémoire polynomiale,
mais dont le temps de calcul est arbitrairement grand.
Autrement dit, IP = PSPACE.

Or on suspecte également PSPACE d'être strictement plus grand que NP,
c'est-à-dire que certains problèmes de recherches de solution
qui n'ont pas de vérifiabilité de solution efficace
peuvent néanoins moins être résolus avec une place mémoire raisonnable,
ou, donc, peuvent être communiqués de manière convaincante 
à un vérificateur faible via des interactions multiples.

Un exemple de problème PSPACE qui ne semble pas dans NP 
est le calcul de la formule de Bayes,
lorsqu'on considère un nombre exponentiel de théories,
chacune étant polynomialement efficace en mémoire 
pour effectuer des prédictions.
En discutant, une superintelligence pourrait en principe me convaincre
de la validité de ses calculs,
même si elle pourrait être incapables de m'expliquer tous ses calculs.

Un autre exemple est celui de certains jeux de plateaux, comme le Hex et le Reversi.
Une hyperintelligence serait en mesure de nous convaincre
qu'elle possède effectivement la stratégie optimale à ces jeux.

On peut même définir des variantes de la classe IP,
comme les classes MIP et IOP,
où l'idée est à chaque fois d'ajouter des contextes d'échanges
qui permettent au vérificateur de vérifier plus en travaillant moins.
Dans les problèmes MIP, pour Multiprover Interactive Proof,
le vérificateur peut interroger plusieurs prouveurs qui connaissent chacun la réponse,
mais il peut les séparer pour les interroger 
sans qu'aucune ne puisse communiquer avec l'autre.
Ce n'est pas forcément très réaliste sur le web,
mais ce concept est en fait très utile pour concevoir 
des arguments succincts de connaissances sans interaction, comme on va en parler bientôt.
De manière spectaculaire, on a démontré que la classe MIP est équivalente à NEXPTIME,
la classe des problèmes de recherche dont la vérification est possible en temps exponentielle.
Et pour le coup, on a démontré que cette classe était strictement plus grande que NP,
et donc que P,
ce qui montre qu'un problème difficile de la classe MIP 
ne pourra pas être résolu par une superintelligence,
y compris dans le cas où P = NP.

Enfin, dans les problèmes IOP, pour Interactive Oracle Protocol,
le vérificateur a la capacité de laisser parler le prouveur très longtemps
en l'ignorant complètement, 
sauf pour attraper quelques informations précises choisies par le vérificateur.
Et surtout, le vérificateur ne perd aucun temps ni travail
à laisser parler le prouveur très longtemps ;
un peu comme si le prouveur parlait infiniment vite,
sauf au moment de dire les informations que le vérificateur veut noter.
Là encore c'est a priori difficile de réussir cette prouesse en pratique ;
mais ce qui importe, c'est qu'on peut l'exploiter pour concevoir 
des arguments succincts de connaissances sans interaction.


## Les SNARK

Dans tous les protocoles IP, MIP et IOP,
le vérificateur exploite le hasard, pour lancer des défis au prouveur.
Et c'est le fait que le prouveur soit incapable d'anticiper ce hasard,
qui fait que le vérificateur peut vérifier les propos du prouveur 
avec relativement peu d'efforts.

Eh bien, en 1986, les informaticiens Amos Fiat and Adi Shamir
ont proposé de laisser le prouveur simuler ce travail du vérificateur.
Autrement dit, le prouveur va lui-même se lancer des défis au hasard.
Mais pour que le prouveur ne puisse pas contrôler ce hasard,
on va aussi lui imposer un procédé pour générer le hasard ;
ou plutôt, pour se lancer un défi qu'il ne pouvait pas avoir anticipé
avant de se lancer dans l'opération de preuve.
En pratique, à chaque fois que le vérificateur devait lui lancer un défi aléatoire,
le prouveur va devoir prendre toutes les données du problèmes,
et les rentrer dans un générateur de nombre aléatoire,
qui va typiquement s'appuyer sur une fonction de hachage cryptographique,
un objet dont je vous ai parlé dans un épisode de String Theory.  
https://tournesol.app/entities/yt:rO5aQzgKOs0

En effet, on pense aujourd'hui, même si on ne l'a pas démontré,
qu'il extrêmement difficile de prévoir l'issue de la fonction de hachage cryptographique,
étant donné son entrée, à part en devinant au hasard,
ou en effectuant le calcul de la fonction de hachage cryptographique.
Et du coup, une telle fonction nous semble bien simuler le hasard,
notamment le hasard au sens de Laplace et du bayésianisme,
à savoir des informations autrement imprévisibles.

Quoi qu'il en soit, en utilisant une telle fonction pour simuler les défis du vérificateur,
le prouveur peut donc simuler un échange entre lui et le vérificateur,
ou même entre le vérificateur et plusieurs prouveurs indépendants,
ou même avec un vérificateur qui n'écoute qu'une poignée d'informations
envoyées par le prouveur.
Il peut ensuite envoyer un transcript de l'échange au vérificateur.

Eh bien, ça, c'est devenu le Saint-Graal de la vérification !
Grâce à l'algorithme de Fiat-Shamir, à partir de preuves IP, MIP ou IOP,
on a obtenu un transcript qu'on appelle 
un argument succinct de connaissance sans interaction,
ou SNARK, conformément à l'acronyme anglais.
Un SNARK, c'est un peu comme une preuve dans un problème NP, 
c'est-à-dire qu'il permet à un prouveur de convaincre un vérificateur 
qu'il connaît la solution à un problème difficile,
que le vérificateur n'a pas les moyens de résoudre lui-même
(potentiellement parce que le problème a été conçu par le prouveur,
à partir de la solution).

Cependant, les SNARK ont trois spécificités importantes,
qui les distinguent des preuves des problèmes NP :

1) Le SNARK est beaucoup plus court la preuve du problème NP.
Voilà qui permet notamment à un vérificateur faible de le vérifier très facilement,
même pour des problèmes extrêmement complexes ;
potentiellement plus difficiles à résoudre que des problèmes NP.
Le fait que le SNARK soit très court permet aussi au vérificateur 
de collecter et de compiler les preuves dans une base de données,
et ainsi d'assurer la validité d'un très grand nombre d'opérations à l'aide de SNARK.
On retrouve typiquement abondammment les SNARK dans les systèmes type Blockchain.

2) Mais le contre-coup, c'est que le SNARK n'est valide qu'avec très grande probabilité.
Mais son nombre de bits de sécurité informationnel est tellement grand que,
en pratique, on peut considérer tous les SNARKs produits dans le millénaire à venir
comme valides avec grande probabilité.

3) Et par ailleurs, le SNARK n'est valide que si les prouveurs qui l'ont produit 
ont une puissance de calcul limitée.
Pour le préciser, on dit parfois que les SNARK sont des *arguments*,
plutôt que des *preuves*.
Cependant, si on suppose P ≠ NP, 
et si on conçoit les SNARK avec un nombre de bits de sécurité calculatoire suffisant,
typiquement de l'ordre de 120 bits,
alors même une superintelligence sera incapable de produire des SNARK trompeurs,
dans le sens où ils seront acceptés par le vérificateur,
alors que le vérificateur ne devrait pas les accepter.

En fait, en pratique, 
on peut considérer que les faiblesses (2) et (3) des SNARK
ne sont pas des limitations pratiques.
Voilà qui suggère que les SNARK sont des solutions extrêmement puissantes
pour permettre à un vérificateur faible 
d'exiger des preuves de la part d'une superintelligence
que ladite superintelligence se conforme bien avec les exigences du vérificateurs faibles,
come par exemple la loi.

Est-ce qu'on pourrait par exemple utiliser les SNARK
pour exiger des concepteurs des intelligences artificiels,
qu'ils prouvent à des juristes que leurs données d'entraînement
ne violent pas des droits d'auteur ou des données personnelles ?

Peut-être. Honnêtement, on est vraiment là à la frontière de la connaissance,
à la fois en droit et en intelligence artificielle, 
mais aussi en cryptographie.
Ce que je peux vous dire, c'est que de plus en plus d'articles de recherches
explorent le machine learning vérifiable,
en combinant ses opérations à la conception de SNARK.  
https://ieeexplore.ieee.org/abstract/document/9454203  
https://ieeexplore.ieee.org/abstract/document/10379135  
https://link.springer.com/chapter/10.1007/978-3-031-54773-7_15

Et d'ailleurs, ces articles vont souvent chercher à défendre le concepteur aussi,
en rendant les SNARK "sans divulgation de connaissance"
(on parle de zk-SNARK pour zero-knowledge SNARK),
c'est-à-dire que les SNARK prouvent juste la validité de certains calculs
de réseaux de neurones,
sans dévoiler quoi que ce soit à propos du détail de ces réseaux de neurones.

Et bon, les articles que j'ai vu s'intéressent surtout à l'inférence,
donc typiquement quand vous jouez avec des algorithmes génératifs déjà entraînés,
et semblent ainsi encore loin de pouvoir répondre à la question juridique
que j'ai soulevée plus haut.

Il y a encore beaucoup de travail fascinant pour les chercheurs,
qu'il serait peut-être bon de prioriser,
dans un monde que les superintelligences que sont Google et compagnie
ont déjà remplis de technologies extrêmement peu vérifiables ;
et extrêmement peu vérifiées.


## Conclusion

Les limites calculatoires peuvent paraître insatisfaisantes
pour ceux qui considèrent la connaissance comme le Graal ultime.
Cependant, j'espère que j'ai pu vous faire sentir aujourd'hui
en quoi ces limites calculatoires sont en fait une bénédiction,
pour se protéger de superintelligences capables d'effectuer
beaucoup plus d'opérations que nous, 
grâce à leurs ressources humaines et matérielles.

En particulier, c'est assez remarquable que,
grâce à des problèmes NP,
un prouveur faible peut être mis sur la même marche que cette superintelligence,
même avec un arbitre faible.
Voilà qui semble par exemple essentiel
pour rétablir un droit d'amplification proportionné en ligne,
qui paraît beaucoup plus indispensable que la liberté d'expression.
Et oui, tant qu'on ne régule pas l'amplification en ligne à l'aide de cryptographie,
les superintelligences malveillantes,
armées de fermes de trolls humains et électroniques,
seront capables d'exploiter la supériorité de leurs moyens de production et de diffusion
de l'information pour imposer leurs propagandes,
et noyer la parole citoyenne.

Certes, il y a un million de dollars en jeu pour le problème P versus NP.
Mais j'espère que je vous ai convaincu qu'il y a en fait beaucoup plus que cela en jeu.
L'hypothèse P ≠ NP est vraiment la pierre angulaire de nombreuses solutions cryptographiques,
qu'il me semble indispensable de mieux comprendre et de faire comprendre,
ainsi que de faire adopter massivement.
Mais surtout, on peut même aller au-delà de cette hypothèse.
Grâce aux SNARK, et aux preuves à divulgation nulle de connaissance,
il est en fait certainement possible d'importer en ligne un très grand nombre
des propriétés de délibération citoyenne hors ligne,
notamment des notions de confidentialité du votes, d'anonymat des lanceurs d'alerte
ou encore de vérifiabilité des décomptes des voix.

Mais pour espérer un jour en arriver là,
si possible avant l'effondrement enclenché des démocraties à travers le monde,
il va nous falloir investir beaucoup plus de ressources humaines, matérielles et financières,
dans une véritable stratégie de cyberdéfense de l'espace numérique,
que ce soit à l'échelle individuelle, à l'échelle de nos organisations,
ou à l'échelle de nos démocraties,
en devenant tous beaucoup plus des acteurs informés de la cybersécurité.

Pour protéger nos démocraties et les nombreux systèmes numériques sur lesquels elle s'appuie,
on a désespérément besoin de s'armer contre toutes sortes de superintelligences déjà existantes.

