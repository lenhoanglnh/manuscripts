# À quoi ressemble le réseau de neurones de ChatGPT ? (Transformeurs)

Vous savez peut-être que ChatGPT,
et plus généralement les modèles de langage,
sont des réseaux de neurones.
Mais une chose que je n'ai toujours pas abordé sur Science4All,
c'est la structure des réseaux de neurones, 
qu'on appelle des *transformeurs*.

Et pour cause, les transformeurs venaient d'être définie en 2017, 
lorsque je faisais ma série sur l'intelligence artificielle,
et on n'était pas sûr alors que c'était l'architecture des IA du futur.
Mais aujourd'hui que cette architecture est devenue ultra-standard
dans les algorithmes génératifs les plus médiatisés, comme ChatGPT,
je vous propose de la décortiquer et de comprendre pourquoi elle "marche" ---
tout en insistant sur les limites béantes de la théorie mathématiques des transformeurs,
notamment en terme de sécurité.


## Les modèles de langage

Pour cette vidéo, je vais m'intéresser en particulier 
au modèle de langage Llama 3,
car l'architecture de ce modèle est une information publique.
D'ailleurs, vous pouvez installer Llama 3 chez vous ---
même si, je préfère vous prévenir, sans carte graphique puissante,
générer du texte avec Llama 3 va être long et laborieux.
Je vais vous parler en particulier ici du modèle à 405 milliards de paramèters.
Si vous voulez juste utiliser Llama 3 en mode chatbot,
je vous invite à aller sur duckduckgo, 
où vous pourrez aussi utiliser Mistral, ChatGPT et Claude 3.  
https://duckduckgo.com/?q=_&ia=chat

Je vous rappellerais juste de ne pas envoyer d'informations sensibles à des chatbots, 
dont les fournisseurs ont désormais embauchés des anciens agents de la NSA.  
https://x.com/Snowden/status/1801610725229498403

Venons-en maintenant à l'architecture de Llama 3.
Celle-ci se compose d'un "tokenizer", 
d'une représentation vectorielle des tokens,
de 126 couches de "blocs du transformer",
d'un module de dé-représentation chargé d'assigner des probabilités aux différents tokens,
et enfin un "detokenizer".

Détaillons ces 5 composants.
Le tokenizer est un algorithme qui va prendre une suite de caractère,
et va le décomposer en composants appelés tokens.
Un token peut être un mot, un morceau de mot, ou même un simple caractère,
comme une lettre de l'alphabet ou un point.
Llama 3 dispose de 128 000 tokens.
Et donc, passé la première couche, 
le texte donné à Llama 3 va être transformé en une suite de d'identifiants de tokens,
c'est-à-dire une suite de nombre, 
tous étant des entiers entre 0 et 127 999.
Pour Llama 3, ce tokenizer est appris indépendamment du coeur du réseau de neurones
qu'est le transformer.
Ainsi, si le prompt donné à Llama 3 a quelque chose comme 200 mots,
le tokenizer va le transformer en une suite de quelque chose comme 400 tokens.

Puis, la seconde étape va consiste à transformer chaque token
en une représentation vectorielle du token.
Pour cela, on va utiliser un tableau de conversion,
qu'on appelle dans le jargon une matrice des représentations vectorielles des tokens.
Cette matrice est appelée tok_embeddings dans le code de Llama 3.
Elle est de dimension 128 000 par 16 384.
Le nombre 128 000 correspond bien sûr au nombre de tokens,
alors que 16 384 correspond à la dimension de l'espace de représentation des tokens.
Cette matrice va nous permettre de transformer la suite de tokens
en une suite de représentations vectorielles.
Comme vous l'imaginez peut-être, l'identifiant du token, s'il est égal à k,
est remplacé par la k-ième colonne de la matrice des représentations vectorielles des tokens.
En faisant cela token par token,
on a une transformation de la suite de 400 tokens 
en une suite de 400 vecteurs de dimension 16 384.
Une suite de tels vecteurs forme naturellement une matrice,
qui va ainsi être de dimension 400 par 16 384.
On peut alors parler de représentation matricielle du prompt.

