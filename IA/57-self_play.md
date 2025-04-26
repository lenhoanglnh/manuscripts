# Faut-il trop réfléchir ?

> Quelques notes au ukulélé.

Est-ce qu'on vous a déjà dit de réfléchir moins pour mieux agir ?
Est-ce mathématiquement possible de "trop réfléchir",
de "overthink" comme on le dit en anglais,
c'est-à-dire de réfléchir tellement que notre performance est dégradée ?
Et pourquoi est-ce que je parle de cela 
dans une vidéo de la série sur l'intelligence artificielle ?

Eh bien, pour être honnête, 
c'est parce que j'ai été frappé par la conclusion de la vidéo de David,
alias Science Étonnante,
qui semble conclure en disant que davantage de réflexion
pourrait permettre aux algorithmes génératifs 
de combler l'absence de nouvelles données d'entraînement.

> Si les données humaines sont les énergies fossiles de l'IA,
> l'apprentissage par renforcement sur les problèmes vérifiables,
> c'est donc, en quelque sorte, leur énergie renouvelable.
> Alors, si cette intuition est correcte,
> il est vraisemblable qu'à l'avenir, 
> la course ne soit plus vers le gigantisme des modèles pré-entraînés,
> mais vers l'intelligence des modèles fine-tunés.

En fait, j'ai trouvé cette conclusion assez confuse,
et pas seulement parce que la réflexion des algorithmes génératifs
est très loin de n'utiliser que des énergies renouvelables.
Pour être plus précis, la citation de David donne l'impression
que les données humaines peuvent être parfaitement substituées par de la réflexion,
tout comme l'énergie fossile peut être substituée par des énergies renouvelables.

Or ça, ça me paraît extrêmement trompeur,
ne serait-ce que pour des questions d'unités physiques.
L'énergie fossile et l'énergie renouvelable peuvent toutes deux se mesurer en joules.
Mais les données humaines se mesurent en bits, 
ou en giga-octets qui correspondent à 8 x 10⁹ bits.
Tandis que la réflexion se mesure en nombre d'opérations par secondes, typiquement en FLOAPs.
Or les FLOAPs et les giga-octets, ça paraît extrêmement différent.

Mais surtout, de manière plus fondamentale,
la complexité des données, cela renvoie à la notion de complexité de Solomonoff ;
tandis que le temps de réflexion, cela renvoie à la complexité en temps de calculs.
Aujourd'hui, je vous propose de bien clarifier ces distinctions,
mais aussi de voir dans quelle mesure il est possible de convertir l'une en l'autre,
pour mieux comprendre l'intérêt des systèmes d'apprentissage,
mais aussi leurs limites fondamentales.


## Jeu de go versus IA de recommandation

Commençons par un quizz.
Laquelle des deux tâches suivantes est la plus difficile ?
Le jeu de go, ou les IA de recommandation ?

Si vous avez suivi l'abattage médiatique autour de l'intelligence artificielle,
vous serez peut-être très tentés de parler du jeu de go.
Mais si vous suivez l'argent, et la valeur économique des IA,
vous vous précipiterez sans doute sur les IA de recommandation,
qui sont l'objet d'une bataille entre multinationales 
à coups de centaine de milliards de dollars d'investissement.

Mais mettons les considérations médiatico-économiques de côté.
Réfléchissons plus fondamentalement à la question,
avec les lunettes de la science de l'information.
Qu'est-ce qui rend le jeu de go difficile,
et qu'est ce qui rend la recommandation de contenus difficile ?

À bien y réfléchir, si le go est un jeu difficile,
c'est en fait uniquement pour des considérations de temps de calculs.
En fait, si on omet ces considérations, 
résoudre le jeu de go est assez trivial :
il existe un algorithme très court, appelé minimax,
qui permet de résoudre exactement ce jeu,
notamment si on lui ajoute la description des règles du jeu,
elle aussi assez courte.

Il faut alors bien se rendre compte de la nature de la tâche
du développement d'algorithmes d'intelligence artificielle pour résoudre le go.
Ces algorithmes n'ont pas besoin de comprendre les lois de la physique,
la psychologie humaine ou la géopolitique mondiale.
Il s'agit uniquement pour eux d'accélérer les calculs monumentaux de minimax,
quitte à perdre en rigueur, et donc en garantie de calcul de la stratégie optimale.
Faire de l'IA pour le jeu de go, 
c'est calculer en temps raisonnable une assez bonne heuristique
d'un autre algorithme parfaitement connu et déterministe.
La difficulté réside uniquement dans le fait de court-circuiter des étapes de calculs.

> NB : Il y a aussi des défis en termes de gestion de l'espace mémoire de calculs.
Autrement dit, il s'agit de construire une heuristique avec des ressources limitées,
en temps et en mémoire de calcul.

Et ça, ça contraste fortement avec la difficulté de la recommandation de contenus.
Certes, en pratique, les IA de recommandation sont elles aussi confrontés 
à d'énormes défis de temps de calculs,
d'une part parce que les utilisateurs des réseaux veulent que,
à chaque clic et à chaque swipe sur leurs téléphones,
leur application leur recommande des nouveaux contenus excitants
en une fraction de secondes,
et d'autre part parce que ces requêtes des utilisateurs ont lieu 
des centaines de milliards de fois chaque jour.
S'il faut une seconde pour répondre à chaque requête,
cela représente tout de suite des centaines de milliards de seconde de calcul,
soit 3000 ans de calculs.
Bien sûr, ce calcul est largement parallélisé en pratique,
si on veut faire tous les calculs le jour même,
il faut des millions de machines.
Clairement, en pratique, chaque recommandation doit être effectuée en une fraction de secondes,
typiquement en millisecondes.

