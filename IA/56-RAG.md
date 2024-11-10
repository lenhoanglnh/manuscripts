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
Comment peut-on indexer d'énormes quantités d'informations avec les algorithmes de langage,
et ensuite identifier celle qui est la plus pertinente pour une requête donnée ?


## Comment enseigner des informations aux algorithmes de langage ?

Quatre grandes catégories de solutions ont été proposées
pour faire en sorte qu'un algorithme de langage apprenne une information.
En premier lieu, il y a le pré-entraînement, ou "pre-training",
qui est correspond au "P" dans ChatGPT.

Rappelez-vous que le principe de base de la conception des algorithmes de langage
consiste à ingurgiter d'énormes quantités de textes,
généralement en très grande partie téléchargées du web,
et à modifier les centaines de milliards de paramètres de ces algorithmes
pour qu'ils soient capables de régurgiter des textes semblables
à ceux des données d'entraînement.
C'est en cela qu'on les appelle parfois des "perroquets stochastiques".

Mais du coup, ce faisant,
si l'entraînement a exposé ces algorithmes à de nombreux textes 
qui disent que le projet Tournesol est un projet de démocratie numérique,
alors les algorithmes de langage vont fournir à leur tour de telles descriptions,
et ce avec grande probabilité.

En pratique, ce pré-entraînement est toutefois très insuffisant
pour que les algorithmes de langage soient capables de se comporter de manière satisfaisante.
Après tout, sur le web, on trouve beaucoup de textes publiés qui sont, disons,
écrits de manière pas entièrement satisfaisante.
On sait par exemple que Google a entrainé ses algorithmes 
sur [des articles de Breitbart](https://www.theguardian.com/technology/2023/apr/20/fresh-concerns-training-material-ai-systems-facist-pirated-malicious),
un média américain que Wikipedia accuse de publier des histoires intentionnellement trompeuses.
Au delà du problème des droits d'auteur que cela soulève,
il y a clairement un problème de qualité de l'information,
si l'algorithme de langage de Google se contente de répéter des informations de Breitbart.
Idem d'ailleurs pour [Facebook](https://gizmodo.com/ai-bard-google-facebook-trained-on-breitbart-rt-1850352405).

Pour augmenter la fiabilité de l'algorithme,
on peut alors effectuer un "peaufinage", qu'on appelle "fine-tuning" en anglais,
et qui consiste typiquement à demander à des humains d'évaluer différentes réponses de l'algorithme.
L'approche la plus standard a été publicisée 
sous le nom de "reinforcement learning with human feedback",
alors qu'elle revient simplement à appliquer les algorithmes des années 1950
comme on l'a vu dans une [vidéo précédente](https://tournesol.app/entities/yt:2cvj2-Vh8Uc).
Cette approche consiste à demander à des humains de fournir des jugements comparatifs
entre des réponses proposées par l'algorithme,
et à ensuite modifier l'algorithme pour qu'il favorise la génération de textes
que les humains sondés préfèrent,
un peu comme on le fait sur Tournesol dans le cas des IA de recommandation.
Cependant, cette approche de peaufinage est coûteuse,
à la fois en termes de ressources humaines et de ressources en calculs,
et son efficacité est loin d'être suffisante pour une tâche aussi complexe que le langage.

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
Alors, il y a différentes astuces pour tenter d'augmenter cette fenêtre contextuelle,
mais les performances sont limitées,
et elles ne suffisent pas à retenir des énormes quantités d'information,
comme l'ensemble des transcripts des vidéos Science4All par exemple.

On en vient alors à la quatrième et dernière approche,
qui va demander plus de travail humain et calculatoire que le pré-prompting,
mais nettement moins que le pré-entraînement et le peaufinage.
Cette approche, c'est donc le "Retrieval Augmented Generation" ou RAG,
qui va être "non-paramétrique",
c'est-à-dire qu'elle va s'appuyer sur une base de données qui va grossir
au fur et à mesure qu'on demande à l'algorithme d'apprendre plus d'informations.
On utilise d'ailleurs actuellement nous aussi un algorithme non-paramétrique sur Tournesol.

L'idée du RAG est la suivante :
on va indexer tout un tas de documents qu'on souhaite enseigner à l'algorithme,
et on va définir des méthodes pour lui permettre d'identifier,
étant donné une requête d'un utilisateur,
les bouts de documents qui sont les plus pertinents
pour répondre à la requête de l'utilisateur.
Ces bouts de documents sont ainsi "récupérés",
et ils seront alors ajoutés à un preprompt fourni à l'algorithme, 
d'où "l'augmentation".
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
c'est que les mots dont le sens est intuitivement similaire
ont tendance à avoir des représentations vectorielles similaires.
Le mot "chien" est ainsi proche du mot "chat".
On peut donc utiliser la similarité des représentations vectorielles
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

Mieux encore, on peut considérer qu'il s'agit là d'un bon premier pas,
mais on peut ensuite optimiser l'opération de pooling
pour qu'il se conforme à des [jugements humains de similarité de textes](https://arxiv.org/abs/2212.09741),
ou à des [corpus de textes avec des questions et des réponses](https://arxiv.org/abs/2201.10005).
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


## Structurer et rechercher dans les bases de données vectorielles

OK. Mais il y a toutefois un problème avec cette approche.
Et c'est un problème de taille. Littéralement.
En effet, dans certaines applications, comme perplexity.ai,
le nombre de documents à analyser est gargantuesque ;
en l'occurence il s'agit de l'ensemble du web, 
et donc au moins des millions de milliards de pages web !

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
Et bon, si on avait tout deux étaient davantage informés,
on aurait su que le problème avait été mathématiquement résolu 3 ans plus tôt, en 2015, 
[par les informaticiens Alexandr Andoni et Ilya Razenshteyn](https://dl.acm.org/doi/pdf/10.1145/2746539.2746553).

Plus précisément, étant donné n vecteurs de la base de données vectorielle,
chaque vecteur étant de dimension d, qu'on illustre ici avec le cas $d = 2$,
le problème du plus proche voisin consiste à concevoir un algorithme qui,
étant donné un vecteur requête x,
retourne le vecteur y le plus proche de x dans la base de données.
Ce problème est simple à résoudre en dimension $d = 1$ :
il suffit de trier les vecteurs de la base de données par ordre croissant,
puis d'effectuer une recherche dichotomique.
Le temps nécessaire pour résoudre ce problème est alors logarithmique en n,
c'est-à-dire en gros quasi instantanné.

Cependant, en grande dimension, le problème est tout de suite beaucoup plus difficile.
À tel point qu'on s'intéresse alors uniquement à des approximations du problème.
Ainsi, le problème du plus proche voisin approximatif avec erreur multiplicative c
est celui de concevoir un algorithme qui, étant donné un vecteur requête x,
retourne un vecteur z de la base de données tels que
la distance entre x et z est inférieure à c fois celle entre x et y ;
où y est le plus proche vecteur dans la base de données.
Donc, par exemple, dans ce dessin, c'est ok de retourner ce point,
mais cet autre point est beaucoup trop loin et ne devrait pas être renvoyé.

De façon amusante, ce problème ressemble beaucoup à celui de la cryptographie postquantique,
dont on reparlera plus tard dans la série sur la cybersécurité...

En tout cas, en 2015, Andoni et Razenshteyn ont conçu un algorithme
dont le temps de calcul de l'ordre de $d n^{\frac{1}{2c^2 - 1}}$,
ce qui est optimal.
Ainsi pour $c = 2$, ce temps de calcul est $d n^{1/7}$,
ce qui est beaucoup moins de $dn$,
dès lors que la base de données vectorielles contient un grand nombre n d'entrées.
Si $n = 10^{14}$, soit cent mille milliards,
alors $n^{1/7} = 100$, ce qui est beaucoup moins que $n$ lui-même.

L'idée de base de l'algorithme d'Andoni et Razenshteyn,
c'est de prendre des directions aléatoires de l'espace et de les sauscissonner.
En faisant cela pour un certain nombre de directions,
qui reste très inférieur à la dimension d de l'espace,
on obtient des sortes de cellules de l'espace,
qu'on peut alors numéroter.
Notez qu'on va sauscissonner uniquement un petit nombre de directions,
si bien que les cellules en questions seront en fait infinies
selon les directions orthogonales aux directions aléatoires sélectionnées.

Néanmoins, en gros, avec grande probabilité, 
deux vecteurs seront assez proches si seulement si ils sont dans la même cellule.
Cette technique de sauscissonnage aléatoire et partiel de l'espace
est ce qu'on appelle celle du hachage avec sensibilité locale, ou LSH en anglais.
Et bon, en fait, seule, elle ne suffit pas.
Mais en ajoutant de nombreuses autres astuces,
qui affinent notamment les cellules en fonction des données,
Andoni et Razenshteyn ont réussi à concevoir un algorithme optimal.

Notez toutefois que ces techniques de sauscissonage ne sont en fait pas
les plus abondamment utilisées aujourd'hui,
notamment car cela peut rester un peu lent pour certaines applications,
où on tient vraiment à un temps de calcul logarithmique en la taille de la base de données.
On préfèrera alors généralement la solution des graphes
de "petit monde hiérarchiquement navigable",
"hierarchical navigable small world" ou HNSW en anglais.

L'idée globale des HNSW,
c'est de mettre les données de la base de données vectorielles sur plusieurs étages,
avec peu de données sur les étages les plus hautes,
et beaucoup plus dans les bas étages.
Sur chaque étage, on va construire un réseau de proches voisins,
et on va créer des passerelles des étages au-dessus vers en dessous.
Étant donné une requête,
on va alors chercher la donnée du premier étage les plus proches,
puis explorer les données du second étage connectées à celle du premier étage sélectionnée,
et ainsi de suite en descendant dans les plus bas étages.

Là encore, il y a énormément d'astuces qui ont été introduites 
pour bien concevoir un graphe HNSW,
et pour optimiser son exploration.
Mais l'idée importante, c'est qu'en adoptant une structure hiérarchique,
on est capable d'accélérer l'exploration,
et de la rendre surtout logarithmique 
en le nombre de données de la base de données vectorielles,
même si du coup, en n'explorant qu'une toute petite partie du graphe,
on aura beaucoup moins de garanties sur la quasi-optimalité
de l'élément sélectionné par la recherche dans le graphe HNSW.

> NB : Une troisième classe d'algorithmes de recherche 
> dans les bases de données vectorielles
> est la quantization du produit cartésien.
> Cependant, de ce que je comprends, 
> elle semble moins solide théoriquement
> et moins déployée en pratique...

Notez que de nombreux enjeux sont encore ouverts,
comme combiner ces structurations des bases de données vectorielles
dans un but d'exploration approximative mais très efficace,
avec des considérations comme le chiffrement de ces bases de données,
voir idéalement leur exploration par chiffrement homomorphe...


## Quelques autres considérations

L'un des intérêts de la structure non-paramétrique du RAG,
c'est qu'il permet de naturellement segmenter les données auxquelles un RAG a accès,
en fonction des privilèges de l'employer qui l'utilise.
Ainsi, le calcul des représentations vectorielles des documents internes d'une entreprise
peut très bien s'effectuer sans tenir compte de ces privilèges,
ce qui réduit les besoins de refaire le travail pour chaque niveau de privilège.
Cependant, on peut ensuite concevoir plusieurs bases de données vectorielles,
avec pour chacune l'ensemble des données 
auxquelles une catégorie d'employés peut accéder.
Voilà qui revient à appliquer le principe de cloisonnement avec moindre privilège,
dont Romain du Marais et moi vous parlons dans notre livre
"Guide de survie au cybercrime en entreprise" paru chez Dunod,
avec une préface de Guillaume Poupard.

Bien sûr, idéalement, il faut aussi appliquer la défense en profondeur,
et combiner cette solution à d'autres pour protéger au mieux 
les données de votre entreprise contre la croissance terrifiante du cybercrime.

Par ailleurs, pour améliorer les performances de récupération de l'information,
en pratique,
on s'est rendu compte qu'il était utile de demander à des algorithmes de langage
de reformuler la requête de plusieurs manières,
et d'ensuite prendre une représentation vectorielle de toutes ces formulations.
Autrement dit, on automatise le "prompt engineering".
Voilà qui peut améliorer la procédure de récupération de l'information.

Par ailleurs, on peut demander à des humains d'évaluer les performances
de la récupération de l'information,
pour ensuite modifier les paramètres de l'opération de récupération de l'information,
notamment au niveau du calcul des représentations vectorielles,
ainsi qu'au niveau des réécritures multiples de la requête de l'utilisateur,
typiquement avec des algorithmes à la Bradley-Terry,
comme on en a parlé dans une [vidéo précédente](https://tournesol.app/entities/yt:2cvj2-Vh8Uc).

Et j'insiste à nouveau là dessus,
ces opérations de récupération de l'information,
à partir de représentations vectorielles et de plus proches voisins approximatifs,
sont non seulement la partie la plus utile du RAG en pratique,
après tout, c'est un peu le job de Google Search
qui a fait la grandeur de l'un des plus grands géants du web,
mais c'est aussi la partie la plus simple à sécuriser.

Et oui, on obtient alors finalement un moteur de recherche,
avec une liste de sources où trouver les réponses à la requête,
sans avoir un algorithme génératif 
qui pourrait générer du [bullshit](https://tournesol.app/entities/yt:JcFRbecX6bk)
et nous expliquer des âneries d'apparence crédible.

Mais si vous tenez vraiment à la partie générative,
vous pouvez réduire les risques d'âneries avec différentes astuces,
typiquement en retravaillant les extraits récupérés par la phase de récupération récupération,
en identifiant les morceaux de ces extraits les plus pertinents,
et de n'ajouter que ces derniers au prompt de l'algorithme génératif,
sur lequel il s'appuiera pour générer une réponse.

Il y a aussi toutes sortes de modules additionnels qui ont été proposés,
et je vous renvoie par exemple à ce survey 
pour en savoir [plus](https://arxiv.org/pdf/2312.10997).
Cependant, même si tout ceci aide, ne vous attendez pas à des miracles.
Même avec un RAG, les algorithmes génératifs produisent encore souvent des âneries,
et il faut donc vraiment éviter d'utiliser la sortie de ces algorithmes
directement en entrée d'autres algorithmes,
surtout pour les applications sensibles comme l'analyse automatisée des emails d'une entreprise
et plus encore [l'envoi automatisé de réponses aux emails](https://arxiv.org/abs/2403.02817).


## Conclusion

Aujourd'hui, les RAG sont vraiment les systèmes fondés sur les modèles de langage 
les plus naturels à intégrer dans des cas d'usage en entreprise ;
et c'est en fait un peu plus particulièrement le cas du "R" de RAG.
Même si ça ne soulève pas la même hype que le "G",
l'indexation de l'information à partir de représentations vectorielles
est en train de modifier en profondeur la manière dont on stocke l'information,
et surtout dont on peut la récupérer.

En fait, pour finir cette vidéo, j'aimerais pousser l'analogie avec le cerveau humain.
Surtout à l'ère d'Internet, en tout cas en ce qui me concerne,
quand on me pose une question,
avant même de répondre, je cherche à avoir constamment une source en tête,
qui justifierait ce que je pourrais dire ensuite.
Autrement dit, mon cerveau semble avoir conçu une sorte de base de données vectorielles
de mes sources d'information.
Mais alors, comment fait-il pour encoder ces sources en vecteurs ?
Comment encode-t-il les questions qu'on me pose en vecteur ?
Et comment utilise-t-il ces encodages pour identifier,
parmi l'immensité des sources que je connais,
celles qui seront les plus pertinentes pour répondre à une question donnée ?
Est-ce que mon cerveau effectue vraiment des opérations vectorielles ?

Clairement c'est très difficile à dire.
Mais clairement aussi, cette manière de penser,
avec des références systématiques à des sources,
c'est quelque chose qui me semble être une bonne manière de penser,
notamment pour éviter de bullshitter et pour gagner en fiabilité épistémique.
C'est en tout cas vraiment ainsi que j'écris mes articles scientifiques,
mais aussi mes scripts de vidéos scientifique et mes fils Twitter.

Et quand on commence à raisonner ainsi,
on se rend aussi vite compte que toutes les sources ne sont pas aussi fiables.
Autrement dit, en pratique, ce qui compte, 
ce n'est pas uniquement la similarité sémantique entre la requête et l'information récupérée.
La fiabilité de la source doit intervenir pour déterminer
s'il faut vraiment lui faire appel pour répondre à la requête.
Voilà qui requiert une évaluation de la recommandabilité de la source.

Eh bien, ça, c'est exactement ce que faisait l'algorithme PageRank de Google, 
à partir des liens entre les pages web,
que Google a remplacé il y a longtemps déjà 
par des solutions clairement beaucoup plus sophistiquée,
mais aussi malheureusement beaucoup plus opaque.

Quoi qu'il en soit, 
on peut douter de la conformité des recommandations de Google
avec celle que feraient les citoyens ou les experts pertinents.
Or résoudre le problème de l'évaluation collaborative des sources d'information,
de sorte à ensuite faciliter la tâche de recommandation des sources d'information,
aussi bien pour les algorithmes que pour les humains,
ça me semble être l'urgence démocratique numéro 1 du monde moderne.
Et pour y arriver, j'ai participé à la création et au développement de la plateforme Tournesol,
qui vise à évaluer la recommandabilité des vidéos YouTube
en s'appuyant sur l'intelligence collective,
à laquelle je vais, comme si souvent, vous appeler à contribuer.
Vous pouvez en particulier nous aider en participant à l'évaluation des vidéos,
en contribuant au code et aux algorithmes qui font tourner la plateforme
et en effectuant des dons à l'Association Tournesol.
Merci beaucoup d'avance.

Tant qu'on n'aura pas fait l'effort d'identifier collectivement les vidéos 
que YouTube devrait recommander massivement,
on restera encore bien embêté,
lorsque Google nous rétorque qu'il n'y a pas d'autres manières
de recommander des contenus à consommer qu'en s'appuyant sur des entreprises privées.
J'espère que je peux compter sur vous,
pour montrer qu'une voie plus sécurisée et démocratique est possible.



