# Les mathématiques de l'impossible

Il y a quelques mois, un groupe de chercheurs, dont je fais partie,
a publié en preprint un article qui récapitule 
les théorèmes mathématiques d'impossibilité de sécurité 
des grands modèles de machine learning à hautes performances.

En particulier, on y rappelle le théorème suivant, qui résulte d'une combinaison d'articles :
Pour tout algorithmes de minimisation d'une fonction de perte (même supposément rendus "sécurisés"),
il existe une instance différentiable et une attaque par empoisonnement telles que,
à terminaison, le gradient de la fonction de perte restreinte aux vraies données
sera de taille supérieure à une mesure de l'hétérogénité des données honnêtes.

Notre article liste par ailleurs des raisons de penser que, 
dans de nombreux cas d'applications comme les algorithmes de langage et les IA de recommandation,
l'hétérogénéité des données honnêtes est énorme,
surtout lorsque les modèles d'apprentissage ont un très grand nombre de paramètres.
Voilà qui suggère que l'algorithme d'apprentissage aura très mal appris, une fois attaqué.
C'est notamment cela qui nous pousse à présumer l'extrême manipulabilité de toute IA avec beaucoup de paramètres,
et à appeler à l'interdiction des IA avec beaucoup trop de paramètres,
comme le demande explicitement mon co-auteur El Mahdi El Mhamdi dans une interview (Canal+?) Usbek et Rica ---
en fait, il n'y a pas que la manipulabilité des IA ; 
il y a aussi leur incapacité à apprendre des facultés spectaculaires 
sans aussi apprendre des informations sensibles, voirement extrêmement sensibles,
violant ainsi les lois déjà existantes sur les droits d'auteur et le RGPD.

Cependant, comme beaucoup semblent perturbés par la possibilité de théorèmes d'impossibilité,
ou sur le sens à donner à ces théorèmes,
y compris d'ailleurs des académiques, 
et même en particulier des chercheurs en machine learning 
qui ne sont pas tous toujours les plus fins sur les subtilités mathématiques,
je me suis dis que ça vaudrait la peine de parler 
un peu des théorèmes d'impossibilité de manière générale,
pour mieux cerner ce qu'ils impliquent, 
et dans quelles mesures l'impossibilité est contournable.

Et pour bien rendre tous ces problèmes concrets, 
on va s'attarder sur un problème très simple : le calcul sécurisé d'une moyenne.

## La sécurité d'une moyenne

Imaginons qu'on cherche à estimer la fortune moyenne de 5 traders de la finance.
Supposons que chaque trader connaît sa fortune ; mais aussi qu'il est le seul à la connaître.
Pour déterminer la fortune moyenne, on peut demander à chaque trader de nous la révéler,
et on peut ensuite prendre la moyenne des nombres révélés par les traders.

Mais pour éviter que chaque trader n'ait à révéler sa fortune à ses confrères,
ce qui pourrait leur donner beaucoup d'incitatifs à mentir,
d'ailleurs aussi bien à la baisse qu'à la hausse,
on demande à chaque trader de noter sa fortune dans une machine ultra sécurisée,
dont ne sortira que le résultat du calcul de la moyenne.
Autrement dit, la collecte de donner et les calculs forment une boîte noire,
d'où il est impossible de sortir une quelconque information.

Si ce que je dis là est très hypothétique, 
notez qu'il s'agit en fait d'un dispositif en fait très réaliste,
surtout si on intègre des principes de chiffrements homomorphes.
Mais même sans chiffrement, il existe des solutions à base de calcul réparti sécurisé,
qui permettent d'obtenir les propriétés de la boîte noire que j'ai décrite ;
et je vous invite d'ailleurs à y réfléchir et à proposer de telles solutions en commentaires.

Bref. Ces détails de privacy sont intéressants, 
mais ce n'est pas ce qui va nous préoccuper aujourd'hui.
Supposons que l'on ait mis en place une telle boîte noire.
À quelle point est-elle sécurisée vis-à-vis de sa sortie ?
Ou plus précisément, à quel point peut-on garantir que la moyenne calculée par la boîte noire
est bien une bonne estimation de la moyenne des fortunes des traders ?

