# Le principe fondamental de la cybersécurité

Comment éviter qu'une mise à jour défaillante de l'un des nombreux logiciels
utilisés par le système d'information de votre organisation
ne provoque à une panne majeure
qui force l'interruption de votre activité, pendant plusieurs jours,
et qui implique des pertes désastreuses ?

Comment protéger le socle informationnel de votre organisation,
et empêcher l'industrie grandissante du cybercrime d'infiltrer vos processus internes,
de réaliser une arnaque en provoquant des transferts d'argent illicites,
d'effectuer une exfiltration des données de vos clients et de vos secrets industriels
ou d'exiger une rançon pour restaurer des machines de traitement d'information paralysées ?

Eh bien, pour répondre à ces questions, 
en ce moment même on est en train de publier un livre chez Dunod avec Romain du Marais, 
vulgarisateur de la chaîne Pour 1nf0 et responsable de la sécurité des systèmes d'information.
Le livre s'intitule "Guide de survie au cybercrime",
et il commence par une préface de Guillaume Poupard,
qui est un peu le big boss de la cybersécurité en France.

Bien entendu, je ne vais pas pouvoir résumer ce livre en trois mots.
Mais s'il fallait retenir un principe de notre livre,
c'est probablement la notion de *défense en profondeur*.
Tel est, selon nous, un des principes fondamentaux de la cybersécurité.


## La défense en profondeur

En fait de nos jours, pour toutes les organisations,
la question n'est plus de savoir « si » on sera attaqué dans le cyber espace.
Vu la croissance terrifiante de l'industrie du cybercrime,
et ses coûts engendrés sur la société qui ont été estimés 
à 11 mille milliards de dollars en 2023 ---
je répète, 11 mille milliards de dollars, soit 4 fois le PIB de la France ! ---
ce n'est qu'une question de temps avant que votre organisation soit attaquée.

> @RduMarais : En fait elle est déjà attaquée, 
> mais soit vous ne le savez pas... et c'est un problème,
> soit ce ne sont que des attaques simples qui n'ont pas encore réussi 
> à faire des dégâts visibles.
> Mais du coup, ça ce n'est qu'une question de temps
> avant que vous intéressiez des attaquants plus costauds !

La question qu'il faut se poser, 
c'est donc pas « si » on sera attaqué
mais plutôt « et alors ? ».
Et ainsi anticiper les attaques et prendre les mesures les plus pertinentes
pour minimiser les impacts de ces attaques 
sur votre organisation.

Autrement dit, la défense en profondeur, 
c'est l'idée qu'il ne faut jamais concevoir un système informatique
en se disant qu'il ne sera jamais piraté.
Au contraire, il faut vraiment le concevoir de sorte que même une fois compromis,
les attaquants ne pourront pas provoquer de dégâts.

Une image à avoir en tête est typiquement celle du "fromage suisse".
Aucune couche de défense ne doit être considérée incontournable ;
après tout, tout antivirus peut échouer à détecter certains virus,
tout logiciel peut avoir écrit avec des failles
et toute machine peut avoir des portes dérobées.
Mais en empilant adéquatement les couches de défense, 
même si chacune a ses trous, au bout d'un moment vous êtes quand même suffisamment bien protégés.
https://en.wikipedia.org/wiki/Swiss_cheese_model

Ainsi, si on imagine que la probabilité qu'un attaquant perce une couche est égale à 10%,
le fait de devoir percer 10 couches, en supposant les probabilités indépendantes,
ça va être égal à (10%) puissance 10,
ce qui fait 1 chance sur 10 milliards.
Voilà qui confère une protection beaucoup plus grande qu'une couche robuste à 99,99%.


## Divers principes opérationnels

En pratique, la défense en profondeur c'est difficile à implémenter,
Parce qu'on ne conçoit pas le système d'information de zéro, 
Mais on doit faire avec un grand nombre de composants potentiellement défectueux.