Ensuite, cette représentation matricielle va subir une suite de transformations, 
par les 32 couches de "blocs-transformers", qu'on va détailler par la suite.
C'est la troisième étape, la plus importante, la plus complexe et la plus coûteuse en calculs.
Intuitivement, chaque couche va ajouter une modification à la représentation matricielle,
de sorte que, petit à petit, 
chaque colonne se transforme en un vecteur capable de prédire le token suivant.

La 4e étape exploite la représentation matricielle finale,
dont chaque colonne contient intuitivement les informations de prédictions des tokens suivants,
pour prédire les probabilités des tokens suivants.
Pour ce faire, il y a d'abord une "dé-représentation vectorielle" de chaque colonne,
en multipliant cette colonne par une "matrice de "dé-représentation vectorielle".
Cette matrice, appelée "output" dans le code de Llama 3,
est une matrice de taille 16 384 par 128 000.
Intuitivement, chaque ligne nous dit comment chaque coordonnée de la représentation vectorielle
doit être transformée en une "intensité" pour chaque token.
Les "intensités" pour chaque token sont sont obtenues en ajoutant
les intensités pour chaque coordonnée, 
pondérées par la valeur de la représentation vectorielle sur cette coordonnée.

Bref. La multiplication nous fournit alors une nouvelle matrice, de taille 400 par 32000. 
Pour chaque position et pour chaque token,
l'intensité de la probabilité que, à la position suivante, 
il y ait le token en question.
Cette "intensité" est alors transformée en une probabilité,
en prenant l'exponentielle de l'intensité,
puis en divisant chaque coordonnée par la somme des exponentielles de la colonne.
Cette opération est connue sous le nom d'opération "Softmax",
et on dit parfois qu'elle transforme des logits, qui sont ce que j'ai appelé "intensité",
en probabilités.

Quoi qu'il en soit, il sort de cette 4e étape une matrice 400 par 128 000,
qu'on peut appeler la matrice des probabilités des tokens suivants,
et qui dit pour chaque position et chaque token,
la probabilité que la position suivante contienne le token en question,
étant donné tous les tokens qui précédènt cette position.

Enfin, il y a une dernière phase, appelée la détokenization,
qui va permettre de transformer la matrice de probabilités des tokens suivants,
qui est en fait une suite de probabilités des identifiants des tokens suivants,
en une suite de probabilités de textes qui suivent,
en remplaçant les identifiants des tokens par les caractères auxquels le token correspond.

En particulier, en regardant le dernier élément de la suite,
on obtient des probabilités pour le token qui suit immédiatement le prompt.
En tirant au hasard selon ces probabilités,
on obtient un générateur aléatoire de tokens suivants.
Et en répétant les appels au Transformer, 
on obtient un algorithme qui génère du texte probable,
à la suite de n'importe quel prompt.

Notez finalement que pour en faire un chatbot,
les industriels truquent ensuite les prompts donnés à compléter.
Mais pour plus de détails à ce sujet, je vous renvoie à l'excellente vidéo de Monsieur Phi,
qui insiste notamment sur à quel point ce procédé est loin d'être robuste,
et prêt pour un déploiement massif dans des cas d'usage aussi adversarial qu'Internet,
ou la lecture d'emails contenant potentiellement à la fois 
des secrets industriels et des spams d'inconnus...


## Les blocs de transformer

Chaque bloc de transformer est composé de deux sous-modules :
un module d'attention et un module de feedforward.
Le module d'attention est celui qui va chercher à propager de l'information,
de l'arrière vers l'avant, pour faire en sorte 
que la prédiction du prochain token tienne bien compte de l'ensemble des tokens précédents,
et pas juste du dernier token.
Le module de feedforward, lui, ne propage pas d'informations entre les tokens.
Il s'agit juste d'une correction pour chaque token, à ce moment du calcul.

Détaillons d'abord le feedforward, car il est plus simple.
C'est vraiment juste un réseau de neurones classique,
qui prend un vecteur de dimension 16 384 en entrée,
le transforme en deux vecteurs de dimension 53 248,
avec deux matrices de dimension 16 384 par 53 248 qui vont être optimisées pendant l'apprentissage.
Une opération non-linéaire, appelée Sigmoid Linear Units,
est appliquée à l'un des vecteurs obtenus.
Cette opération resssemble à une version plus lisse de la fonction ReLU,
qui transforme les coordonnées négatives en 0 et laisse les coordonnées positives telles quelles,
Comme beaucoup de choses à propos des transformeurs,
les détails de cette opération ne semblent avoir aucune importance fondamentale
sur la nature et les performances des transformeurs.
Ne nous y attardons pas davantage.

