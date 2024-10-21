# Indexer l'information avec des modèles de langage (RAG)

La dernière fois, je vous ai parlé du fonctionnement des algorithmes de langage,
et en particulier des transformers,
cette architecture de réseaux de neurones devenue omniprésente
dans les algorithmes modernes comme ChatGPT ou Llama.
Et si vous vous en souvenez, 
j'ai parlé d'une application raisonnablement sécurisable de ces systèmes,
à savoir l'indexation de l'information.
Dans le jargon, on parle souvent de RAG, pour Retrieval Augmented Generation ;
et la partie qui me semble sécurisable et utile,
c'est surtout le "R" pour "Retrieval",
c'est-à-dire la "Récupération" de l'information.

L'idée du RAG, c'est ajouter au dessus de la couche de "R"
une couche de génération de textes,
parce que, apparemment, si on ne fait pas du génératif en 2024,
on n'est pas dans la hype de l'IA...
En tout cas, si vous voulez tester un exemple de RAG,
je vous invite à teste le site [perplexity.ai](https://perplexity.ai).

"Parle moi du projet Tournesol..."
La réponse est vraiment pas si mal, 
même si elle est un peu trop centrée sur ma personne,
alors que je suis très loin d'être le seul derrière ce projet.
Et tiens, il croit que je suis encore à l'EPFL...
Bref, la génération est discutable, 
notamment parce que tout le texte généré ne s'appuie que sur 2 références, 
qui datent toutes deux de 2021...  
https://www.perplexity.ai/search/parle-moi-du-projet-tournesol-OIvJH3jERquremRhjUHsog

OK. Mais donc, comment ces 2 références ont été récupérées ?
Comment peut-on indexer de l'information textuelle avec les algorithmes de langage,
et ensuite identifier celle qui est la plus pertinente pour une requête donnée ?


## Comment enseigner des informations aux algorithmes de langage ?

Quatre grandes catégories de solutions ont été proposées
pour faire en sorte qu'un algorithme de langage apprenne une information.
En premier lieu, il y a le pré-entraînement, ou "pre-training",
qui est correspond au "P" dans ChatGPT.

Rappelez-vous que le principe de base de la conception des algorithmes de langage
consiste à ingurgiter d'énormes quantités de textes,
généralement en très grande partie téléchargées du web,
et de modifier les centaines de milliards de paramètres de ces algorithmes
pour qu'ils soient capables de régurgiter des textes semblables
à ceux des données d'entraînement.
C'est en cela qu'on les appelle parfois des "perroquets stochastiques".

Mais du coup, ce faisant,
si l'entraînement a exposé ces algorithmes a de nombreux textes 
qui disent que le projet Tournesol est un projet de démocratie numérique,
alors les algorithmes de langage vont fournir à leur tour de telles descriptions,
et ce avec grande probabilité.

En pratique, ce pré-entraînement est toutefois très insuffisant
pour que les algorithmes de langage soient capables de se comporter de manière satisfaisante.
Après tout, sur le web, on trouve beaucoup de textes publiés qui sont, disons,
écrit de manière pas entièrement satisfaisante.
On sait par exemple que Google a entrainé ses algorithmes sur des articles de Breitbart,
un média américain que Wikipedia accuse de publier des histoires intentionnellement trompeuses.
Au delà du problème des droits d'auteur que cela soulève,
il y a clairement un problème de qualité de l'information,
si l'algorithme de langage de Google se contente de répéter des informations de Breitbart.

Pour augmenter la fiabilité de l'algorithme,
on peut alors effectuer un "peaufinage", qu'on appelle "fine-tuning" en anglais,
et qui consiste typiquement à demander à des humains d'évaluer différentes réponses de l'algorithme.
L'approche la plus standard, 
publicisé sous le nom de "reinforcement learning with human feedback",
et qui revient à appliquer les algorithmes des années 1950
comme on l'a vu dans une [vidéo précédente](https://tournesol.app/entities/yt:2cvj2-Vh8Uc),
cette approche consiste à demander à des humains de fournir des jugements comparatifs
entre des réponses proposées par l'algorithme,
et d'ensuite modifier l'algorithme pour qu'il favorise la génération de textes
que les humains sondés préfèrent.
Cependant, cette approche de peaufinage est coûteuse,
à la fois en termes de ressources humaines et de ressources en calculs,
et son efficacité est loin d'être suffisante.

Notez qu'on parle aussi de "peaufinage" pour la poursuite du pré-entraînement,
mais cette fois sur des données proches du cas d'usage de l'algorithme.
C'est typiquement le cas quand on part d'un algorithme open-weight comme Llama,
et qu'on cherche à l'adapter aux contextes d'utilisation d'une entreprise particulière.
Mais là encore, le coût de cette approche est important,
et son efficacité est insuffisante.

Une troisième approche, au delà donc du pré-entraînement et du peaufinage,
est le pré-prompting.
Ça consiste à fournir directement des instructions à l'algorithme,
en invoquant typiquement un personnage imaginaire 
et en demandant à l'algorithme de parler comme ce personnage imaginaire parlerait.
En pratique, le personnage imaginaire sera typiquement un "chatbot bienveillant".
Mais comme Monsieur Phi en parle si bien 
dans sa [vidéo sur le sujet](https://tournesol.app/entities/yt:dDhTMIao-fM),
si cette approche est la plus efficace et la moins coûteuse,
elle demeure encore très largement non-sécurisée ;
et il faut s'attendre à ce que le chatbot déraille.
Mais surtout, le pré-prompting est nécessairement limité car il ne peut pas être trop long.
Les modèles de langage ont en effet une fenêtre contextuelle restreinte,
ce qui fait qu'au bout d'un moment, 
ils oublient complètement ce qui a été dit précédemment.

On en vient alors à la quatrième et dernière approche,
qui va demander plus de travail humain et calculatoire que le pré-prompting,
mais nettement moins que le pré-entraînement et le peaufinage.
Cette approche, c'est donc le "Retrieval Augmented Generation",
qui va être "non-paramétrique",
c'est-à-dire qu'elle va s'appuyer sur une base de données qui va grossir
au fur et à mesure qu'on demande à l'algorithme d'apprendre plus d'informations.

L'idée est la suivante :
on va indexer tout un tas de documents qu'on souhaite enseigner à l'algorithme,
et on va définir des méthodes pour lui permettre d'identifier,
étant donné une requête d'un utilisateur,
les bouts de documents qui sont les plus pertinents
pour répondre à la requête de l'utilisateur.
Ces bouts de documents sont ainsi "récupérés",
et ils seront alors ajoutés à un preprompt fourni à l'algorithme, d'où "l'augmentation".
Enfin, on va demander à l'algorithme de générer une réponse avec ce préprompt,
d'où le nom de "Retrieval Augmented Generation".
La boucle est bouclée !


## Indexer les documents par des représentations vectorielles

OK, ça c'est pour la vue d'ensemble de l'approche.
Mais il reste à définir comment l'algorithme de langage peut identifier,
dans un énorme tas de documents,
les extraits qui sont les plus pertinents pour répondre à une requête donnée.
Et bien, l'astuce devenue prédominante,
c'est d'utiliser des représentations vectorielles des extraits des documents.

Pour cela, on peut faire un petit retour en arrière, il y a une décennie,
avec l'introduction de word2vec,
un algorithme dont je vous ai parlé il y a maintenant 6 ans... 
et oui le temps passe vite...
La recherche sur les réseaux de neurones artificiels avait déjà alors réussi
à construire une sémantique des mots,
en remplaçant chaque mot par une liste de nombres,
et avec des propriétés remarquables comme le fait que
si on prend le vecteur associé au mot "roi",
si on lui retranche celui associé au mot "homme",
et si on ajoute celui associé à "femme",
on obtient un vecteur très proche du vecteur du mot "reine".

Au delà de cette opération algébrique mystérieuse,
l'observation fondamentale de word2vec,
c'est que les mots dont le sens est intuitivement similaires
ont tendance à avoir des représentation vectorielle similaire.
Le mot "chien" est ainsi proche du mot "chat".
On peut donc utiliser la similairét des représentations vectorielles
pour déterminer si deux mots se font référence,
et donc s'il est pertinent de penser à l'un quand on nous parle de l'autre.

Eh bien, cette idée intuitive, 
elle a depuis été généralisée à la représentation sémantique de phrases,
voire à celle de paragraphes ou même de documents entiers.
Et bon, j'aimerais pouvoir vous dire 
qu'il y a une méthode sur laquelle la recherche a convergé,
et qui est la bonne méthode pour mesurer la proximité sémantique de deux phrases.

En pratique, il s'agit en fait encore d'un énorme champ de recherche,
et tout ce que je dis aujourd'hui de trop précis risque bien fort d'être contredit 
dans les années à venir ;
voire peut-être même dans les mois à venir.

Mais en tout cas, jusque là, l'une des idées les plus dominantes
consiste à exploiter les algorithmes de langage 
pour déterminer des représentations sémantiques des phrases.
Plus précisément, on a vu que, via un transformer comme Llama 3,
on peut transformer toute une phrase en une représentation matricielle,
notamment au bout du transformer,
qui sera alors optimisé pour prédire les prochains mots.
Eh bien, pendant quelques années au moins,
on combinait les colonnes de la matrice, 
pour ensuite obtenir une représentation vectorielle,
dont la taille est indépendante de la phrase considérée.
On parle parfois d'opération de "regroupement", ou "pooling" en anglais.

À voir : https://arxiv.org/abs/2201.10005

Mieux encore, on peut considérer qu'il s'agit là d'un bon premier pas,
mais on peut ensuite optimiser l'opération de pooling
pour qu'il se conforme à des jugements humains de similarité de textes,
ou à des corpus de textes avec des questions et des réponses.
Dernièrement, un [article publié dans ACL](https://arxiv.org/abs/2401.00368) 
suggère qu'on peut même automatiser ces opérations,
en utilisant directement des modèles de langage pour générer
des paires questions/réponses.

Bref. Quels que soient les détails,
on peut exploiter des algorithmes de langage pour construire une fonction,
qui prend n'importe quel morceau de documents ou n'importe quelle requête d'utilisateur,
et qui calcule des représentations vectorielles à partir de tout ça.

En faisant maintenant passer toutes sortes de documents dans cette moulinette,
on peut ainsi concevoir une base de données de représentations vectorielles
des morceaux des documents analysés.
À chaque nouvelle requête, il nous suffira alors d'identifier dans cette base de données
les représentations vectorielles qui collent le mieux à la requête,
c'est-à-dire qui sont les plus similaires à la représentation vectorielle de la requête.
C'est ainsi qu'on espère récupérer les informations les plus pertinentes
pour une requête donnée.


## Structurer les bases de données vectorielles

OK. Mais il y a toutefois un problème avec cette approche.
Et c'est un problème de taille. Littéralement.
En effet, dans certaines applications, comme perplexity.ai,
le nombre de documents à analyser est gargantuesque ;
en l'occurence il s'agit de l'ensemble du web, 
et donc au moins des milliards de pages web !

Chercher à chaque requête le bout de page web le plus proche d'une requête
semble alors requérir autant d'opération qu'il y a de morceaux de documents analysés,
ce qui représente énormément de travail calculatoire à chaque requête !
Comment, dans une base de données vectorielles,
peut-on rapidement identifier les vecteurs les plus proches d'un vecteur donné ?

Eh bien, c'est une question que je me suis posé,
[et que j'ai même posée sur Twitter](https://x.com/le_science4all/status/953777728054022144), 
il y a 6 ans...
en parlant d'ailleurs alors avec Adrien Matissart,
que je ne connaissais pas à l'époque,
mais qui est devenu depuis le Vice-Président de l'Association Tournesol !
Et bon, je ne connais pas assez le domaine pour savoir si des progrès ont été faits,
mais a priori je conjecture encore que la réponse est non,
il n'y a pas de solution sous-linéaire à la maximisation de la recherche d'un plus proche vecteur
dans une base de données vectorielle...

En pratique en tout cas, les RAG s'appuient des algorithmes
de recherche du plus voisin approximatif.

http://sites.computer.org/debull/A23sept/p39.pdf


## Quelques autres considérations

https://arxiv.org/pdf/2312.10997



## Conclusion



