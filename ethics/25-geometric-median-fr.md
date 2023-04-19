# Les maths des IA démocratiques (AISTATS'23)

Imaginez-vous dans Ville du Coin, 
une petite ville de mathématiciens située dans une énorme plaine.
La mairie vient de décider de la construction d'un nouveau musée des maths.
Mais il reste à décider où construire ce musée.
Or, comme chaque citoyen préfère que 
le musée soit aussi proche que possible de leurs domiciles,
et comme les citoyens de Ville du Coin habitent aux quatre coins,
non seulement de la ville, mais même de la région,
les préférences des différents mathématiciens sont donc clairement conflictuelles.

Qui plus est, même si ces mathématiciens sont gentils,
ils sont aussi avant tout mathématiciens,
et ne peuvent donc pas s'empêcher de se comporter de manière stratégique.
En particulier, 
ils sont prêts à mentir sur leurs préférences de position géographique du musée,
si cela permet de rapprocher le musée de leurs lieux de résidence.

Et alors, dans le tas, il y a quelques théoriciens des jeux,
qui savent très bien que, avec un vote par agenda,
on peut facilement se retrouver avec une décision finale catastrophique.
https://tournesol.app/entities/yt:goQ4ii-zBMw

Ces théoriciens connaissent aussi très bien les problèmes de vote utile.
En particulier, ils connaissent des solutions démocratiques 
comme le jugement majoritaire et le scrutin de Condorcet randomisé.
Cependant, ces solutions ne fonctionnent que 
s'il y a un nombre fini de positions possibles du musée des mathématiques.
Or le musée peut vraiment être construit n'importe où dans la plaine.
Il y a donc bien une infinité de solutions.

Comment déterminer démocratiquement le lieu de construction du musée ?
Et, par ailleurs, quel est le rapport entre ce problème théorique
et les intelligences artificielles ?


## Le problème de la moyenne

Les algorithmes de machine learning les plus impressionants aujourd'hui,
qu'il s'agisse de ChatGPT, de MidJourney ou de l'algorithme de recommandation de TikTok,
tous s'appuient sur des réseaux de neurones, 
qui sont des sortes de grosses machines 
avec un très grand nombre de paramètres à ajuster.
Et comme on en a beaucoup parlé dans la série sur l'intelligence artificielle,
ces paramètres sont ajustés à partir des données.

Très concrètement, pour chaque donnée,
l'apprentissage de la donnée par l'algorithme correspond 
à une direction de modification des paramètres de l'algorithmes,
appelée gradient,
qui dit, pour chaque paramètre, à quel point il est pressant de le tourner.

Dans le cas d'un algorithme à deux paramètres,
le gradient associe à chacun des deux paramètres un taux auquel le tourner,
si bien que la direction de modification des paramètres est alors 
une paire de deux nombres.
Ces nombres peuvent d'ailleurs être positifs ou négatifs, 
selon qu'il faille augmenter ou diminuer les valeurs des paramètres.

Si on interprète maintenant ces nombres comme les coordonnées d'un point,
on peut alors placer dans un plan le déplacement adéquat des paramètres.
Et pour rappel, chaque déplacement adéquat est associé à une donnée,
si bien que pour apprendre de toutes les données,
il faut combiner les déplacements adéquats selon chacune des données.

Vous voyez le lien avec le problème de la position du musée des maths ?
Déterminer où placer un musée pour des mathématiciens aux préférences divergentes,
c'est finalement très similaire à déterminer 
comment permettre à un réseau de neurones d'apprendre de plusieurs données différentes.

Et alors, en pratique, dans la quasi-totalité des algorithmes de machine learning,
la solution pour aggréger les déplacements adéquats selon toutes les données
revient à prendre la moyenne de ces déplacements adéquats.

Et peut-être que vous voyez venir où est le problème avec cela.
En pratique, les données utilisées pour entraîner les algorithmes sont rarement sécurisées.
Par exemple, ChatGPT s'appuie sur les textes publiés sur Reddit,
MidJourney généralise les images du web
et l'algorithme de TikTok s'appuie sur les clics et les swipes des utilisateurs.

Or, à l'instar des mathématiciens, 
ces utilisateurs peuvent se comporter de manière stratégique,
surtout si des influenceurs encouragent ces comportements —
D'ailleurs, rien à voir, mais pensez bien à liker, commenter et partager cette vidéo,
et à vous abonner à la chaîne, ainsi qu'à activer la cloche...
et si vous avez plusieurs comptes Google, pensez à le faire avec tous vos comptes Google !

En fait, aujourd'hui, il existe des énormes industries de la désinformation,
donc il serait *irréaliste* de supposer que les données qui alimentent
l'apprentissage des intelligences artificielles les plus puissantes du monde moderne
ne sont pas produites de manières stratégiques.

