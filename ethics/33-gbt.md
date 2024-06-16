# Faut-il parier sur la France contre XXX ? (la cote est à XXX contre XXX)

Samedi prochain, la France affrontera le XXX en XXX de l'EURO 2024.
Au moment où je publie cette vidéo, la cote de sa qualification est à XXX contre XXX.
Autrement dit, si je mise XXX euros et qu'elle se qualifie, je récupère XXX euros.
Est-ce un pari gagnant ?

Avant d'aller plus loin, 
je précise que les jeux d'argent peuvent provoquer des addictions très dangereuses,
qui peuvent mettre des vies en danger.
Prenez soin de ne parier que des montants raisonnables,
et d'accompagner vos proches qui pourraient être victimes de ces addictions.
Je vous recommande vivement cet excellent documentaire d'ARTE,
qui appelle à réguler beaucoup plus drastiquement le marketing prédateur
des géants des paris sportifs notamment,
dont les effets psychologiques abusent des mêmes ressorts 
que les réseaux sociaux et les machiens à sous notamment.  
https://www.youtube.com/watch?v=FQCJS3oZSh4&pp=ygUMYXJ0ZSB3aW5hbWF4

Ce qui va m'intéresser aujourd'hui, 
ce n'est pas tant s'il faut jouer de l'argent,
mais plutôt comment utiliser les mathématiques 
pour prédire les résultats probables des matchs de football ;
et en particulier pour identifier les paris qui peuvent être gagnants en espérance,
c'est-à-dire des paris qui, à la longue, finiront par nous faire gagner de l'argent.

On va parler en particulier de playful:ai,
un site web lancé par des amis, à savoir Lucas Maystre et Victor Kristof,
tout deux diplômés de l'EPFL,
et dont la recherche a produit des modèles mathématiques à l'état de l'art de la recherche,
pour estimer la probabilité de différentes issues des matchs de football.
Comme on en reparlera, leur site effectue en permanence des prédictions bayésiennes
sur l'issue des prochains matchs de football.  
https://playfulai.net/fr

Mais surtout, comme on va le voir, 
ces mathématiques trouvent des applications bien au-delà des paris sportifs.
Ils sont par exemple au coeur de la recherche sur l'alignement des modèles de langage,
et de celle sur la démocratie numérique au coeur notamment de notre projet Tournesol.

En fait, il y a un an, 
j'annonçais sur Twitter notre découverte d'une structure mathématique merveilleuse ;
eh bien, comme on va le voir, 
cette structure est au coeur de l'apprentissage des préférences humaines,
mais aussi, donc, de la prédiction du niveau des équipes de football à l'EURO 2024.


## Le score ELO

Pour comprendre comment fonctionne Playful AI,
on va faire un détour vers un autre problème :
celui d'établir un classement des joueurs d'échec.
La difficulté, c'est que le niveau d'un joueuse ne s'observe pas directement ;
il ne s'observe que comparativement aux niveaux d'autres joueurs,
contre lesquels la joueuse a gagné et perdu.

Comme l'explique très bien David de Science Étonnante dans une de ses dernières vidéos,
dans les années 1960, le chercheur Arpad Elo proposa un nouveau système,
aujourd'hui appelé score ELO,
pour évaluer les niveaux des joueurs à partir de données comparatives.
En bref, après chaque match, le vainqueur va gagner des points, aux dépens du perdant.
Et ce nombre de points gagnés va dépendre des évaluations des niveaux des deux joueurs.

Ainsi, si vous êtes un très bon joueur d'échec, avec un score Elo de 2000,
et si vous battez un joueur médiocre, comme Thibaut,
alors vous ne gagnerez pas beaucoup de points.
À l'inverse, si vous battez un joueur dont le score Elo est 2000,
vous gagnerez pas mal de points.
Enfin, si vous battez un joueur a priori très supérieur à vous, comme Magnus Carlsen,
alors vous gagnerez énormément de points.