Ceci étant dit, même en oubliant ces contraintes de temps de calcul,
l'exercice de la recommandation de contenus reste extrêmement difficile,
comme j'ai pu m'en rendre compte en mars 2020,
quand un ingénieur de Google a répondu à ma requête de prioriser des contenus sur le COVID,
mais en me demandant ensuite lequel prioriser.
Et oui, parce que pour savoir quel est le meilleur contenu de YouTube à recommander sur le COVID,
encore faut-il soit-même connaître l'existence du COVID, 
son fonctionnement, ses impacts sanitaires,
mais aussi les meilleures façons d'en parler au grand public,
en étant rigoureux scientifiquement, mais aussi en étant attentionnément écouté par ce public,
et en ayant si possible un maximum d'impact sur son changement de comportement.
Le tout sans oublier les dimensions d'économie et de santé mentale
qu'implique la crise du COVID.

Vous le voyez peut-être venir :
pour déterminer quelles sont les meilleures recommandations à effectuer,
il faut effectuer un profilage psychologique des 3 milliards d'humains,
comprendre leurs goûts, leurs capacités d'attention et leurs connaissances préalables,
mais aussi comprendre l'état des menaces sanitaires,
les enjeux économiques et les influences géopolitiques.
Ça fait, beaucoup d'information diverses et variées sur le monde,
qu'il va falloir enseigner aux systèmes d'intelligence artificielle.
La complexité ici ne vient pas uniquement des contraintes en ressources de calcul ;
elle vient en fait même surtout de la collecte et de l'analyse de données
qui nous renseignent sur l'état du monde,
et sans lesquelles il est impossible d'effectuer de bonnes recommandations.

Alors, je parle ici d'effectuer des recommandations d'intérêt général,
mais y compris pour des tâches beaucoup moins nobles 
comme recommander les contenus à des milliards d'humains
qui auront le plus de chances de les retenir sur les réseaux sociaux,
pour ensuite pouvoir leur montrer des publicités ciblées,
il est essentiel de collecter et d'analyser des quantités massives d'information.

Eh bien, en ce sens, 
les IA de recommandation sont beaucoup, beaucoup, beaucoup plus complexes
que les algorithmes optimisés pour le jeu de go ou pour les échecs.
En termes techniques, on dit que la tâche de la recommandation de contenus
a une énorme complexité de Solomonoff, parfois aussi appelée complexité de Kolomogorov,
dans le sens où rien que décrire un algorithme qui résout cette tâche
est extrêmement laborieux,
car il faudrait inclure dans cet algorithme une description d'énormément de choses,
comme les détails des psychologies des 3 milliards d'utilisateurs des réseaux sociaux.


## Les algorithmes génératifs

OK, mais où se trouvent les algorithmes génératifs dans tout ça ?
Est-ce concevoir un chatbot est difficile ?
Ou plutôt, en quel sens construire un chatbot est-il difficile ?

Clairement, concevoir un chatbot performant est une tâche à haute complexité de Solomonoff.
En effet, le chatbot doit connaître un minimum de langage naturel,
et ce langage naturel est en fait bien plus complexe 
que les règles du jeu de go ou des échecs.
Cependant, on peut raisonnablement penser que,
au moins pour avoir des discussions basiques,
le chatbot ne requiert pas la compréhension de la psychologie de 3 milliards d'humains,
ni même la connaissance de l'économie et de la géopolitique mondiale.

De même, si on attend uniquement du chatbot qu'il prouve des théorèmes mathématiques,
ou qu'il génère des codes simples de programmation,
on peut s'attendre à ce qu'il y parvienne avec peu d'informations ;
essentiellement, il lui suffit de connaître les axiomes des mathématiques,
ou la documentation d'un langage de programmation.
Bien sûr, tout ceci n'est pas trivial, 
et requiert peut-être un article ou un livre pour être décrit.
Mais pour le coup, un article ou un livre suffit.
Au sens de Solomonoff, les mathématiques et la programmation ne sont pas si complexes.
Ce sont des tâches en fait relativement simples.

En fait, si les mathématiques et la programmation sont difficiles,
ce n'est pas au sens de Solomonoff,
mais c'est au sens de la théorie de la complexité en ressources de calcul,
exactement comme le jeu de go ou des échecs.

Mais est-ce que le LLM réfléchit ?

Imitation de la pensée.

Ne pas sous-estimer l'imitation.


## Système 2 -> Système 1

Citation de Terence Tao.


## Entraîner le système 1

Le système 1 apprend du système 2.

Mieux encore, si on a des solutions vérifiables.

Automatisation avec un algorithme de vérification (NP).


## Les limites

Complexité de Solomonoff

Le jeu de go et les preuves de théorèmes sont à faible complexité en temps de calcul !

Mais comparer la pure réflexion à lde l'énergie renouvelable,
bon déjà, c'est un peu ironique car ça s'appuie souvent aujourd'hui sur des énergies fossiles,
mais surtout, ce serait comme dire que la science et la philosophie morale
pouvaient être résolus sans collecter de données sur l'état du monde.

C'est aussi ignorer toutes les difficultés liées à la collecte et l'analyse de données :
facteurs de confusion, a prioris bayésiens, raisonnements avec incertitude,
biais sociologiques dans les données,
données stratégiquement choisies par les fournisseurs,
données adversarialement choisies par les attaquants...

Et c'est surtout ignorer la dimension politique et sociétale de ces objets,
en particulier les problèmes d'alignement avec les préférences humaines.


## Conclusion

Attention au coolwashing.

Attention à la mute-newsisation des enjeux sociétaux.

