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

De façon plus précise, chaque score Elo X va être associé à un poids P_X = 10^(X/400),
qui va clairement augmenter exponentiellement avec le score X.
Maintenant, si vous avez un score Elo égal X,
et si vous battez un adversaire dont le score Elo est égal à Y,
alors le nombre de points que vous allez gagner sera P_Y / (P_X + P_Y).
On voit bien avec cette formule, que si X est beaucoup plus grand que Y,
ce qui correspond à battre Thibaut,
alors vous gagnerez très peu de points.
À l'inverse, si vous battez un joueur de votre niveau, 
autrement dit si X = Y,
alors vous gagnerez un demi-point.
Enfin, si vous battez bien meilleur que vous, alors vous gagnerez presque un point complet.

Notez que si vous perdez, alors vous perdrez cette fois P_X / (P_X + P_Y),
histoire de bien rendre les calculs symétriques entre les deux joueurs.

Alors, sachant que les scores Elo sont plus de l'ordre de 2000,
vous vous dites peut-être que ça va être très long d'atteindre le score Elo 2832 de Magnus Carlsen,
même en supposant que vous êtes meilleur que lui.
Eh bien, en pratique, le système Elo tient bien cela en compte, 
en multipliant le score gagné Y / (X+Y) par un facteur K.
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
est donnée par P_X / (P_X + P_Y),
où P_X croît exponentiellement avec X.
C'est le cas du P_X du Elo, où P_X = 10^(X/400),
mais on peut imaginer de façon plus générale une fonction P_X de la forme P_X = e^(tX),
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
la vraisemblance de ces résultats sachant les scores X_i des différents joueurs est égale
au produit des P_i / (P_i + P_j),
pour tous les matchs entre i et j, et où i désigne le vainqueur du match,
et où P_i est, comme vous l'imaginez, P_(X_i).

Alors, manipuler des multiplications, c'est toujours un peu compliqué.
Donc l'astuce usuelle est alors de prendre le logarithme, 
qui va transformer la multiplication en somme.
Il s'agit alors de maximiser la log-vraisemblance,
qui est alors la somme des log (P_i / (P_i + P_j)).

Et pour maximiser une telle quantité, 
on va chercher à annuler les dérivées partielles par rapport aux scores X_i.
Si on prend un unique terme log (P_i / (P_i + P_j)),
et si on exploite le fait que P_i est de la forme e^(tX_i),
on obtient une dérivée par rapport à X_j est égale à - P_j / (P_i + P_j).
Autrement dit, on obtient exactement l'opposé des points 
que i gagne après sa victoire contre j dans le système Elo, au facteur K près.

En fait, ce calcul de la dérivée d'un terme de la quantité à minimiser, 
et le fait d'ajouter l'opposée de ce terme multiplié par un facteur,
c'est exactement ce que propose l'algorithme de descente de gradient stochastique,
qui est vraiment le moteur de l'apprentissage des réseaux de neurones.  
https://tournesol.app/entities/yt:mRcP592mQ9w  
https://tournesol.app/entities/yt:Q9-vDFvDdfg

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


## Alignement des algorithmes

Fine-tuning, RLHF.

DPO.


## GBT

Tenir compte des différences de scores.

Root law.

Guaranties mathématiques.

Application à Climpact & Tournesol.


## Les droits de vote

Juger plus de contenus == plus de pouvoir ?

Limiter l'influence maximale de chaque évaluateur.