De façon plus précise, chaque score Elo X va être associé à une *puissance* $P_X = 10^(X/400)$,
qui va clairement augmenter exponentiellement avec le score X.
Maintenant, si vous avez un score Elo égal X,
et si vous battez un adversaire dont le score Elo est égal à Y,
alors le nombre de points que vous allez gagner sera la puissance de Y
divisée par la somme des puissances des deux joueurs,
c'est-à-dire $P_Y / (P_X + P_Y)$.
On voit bien avec cette formule, que si X est bien plus grand que Y,
ce qui correspond à battre Thibaut,
alors $P_X$ va être beaucoup, beaucoup plus grand que $P_Y$,
et vous gagnerez alors très peu de points.
À l'inverse, si vous battez un joueur de votre niveau, 
autrement dit si X = Y,
alors vous gagnerez un demi-point.
Enfin, si vous battez bien meilleur que vous, alors vous gagnerez presque un point complet.

Notez que si vous perdez, alors vous perdrez cette fois $P_X / (P_X + P_Y)$,
histoire de bien rendre les calculs symétriques entre les deux joueurs.

Alors, sachant que les scores Elo sont plus de l'ordre de 2000,
vous vous dites peut-être que ça va être très long d'atteindre le score Elo 2832 de Magnus Carlsen,
même en supposant que vous êtes meilleur que lui ;
il va falloir gagner des milliers de parties.
Eh bien, en pratique, le système Elo tient bien cela en compte, 
en multipliant le score gagné $P_Y / (P_X+P_Y)$ par un facteur K.
Typiquement, un joueur qui joue peu, et donc le score Elo est donc a priori mal estimé,
pourra avoir un facteur K plus élevé.

En fait, le facteur K est intimement lié au dilemme innovation/sécurité 
dont je vous avais parlé dans une vidéo précédente.  
https://tournesol.app/entities/yt:1vbbdwpN-qc

En terme bayésien, c'est même encore plus lié au dilemme biais/variance,
qui correspond à une vidéo encore un peu plus vieille.  
https://tournesol.app/entities/yt:Jeyb9BbKtpE

Et en terme d'apprentissage statistique, 
le facteur K correspond exactement au pas de l'itération de la descente de gradient,
au learning rate en anglais,
pour minimiser la vraisemblance des données dans un modèle probabiliste.
Et c'est cette observation qui va être la plus intéressante pour nous !


## Le modèle de Bradley-Terry

En 1952, les statisticiens Ralph Bradley et Milton Terry proposèrent 
un modèle probabiliste de l'issue d'un match, à partir du niveau des adversaires.
Ce modèle est très simple : 
la probabilité qu'un joueur de niveau X batte un adversaire de niveau Y 
est donnée par $P_X / (P_X + P_Y)$,
où P_X croît exponentiellement avec X.
C'est le cas du $P_X$ du Elo, où $P_X = 10^(X/400)$,
mais on peut imaginer de façon plus générale une fonction $P_X$ de la forme $P_X = e^{tX}$,
avec un paramètre t qui va définir l'échelle des scores.

Mais maintenant, contrairement au score Elo, dans le modèle de Bradley-Terry,
X et Y vont être des scores inconnus qu'on va estimer,
sans faire d'hypothèse en amont sur leurs valeurs,
comme leurs valeurs calculées jusque là.

Quand on a un modèle probabiliste comme cela, avec des paramètres inconnus,
il est courant de chercher à estimer ces paramètres en sélectionnant ceux
qui rendent les données observées aussi vraisemblables que possible.
Dit autrement, il s'agit ainsi de sélectionner les scores 
qui maximisent la vraisemblance des données sachant ces score.
Ces scores sont alors appelés maximums de vraisemblances.

En supposant que les résultats des différents matchs sont indépendants,
la vraisemblance de ces résultats sachant les scores $X_i$ des différents joueurs est égale
au produit des $P_i / (P_i + P_j)$,
pour tous les matchs entre i et j, et où i désigne le vainqueur du match,
et où $P_i$ est, comme vous l'imaginez, $P_{X_i}$.