Eh bien, j'ai envie de dire aucunement. 
En effet, il suffit qu'un seul des 5 traders soit malveillant, 
pour qu'il puisse discréditer complètement le résultat.
Ainsi, s'il annonce que sa fortune en euros est 5 fois supérieure au nombre de particules dans l'univers,
alors le mécanisme va conclure que le salaire moyen des 5 traders sera supérieur
au nombre de particules dans l'univers.

Bref. La moyenne a une très mauvaise sécurité.
Mais peut-on faire mieux. 
Est-il possible de modifier la boîte noire, pour une estimation plus sécurisée de la moyenne ?
Mais surtout, quelle sera vraiment la garantie de sécurité ainsi obtenue ?
À quoi ressemble une garantie de sécurité ?

Si vous avez suivi ma chaîne, et en particulier si vous avez vu cette vidéo,
ou celle-ci, ou celle-là, ou encore cette autre vidéo,
une réponse pourrait vous sauter aux yeux : utiliser la médiane plutôt que la moyenne.
Autrement dit, la boîte noire collecte à nouveau les fortunes déclarées des traders.
Cependant cette fois, au lieu d'en calculer la moyenne,
elle trie les fortunes déclarées et rapporte celle du milieu.

OK. Mais quelle garantie de sécurité aura-t-on alors pour cette médiane ?
Que peut-on garantir de l'erreur entre la médiane et la vraie fortune moyenne des traders ?

Eh bien, il y a de nombreuses manières de formaliser cette question et d'y répondre.
Pour aujourd'hui, je vous propose une réponse simple.
Tant que la majorité des traders répond honnêtement,
on a la garantie qu'il existe un trader mieux payé que la médiane estimée,
et un trader moins bien payé qu'elle.

En effet, si la majorité des traders sont honnêtes, 
ça veut dire que 3 d'entre eux ont dit vrai.
Mais alors, peu importe les valeurs rapportées par les traders malhonnêtes,
la médiane des 5 valeurs déclarées sera forcément à droite du trader honnête le moins bien payé,
et forcément à gauche du trader malhonnête le mieux payé.

En cela, pourvu que la majorité des traders est honnête,
le résultat de notre boîte noire représentera quelque chose de concret,
à propos des fortunes des traders.


## Anatomie des théorèmes de sécurité et d'impossibilité

Si je vous ai décrit ce problème d'estimation de la moyenne,
ce n'est pas tant pour vous montrer toute la richesse de ce problème ---
même si j'espère que vous imaginez les jolies mathématiques qui en résultent,
surtout lorsqu'on passe en dimensions supérieures.

Ce qui m'intéresse en tout cas aujourd'hui, 
c'est surtout de bien comprendre la notion de sécurité mathématique.
Une preuve de mathématique de sécurité, 
c'est quelque chose qui prend généralement la forme suivante :

Il existe un algorithme (ici la médiane) tel que,
Pour toutes données fournies par des utilisateurs honnêtes (ici au moins 3 traders),
Et pour toute attaque contre cet algorithme appartenant à une classe d'attaques considérée (ici la déclaration malhonnête de 2 traders),
L'algorithme fait quelque chose de raisonnable (ici donner une grandeur encadrée par les vraies fortunes de deux traders).

Les théorèmes mathématiques de sécurité sont généralement de la sorte.
Par exemple, en cryptographie, un théorème fondamental est le suivant :

Il existe un algorithme de chiffrement tel que,
Pour toutes données à chiffrer,
et pour toute attaque cherchant à déchiffrer le message chiffré,
l'attaque appliquée aux données chiffrées par l'algorithme échouera à déchiffrer les données.

En fait, exprimé ainsi, le théorème est faux, 
notamment parce qu'il faut interdire à l'attaquant d'avoir accès aux clés du chiffrement.

Et la manière d'y arriver classiquement est du supposer cette clé aléatoire,
et d'interdire l'attaquant de l'utiliser pour déchiffrer les données.
Mais comme il y a de l'aléatoire qui est introduit, la garantie ne peut plus être déterministe ;
on cherche alors une garantie avec très grande probabilité.
Autre précision à ajouter : l'attaquant doit être restreint à des algorithmes rapides,
ou plus précisément dont le temps de calcul est polynomial.
Enfin, dernier détail, et de taille : ce théorème de sécurité du chiffrement n'est pas démontré.
En fait, la sécurité du chiffrement actuel n'est qu'une conjecture,
dont la démonstration requiert au moins celle du fameux problème P versus NP,
qui est le problème le plus prestigieux de l'informatique théorique.
Bref. Tout ça pour dire que la sécurité du chiffrement est un peu plus complexe à exprimer,
mais elle repose fondamentalement sur les mêmes mécaniques 
que le théorème de sécurité qu'on a vu pour la médiane.