Mais donc, dans le contexte stratégique, voire de guerre informationnelle du web,
est-ce que la moyenne est une solution adéquate pour aggréger différentes directions ?
Clairement, non.
En effet, en exaggérant la position où ils préfèrent placer le musée,
chaque mathématicien peut tirer la décision finale vers sa position préférée.
La moyenne encourage en fait l'expression de préférences extrêmes.

Pour les mathématiciens. 
Et pour les internautes qui veulent influencer les algorithmes de machine learning aussi.


## La médiane géométrique

L'intuition selon laquelle, en se mettant plus loin, 
les mathématiciens tirent plus fort sur la position du musée est en fait tout à fait formalisable.
Imaginons qu'on laisse un caillou, 
et que chaque mathématicien attachait une ficelle au caillou,
puis se plaçait au niveau de la position qu'il dit préférer.
Et supposons enfin que la force avec laquelle il tire est proportionnelle
à la distance qui le sépare du caillou.
Alors la moyenne correspondra exactement à la position d'équilibre,
c'est-à-dire à la position du caillou qui est telle 
que les forces avec lesquelles chaque mathématicien tire sur le caillou s'annulent.

Et ça, je laisse les matheux parmi vous le démontrer.

Du point de vue de la théorie des jeux, cette situation est clairement insatisfaisante,
et montre très bien en quoi la moyenne induit des incitatifs problématiques.
On peut aussi y voir une forme d'inéquité.
D'une certaine manière, avec la moyenne, 
les positions les plus extrêmes sont davantage valorisées,
puisque ceux qui les adoptent auront plus d'influence sur la position du musée —
ou sur les paramètres et donc le comportement des algorithmes de machine learning.

Eh bien, c'est ce constat qui a poussé des collègues de l'EPFL et moi 
à proposer un scrutin plus juste,
où chaque mathématicien tire avec sur le caillou avec une force unitaire,
indépendamment de la distance qui sépare le mathématicien du caillou.

En fait, le scrutin qu'on décrit correspond à un objet mathématique bien connu, 
qui fut déjà étudié des siècles plus tôt,
notamment par un certain Pierre de Fermat,
puis par l'économiste et géographe Alfred Weber, le frère du sociologue Max,
notamment dans un cadre de minimisation de transport.

En effet, on peut démontrer, 
et là encore je laisse la démonstration en exercice pour les matheux parmi vous,
que le processus où chaque mathématicien tire le caillou avec une même force unitaire
conduit essentiellement toujours à un unique point d'équilibre,
qui a par ailleurs la propriété de minimiser la somme des distances
entre ce point et les positions préférées des différents mathématiciens.

En fait, le seul cas où ce point d'équilibre n'est pas unique,
c'est lorsque les mathématiciens sont en nombre pair, et sont alignés le long d'une droite.
À ce moment-là, tout un segment qui sépare les deux mathématiciens du milieu
correspond à des points d'équilibre, 
où une moitié des mathématiciens tire d'un côté,
et l'autre tire de l'autre côté.

En fait, en dimension un, toute position d'équilibre sépare nécessairement
l'ensemble des mathématiciens en deux ensembles de même taille.
Les plus perspicaces parmi vous le voit peut-être venir :
en dimension un, un point est une position d'équilibre 
si et seulement s'il est une médiane des positions préférées des mathématiciens.

Ainsi l'équilibre du processus qu'on décrit est une généralisation de la médiane de dimension un ;
c'est pourquoi les mathématiciens modernes l'appellent la médiane géométrique.
Et parce qu'elle correspond au résultat d'un processus qui paraît juste,
il semble s'agir d'un excellent candidat pour être le scrutin 
que les mathématiciens devraient adopter pour sélection la localisation géographique du musée,
et que les concepteurs d'algorithmes de machine learning pour le web
devraient adopter pour ne pas encourager l'exaggération des préférences des internautes.


## La médiane géométrique n'offre pas de garantie contre le vote utile

Mais, est-ce bien le cas ?
La médiane géométrique encourage-t-elle vraiment les mathématiciens 
à exprimer leurs vraies préférences pour la position du musée ?

Il y a trois ans, j'ai été tellement sûr que la réponse à ces questions était oui,
que je l'ai laissée en exercice d'échauffement pour un étudiant en Master
dont j'encadrais un stage de recherche,
et à qui j'avais laissé des questions de recherche beaucoup plus poussées...
Après tout, me disais-je, si je préfère que le musée soit proche de chez moi,
j'ai tout intérêt à le tirer vers chez moi, non ?

En particulier, clairement, je n'ai pas intérêt à exagérer mes préférences,
puisque je tirerais alors dans la même direction, 
mais en aucun cas je ne tirerais plus fort.
Comme le disait mon prof de prépa,
ça se sent bien, ça doit se démontrer facilement, non ?