Alors, manipuler des multiplications, c'est toujours un peu compliqué.
Donc l'astuce usuelle est alors de prendre le logarithme, 
qui va transformer la multiplication en somme.
Il s'agit alors de maximiser la log-vraisemblance,
qui est alors la somme des $\log (P_i / (P_i + P_j))$.

Et pour maximiser une telle quantité, 
on va chercher à annuler les dérivées partielles par rapport aux scores X_i.
Si on prend un unique terme $\log (P_i / (P_i + P_j))$,
et si on exploite le fait que $P_i$ est de la forme $e^{tX_i}$,
on obtient une dérivée par rapport à X_j est égale à $- P_j / (P_i + P_j)$.
Autrement dit, on obtient exactement l'opposé des points 
que i gagne après sa victoire contre j dans le système Elo, au facteur K près.

En fait, ce calcul de la dérivée d'un terme de la quantité à minimiser, 
et le fait d'ajouter l'opposée de ce terme multiplié par un facteur,
c'est exactement ce que propose l'algorithme de descente de gradient stochastique,
qui est vraiment le moteur de l'apprentissage des réseaux de neurones.  
https://tournesol.app/entities/yt:mRcP592mQ9w  
https://tournesol.app/entities/yt:Q9-vDFvDdfg

D'ailleurs, en pratique, 
dans le cadre du classement de la Fédération Internationale Des Échecs,
la mise à jour des scores ne Elo ne se fait pas juste après un match,
mais plutôt après un tournoi, qui correspond à une suite de matchs.
Et ça, ça correspond exactement à une descente de gradients stochastiques
avec des gradients stochastiques estimés par batchs de données.

Cette interprétation probabiliste des scores Elo permet d'ailleurs 
de comprendre et prouver la cohérence statistique,
c'est-à-dire le fait de retrouver les vrais niveaux des joueurs,
notamment dans des simulations comme celles qu'a fait David dans sa vidéo.   
https://en.wikipedia.org/wiki/Consistent_estimator  
https://tournesol.app/entities/yt:9oRDksmH0zM

L'avantage toutefois d'avoir une approche plus probabiliste,
c'est qu'on n'aura pas à attendre que les joueurs jouent un grand nombre de matchs
pour que leur score estimé par le maximum de vraisemblance sera assez juste.
En termes statistiques, on aura une meilleure complexité d'échantillonnage :
pour un nombre fixé de résultats de matchs, 
on aura une meilleure estimation des niveaux des joueurs.

En particulier, si une très bonne joueuse joue ses premiers matchs officiels,
alors ses premières victimes risquent de perdre beaucoup de points,
car ils perdent contre une joueuse qui a alors un très mauvais score Elo.
Mais au fur et à mesure que le score Elo de la très bonne joueuse sera mieux estimé,
alors les autres joueurs qui perdront contre elle perdront moins de points.
Le moment de la défaite influe alors sur le score des joueurs, ce qui paraît injuste ---
et n'arriverait pas si on prend l'approche probabiliste.

Par ailleurs, on pourra plus naturellement corriger des anomalies,
comme le fait que les scores Elo des joueurs de Chess.com semble surévalué par rapport 
au score Elo attribué par la Fédération Internationale des Échecs à partir des matchs hors-ligne,
qui semble dû à des phénomènes subtils d'inflations de scores dus à l'arrivée de nouveaux joueurs.
On a un phénomène similaire entre le Elo des joueurs français et celui des joueurs russes.

Mieux encore, si on met une casquette pleinement bayésienne,
on peut faire mieux que le maximum de vraisemblance 
et inclure des a prioris pour estimer les niveaux probables de joueurs
qui ont joué très peu de matchs, 
mais au sujet desquels on a d'autres informations qui n'ont pas été répertoriées dans nos données,
et même aller plus loin en estimant l'incertitude qu'il faut avoir sur le niveau estimé d'un joueur.

Bref, l'approche probabiliste est bien meilleure sur de nombreux aspects.
Elle a toutefois un défaut de taille : 
elle requiert des calculs plus difficiles à comprendre pour les joueurs.
En particulier, votre score pourrait évoluer,
même si vous n'avez pas joué,
par exemple si celle qui vous a battu a ensuite battu des joueurs beaucoup plus fort que vous.

