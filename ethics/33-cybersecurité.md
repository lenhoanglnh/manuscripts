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

Eh bien, aujourd'hui même, Romain du Marais, 
vulgarisateur de la chaîne Pour 1nf0 et responsable de la sécurité des systèmes d'information,
et moi-même publions chez Dunod un livre dédié à ces questions,
intitulé "Guide de survie au cybercrime",
avec une préface de Guillaume Poupard,
qui est un peu le big boss de la cybersécurité en France.

Bien entendu, je ne vais pas pouvoir résumer ce livre en trois mots.
Mais s'il fallait retenir un principe de notre livre,
c'est indiscutablement la notion de *défense en profondeur*.
Tel est, selon nous, le principe fondamental de la cybersécurité.


## La défense en profondeur

De nos jours, pour toutes les organisations,
la question n'est plus de savoir « si » on sera attaqué dans le cyber espace.
Vu la croissance terrifiante de l'industrie du cybercrime,
et ses coûts engendrés sur la société qui ont été estimés 
à 11 mille milliards de dollars en 2023 ---
je répète, 11 mille milliards de dollars, soit 4 fois le PIB de la France ! ---
ce n'est qu'une question de temps avant que votre organisation soit attaquée.

La question qu'il faut se poser, 
c'est donc plutôt d'anticiper les cyber attaques dont vous serez la cibles,
et surtout de prendre les mesures les plus pertinentes
pour minimiser l'ampleur des impacts des attaques 
sur l'activité de votre organisation.

Autrement dit, il ne faut pas concevoir un système d'information
en imaginant qu'il ne sera jamais infiltré.
Il faut davantage le concevoir de sorte que même une fois infiltré,
les attaquants ne pourront pas provoquer des dégâts catastrophiques.

Une image à avoir en tête est typiquement celle du "formage suisse".
Aucune couche de défense ne doit être considérée incontournable ;
après tout, tout antivirus peut échouer à détecter certains virus,
tout logiciel peut avoir écrit avec des failles
et toute machine peut avoir des portes dérobées.
Mais en empilant adéquatement les couches de défense,
vous pouvez réduire drastiquement la probabilité d'être vulnérable.  
https://en.wikipedia.org/wiki/Swiss_cheese_model

Ainsi, si on imagine que la probabilité qu'un attaquant perce une couche est égale à 10%,
le fait de devoir percer 10 couches, en supposant les probabilités indépendantes,
ça va être égal à (10%) puissance 10,
ce qui fait 1 chance sur 10 milliards.
Voilà qui confère une protection beaucoup plus grande qu'une couche robuste à 99,99%.


## Divers principes opérationnels

En pratique, pour implémenter la défense en profondeur au mieux,
c'est-à-dire concevoir un système d'information résilient
à partir d'un grand nombre de composants potentiellement défectueux,
l'empilement des couches de défense n'est pas la stratégie possible,
et pas forcément toujours la plus efficace.

Dans le livre plein d'exemples concrets,
on identifie ainsi un certain nombre de principes opérationnels,
auxquels il est utile de penser pour renforcer notre défense en profondeur.

Par exemple, 
surtout quand il s'agit de sauvegardes de données ou d'identifiants d'authentification,
il est indispensable de miser sur la redondance des solutions,
mais aussi sur leur diversification.
Typiquement, je vous invite très vivement à utiliser des mots de passe radicalement différents
pour les différents services informatiques que vous utilisez,
de sorte que, même si l'un de vos mots de passe parvient à être deviné par un attaquant,
peut-être parce qu'un service que vous utilisez s'est fait piraté comme cela arrive souvent,
l'attaquant demeure incapable d'accéder aux autres services informatiques que vous utilisez.

De même, il est critique de ne pas garder les sauvegardes de données à un même endroit,
ou de permettre l'accès à ces sauvegardes via une même machine d'un administrateur.
Et oui, il suffira alors à l'attaquant d'accéder à cette unique machine de l'administrateur,
pour ensuite pourrir toutes les sauvegardes,
et ainsi effectuer une attaque par ransomware dévastatrice.
Typiquement, une telle attaque va chiffrer toutes les données de l'organisation,
de sorte à paralyser complètement son activité,
et exiger une rançon pour restaurer vos données.