Donc ce principe de défense en profondeur, il va se décliner en plein de façon de mettre de la sécurité
à tous les niveaux du SI :
c'est protéger l'accès au SI pour ne pas être piraté, 
c'est aussi concevoir des systèmes difficiles à pirater au cas ou ça arrive,
empêcher que le piratage d'un composant permette d'accéder à un autre,
et même finir par une couche de détection... au cas où tout ça n'a pas marché.

Dans le livre, on part de plein d'exemples concrets,
et au fil du livre on identifie un certain nombre de principes opérationnels,
auxquels il est utile de penser pour renforcer notre défense en profondeur.

Par exemple, un principe important c'est de miser sur la redondance des solutions,
et aussi sur leur diversification.
C'est indispensable quand il s'agit de sauvegardes ou d'authentification.
Typiquement, je vous invite très vivement à utiliser des mots de passe radicalement différents
pour les différents services informatiques que vous utilisez,
de sorte que, même si l'un de vos mots de passe parvient à être deviné par un attaquant,
l'attaquant demeure incapable d'accéder aux autres services informatiques que vous utilisez.

De même, il est critique de ne pas garder les sauvegardes de données à un même endroit,
ou de permettre l'accès à ces sauvegardes par une machine qui est utilisée pour autre chose.
Parce qu'il suffira alors à l'attaquant d'accéder à cette machine,
pour ensuite pourrir toutes les sauvegardes,
et effectuer une attaque par ransomware dévastatrice.

Ce genre d'attaques est très courante !
Elle va chiffrer toutes les données de l'organisation,
de sorte à paralyser complètement son activité,
et exiger une rançon pour restaurer vos données.

Autre principe opérationnel essentiel : le monitoring de votre système d'information.
Il vous faut constamment avoir accès et analyser toutes sortes d'opérations sur vos machines,
de sorte à identifier toute anomalie suspecte aussi vite que possible,
et bloquer les attaquants avant qu'ils ne parviennent à accéder 
aux parties les plus sensibles de votre réseau.

D'ailleurs, pour ralentir, voire bloquer, les attaquants dans leurs démarches,
il est aussi indispensable de décomposer votre système en un grand nombre de composants,
et à limiter les droits de chaque composant aux **moindres privilèges** nécessaires.
C'est typiquement ce que font déjà les téléphones et les navigateurs web,
en interdisant l'accès d'une application ou d'un onglet à la caméra ou au microphone 
de votre machine.
Ainsi, votre système d'information ressemblera à une sorte de sous-marin,
avec un grand nombre de compartiments distincts,
et avec une conception telle que l'infiltration d'un compartiment
puisse être restreinte uniquement à ce compartiment,
sans mettre en péril les autres compartiments du sous-marin.
On parle dans le jargon de cloisonnement, d'isolation ou de sandboxing des composants.

Mais s'il y a un seul conseil opérationnel que je devais vous donner,
ce serait davantage, et de très loin,
le principe qui consiste à réduire au maximum la surface d'attaque,
c'est-à-dire le nombre de portes d'entrée 
par lesquels les attaquants pourront infiltrer votre système d'information,
à l'instar des chateaux-forts dont la seule entrée accessible est un pont levis.
Pour minimiser la surface d'attaque, rien de plus simple.
En fait ça revient à appliquer tout simplement une certaine sobriété numérique,
c'est-à-dire de minimiser le nombre de logiciels,
d'extensions navigateurs ou de fonctionnalités à déployer.
Plus votre machine sera spécialisée dans un petit nombre de tâches précises,
et conçue pour ne réaliser que ces tâches, plus vous serez protégés.

Et bon, malheureusement, en pratique,
le marketing des géants du numérique va complètement à l'encontre de ce principe,
en proposant des solutions fourre-tout,
ou cherchant à intégrer toutes sortes de gadgets peu utiles,
notamment à base d'algorithmes génératifs.
Méfiez-vous sérieusement de ce genres de solutions pseudo-futuristes,
mais dont la valeur ajoutée ne justifie pas nécessairement 
l'exposition à des risques additionnels.