La beauté du Elo, c'est qu'il est remarquablement simple à comprendre :
votre score n'évolue qu'après un match.
Il augmente si vous avez gagné, et décroît sinon.
Et le changement est lié à la différence de niveau entre les joueurs.


## Playful:ai

Pour estimer les niveaux des équipes de football de l'EURO 2024,
l'équipe de Playful:ai ne s'est clairement pas attardé sur cette explicabilité.
Ils ont préféré avoir des estimations aussi bayésiennes que possibles.
C'est pourquoi ils sont partis du modèle de Bradley-Terry,
qu'ils ont ensuite adapté pour peaufiner les préditions des matchs.

Notez que, de plus, Playful:ai tient compte du fait 
que le niveau d'une équipe évolue au cours du temps.
Clairement, l'équipe de France des Mbappé, Griezmann et Tchouaméni
n'est pas la même que celle des Gourcuff, Toulalan et Escudé.

Je ne rentre pas dans les détails de comment cette évolution est prise en compte,
mais ce qu'il faut bien voir, 
c'est que le modèle de Bradley-Terry peut naturellement être utilisé comme une pièce
dans un puzzle plus large,
qui modélise un bien plus grand nombre de considérations pertinentes
à l'estimation des niveaux des équipes de football.

En particulier, même si ce n'est pas finalement le modèle qu'ils ont adopté pour Playful:ai,
Lucas Maystre, Victor Kristof et leur directeur de thèse Matthias Grossglauser,
avaient précédemment considéré un modèle selon lequel 
le niveau d'une équipe était le somme des niveaux des joueurs.
Selon ce modèle, il ne s'agit plus d'estimer ce que vaut une équipe ;
il s'agit d'estimer le niveau des footballeurs, pour en déduire le niveau des équipes.

Le gros avantage de cette approche, 
c'est qu'elle permet d'exploiter les résultats des matchs de clubs,
beaucoup plus nombreux,
pour évaluer les niveaux des équipes nationales.

Malheureusement, elle a aussi quelques défauts.
En premier lieu, elle requiert beaucoup plus de calculs, car il y a beaucoup de joueurs.
Un truc chouette, c'est que des astuces à base de méthodes de noyau, ou kernel en anglais,
peuvent être utilisées pour court-circuiter l'estimation des niveaux individuels des joueurs
et obtenir des estimations avec moins de calculs.

Mais surtout, le plus gros problème, 
c'est que cette méthode nécessite de collecter les informations 
à propos des joueurs qui ont participé aux différents matchs.
Malheureusement, ces données sont souvent déficientes ; et c'est vraiment là que le bât blesse.

Pour être honnêtre, j'espérais initialement faire une vidéo sur le GOAT du football,
à savoir le meilleur joueur de tous les temps ;
mais cette difficulté d'accès aux données est ce qui a rendu cette ambition caduque.

Quoi qu'il en soit, grâce à playful:ai, désormais relayé par le journal 20 Minutes,
je peux vous fournir une réponse à la question de cette vidéo.
Selon un modèle bayésien en tout cas, 
la probabilité de victoire de la France est égale à XXX.
Donc votre espérance de gain est XXX * XXX - XXX, ce qui est... XXX.


## Alignement des modèles de langage

Le modèle de Bradley-Terry a récemment suscité énormément d'intérêt, 
notamment dans le cadre de ce que les Big Techs appellent "l'alignement des modèles de langage",
et qu'on appelle parfois plus communément le "fine tuning".
En particulier, dans ce cadre, on demande à des juges humains
de comparer différentes réponses possibles d'un modèle de langage,
pour ensuite modifier le modèle de langage et le pousser à préférer certaines formes de complétion.

Alors, historiquement, l'approche annoncée en fanfare par OpenAI lors du lancement de ChatGPT
a été nommée "Reinforcement Learning with Human Feedback",
notamment suite à des travaux de Google et OpenAI de 2017,  
https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html  
complétés dans un article de 2020.  
https://arxiv.org/pdf/1909.08593