Autre principe opérationnel essentiel : le monitoring de votre système d'information.
Il vous faut constamment avoir accès et analyser toutes sortes d'opérations sur vos machines,
de sorte à identifier toute anomalie suspecte aussi vite que possible,
et bloquer les attaquants avant qu'ils ne parviennent à accéder 
aux parties les plus sensibles de votre réseau.

D'ailleurs, pour ralentir, voire bloquer, les attaquants dans leurs démarches,
il est aussi indispensable de décomposer votre système en un grand nombre de composants,
et à limiter les droits de chaque composant au moindre privilège 
qui lui est nécessaire pour fonctionner correctement.
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
Il suffit tout bêtement d'appliquer la sobriété numérique,
c'est-à-dire de minimiser le nombre de logiciels,
d'extensions navigateurs ou de fonctionnalités à déployer.
Plus votre machine sera spécialisée dans un petit nombre de tâches précises,
et conçue pour ne réaliser que ces tâches, plus vous serez protégés.

Et bon, malheureusement, en pratique,
le marketing des géants du numérique va complètement à l'encontre de ce principe,
en proposant des solutions fourre-tout comme Microsoft 365,
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

Ainsi, au lieu d'y voir des vecteurs de faille potentiels,
nous vous invitons à y voir des solutions pour augmenter drastiquement
la résilience de votre organisation à des cyber-attaques,
qui chercheraient à nuire aux flux de traitement et de communication de l'information
au sein de votre organisation.
Faites de vos collaborateurs des acteurs de la cybersécurité.

Bien sûr, pour y arriver, 
on ne vous recommande pas d'enseigner les lignes de commande à tous vos collègues,
ou de leur apprendre à coder en Rust.
D'une part, parce que ça risque de ne pas les intéresser.
Mais surtout, parce qu'il n'y a nul besoin d'être technique
pour contribuer de manière essentielle à la cybersécurité de votre organisation.

En fait, les plus grandes contributions à la cybersécurité,
ce ne sont généralement pas des lignes de codes ;
ce sont davantage des questions comme 
"que se passe-t-il si cette machine se fait pirater ?"
"A-t-on un plan de crise, en cas d'attaque par ransomware ?"
"Comment notre site web réagit-il, si un utilisateur fait ceci ?"
"Notre investissement en cybersécurité jusque là est-il suffisant ?"

Si vous pensez pouvoir poser ces questions,
c'est que notre livre est fait pour vous.
Son objectif, c'est vraiment de permettre à toutes sortes de collaborateurs
de mieux comprendre les enjeux et les menaces de cybersécurité,
les grands principes d'une cyberdéfense pertinente et efficace,
et les nombreuses questions qu'il faut se poser,
pour évaluer l'exposition aux risques de vos organisations,
et pour réduire drastiquement l'impact des cyber attaques.

Il est urgent de ne pas délaisser la cybersécurité à une poignée de geeks dans votre organisation.
Seuls, ils n'y arriveront pas, seront frustrés, et vous frusteront.
Nous devons sécuriser notre espace informationnel ensemble.


## Au delà de la réponse individuelle

Si jusque là, j'ai beaucoup insisté sur les actions individuelles que vous pouvez entreprendre
pour augmenter drastiquement la résilience de vos organisations face à la menace cyber,
je ne peux suffisamment insister sur l'importance d'une réponse sociétale à cette menace.
À moins que vous ne soyez une petite organisation d'experts dans le domaine,
vous utilisez forcément un grand nombre de solutions vendues par des fournisseurs,
dont les logiciels sont trop souvent minées de bugs, de failles, voire de portes dérobées ;
et qui sont souvent plus occupées à développer de nouvelles fonctionnalités,
ou des algorithmes génératifs spectaculaires,
qu'à investir massivement dans la sécurité des produits défectueux 
qu'ils ont déjà commercialisés à très grande échelle ---
à l'instar de Microsoft dont la faille exploitée par les hackers chinois à l'été 2023
n'a toujours pas été identifiée, 
selon un rapport alarmant de l'agence nationale de cybersécurité des États-Unis.  
https://www.cisa.gov/sites/default/files/2024-04/CSRB_Review_of_the_Summer_2023_MEO_Intrusion_Final_508c.pdf  
https://edition.cnn.com/2024/06/13/tech/microsoft-president-congress-cybersecurity-failures/index.html