Eh bien non...
Après plusieurs semaines, l'étudiant a fini par douter que la réponse était oui,
et on a ensuite fini par montrer que la réponse était non.

Et je peux d'ailleurs vous montrer un contre-exemple,
c'est-à-dire une situation où un mathématicien a intérêt à mentir
sur la position du musée qu'il préfère.

Imaginez trois mathématiciens Pierre, Alfred et Ramanujan.
Pierre et Alfred habitent assez près l'un de l'autre,
mais Ramanujan habite très loin, presque à l'infini.
Dans la configuration à l'écran, 
vous pouvez voir que la médiane géométrique sera un point tel que
les angles à l'écran correspondent tous à un tiers de tour.

En effet, on voit alors que les forces unitaires 
avec lesquelles Pierre, Alfred et Ramanujan tirent sur la position du musée
vont bien s'annuler.

Eh bien, à bien y réfléchir, on peut se rendre compte 
que Pierre peut rapprocher cette médiane géométrique, 
en prétendant préférer un point un peu plus en haut à droite à l'image.
En effet, pour cette autre position préférée de Pierre,
la médiane géométrique se déplace dans la même direction,
notamment si on suppose que Ramanujan est tellement loin à droite
que sa force unitaire demeurera toujours quasi-parfaitement vers la droite.
La force d'Alfred est inchangée, alors que celle de Pierre aussi,
puisqu'on a simplement translaté le cas de figure précédent.

Sauf que là, patatra, la médiane géométrique s'est rapprochée
de la vraie position préférée d'Alfred.
Un petit calcul trigonométrique montre même qu'on s'est rapproché 
d'un facteur sinus(1/6 de tour),
ce qui correspond à sqrt(3)/2, soit environ 87% de la distance initiale.

En mentant sur ses préférences,
Pierre a ainsi réduit la distance entre chez lui et le musée de 13%.
Est-ce le pire cas ? 
Peut-on imaginer un cas où, en mentant sur ses préférences,
Pierre peut gagner un facteur 50% ? Voire 99% ?

Si le stagiaire n'a malheureusement pas eu le temps de répondre à ces questions,
il a suffisamment clarifié le problème pour m'aider à mieux le comprendre,
mais aussi et surtout pour m'aider à embarquer dans le projet d'autres chercheurs,
notamment El Mahdi El Mhamdi, Professeur à l'École Polytechnique,
mais aussi et surtout l'excellent doctorant Sadegh Farhadkhani de l'EPFL.

Et ensemble, on a réussi à démontrer qu'il n'y avait pas de borne à ce que Pierre pouvait gagner.
Il existe ainsi des cas où il peut réduire la distance au musée de 99,999%.
Et plus généralement, pour tout epsilon strictement positif, 
il peut réduire cette distance d'un facteur 1 - epsilon.
Les incitatifs à mentir sur ses préférences seraient alors énormes.


## En pratique, ce n'est pas si horrible

Alors, en effet, il y a des cas tordus où les incitatifs à mentir sont énormes.
Mais ces cas tordus sont-ils ceux qu'on rencontre en pratique ?
Comment quantifier les incitatifs à mentir dans des cas pratiques ?

Telles sont les questions qui nous animèrent ensuite,
avec à nouveau cette intuition que, 
si la médiane géométrique peut faire survenir des bizarreries en termes d'incitatifs,
celles-ci restent des cas extrêmes, et peut-être peu réalistes.

Pour formaliser cette intuition, 
nous avons proposé d'étudier le cas où Ville du Coin est extrêmement peuplé,
et où les préférences des citoyens sont naturellement décrites 
par une distribution de préférence.
En fait, comme des vrais théoriciens que nous sommes, 
on a même fait le cheminement inverse, 
en supposant au préalable une distribution de préférence,
puis en considérant que les préférences des citoyens étaient tirées au hasard
de cette distribution de préférence.

Voilà qui nous permet de fixer un cadre asymptotique où,
dans la limite d'un grand nombre de citoyens,
la distribution empirique des préférences de ces citoyens 
colle avec la distribution théorique initiale.

La question qu'on se pose est alors suivante :
quand le nombre de citoyens est suffisamment grand,
ne peut-on pas démontrer que les incitatifs à mentir seront nécessairement limités,
notamment par des propriétés de la distribution théorique des préférences ?

Eh bien, le théorème principal que nous avons démontré est que la réponse à cette question est oui.
Et on a même fourni une quantification des incitatifs à mentir.

De façon intrigante, ces incitatifs dépendent d'une forme de polarisation de la distribution théorique des préférences.
Dans le cas d'une distribution isotrope, où toutes les directions sont aussi polarisées,
ces incitatifs à mentir sont toujours quasi-nuls.