En gros, l'idée de ces approches est de modéliser les juges humains 
par une fonction qui assigne un score à chaque réponse de ChatGPT.
Ce score est une fonction linéaire d'une représentation vectorielle de la réponse.
Autrement dit, on représente la réponse par une suite de nombres,
et on suppose que le score de la réponse est une somme pondérée de la suite de nombres.
Il s'agit ensuite de déterminer les coefficients de la fonction linéaire,
c'est-à-dire la valeur, positive ou négative, d'avoir un grand nombre dans chaque case.
Autrement dit, on va estimer la contribution de chaque coordonnée au score de la réponse,
un peu comme on cherchait à déterminer les niveaux des joueurs des équipes de football.

Bref, pour ceux qui ont l'habitude de faire de l'apprentissage des préférences humaines,
ce dispositif est loin d'être aussi révolutionnaire 
que ce que le marketing surpuissant d'OpenAI peut laisser croire.
Il y a trop souvent une tendance,
dans les organisations qui développent des algorithmes génératifs,
à survendre leurs travaux, et à ignorer ceux des autres,
simplement parce que ces organisations font des profits énormes 
grâce au buzz qu'elles génèrent ;
alors que, en pratique, dans les nombreuses entreprises clientes avec qui j'ai échangé,
le retour d'expérience est davantage que 
la valeur commerciale de ces algorithmes génératifs est en fait loin d'être incroyable,
dès lors qu'il faut faire plus que simplement pondre des codes basiques
ou dès lors que la fiabilité des informations générées est un tant soit peu importante.

En fait, côté recherche, l'énorme littérature scientifique
sur l'élicitation et l'apprentissage des préférences n'a pas attendu 
la recherche sur l'alignement pour développer des solutions.
En fait, les IA les plus puissantes et les plus lucratives des Big Techs,
à savoir les algorithmes de ciblage publicitaire et de recommandation,
sont obsédées depuis bien longtemps par les préférences humaines,
et cherchent constamment à prédire ce qui vous plaira.
Et pour ce faire, elles exploitent en fait massivement Bradley-Terry 
et les jugements comparatifs des internautes,
en considérant typiquement que vous cliquez sur l'option qui vous attire le plus,
pour estimer ce que vous préférez.
Bref. Méfiez-vous énormément de la hype, surtout quand elle vient d'OpenAI,
qui tend à faire croire qu'ils ont inventé la roue 
que d'autres chercheurs ont créée bien avant...  

Mais bon, l'influence du marketing d'OpenAI sur le monde académique est tellement grand,
que je me suis senti obligé de rajouter l'expression "Reinforcement Learning with Human Feedback"
dans mes articles de recherche,
car cela augmente clairement drastiquement la probabilité que l'article soit accepté.
Et oui, je relaie moi aussi le marketing d'OpenAI dans les publications scientifiques,
pour espérer passer le filtre de la revue par le comité de lecture
composé d'humains fortement exposés à ce marketing.

Mais surtout là où les travaux d'OpenAI ont été très largement survendus,
c'est que le "Reinforcement Learning with Human Feedback" n'est en fait pas 
le coeur de "l'alignement des chatbots" ;
le gros du travail de "dressage" des algorithmes de langage 
réside beaucoup plus dans le fameux pré-prompt,
dont Monsieur Phi vous a excellemment bien parlé,
et dont beaucoup de chercheurs ont identifié les énormes limites en termes de sécurité ;
pour s'en rendre compte, il suffit de taper "LLM jailbreaking" ou "prompt injection"
sur un moteur de recherche comme DuckDuckGo.

Quoi qu'il en soit, des chercheurs de Stanford ont par la suite montré
que le "Reinforcement Learning with Human Feedback" est en fait équivalent
à une approche peut-être plus simple, 
ou en tout cas plus directe puisqu'ils l'ont appelé "Direct Preference Optimization",
qui consiste à voir les jugements comparatifs des juges humains
comme des votes directement sur les paramètres du modèle de langage.  
https://arxiv.org/pdf/2305.18290