Puis, on effectue une multiplication par coordonnées entre les deux vecteurs de dimension 11 008.
Enfin, on applique une autre transformation linéaire,
pour transformer le résultat en un vecteur de dimension 16 384,
à l'aide d'une troisième matrice de dimension 53 248 par 16 384.
Le feedforward contient donc 3 matrices paramètres à optimiser, 
donc chacune à 53 248 x 16 384 coordonnées.
Et il va en fait calculer, pour chaque colonne de la représentation matricielle du prompt,
une modification à effectuer à cette colonne, qui ne dépend que de la colonne même.
Et donc, la sortie, ça va être l'entrée, plus le résultat des opérations qu'on a décrites.

Passons maintenant au module d'attention.
chaque module d'attention est lui même composé de plusieurs opérations parallèles identiques,
mais avec des paramètres différentes.
Chaque opération parallèle est appelée une tête du module multi-tête d'attention.
Dans Llama 3, on a 128 têtes d'attention.

Rappelez-vous que ce module d'attention est en charge de la diffusion de l'information,
des tokens antérieures aux tokens suivants.
Pour ce faire, chaque tête d'attention va déterminer l'information que chaque token doit diffuser,
en fonction de la représentation de ce token.
Pour chaque token, cette information va être directement 
sous la forme d'un vecteur de dimension 16 384,
à ajouter aux représentations vectorielles des autres tokens.

Pour déterminer l'information à diffuser par un token, 
on utilise une matrice de diffusion informationnelle de la tête d'attention,
dont la dimension est 16 384 par 16 384,
et qui va être un autre paramètre du module d'attention 
à optimiser en fonction des données d'entraînement.
En multipliant la représentation matricielle, de dimension 400 par 16 384,
par cette matrice de diffusion informationnelle,
on obtient une matrice de dimension 400 par 16 384,
qui dit, pour chaque token, l'information vectorielle 
qu'il veut transmettre aux représentations vectorielles des autres tokens.

NB: En fait, Llama 3 factorise la matrice 16 384 par 16 384
par deux matrices de dimension 16 384 par 128, et 128 par 16 384.
Voilà qui permet de réduire le nombre de paramètres du module d'attention.

Reste maintenant à déterminer à quel point cette information à diffuser doit être diffusée.
Pour cela, pour chaque tête d'attention, 
on va introduire 2 autres matrices de dimension 16 384 par 128 qui vont être apprises,
chaque colonne de la représentation matricielle va être transformée
entre 2 vecteurs de dimension 128,
qu'on peut appeler la représentation bivectorielle dans la tête d'attention du token.
Appelons x_i et y_i les vecteurs de dimension 128 qui correspondent au token à la position i.
Ce sont ces vecteurs qui vont être utilisés 
pour déterminer à quel point diffuser l'information des premières positions aux positions suivantes.

Plus précisément, pour chaque paire de positions i < j,
on va calculer le produit scalaire entre x_i et y_j, 
ce qui va nous donner la modification à effectuer à j, à cause de i.
Alors, plus précisément, cette modification est obtenue suite à d'autres opérations encore,
notamment un softmax qui va permettre de borner l'impact de i sur j,
et une manière d'encoder la différence de positions entre i et j,
avec l'intuition que si i et j sont très distants, ils interagiront différemment.
Mais là encore, il vaut mieux, surtout au début, éviter de se perdre dans des détails,
qui ne semblent en fait pas fondamentaux à la nature et à la performance des transformeurs.

Toujours est-il qu'on obtient ainsi une matrice, de dimension 400 par 400,
qui décrit des impacts de i vers j pour i < j,
et qui ne décrit aucun impact dans la direction opposée.
Eh bien, on va multiplier cette matrice par la matrice 400 par 16 384 
des informations à diffuser dans la tête d'attention par chaque token.
Pour chaque position, cette opération va permettre de collecter les informations
que les autres positions veulent lui diffuser,
pondérées par la matrice d'impact, 
qui garantit au passage une diffusion uniquement de la gauche vers la droite.