## Devenons tous acteurs de la cybersécurité

Dans notre livre, Romain et moi considérons 
que le système d'information de votre organisation,
c'est, eh bien, tout ce qui permet à votre organisation
d'effectuer l'ensemble des tâches informationnelles auxquelles elle confrontée.
Bien sûr, cela inclut les disques durs qui stockent l'information,
les processeurs qui traitent et modifient l'information,
les réseaux qui permettent la réception et la communication de l'information,
et les nombreux postes de travail et smartphones,
qui permettent à vos collaborateurs d'interagir avec les technologies d'information.

Mais ce n'est pas tout.
Pour nous, vos collaborateurs sont aussi des éléments essentiels
de vos systèmes d'information,
ce qui impliquent que eux aussi peuvent être des composants faillibles,
ou, à l'inverse, devenir des atouts pour la cybersécurité de votre organisation.

> @RduMarais 

On entend souvent que la faille est "entre la chaise et le clavier".
Et en effet, beaucoup d'attaques, notamment les attaques par ingénierie sociale,
cherchent à provoquer et exploiter des erreurs de vos collaborateurs.
Cependant, si un de vos collaborateurs commet une erreur, et si cela conduit à un effondrement du SI,
c'est que votre SI et votre organisation ont failli.
D'un côté, il est essentiel d'avoir appliqué la défense en profondeur : 
votre SI doit être conçu de sorte que les erreurs d'un unique employé ne doivent pas pouvoir conduire
à une compromission de l'ensemble du SI.
De l'autre, il est indispensable d'accompagner vos collaborateurs,
et de déterminer avec eux des solutions pour leur permettre 
de mener à bien et en toute sécurité leurs propres missions.
En fait on peut même aller plus loin : plutôt que d'être dans l'opposition,
faites de vos collaborateurs des acteurs de la cybersécurité ! 
C'est elles et eux qui connaissent les systèmes sur lesquels ils bossent,
et c'est elles et eux les premiers qui pourront détecter que quelque chose cloche.

Bien sûr, pour y arriver, 
on ne vous demande pas d'enseigner le hacking à tous vos collègues.

> @RduMarais enfin si, moi c'est ce que je fais avec mes collègues, parce que si tu sais hacker tu sais défendre

> @lenhoanglnh ah ouais ? ok (ou whatever the line you wanna say)

Mais en réalité, il y a pas besoin d'être technique
pour contribuer à la cybersécurité !
Il y a surtout besoin que tout le monde s'empare du sujet.

En fait, les plus grandes contributions à la cybersécurité,
ce ne sont généralement pas des lignes de codes ;
ce sont davantage des questions comme 
"que se passe-t-il si cette machine se fait pirater ?"
"A-t-on un plan de crise, en cas d'attaque par ransomware ?"
"Comment notre site web réagit-il, si un utilisateur fait ceci ?"
"Notre investissement en cybersécurité jusque là est-il suffisant ?"

Si vous pensez vous poser ces questions,
c'est que notre livre est fait pour vous.
Son objectif, c'est vraiment de permettre à tous les collaborateurs
de mieux comprendre les enjeux et les menaces de cybersécurité,
les grands principes d'une cyberdéfense pertinente et efficace,
et les nombreuses questions qu'il faut se poser,
pour évaluer l'exposition aux risques de vos organisations,
et pour réduire drastiquement l'impact des cyber attaques.

C'est urgent de ne pas délaisser la cybersécurité à une poignée de geeks dans votre organisation.
Seuls, ils n'y arriveront pas, seront frustrés, et vous frusteront.
Nous devons sécuriser notre espace informationnel ensemble.


## Au delà de la réponse individuelle