Ainsi, lorsqu'on dit qu'on préfère une réponse A à une réponse B,
on dit finalement qu'il faut tourner les paramètres d'un algorithme,
de sorte à favoriser la réponse A à la réponse B.
Cette intuition peut être parfaitement formalisée,
à travers un modèle de Bradley-Terry paramétré par les paramètres de l'algorithme ;
autrement dit, l'alignement des réseaux de neurone,
qu'il s'agisse d'un modèle de langage ou d'une IA de recommandation,
ce n'est finalement pas beaucoup plus qu'un modèle bayésien paramétré de Bradley-Terry,
avec un a priori fourni par le modèle pré-entraîné.

Dit plus simplement,
en disant que vous préférez une réponse A à une réponse B,
vous ne faites rien d'autre que fournir une sorte de résultat d'un match entre A et B,
et la mécanique de Bradley-Terry permet de modifier automatiquement des algorithmes 
pour coller davantage à vos préférences.


## La généralisation de Bradley-Terry

Il y a un an, je partageais sur Twitter la joie intense d'une découverte mathématique,
que mon ami Julien Fageot et moi avions faites,
en cherchant à généraliser le modèle de Bradley-Terry 
pour tenir compte de jugements comparatifs quantitatifs.  
https://x.com/le_science4all/status/1666199278841212928

Concrètement, une victoire 7-0 nous dit un peu plus sur la différence de niveau entre les équipes
que le simple fait qu'il y a eu une victoire.
Ne pourrait-on pas exploiter cette information sur la différence de buts
pour peaufiner notre estimation des niveaux des équipes ?

Ce problème est au coeur de Tournesol, 
où les jugements des contributeurs sont des comparaisons quantiatives entre vidéos,
dans la mesure où il y a un slider qui peut être déplacé presque continûment de gauche à droite.
Et c'est donc rapidement devenu l'un des nombreux problèmes fondamentaux du projet,
et, il me semble, plus généralement, au coeur de tout projet de démocratie numérique.
En effet, si on veut que les citoyens votent, il faut définir leurs modes d'expression ;
ce qu'on appelle dans le jargon le problème de l'élicitation des préférences.

Pour des raisons notamment de facilité de calculs,
j'ai initialement opté pour un modèle quadratique, 
qu'on appelle aujourd'hui dans le code de Tournesol le modèle Hookien,
en référance au ressort à énergie potentielle quadratique du modèle du physicien Robert Hooke.
Mais on s'est rendu compte que ce modèle peut justifié théoriquement
avait de surcroît de nombreuses mauvaises propriétés :
en particulier, pour des raisons que je vous épargne aujourd'hui,
il pouvait arriver que, en accroissant le jugement comparatif entre deux vidéos,
on en venait à décroître le score de la vidéo jugée plus positivement.
Clairement cette propriété était fortement indésirable ;
elle poussait même des contributeurs de tournesol à éviter les jugements extrêmes.

Clairement, il fallait un modèle plus solide théoriquement.
J'ai alors ressorti de mes tiroirs un vieux modèle que j'avais initialement considéré,
sans toutefois avoir su démontrer qu'il avait les propriétés escomptées.
Et j'ai ensuite eu la chance de pouvoir en parler à Julien.
Et honnêtement, la merveilleuse structure mathématique dont parle mon tweet,
c'est beaucoup plus à Julien qu'à moi qu'on la doit !

Non seulement Julien a démontré que mon modèle avait la propriété de monotonie ;
qui dit que si on rend une comparaison davantage favorable à A contre B,
alors ça va nécessairement améliorer le score de A, et décroître celui de B.
Mais surtout, Julien a démontré que mon modèle faisait partie d'une famille plus générale
qu'on a ensuite appelé "modèle de Bradley-Terry généralisé",
dont tous les membres avait cette propriété de monotonie.

Mieux encore, toute cette famille, 
dont les membres sont paramétrés par une loi de probabilité qu'on appelle la loi racine,
garantit que la log-vraisemblance sera toujours convexe,
et même souvent calculable explicitement,
grâce à des connections avec les fonctions génératices des cumulants,
qui ont été beaucoup étudiées précédemment par d'autres chercheurs.