La matrice qu'on obtient, de dimension 400 par 16 384,
va donner les modifications à ajouter à la représentation matricielle du prompt,
selon une tête du module d'attention.
Eh bien, la représentation matricielle va être mise à jour,
en ajoutant toutes les modifications suggérées par toutes les têtes du module d'attention.
Voilà comment l'information est diffusée entre tokens par le transformeur.

Et donc pour récapituler, le coeur du transformeur,
ça va être une suite d'opérations sur la représentation matricielle du prompt,
obtenue après tokenization et représentation vectorielle des tokens,
qui enchaînent des modules d'attention pour diffuser l'information entre tokens,
et des feedforwards qui corrigent chaque représentation de chaque token,
sans tenir compte des représentations des autres tokens.


## Quelques remarques additionnelles

Alors, si vous avez lu d'autres contenus sur les transformeurs,
vous êtes peut-être surpris que je ne parle pas de "queries", "keys" et "values",
comme c'est le cas par ailleurs dans le code de Llama 3.
La raison principale pour laquelle j'ai évité ces termes,
c'est qu'ils me semblent plus induire en erreur qu'utiles à la compréhension.
Pire encore, ils donnent une vague impression de compréhension,
ce qui peut laisser entendre que ces systèmes sont mieux compris qu'ils ne le sont réellement.

