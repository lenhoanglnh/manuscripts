# Le réseau de neurones derrière ChatGPT

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
même si, je préfère vous prévenir, sans carte graphique,
générer du texte avec Llama 3 va être long et laborieux.

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
de 32 couches de "blocs du transformer",
d'un module de dé-représentation chargé d'assigner des probabilités aux différents tokens,
et enfin un "detokenizer".

Détaillons ces 5 composants.
Le tokenizer est un algorithme qui va prendre une suite de caractère,
et va le décomposer en composants appelés tokens.
Un token peut être un mot, un morceau de mot, ou même un simple caractère,
comme une lettre de l'alphabet ou un point.
Llama 3 dispose de 32 000 tokens.
Et donc, passé la première couche, 
le texte donné à Llama 3 va être transformé en une suite de d'identifiants de tokens,
c'est-à-dire une suite de nombre, 
tous étant des entiers entre 0 et 31 999.
Pour Llama 3, ce tokenizer est appris indépendamment du coeur du réseau de neurones
qu'est le transformer.
Ainsi, si le prompt donné à Llama 3 a quelque chose comme 200 mots,
le tokenizer va le transformer en une suite de quelque chose comme 400 tokens.

Puis, la seconde étape va consiste à transformer chaque token
en une représentation vectorielle du token.
Pour cela, on va utiliser un tableau de conversion,
qu'on appelle dans le jargon une matrice des représentations vectorielles des tokens.
Cette matrice est appelée tok_embeddings dans le code de Llama 3.
Elle est de dimension 32 000 par 4096.
Le nombre 32 000 correspond bien sûr au nombre de tokens,
alors que 4096 correspond à la dimension de l'espace de représentation des tokens.
Cette matrice va nous permettre de transformer la suite de tokens
en une suite de représentations vectorielles.
Comme vous l'imaginez peut-être, l'identifiant du token, s'il est égal à k,
est remplacé par la k-ième colonne de la matrice des représentations vectorielles des tokens.
En faisant cela token par token,
on a une transformation de la suite de 400 tokens en une suite de 400 vecteurs de dimension 4096.
Une suite de tels vecteurs forme naturellement une matrice,
qui va ainsi être de dimension 400 par 4096.
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
est une matrice de taille 4096 par 32000.
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

Quoi qu'il en soit, il sort de cette 4e étape une matrice 400 par 32000,
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


## Les modules d'attention

Ça flirte avec de la pseudo-science !

Avant tout une structure différentiable, avec des dérivées stables.


En particulier, on va voir que,
si les transformeurs ont indéniablement "fait leurs preuves",
en permettant toutes sortes de prouesses spectaculaires,
ils échouent à s'appuyer sur des fondements scientifiques rigoureux ;
et il y a au contraire tout un jargon douteux autour de ces objets,
mais clairement amplifié par le marketing puissant des industries de la tech.


## Installer Llama 3

Notez qu'il reste possible de lancer Llama 3 avec une carte graphique de PC de gamer,
avec des performances raisonnables, en utilisant le memory mapping.
Je l'ai fait notamment dans le cadre de mon entreprise Calicarpa
où on s'intéresse à la sécurité, ou plutôt au manque de sécurité, de tels systèmes,
pour aider les entreprises à mieux cerner les usages intéressants des modèles de langage,
et ceux qu'il faut absolument éviter pour ne pas finir comme Air Canada notamment.


## Les Visual Transformers


## Conclusion