Enfin, l'ajout d'un a priori bayésien gaussien garantissait pour une sous-famille
des propriétés désirable de résilience du modèle à des jugements erronés ;
et oui, sur Internet, ça arrive très souvent de faire une erreur grossière,
comme confondre la vidéo de gauche et de droite au moment de la comparaison !

La découverte de cette structure mathématique merveilleuse a vraiment été
l'un des grands temps forts de l'année 2023 pour moi,
et j'y vois une contribution importante à la recherche sur l'apprentissage des préférences humaines.
Et je ne suis pas le seul ;
j'ai le grand plaisir de vous dire que notre article de recherche a été accepté à publication
dans la prestigieuse conférence académique AAAI 2024.

En tout cas, côté Tournesol, on s'est rapidement précipité 
pour ajouter cette découverte mathématique 
aux algorithmes qui aggrègent les jugements des contributeurs,
pour ensuite identifier les vidéos qui, selon nos contributeurs,
sont les meilleures à recommander massivement
parmi toutes les vidéos publiées sur YouTube !


## L'élicitation et l'apprentissage des préférences

De façon plus générale, 
tout projet de démocratie numérique est inéluctablement confronté
au problème de l'espace de paroles des citoyens.

Dans les scrutins classiques, cet espace est extrêmement limité,
puisqu'il correspond à ne choisir qu'un candidat politique parmi une poignée d'alternatives.
À l'inverse, sur des réseaux sociaux notamment,
cet espace est rapidement chaotique, 
puisque les citoyens peuvent produire des threads interminables,
qu'il va être difficile d'agréger en une décision collective à prendre,
qui résulterait clairement des avis citoyens exprimés.

Des méthodes alternatives d'expression, semi-structurées, semblent requises.
C'est ce que propose notamment la plateforme Pol.Is, Make.org et les Community Notes de Twitter,
où les participants peuvent émettre de courtes propositions,
et évaluer les propositions des autres, avec des jugements directs à coups de likes et dislikes.
Voilà des formes de délibération beaucoup plus structurées et faciles à analyser,
et qui permettent néanmoins d'entrer dans bien plus de complexité que les scrutins classiques.

Cependant, on pourrait vouloir explorer des propositions plus complexes,
qui ne tiennent pas en 140 caractères,
et on pourrait vouloir émettre des jugements plus subtils que juste "like" ou "dislike".
Et bien, d'une certaine manière, c'est précisément ce que propose Tournesol.
Les propositions considérées sont les vidéos YouTube, 
qui chacune contient en fait des narratifs sous-jacents, avec différentes justifications ---
et j'ai envie de dire même une chanson douce,
que me chantait ma maman, promeut un narratif de ce genre !

Tournesol propose ainsi d'évaluer ces différentes propositions.
Et plutôt qu'un simple "like" ou "dislike", 
on demande donc des comparaisons quantitatives, 
qu'on analyse avec un modèle généralisé de Bradley-Terry.

Cependant, il est loin d'être clair
que cette élicitation de préférences par comparaisons quantitatives
est la meilleure des formes d'expression possible.
En particulier, nombre de contributeurs au projet nous ont suggéré d'avoir un système de notation,
car celui-ci pourrait être plus simple à utiliser.
Voilà qui correspond à un vieux débat dans le domaine :
faut-il préférer les jugements directs, comme sur IMDB, ou comparatifs ?

Eh bien, on a fait récemment des progrès dans ce débat, que je vous détaillerai une autre fois.
Mais intuitivement, si ce qui nous intéresse, 
c'est de discerner les tops vidéos parmi les excellentes vidéos,
et de ne jamais recommander les vidéos bofs,
alors une combinaison judicieuse de jugements directs et comparatifs semble être optimale.
En particulier, les jugements directs semblent très utiles pour dérecommander,
mais les jugements comparatifs semblent plus utiles pour recommander le very best.

Mais tout ça, on en reparlera sans doute une prochaine fois...


## Conclusion