Si l'on veut davantage protéger nos sociétés des failles de fournisseurs informatiques,
qui plus est souvent américains ou chinois,
comme Intel, Google, OpenAI, Lenovo ou autres Huawei,
il va nous falloir augmenter drastiquement les exigences légales 
vis-à-vis des produits commercialisés,
comme cela est la norme dans toutes sortes de produits non numériques.

Mais ce n'est pas tout.
Sachant que les produits numériques sont souvent conçus avec des portes dérobées,
ou avec des systèmes de mise à jour qui permettent le contrôle à distance,
et dans un contexte où les tensions géopolitiques augmentent à travers le monde,
avec des dirigeants politiques qui ne sont pas toujours les plus dignes de confiance,
il est urgent de favoriser beaucoup plus des solutions informationnelles
sur lesquelles nos organisations, voire nos sociétés, ont beaucoup plus de contrôle,
à l'instar des logiciels libres et open source comme Linux,
qu'une loi suisse exige désormais pour les agences gouvernementales,
et que la gendarmerie française a déjà adoptés.

Enfin, les journalistes, les développeurs et les scientifiques 
me semblent avoir une responsabilité particulière dans la cyberdéfense,
tout simplement car leurs compétences représentent un grand pouvoir,
et que, comme le dit l'oncle de Spiderman,
de grands pouvoirs impliquent de grandes responsabilités.

Si au lieu de s'extasier devant une innovation technologique
dont le niveau de sécurité est extrêmement faible,
on donne tous beaucoup plus d'attention à la cybersécurité et aux solutions plus auditables,
voire plus généralement aux technologies de l'information 
qui ont davantage de chance de renforcer nos démocraties que de les affaiblir,
nulle doute qu'on armera ainsi beaucoup mieux nos sociétés,
pour les rendre plus résilientes à l'industrie mençante du cybercrime.


## Conclusion

Vous l'avez certainement constaté,
les médias couvrent de plus en plus des pannes et des attaques informatiques.
La cyber est devenu un enjeu majeur, 
notamment pour la survie des organisations et pour le tissu économique.
Surtout à l'heure où les tensions géopolitiques se sont exacerbées,
et où toutes les industries se sont fortement numérisées,
il est ainsi urgent de donner beaucoup plus d'attention à la cybersécurité,
et de prendre le temps de mieux comprendre les risques, les attaques et les défenses.

Ce faisant, comme on l'a vu,
chacun d'entre vous peut aider, à protéger votre organisation et notre société.
Et pour vous lancer dans votre initiation dans le domaine,
j'ai bien sûr un livre à vous recommander,
à savoir le "Guide de survie au cybercrime en entreprise",
publié chez Dunod, préfacé par Guillaume Poupard, 
et écrit par l'excellent Romain du Marais... Et par moi-même.

De loin, on pourrait croire qu'il s'agit d'un sujet obscur,
plein de règles difficilement compréhensibles et de bonnes pratiques laborieuses à adopter.
Et honnêtement, c'est un peu l'image que j'en avais il y a 10 ans.
Cependant, plus je m'y intéresse, plus j'y vois un domaine avant tout fascinant,
qui mêle aussi bien des mathématiques de très, très haut niveau,
mais aussi des enjeux juridiques, psychologiques et sociologiques,
et qui, clairement, nécessitera la contribution d'une énorme partie de la société,
pour être concrétisée dans le tissu économique et dans nos instances dirigeantes,
de sorte à rendre nos sociétés numériques sûres et résilientes.