Cependant, si la distribution est polarisée dans une direction, 
et beaucoup plus consensuelle dans d'autres directions,
alors les incitatifs à mentir peuvent être importants, dans certains cas.
En fait, les citoyens auront intérêt à paraître plus polarisés encore dans la direction polarisée,
et plus consensuels dans la direction consensuelle.
C'est comme s'il fallait faire le choix conscient de "choisir ses batailles",
et d'abandonner celles qui ne concernent pas les sujets polarisés.

Notre article montre par ailleurs des manières d'atténuer ces incitatifs,
en gros en valorisant différemment les différentes directions.
De façon plus précise, on propose de tordre la médiane géométrique, 
en pénalisant les forces selon certaines directions.
De façon équivalente, ceci revient à imposer des forces unitaires,
mais selon des normes pseudo-euclidiennes.

L'article parle aussi du cas où les préférences des citoyens sont aussi non-isotropes,
c'est-à-dire que, pour ces citoyens, être proche selon certaines directions
est beaucoup plus important qu'être proche selon d'autres directions.

Et j'ai le grand plaisir de vous dire que cet article a récemment été publié
dans la prestigieuse conférence AISTATS 2023,
où il a été présenté par le génial Sadegh Farhadkhani,
dont vous pouvez voir la présentation sur YouTube !


## Les conséquences pratiques

Cette recherche sur la médiane géométrique restera l'un des plus beaux travaux
que j'aurais effectué,
non seulement parce que les mathématiques étaient particulièrement belles,
avec notamment des calculs de tenseurs différentiels du troisième ordre
utiles pour démontrer la convexité de certaines régions de l'espace,
le tout dans un total d'environ 40 pages de preuves,
mais aussi parce que, après Condorcet randomisé,
il s'agissait de l'un de mes premiers travaux théoriques 
avec des vraies conséquences pratiques.

Bon, ça va peut-être vous décevoir vous,
mais cet article m'aura surtout convaincu de ne PAS m'appuyer sur la médiane géométrique
pour la conception des algorithmes de Tournesol.

Après tout, même si les gains à mentir sont en pratique limités,
la stratégie optimale si l'on se permet de biaiser nos préférences révélées,
à savoir se polariser sur des aspects plus polarisés,
me paraît si facile à adopter et si dangereuse en pratique,
qu'il m'a semblé préférable d'adopter des solutions plus robustes aux manipulations stratégiques,
comme la médiane par coordonnée.
Ainsi, sur Tournesol, c'est bien plus cette médiane par coordonnée qui est utilisée —
bon, après, ça vient de motivations qui dépassent le cadre de cette vidéo,
avec notamment une histoire de parisiens mécontents et de marseillais dans l'exaggération
dont je finirai clairement par vous parler sur Science4All.

Cependant, je suis très loin d'avoir enterré la médiane géométrique.
Même si elle s'est fait exclure du coeur des algorithmes de Tournesol,
certaines de ses propriétés remarquables,
comme le fait qu'elle appartient nécessairement au sous-espace affine 
engendré par les positions préférées des citoyens de Ville du Coin,
en font un candidat parfait pour d'autres applications,
comme le vote bayésien sécurisé sur lequel j'aimerais tellement avoir le temps de travailler.

Sérieusement, j'ai déjà les grandes idées de comment concevoir un tel vote,
mais je manque de temps pour vérifier que le vote a les propriétés que je veux qu'il ait.
S'il y a des motivés parmi vous pour investiguer ce sujet,
n'hésitez surtout pas à me contacter pour en savoir plus —
même si bon, un pré-requis sera que vous soyez déjà au moins en thèse en mathématiques,
ou en informatique avec un penchant très mathématique...

Plus généralement, la conception des algorithmes d'apprentissage 
vraiment démocratiques, justes et sécurisés,
avec de surcroît des bonnes propriétés d'incitatifs,
mais aussi de vérifiabilité ou encore de protection des informations sensibles,
c'est vraiment et de loin le plus fabuleux des défis de recherche que je connaisse.

Ce fabuleux chantier implique d'ailleurs aussi bien des aspects très mathématiques, 
comme celui de cette vidéo,
que des défis d'implémentations et d'interfaces utilisateurs,
voire des problèmes de sociologie des contributeurs,
de psychologie du vote ou encore de philosophie politique, morale ou méta-éthique,
le tout incarné dans le projet extrêmement concret qu'est Tournesol.

Je ne peux que vous encourager à rejoindre notre fabuleux chantier,
ou à nous aider à l'accomplir,
en vous emparant des questions de recherche,
en contribuant à Tournesol, en promouvant notre plateforme,
en demandant aux influenceurs et aux médias d'en parler,
ou en effectuant des dons à notre Association à but non lucratif.

