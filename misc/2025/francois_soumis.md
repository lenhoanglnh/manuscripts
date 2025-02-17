# Hommage à François Soumis (1946-2025), mon directeur de thèse décédé

Aujourd'hui une vidéo un peu spéciale.
Mon directeur de thèse, François Soumis, 
est malheureusement décédé il y a quelques jours,
à l'âge de 78 ans,
et je tenais à lui rendre hommage.

Si vous connaissez le monde académique,
vous savez qu'il y a une relation particulière entre tout chercheur 
et son directeur ou sa directrice de thèse.
On parle même parfois de parent académique ;
et moi, en fait, j'ai eu la chance d'avoir de parents académiques,
à savoir George Zaccour, Professeur à HEC Montréal,
et François Soumis, donc, Professeur à l'École Polytechnique de Montréal,
tout deux membres du GERAD,
le Groupe d'Étude et de Recherche en Analyse des Décisions,
où j'ai effectué ma recherche pendant ma thèse.

D'ailleurs, si l'on poursuit la métaphore, les trois à six années de thèse,
quatre dans mon cas,
c'est un peu comme la gestation,
la transformation d'un embryon de scientifique en un véritable chercheur,
qui se conclut avec une défense de thèse,
laquelle correspondrait ainsi à une sorte de naissance du chercheur.

Bon, il y a bien sûr beaucoup de limites à la métaphore.
Et il arrive que le directeur de thèse soit très distant, voire abusif.
Mais à titre personnel, 
j'ai l'immense chance et honneur d'avoir eu deux parents académiques formidables,
notamment, donc, François Soumis.


## Le scientifique