Or donner l'impression que les algorithmes génératifs sont sous contrôle
est un enjeu majeur pour la régulation de ces systèmes.
Ainsi en novembre 2023, de nombreux lobbyistes industriels,
notamment Yann Le Cun de Facebook, qui a développé Llama 3,
Arthur Mensch, PDG de Mistral une entreprise en partenariat avec Microsoft,
et Clem Delangue, PDG de Hugging Face, le plus grand dealer d'algorithmes génératifs,
ont co-signé une lettre envoyée au Président des États-Unis Joe Biden,
dans laquelle ils affirment noir sur blanc que 
« des progrès récents dans le secteur de l'IA ont résolu [le] problème 
[de la nature "boîte noire" des modèles d'IA], 
garantissant ainsi l'intégrité des modèles open-source. »  
https://x.com/martin_casado/status/1720517026538778657

Le tout sans source, et complètement à l'encontre du consensus scientifique,
non seulement sur l'explicabilité des grands modèles de langage,
mais aussi sur la cybersécurité, et donc l'intégrité, 
des énormes systèmes auto-apprenants.

Clairement, des terminologies comme "queries", "keys" et "values"
ajoutent à la confusion déjà énorme sur le degré de contrôle des fournisseurs d'IA
sur les solutions logiciels qu'ils cherchent à vendre avec un minimum de régulation,
bien souvent en mettant leurs clients en danger, plutôt qu'eux mêmes.

Notez par ailleurs que, historiquement et encore dans certains transformeurs,
la propagation de l'information via les modules d'attention peut être bidirectionnelle.
Il est possible que l'information que i veut propager aille aussi vers j < i.
Il n'y a en fait pas grand chose de très fondamental dans les particularités des modules d'attention ;
à part la propriété basique de transmettre des informations entre tokens.

En fait, si les transformeurs sont extrêmement efficaces,
ça me semble surtout grâce à leur structure différentiable, 
qui permet l'apprentissage par descente de gradient stochastique,
à la stabilité des dérivées que permet cette structure différentiable
et à la parallélisation extrême des calculs par les transformeurs.

En particulier, un composant dont on a pas parlé,
mais qui est vraiment indispensable à la stabilité de l'apprentissage,
c'est la normalisation régulière des représentations vectorielles,
en remplaçant un vecteur x par en gros x divisée par la norme de x.
Là encore, en pratique, une solution légèrement différente est utilisée,
mais il me semble s'agir de détails peu fondamentaux ;
le plus important, c'est d'avoir normalisé le vecteur x 
pour éviter que les représentations vectorielles et que les gradients
aient des normes qui explosent ou décroissent exponentiellement vite, 
avec la longueur du transformeur.

Enfin, notez qu'une astuce de plus en plus populaire est d'utiliser des "Mixture of Experts",
comme le propose le modèle de Mistral.
Cette astuce consiste à choisir explicitement de mobiliser ou non certaines sections parallèles du transformeur,
en fonction des représentations matricielles en entrée.
ainsi, moins de calculs doivent être mobilisés par le transformeur,
qui peut néanmoins stocker beaucoup d'informations dans son très grand nombre de paramètres.

Notez d'ailleurs que cette capacité à mobiliser des parties du transformeur 
uniquement lorsque c'est nécessaire
peut être utilisée pour exécuter des gros modèles,
y compris sur des GPU dont la mémoire est insuffisante pour stocker tout le modèle.
Très concrètement, torch propose une fonctionnalité memory-map, ou mmap,
qui permet au GPU d'identifier où sont les modules dans le disque dur,
et de ne les charger qu'au moment où ils sont appelés,
et de les enlever de la mémoire juste après.


## La multi-modalité

Dans sa version de base, 
Llama 3 ne permet que d'effectuer un traitement automatique du langage.
Cependant, il est possible de l'augmenter, 
pour permettre le traitement combiné d'informations de différents formats,
comme du son, des images, des vidéos ou autres.

Dans le cas particulier du son, et en particulier de la voix,
il s'agit simplement d'ajouter un amont un module,
appelé l'encodeur de voix, ou speech encoder,
qui va transformer le son en mots, 
qui seront utilisés tels quels par le modèle de langage.

Le cas des images et des vidéos est plus subtile.
Dans un premier temps, on va entraîner séparément des modules,
capables de transformer une image ou une vidéo en tokens.
Il y a plusieurs façons de faire cela,
notamment une combinaison de réseaux de convolution et de réseaux résiduels.
Mais récemment, l'une des solutions qui semblent dominantes
consistent à réutiliser l'architecture des transformeurs,
en prenant en entrée des représentations de morceaux d'une image.

Bref. Quoi qu'il en soit, ce que l'on veut,
c'est surtout obtenir en sortie du module d'analyse d'image ou de vidéo
une représentation matricielle de l'image ou de la vidéo.
Cette information sera ensuite utilisée,
dans certains blocs Transformeur du modèle de langage.
Typiquement, dans l'article de recherche présentant Llama 3.1,
dans un bloc sur 4, 
juste après le module d'attention qui propage l'information textuelle 
de l'arrière vers l'avant,
on rajoute un module d'attention croisée,
qui va propager de l'information du média visuel vers l'information textuelle.

Bon, l'article n'est pas très précis sur les détails de cette attention croisée,
et, à ma connaissance, le code de cette généralisation multi-modale n'a pas été partagé.
Mais typiquement, ce qui aurait pu être fait,
c'est introduire pour chaque module trois matrices, 
comme on l'a fait pour le module d'attention.
La première est semblable à celle d'un module d'attention :
il transforme chaque colonne i de la représentation matricielle du texte en un vecteur x_i,
typiquement de dimension 128.

La seconde est elle adaptée à l'information visuelle.
Elle va transformer chaque colonne j de la représentation matricielle de l'image,
en un vecteur y_j de même dimension que les x_i.
Et intuitivement, le produit scalaire x_i^T y_j va nous dire à quel point
il faut diffuser la j-ième information de l'image au token à la position i.
Encore une fois, il y a d'autres bidouilles effectuées en plus, 
comme une opération softmax sur le produit scalaire.
Toujours est-il que ces résultats vont nous dire à quel point
les différents aspects de l'image doivent diffuser de l'information 
aux représentations vectorielles des différents tokens.

Pour finir, il reste à déterminer quelle information sera diffusée.
Eh bien, c'est là que la 3e et dernière matrice entre en jeu,
qui est utilisée pour transformer les colonnes de la représentation matricielle de l'image
en des vecteurs de dimension 16 384,
qui correspondent à la modification additive 
que ces colonnes souhaitent effectuer aux représentations des tokens.

Bien entendu, ce que je viens de vous présenter n'est qu'une façon de faire,
parmi la myriade des architectures multi-modales proposées jusque là.
Et bon, c'est vraiment difficile de déterminer laquelle est la plus prometteuse,
surtout si on ne s'appuie que sur des considérations théoriques.
Mais j'ai envie de dire, encore une fois,
que ce qui importe, ce ne sont pas les détails de ces architectures.
Le plus important, c'est qu'il y a un flux de l'information raisonnable dans le réseau,
et surtout, que celui-ci peut être optimisé lors de l'apprentissage,
grâce à une descente de gradient stable.


## Conclusion

Les transformeurs sont donc des structures qui manipulent avant tout 
des représentations matricielles des textes,
et améliorent ces représentations matricielles en diffusant de l'information 
entre positions dans le texte.
Mais surtout, si ces transformeurs semblent efficaces,
ce n'est certainement pas à cause des détails de leur structure ;
leur efficacité semble davantage résider dans la parallélisation des calculs,
et dans les nombreuses astuces pour éviter 
que les représentations matricielles et que les gradients calculés n'explosent,
ou prennent des valeurs dérisoires à cause de la profondeur du réseau.
Bref, ce n'est pas trivial, mais c'est loin d'être extraordinaire ;
et c'est pour ça que je n'ai pas cherché à vulgariser ce concept plus tôt.
Et si je n'avais pas le sentiment que parler des transformeurs serait clickbait,
à cause de toute la hype autour des algorithmes génératifs...
bah, je ne l'aurais pas fait !

Cependant, comme vous le savez si vous me suivez,
si cela permet des prouesses spectaculaires, 
y compris en termes de facultés de raisonnement,
il ne faut pas y voir une manière sécurisée de traiter de l'information.
Les fournisseurs de ces systèmes ne maîtrisent vraiment pas ce que ces systèmes retiennent,
y compris des informations sensibles ou des propriétés intellectuelles,
et encore moins si ce que diront ces algorithmes sera fiable.  
https://fortune.com/2024/01/09/openai-copyright-impossible-new-york-times/

Dès lors, en pratique, les nombreuses entreprises avec qui j'échange sont, à raison,
circonspectes quant à l'intégration de ces systèmes dans des cas d'usage à hauts enjeux.
Du coup, on est extrêmement loin d'une solution économiquement révolutionnaire,
ou d'une course aux algorithmes génératifs 
dont les perdants seraient destinés à être des victimes 
de la guerre économique, de la guerre cyber ou de la guerre physique.
Méfiez-vous sérieusement de la hype, surtout au niveau des entreprises et des régulateurs.

Ceci étant dit, ces systèmes ne sont pas non plus d'aucune utilité.
Pour commencer, de nombreux cas d'usage n'ont aucun besoin de haute fiabilité,
notamment quand il s'agit de divertissement, de marketing ou surtout de cybercrime.
Et clairement, ces domaines, dont l'impact social est douteux, voire extrêmement néfaste,
exploitent depuis un bon bout de temps ces outils,
qu'ils ont transformé en arme de destruction massive ---
notamment dans le cas des deepfakes pornographiques conçus pour le cyber-harcèlement horrible,
en particulier des femmes politiques, journalistes et militantes.

Il y a toutefois un cas d'usage en entreprise tout à fait justifiable et sécurisable,
à savoir en tant que système d'indexation des documents internes,
via des solutions entièrement "on-premise", c'est-à-dire locales à l'entreprise ---
oui parce qu'il faut bien sûr se méfier si une information sensible passe par le cloud.
Dans le monde de la tech, cette indexation est parfois appelée "RAG", 
pour "Retrieval-Augmented Generation".
En bref, il s'agit d'associer à chaque document interne d'une entreprise 
une représentation vectorielle.
Et pour chaque requête en langage naturel,
on peut utiliser un modèle de langage pour identifier les représentations internes
qui correspondent le mieux à la requête,
et donc les documents, voire les morceaux de documents 
qui répondent aux interrogations des employés.

Mais surtout, il ne faut absolument pas réduire le numérique, ni même l'IA,
au seul des algorithmes génératifs.
Au contraire, il est utile de garder en tête qu'il s'agit avant tout de technologies d'information,
qui sont de grande utilité pour toutes les tâches informationnelles de votre organisation.
Et clairement, de nos jours, toutes les entreprises sont surchargées de telles tâches.
Le numérique peut aider à effectuer ces tâches de manière plus efficace, mais aussi plus robuste ;
mais pour cela, il faut absolument qu'on donne beaucoup plus d'attention à la sécurité
des solutions numériques indispensables à notre activité.
Et qu'on soutienne beaucoup plus les régulations 
qui exigent de monter les standards de sécurité du numérique,
comme on l'a fait dans tant d'autres industries, de l'automobile à l'aviation,
en passant par l'agroalimentaire, la pharmaceutique et l'énergie !