L'une des grandes joies des mathématiques, 
c'est de créer des passerelles qui unifient des sujets a priori extrêmement distants.
J'espère que, dans cette vidéo, j'ai pu vous faire sentir cela.
En étudiant les comparaisons, le modèle de Bradley-Terry et ses généralisations
font le pont entre un grand nombre de disciplines,
de l'évaluation des niveaux des joueurs d'échec aux paris sportifs,
en passant par l'apprentissage des préférences humaines,
avec des applications fondamentales pour la démocratie numérique.

En particulier, les modèles de Bradley-Terry se sont retrouvés 
au coeur d'initiatives de démocratie numérique,
comme les excellents projets WeBuildAI pour la gouvernance collaborative du don de nourriture, 
et ses variantes appliquées à l'éthique des voitures autonome ou au don de rein.
https://arxiv.org/abs/1709.06692  
https://dl.acm.org/doi/10.1145/3359283  
https://www.sciencedirect.com/science/article/pii/S0004370220300229

Et j'aimerais tellement pouvoir vous dire qu'un grand nombre de grandes équipes 
travaillent d'arrache-pied pour aller beaucoup plus vite beaucoup plus loin 
dans la recherche sur les fondements mathématiques, 
mais aussi philosophiques, psychologiques et sociologiques,
d'une démocratie numérique sécurisée et satisfaisante.

Malheureusement, à l'heure même où la haine triomphe à travers le monde,
avec une montée terrifiante de l'autoritarisme et de la corruption,
je dois bien avouer que les moyens de recherche alloués à ces sujets d'intérêt public
sont aujourd'hui minimes,
surtout en comparaison des moyens monumentaux alloués aux algorithmes génératifs,
par le privé et par la recherche publique,
lesquels sont en fait beaucoup plus simples à intégrer dans des applications malveillantes,
à commencer par les arnaques en ligne, la désinformation et, peut-être surtout,
le cyberharcèlement via des deepfakes pornographiques.  
https://www.rts.ch/play/tv/doc-a-la-une/video/porno-et-hypertrucage--une-intimite-volee?urn=urn:rts:video:14765180

En tout cas, le projet Tournesol va malheureusement être ralenti.
Notre association à but non lucratif n'ayant pas su récolter des fonds suffisants,
j'ai été contraint de licencier le seul employé de Tournesol,
qui est pourtant une personne fantastique et absolument brillante.
Tournesol va ainsi redevenir un projet entièrement bénévole,
avec des contributeurs dévoués qui, comme moi, 
développons ce projet et effectuons des découvertes scientifiques,
uniquement sur notre temps libre, quelques heures par semaine.

Clairement, si l'on veut combattre efficacement la haine, la corruption et la désinformation,
il va nous falloir rapidement beaucoup plus d'aides.
Et vous pouvez aider.
Vous pouvez aider financièrement, avec des dons à l'Association,
ou en nous accompagnant dans des demandes de subventions.
Vous pouvez aussi aider techniquement, en contribuant au code libre et open source,
ou en collaborant avec nous sur des sujets de recherche.
Et puis, vous pouvez nous aider directement, en fournissant des jugements sur la plateforme,
qui aideront la communauté à identifier davantage de contenus d'intérêt public,
et qui nouriront la base de données publiques pour attirer les chercheurs 
vers les sujets de démocratie numérique,
plutôt que vers la hype des algorithmes génératifs.
Enfin, vous pouvez nous aider en promouvant le projet autour de vous.
Dites à vos proches de participer, interpelez les influenceurs et les journalistes,
et exigez que la démocratie numérique devienne un sujet central,
une réponse indispensable au déclin globalisé des démocraties,
comme on en parle en long, en large et en travers dans notre livre #LaDictatureDesAlgorithmes.

On a désespérément besoin de vous, 
pour avancer la recherche sur l'élicitation et l'apprentissage des préférences des citoyens, 
et pour proposer une solution de gouvernance démocratique de l'espace informationnelle,
et empêcher le contrôle de cet espace par des milliardaires, des multinationales et le cybercrime.