Alors, bien sûr, François est avant tout un chercheur exceptionnel,
qui a non seulement dirigé le GERAD entre 1992 et 1996,
mais qui en était surtout peut-être LA figure dominante quand j'y étais.
Surtout quand il s'agissait d'optimisation, 
François était un peu le big boss des lieux.
Une manière classique de le constater, même si elle a plein de défauts,
c'est de regarder sa page [Google Scholar](https://scholar.google.com/citations?user=TzauinIAAAAJ&hl=en&oi=ao),
et en particulier son nombre de citations et son h-index,
ainsi que le [très grand nombre de prix](https://www.gerad.ca/en/people/francois-soumis),
notamment dans le domaine du transfert technologique,
que François a reçu.

Une des raisons pour lesquelles je voulais travailler avec François,
c'est parce que j'étais à l'époque fasciné par les mathématiques appliquées,
et en particulier par la manière dont des mathématiques très sophistiquées
pouvaient être indispensables pour résoudre des problèmes industriels très concrets.

En particulier, le domaine de François est littéralement appelée la recherche opérationnelle,
ou RO pour les intimes.
Née en pleine seconde guerre mondiale pour résoudre des problèmes de logistique,
cette recherche est marquée par une triptyque logique - algèbre - calcul.
Par exemple, pour déterminer quelles quantités d'hommes, de nourritures et d'obus envoyer au front,
il faut tenir compte de contraintes 
comme le fait qu'il existe un nombre limité de matériels de transport,
que la quantité de nourriture idéale dépend du nombre d'hommes,
et que le nombre d'obus déployable dépend lui aussi de ce nombre d'hommes.
En formalisant plus précisément ces considérations, 
on obtient des contraintes logiques sur les quantités à déployer.
La recherche opérationnelle offre alors une sorte de dictionnaire,
pour traduire ces contraintes logiques en inégalités algébriques.

En pratique, on s'appuie souvent abondamment sur des inégalités entre formes linéaires,
c'est-à-dire avec une somme des variables en jeu.
On évite en particulier tout ce qui est polynomial ;
même si parfois on peut s'autoriser des carrés.
Et si on a ces contraintes sur le langage qu'on utilise pour modéliser les contraintes logiques,
c'est à cause du troisième aspect de la triptyque de la recherche opérationnelle,
à savoir le calcul.
En effet, certaines formulations se prêtent beaucoup plus à d'autres
à la résolution par le calcul.
Quand on dispose avant tout de papiers, de crayons et de travailleurs humains,
comme c'était le cas pendant la seconde guerre mondiale,
c'est déjà une considération essentielle.
Mais quand on change d'échelles avec des supercalculateurs et des problèmes beaucoup plus complexes,
adopter la formulation du problème la plus adaptée au calcul est alors indispensable,
et fait l'objet de tout un champ de recherche.

Le génie de François, 
c'est d'un côté d'avoir su trouver d'excellentes formulations algébriques 
d'un grand nombre de problèmes industriels,
notamment tout ce qui a à voir avec la logistique humaine et matériel,
et de l'autre d'avoir découvert de nouveaux algorithmes plus efficaces
pour résoudre certaines formulations algébriques.

L'un de ces problèmes classiques est celui de la tournée de véhicules :
étant donné certaines tâches de livraisons de biens, ou de transport public,
comment planifier le trajet d'une flotte de véhicules chargés de résoudre ces tâches ?
La difficulté du problème, c'est que dès qu'on dispose d'un grand nombre de tâches et de véhicules,
le nombre de trajets coordonnés envisageables devient astronomique ;
bien trop astronomique pour que tous les trajets soient envisagés par nos machines.

Entre 1958 et 1963, différents chercheurs, 
notamment Ford, Fulkerson, Dantzig, Wolfe, Gilmore et Gomory,
proposèrent alors de résoudre de tels problèmes en n'explicitant que certains trajets,
typiquement ceux qui sont le plus prometteur.
En particulier, Dantzig et Wolfe ont adapté ce principe à la programmation linéaire,
qui est un algorithme capable de résoudre toutes les formulations
composées uniquement d'inégalités entre formes linéaires.
On parle désormais de décomposition de Dantzig-Wolfe ;
et oui, pour ceux qui connaissent, c'est le même Wolfe que dans "algorithme de Frank-Wolfe",
un algorithme très utilisé en machine learning.

Cependant, la formulation du problème du trajet de véhicule requiert une contrainte supplémentaire,
qui vient du fait qu'un trajet a lieu ou non.
Or, Dantzig-Wolfe requiert des variables continues ;
des variables qui typiquement autoriseraient à mettre un demi-camion par trajet.
Clairement, ceci n'est pas réaliste.
Il nous faut introduire des contraintes dites d'intégrité sur certaines variables,
c'est-à-dire que ces variables devront être des nombres entiers.

Eh bien, l'une des plus grandes découvertes de François, 
c'est un nouvel algorithme, 
appelé "génération de colonnes avec branchement et énumération implicite",
ou "column-generation with branch-and-bound" en anglais,
qui permet de résoudre les programmes linéaires avec contraintes d'intégrité
sans expliciter le nombre astronomique de variables en jeu,
mais tout en étant capable de parfois prouver l'optimalité d'une solution.

Et surtout, cet algorithme va illuminer la triptyque,
en augmentant le langage des formulations algébriques adaptées au calcul,
qui lui-même va élargir les contraintes logiques 
que la recherche opérationnelle va être capable de traiter.
Et toute sa carrière, François n'aura cessé d'élargir l'ensemble des contraintes logiques
que le calcul peut résoudre en temps raisonnable.

En particulier, en 1985, François va ensuite créer l'entreprise AD OPT,
pour déployer ses nouvelles solutions à des problèmes concrets dans le monde industriel.
L'entreprise connaît un fort succès, et a depuis été fusionnée avec Kronos.
Mais Kronos a finalement [déménagé](https://prixduquebec.gouv.qc.ca/recipiendaires/francois-soumis/) 
son bureau de recherche et développement de Boston à Montréal ;
ce qui montre bien l'expertise mondiale de François dans le domaine,
surtout quand on sait qu'à Boston il y a le MIT et Harvard !
Il a aussi beaucoup collaboré avec GIRO, qui fournit des logiciels d'optimisation
d'horaires et de trajets de transport en commun à plus de 250 villes,
et où travaillent aujourd'hui encore nombre de ses anciens élèves,
et donc d'amis à moi.

J'ai d'ailleurs souvent parler à François de ses aventures entrepreneuriales.
Il aimait me dire que quand les clients lui demandaient à quel point
ses algorithmes allaient améliorer les performances des clients,
François répondait de manière très franche : 
"ça dépend à quel point vous êtes mauvais !"
Clairement, c'est beaucoup plus facile d'améliorer un système qui n'a jamais été optimisé.


## L'homme

Mais pour moi et tous ceux qui l'ont connu,
François était bien plus qu'un chercheur exceptionnel.
C'était avant tout un personnage, 
une personne à la fois très charismatique,
malgré son accent prononcé de la campagne québécoise.
Et pô juste le simple accent québécois qu'on entend à Montréal...
François était surtout une personne adorable.

Au GERAD, on le connaît avant tout comme un très grand amateur de tarot.
C'est simple.
Tous les midis, avec d'autres collègues du GERAD,
il jouait une partie de tarot,
dont les résultats étaient soigneusement archivés et laissés à la postérité.
Même quand il était en vacances, ou quand il n'avait rien à faire au bureau,
il lui arrivait de venir sur l'heure du dîner,
comme le disent les québécois pour qui "déjeuner" est le repas du matin,
pour ne pas prendre du retard dans le classement du tarot.

François était aussi un grand sportif.
Alors qu'il était en plein milieu de sa soixantaine,
il m'a régulièrement invité à jouer au squash avec lui,
un sport que j'ai découvert à Montréal.
Et alors que j'étais loin d'être mauvais ---
j'ai fait des sports de raquette toute ma vie ---
François ne cessait de me faire courir dans tous les sens et de me foutre des raclées.
D'ailleurs, il arrivait souvent 
que nos rendez-vous professionnels dévient 
en leçons techniques et tactiques de squash.

Toujours prêt à raconter ses innombrables anecdotes,
il aimait par exemple raconter sa jeunesse,
où il allait à l'école en traîneau,
ou celle où les mathématiques s'écrivaient au stylo,
avant d'être transférées à des secrétaires armées de machines à écrire
pour encoder proprement les brouillons,
mais auxquels il fallait néanmoins rajouter les équations à la main.

Quand j'étais encore en thèse, 
il m'avait d'ailleurs invité à lire et publier son mémoire de maîtrise,
un vieux document qu'il avait écrit 40 ans plus tôt,
mais qui semblait contenir des théorèmes encore non publiés.
J'ai lu attentivement ce mémoire, 
qui bien loin de ses considérations d'alors,
traitait de topologie très pure, extrêmement détachée de toutes applications.
On n'a finalement pas cherché à réécrire ce mémoire,
mais c'était fascinant pour moi de voir la distance 
qui séparait ce mémoire des algorithmes de générations de colonne.

En fait, surtout, François, c'est une curiosité débordante.
Il m'est arrivé quelques fois de faire des exposés de vulgarisation scientifique 
devant un public où se trouvait François.
François s'asseyait généralement au premier rang,
et levait la main comme un élève passionné,
n'hésitant pas à proposer des idées à moitié complète,
ou à participer à des ateliers davantage destinés à des enfants.

Je pense en particulier à un événement grand public
où j'illustrais des solutions de partage de gateaux,
à partir d'une découpe d'un ensemble de bonbons.
Il s'est levé très vite pour être l'un des bénéficiaires de la découpe,
et pour essayer de stratégiser pour en avoir le plus possible.
François, même alors du haut de ses presque 70 ans,
était encore un enfant émerveillé 
par tous les problèmes mathématiques qui lui traversaient l'esprit,
et il se précipitait pour non seulement les résoudre,
mais aussi les généraliser et les décortiquer.

Le dernier message que François m'a envoyé résume parfaitement cela.
En 2023, je l'ai félicité pour son Prix d'Excellence en Recherche et en Innovation.
À 76 ans, il m'a répondu simplement
"Je continue car j'ai du plaisir. Dis-moi ce que tu fais maintenant."
Merci François pour cette curiosité permanente.


## Il a changé ma vie

Je ne m'en rendais pas forcément compte avant de faire cette vidéo,
mais François est peut-être la personne au monde 
qui aura le plus affecté le cours de ma vie.
Il m'aura en tout cas constamment énormément soutenu, 
dans tout ce que je faisais et dans tout ce que je voulais faire.

C'est entièrement grâce à lui si, après mon doctorat, en 2014,
j'ai ensuite eu la chance d'effectuer un post-doctorat au MIT.
Il a en gros pris le téléphone, appelé le Professeur Patrick Jaillet,
et quelques semaines plus tard, l'affaire était réglée.
Puis, à l'approche de la fin de mon post-doctorat,
François m'a poussé à revenir à Montréal, 
et à travailler avec Yoshua Bengio notamment.
Pour rappel à l'époque, le deep learning venait d'exploser sur la scène académique,
et il y avait clairement beaucoup à faire à Montréal.
Et si le Québec avait quelques montagnes à la hauteur des Alpes,
j'aurais certainement accepté.

Mais au delà des opportunités professionnelles,
François, c'était la garantie d'une liberté académique, 
et même d'une liberté extra-académique exceptionnelle.
Si j'ai pu consacrer beaucoup de temps à la vulgarisation,
c'est grâce au cadre que m'a offert François,
où ce temps était valorisé.
Sans François, il n'y aurait sans doute pas eu de Science4All.

La liberté académique et la curiosité de François, 
c'est aussi ce qui m'a permis d'explorer les questions de recherche qui me fascinaient,
même si elles s'éloignaient des sentiers battus de François.
Dans ma thèse, je n'ai finalement pas fait de génération de colonnes ;
je me suis beaucoup plus intéressé à des notions 
comme l'équité et la compatibilité avec les incitatifs,
comme j'en ai beaucoup parlé dans ma série sur la démocratie.
Bien sûr, il y avait un peu de programmation linéaire par ci par là,
mais les sujets d'expertise de François étaient en périphérie de ma recherche.

Mais plutôt que de me recentrer sur des sujets qu'il maîtrise,
François a exprimé beaucoup de plaisir à me suivre dans mes investigations,
tout en cherchant ici et là des nouvelles idées ou des points d'amélioration.
Il était vraiment l'inverse d'un micro-manager, 
ce qui pouvait être déstabilisant pour certains,
mais pour moi c'était vraiment le directeur de thèse idéal.

François m'a surtout aidé à trouver mon autre encadrant de thèse, Georges Zaccour,
et à ainsi faire le pont entre deux sections du GERAD qui ne collaborent pas souvent.
C'est grâce à François que je me suis vraiment senti comme un explorateur 
en faisant de la recherche,
autorisé et même encouragé à prendre les directions que je souhaite.
Merci François.

En fait, et surtout, si je me suis lancé dans le monde de la recherche, 
c'est vraiment grâce à François.
C'est peut-être difficile à croire aujourd'hui, 
vu à quel point je parle de science désormais,
mais quand je suis arrivé à Montréal en provenance de l'École Polytechnique en France,
je voulais être ingénieur ; pas chercheur.
Si j'ai choisi d'aller à Montréal, 
c'était notamment parce qu'il y avait moins de cours à y suivre,
et qu'il y avait au lieu de cela un projet de recherche à effectuer,
ce qui me semblait beaucoup plus intéressant et moins chronophage que des cours.

Mais rapidement, mon projet de Maîtrise Recherche a soulevé toutes sortes de questions fascinantes,
des questions qui faisaient écho avec mes stages précédents
et le goût que je commençais à avoir pour la théorie des jeux.
Et François en a profité. 
Il m'a offert des problèmes et des conditions de travail auxquels je ne pouvais pas dire non.
Et c'est comme ça que je suis devenu chercheur en maths.

Comme il s'en félicitait lors de ma soutenance de thèse,
François m'a piégé à faire de la recherche.
Je ne saurais suffisamment l'en remercier.
Personne n'a eu plus d'influence sur mon parcours professionnel que François.
Merci François.
Merci à toi.