Autre exemple de théorème de sécurité : celui dont j'ai parlé dans le Vortex.
Il existe un algorithme de communication et de décision tel que, 
Pour toutes suggestions de décision des quatre généraux honnêtes,
et pour tout comportement des généraux malhonnêtes,
ou bien au moins deux généraux honnêtes attaqueront, ou bien aucun n'attaquera.

Bien sûr, là encore, 
il y a plein de précisions à formaliser pour rendre le théorème de sécurité vraiment mathématique.
Mais mon but ici n'est pas de rentrer dans ces détails ;
il s'agit de vraiment comprendre surtout l'anatomie des théorèmes de sécurité.

Ainsi, formellement, la sécurité mathématique, ça prend la forme : 
il existe un algorithme tel que pour toute instance et toute attaque, tout va bien.

OK. Mais donc qu'est-ce que serait une impossibilité mathématique de sécurité ?
Et bien, il s'agit tout simplement de la négation de la sécurité.
Une impossibilité de sécurité, c'est un théorème qui prend la forme :
Quelque soit l'algorithme (supposément sécurisé),
il existe une instance et une attaque tel que,
l'exécution de l'algorithme pour cette instance et sous cette attaque sera dangereuse.

Et pour être concret, on peut formaliser l'impossibilité de sécuriser le calcul exact de la moyenne :
Quelque soit votre algorithme de calcul de la moyenne,
il existe une instance (disons, 5 traders qui disent 1000, dont 4 sont honnêtes)
et une attaque (disons le 5e trader dit 0),
telle que la sortie de l'algorithme n'est pas la vraie fortune moyenne.

Et pour être clair même cette version triviale de théorème d'impossibilité n'est pas complètement triviale.
Oui, si on considère que l'algorithme est la moyenne, 
alors le contre-exemple que j'ai esquissé montre que l'algorithme se trompe.
Mais la difficulté est qu'il faut démontrer l'impossibilité pour tous les algorithmes. 
Pas juste la moyenne !

Bon ceci dit, le cas que je viens de citer n'est pas non plus difficile,
et j'invite les matheux parmi vous à le démontrer.
Voire à démontrer des versions plus fortes, 
comme le fait qu'il ne peut pas y avoir de bornes d'erreur dadns l'estimation de la moyenne.

L'exemple de notre article est l'impossibilité du machine learning sécurisé :
Pour tout algorithmes de minimisation d'une fonction de perte (même supposément rendus "sécurisés"),
il existe une instance différentiable et une attaque par empoisonnement telles que,
à terminaison, le gradient de la fonction de perte restreinte aux vraies données
sera de taille supérieure à une mesure de l'hétérogénité des données honnêtes.