Si jusque là, j'ai beaucoup insisté sur les actions individuelles que vous pouvez entreprendre
pour augmenter drastiquement la résilience de vos organisations face à la menace cyber,
je ne peux que insister sur l'importance d'une réponse sociétale à cette menace.
À moins que vous ne soyez une petite organisation d'experts dans le domaine,
vous utilisez forcément un grand nombre de programmes vendus par des fournisseurs,
et ces les logiciels sont trop souvent minées de bugs, de failles, voire de portes dérobées ;
ces fournisseurs sont souvent trop occupées à développer de nouvelles fonctionnalités gadgets,
au détriment de la sécurité des produits défectueux
qu'ils sont déjà en train de vendre à très grande échelle ---
à l'instar de Microsoft qui vend Windows avec des mécanismes d'authentification 
qui sont vulnérables aux mêmes attaques depuis 10 ans.
https://medium.com/@offsecdeer/ntlmv1-domain-compromise-9bd8dd7e9891
https://www.crowdstrike.fr/cybersecurity-101/pass-the-hash/

Si l'on veut davantage protéger nos sociétés des failles de fournisseurs informatiques,
il va nous falloir augmenter drastiquement les exigences légales 
vis-à-vis des produits commercialisés,
comme cela est la norme dans toutes sortes de produits non numériques.

Mais ce n'est pas tout.
Sachant que les produits numériques sont parfois conçus avec des portes dérobées,
ou avec des systèmes de mise à jour qui permettent le contrôle à distance,
et dans un contexte où les tensions géopolitiques augmentent à travers le monde,
avec des dirigeants politiques qui ne sont pas toujours de confiance,
il est urgent de favoriser beaucoup plus des solutions informationnelles
sur lesquelles nos organisations ou nos sociétés ont beaucoup plus de contrôle.
C'est l'idée des logiciels libres et open-source comme Linux,
qu'une loi suisse exige désormais pour les agences gouvernementales,
et que la gendarmerie française a déjà adoptés.

Enfin, les journalistes, les développeurs et les scientifiques 
me semblent avoir une responsabilité particulière dans la cyberdéfense.

Si au lieu de s'extasier devant une innovation technologique
dont le niveau de sécurité est extrêmement faible,
on donne tous plus d'attention à la cybersécurité et à la fiabilité des solutions,
voire plus généralement aux technologies de l'information 
qui ont davantage de chance de renforcer nos démocraties que de les affaiblir,
nul doute qu'on armera ainsi beaucoup mieux nos sociétés,
pour les rendre plus résilientes au cybercrime.


## Conclusion

Vous l'avez certainement constaté,
les médias couvrent de plus en plus des pannes et des attaques informatiques.
La cyber est devenu un enjeu majeur, 
notamment pour la survie des organisations et pour le tissu économique.
Surtout à l'heure où les tensions géopolitiques se sont exacerbées,
et où toutes les industries se sont fortement numérisées,
il est ainsi urgent de donner beaucoup plus d'attention à la cybersécurité,
d'arrêter d'en parler comme un sujet mystérieux et incompréhensible, 
parce qu'il nous concerne tous !

Ce faisant, comme on l'a vu,
chacun d'entre nous peut aider, à protéger votre organisation et notre société.
Et pour vous lancer dans votre initiation dans le domaine,
j'ai bien sûr un livre à vous recommander,
C'est notre "Guide de survie au cybercrime en entreprise",
publié chez Dunod, préfacé par Guillaume Poupard, 
et écrit par l'excellent Romain du Marais... Et par moi-même.

De loin, on pourrait croire qu'il s'agit d'un sujet obscur,
plein de règles difficilement compréhensibles et de bonnes pratiques laborieuses à adopter.
Et honnêtement, c'est un peu l'image que j'en avais il y a 10 ans.
Cependant, plus je m'y intéresse, plus j'y vois un domaine avant tout fascinant,
qui mêle aussi bien des mathématiques de très, très haut niveau,
mais aussi des enjeux juridiques, psychologiques et sociologiques,
et qui, clairement, nécessite qu'on y contribue tous,
pour être concrétisée dans le tissu économique et dans nos instances dirigeantes,
de sorte à rendre nos sociétés numériques sûres et résilientes.