Et on pourrait aussi prendre l'exemple du théorème FLP de la vidéo précédente :
Pour tout algorithme distribué de communication et de prise de décision,
Il existe une instance et une attaque (qui consiste juste en une panne d'une machine),
tel que l'algorithme conduira ou bien à des décisions divergentes, 
ou bien à des décisions toujours triviales, ou bien à une absence de prise de décision.

Bref. Notre théorème d'impossibilité n'est vraiment pas particulier.
Il s'inscrit dans une longue tradition de théorèmes d'impossibilité.

## Contourner et affiner l'impossibilité

Ceci étant dit, si notre théorème d'impossibilité est, je pense, 
le théorème naturel auquel aboutirait un mathématicien 
qui souhaite étudier la sécurité du machine learning à la manipulation par l'empoisonnement,
il est bien sûr limité ; comme tous théorèmes d'impossibilité.
En particulier, il peut être possible de "contourner" un théorème d'impossiblité,
en modifiant 3 composants du théorèmes.

Pour rappel, un théorème d'impossibilité est de la forme :
Pour tout algorithme (supposément sécurisé),
il existe une instance (d'un ensemble d'instances) tel que,
il existe une attaque (d'un ensemble d'attaques) tel que
ça n'ira pas bien.

Le théorème n'est bien sûr plus valide si on change la formalisation de "ça n'ira pas bien".
Et d'ailleurs, un problème ouvert fascinant de la sécurité du machine learning,
ça consiste justement à avoir des définitions plus pertinentes de "ça n'ira pas bien",
que celle proposée dans notre article ;
c'est notamment ce que mes co-auteurs ont fait dans un nouvel article récemment publié ---
même si l'impossibilité était déjà trivialement déduite de celles qu'on avait déjà prouvées.

CITATION

> Leur grosse contribution est plus le théorème de sécurité complémentaire,
pour une certaine famille d'instances qui n'avaient pas été particulièrement étudiées précédemment.

De même la Blockchain a "contourné" l'impossibilité FLP dont on a parlé dans la vidéo précédente,
en affaiblissant le "ça n'ira pas bien".
Le théorème de sécurité de la Blockchain considère ainsi que "ça va bien",
même lorsque des décisions précédemment effectuées sont finalement rejetées,
pourvu que ces cas sont suffisamment peu probables.

Mais modifier la notion de "ça n'ira pas bien" n'est pas la seule façon 
de contourner un théorème d'impossibilité.
Une autre approche consiste à modifier l'ensemble des attaques considérées.
Ou dit autrement, un algorithme non-sécurisé contre des attaquants puissants
peut tout à faire être sécurisé contre des attaquants beaucoup moins puissants.

Cet affaiblissement des attaquants est typiquement au coeur de presque toute la cryptographie,
qui suppose généralement que l'attaquant n'a qu'une puissance de calcul limitée,
et est en particulier incapable de résoudre des problèmes comme la factorisation des grands nombres
en temps raisonnable,
ou résoudre les problèmes de "Proof of Work" exigés par la Blockchain.

Il faut toutefois faire très attention à ne pas sous-estimer les attaquants,
surtout à l'heure du progrès technologique fulgurant et de l'explosion exponentielle du cybercrime.
Selon de nombreuses sources, les attaquants disposent de revenus 2 à 3 fois supérieurs
au PIB de la France !

Enfin, une troisième façon de contourner l'impossibilité,
qui est de loin la plus prometteuse dans le cas du machine learning,
cela consiste à caractériser plus précisément les instances de machines learning rencontrées en pratique ;
et en particulier pour les algorithmes de langage et les IA de recommandation.
Ainsi, si ces problèmes ont en fait un profil particulier,
il pourrait éventuellement être possible de concevoir des IA sécurisées pour ces cas particuliers,
et qui ne seraient pas sécurisées dans un cadre plus général.

C'est typiquement l'approche qui est utilisée pour contourner des impossibilités en théorie des graphes.
Alors qu'aucun algorithme ne peut rapidement calculer certaines propriétés des grands graphes,
il peut être possible qu'un algorithme y parvienne pour tous les graphes d'une certaine structure.

Cependant, à ce jour, il ne me semble y avoir aucun travail scientifique
ayant identifié des propriétés fondamentales des données de langage et de recommandation,
qui permettraient de concevoir des algorithmes sécurisés 
pour tous les problèmes de machine learning ayant ces propriétés fondamentales.
En l'occurence, j'ai même une présomption d'absence de telles propriétés fondamentales ;
ou dit autrement, je pense que ces applications ont les caractéristiques 
de la difficulté générale de sécuriser les algorithmes d'apprentissage.

Bien sûr, on sort là du cadre des mathématiques, 
puisqu'on parle de choses non seulement non démontrées,
mais surtout beaucoup plus difficilement formalisables.

Toujours est-il que l'état des connaissances scientifiques à l'heure actuelle 
me pousse largement à penser que la sécurisation des IA est très largement impossibles,
tant que celles-ci ont un très grand nombre de paramètres et visent sérieusement la performance ;
et plus encore que beaucoup d'IA spectaculaires déjà déployées massivement 
sont extrêmement non-sécurisées ; et même très illégales.

Et pour contourner cette impossibilité, 
il faudra au préalable avoir développé des arguments convaincants
qui montrent que les instances considérées par ces IA sont en fait très spécifiques,
et se prêtent particulièrement bien à la sécurisation.



