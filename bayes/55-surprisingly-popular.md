# Une astuce bayésienne pour identifier l'expertise

Une heure de streaming Netflix en 4k via la 4G pollue plus 
que manger un repas de viande rouge, vrai ou faux ?
Imaginez que, pour répondre à cette question, 
vous fassiez appel au vote du grand public,
qui répond vrai à 70%, et faux à 30%.
Faut-il suivre l'avis de la majorité ?  
https://agirpourlatransition.ademe.fr/particuliers/bureau/calculez-lempreinte-carbone-usages-numeriques

Clairement, la réponse dépend avant tout de l'expertise de la majorité.
Mais comment distinguer au sein des votants ceux qui ont un avis informé
de ceux qui croient savoir, mais se trompent ?
Y a-t-il une solution simple pour identifier l'expertise,
et ainsi guider nos choix sur la base des connaissances scientifiques ?

Alors, bien sûr, on pourrait vouloir exploiter les diplômes des uns et des autres,
ou leurs degrés d'engagement avec les questions politiques,
pour répondre à ces questions.
Mais aujourd'hui, je vais vous parler d'une solution absolument remarquable,
découverte en 2017 par les chercheurs Drazen Prelec, Sebastian Seung et John McCoy,
dont l'article a été publié dans la prestigieuse revue scientifique Nature.  
https://www.nature.com/articles/nature21054?error=cookies_not_supported&code=2e90e214-6ef4-4338-ae71-d4ee5cee7826

Cette solution consiste à demander aux sondés,
non seulement leur pari sur la bonne réponse,
mais aussi leur pari sur les résultats du sondage.
Imaginons ainsi que certains parient que 60% répondront "vrai",
mais que l'écrasante majorité parie que 90% répondront "vrai",
de sorte que si je prends la moyenne des paris, 
j'obtiens un pari moyen de 85% de vrai, et donc 15% de faux.

Et bien, on voit que la réponse "faux" est en fait beaucoup plus fréquente
que ce que les gens ont parié.
C'est une réponse dont la popularité surprend :
on s'attendait à ce qu'elle soit moins populaire.
Eh bien, Prelec, Seung et McCoy affirment que ceci suffit à conclure
que la bonne réponse est "faux" --- quand bien même c'était la réponse minoritaire !
Autrement dit, selon eux, les 30% à avoir répondu "faux" sont davantage des experts.

Honnêtement, lorsque j'ai découvert cette solution,
j'ai vraiment été extrêmement sceptique.
Dans leur article, les chercheurs prennent l'exemple de l'affirmation 
"Philadelphie est la capitale de la Pennsylvanie",
avec des chiffres semblables à ceux que j'ai cité.
Et mon réflexe, ça a été de me dire : 
"OK, ça marche pour ce cas, car dans ce cas est piège,
et seuls les experts connaissent non seulement la bonne réponse, 
et le fait que c'est un piège."
Et l'explication dans l'article de Nature ne m'a pas vraiment convaincu.

Il m'a vraiment fallu me plonger dans les mathématiques, 
fournies en supplément à l'article,
pour que je me dise qu'il y avait en fait quelque chose de profond.
En particulier, un argument bayésien montre bel et bien 
que les affirmations avec une popularité insoupçonnée
ont tendance à être souvent juste.

Dans leur article, Prelec, Seung et McCoy suggèrent même
que s'appuyer sur la popularité insouçonnée permet d'identifier l'expertise,
ce qui permettrait de puiser mieux encore dans la *sagesse des foules*,
voire de concevoir une forme de vote épistocratique.

Aujourd'hui, on va explorer le degré d'applicabilité de cette approche,
à la fois d'un point de vue empirique et théorique,
en nous appuyant sur un questionnaire que j'ai fait circuler auprès de mes abonnés !


## Le théorème de la popularité insoupçonnée d'une vérité

Imaginons donc une théorie T,
qui peut être une affirmation comme 
"1h de Netflix pollue plus que 1 repas de viande rouge",
et considérons la possibilité qu'elle soit vraie ou fausse.
Chaque possibilité donne lieu à une branche d'un multivers.
Il y a donc une branche T-vraie, et une branche T-fausse.

L'observation qui va être clé,
consiste simplement à dire que dans T-vraie,
on s'attend à ce qu'il y aura plus de gens qui recevront des informations,
qui les pousseront à croire T plus vraie.
Dit autrement, la proportion de gens qui votent pour T, 
qu'on va appeler pro-T,
est en espérance plus grande dans T-vraie que dans T-fausse.

Maintenant, si les votants sont des bayésiens,
alors ils ne peuvent complètement exclure aucune des deux branches du multivers.
Certains considèreront T-vraie beaucoup plus probable,
d'autres auront des informations différentes qui les pousseront à être plus sceptique.
Mais tous assigneront au moins une toute petite crédence à chacune des deux branches.

Mais alors, pour évaluer la proportion des gens qui répondront T-vraie,
d'après la loi des probabilités totales,
chaque votant va imaginer cette proportion dans le monde T-vraie,
ainsi que celle dans le monde T-fausse,
et le votant va alors prendre une moyenne entre les proportions obtenues,
pondérées par sa crédence a posteriori en les différentes branches.

Maintenant, si, dans chaque branche du multivers, 
les informations collectées par les votants sont supposées indépendantes, 
alors cette proportion imaginée par le votant ne doit pas dépendre du votant.
Elle découle uniquement de l'hypothèse T-vraie.
Et donc le nombre de pro-T imaginée par un votant lorsqu'il suppose T vraie
est égal au nombre de pro-T dans la branche T-vraie.
De même, le nombre de pro-T imaginée par un votant lorsqu'il suppose T fausse
est égal au nombre de pro-T dans la branche T-fausse.

Mais donc, chaque votant va prédire un nombre de pro-T 
qui est entre celui dans la branche T-vraie, et celui dans la branche T-fausse.
Et ça, ça implique que cette prédiction sera inférieure au nombre de pro-T dans T-vraie.
On vient de conclure la preuve !

Si T est vraie, 
alors les prédictions de tous les votants du nombre de pro-T
vont être inférieures au nombre de pro-T qu'il y aura effectivement eu dans T vraie.
Le fait de transcender les prédictions prouve la vérité d'une affirmation.
Et au passage, ceci valorise les pro-T,
qu'on peut juger mieux informés que les anti-T.

De façon symétrique, si T est fausse,
alors le nombre de pro-T sera plus grand que selon les prédictions des votants.


## Le cas des QCM

Quand il y a plus de 2 choix possibles,
et donc pas juste T ou non-T,
les auteurs ont proposé et justifié une généralisation.
Illustrons-le dans le cas avec 3 choix possibles, qu'on va appeler A, B et C.

On va alors s'intéresser aux chassés-croisés.
À quel point les gens qui votent A croient qu'il y aura beaucoup de B,
par opposition aux prédictions des électeurs de B sur le nombre de votes pour A ?
Les pro-A prédisent-ils davantage la popularité de B,
que les pro-B ne prédisent la popularité de A ?
Intuitivement, le fait que ce ratio est grand revient à dire que
les prédictions de popularité de A sont sous-estimées,
et donc, si on suit notre logique, ça nous pousse à davantage valoriser les pro-A.

Eh bien, le scrutin proposé par Prelec, Seung et McCoy,
qu'ils appellent le vote du candidat "surprenamment populaire"
consiste à calculer, pour chaque candidat X,
tous les ratios de ce genre, où X est comparé à des alternatives Y,
en comparant les prédictions pro-Y chez les pro-X aux prédications pro-X chez les pro-Y.
Le nombre de voix reçues par X est ensuite multiplié par cette somme de ratios.
Le résultat est appelé le nombre de voix normalisé par les prédictions pour X.
Le candidat élu est alors celui qui a le plus grand nombre de voix normalisé par les prédictions.

Dans notre exemple à 3 choix, 
pour la réponse A, 
il faut donc calculer le chassé-croisé avec B,
et donc le ratio entre la popularité prédite de B par les pro-A,
et la popularité prédite de A par les pro-B.
Et ajouter ça avec le chassé-croisé avec C.
Enfin, tout ça est multiplié par la popularité effective de la réponse A.

On fait ensuite de même pour la réponse B,
ce qui correspond à ajouter le ratio popularité prédite de A par les pro-B 
par la popularité prédite de B par les pro-A,
avec le ratio popularité prédite de C par les pro-B 
par la popularité prédite de B par les pro-C.
Et de multiplier la popularité effective de B par le résultat.

Et puis idem pour C.
Dans notre exemple, le vote le plus populaire, corrigé par les prédictions, est la réponse A.

De façon remarquable, là encore,
les auteurs fournissent une justification bayésienne à ce scrutin,
en prouvant que ce scrutin garantit l'élection de la bonne réponse,
si on suppose les électeurs bayésiens avec des ,
et sous certaines hypothèses additionnelles comme le fait 
que les pro-X sont tous pro-X pour la même raison : 
à savoir une information à laquelle seuls eux ont eu accès.

Bon, du coup, le degré d'applicabilité de cette généralisation est plus discutable.
Néanmoins, ce théorème suggère qu'il s'agit néanmoins d'une manière intéressante
de mieux estimer les bonnes réponses, dans le cas des questions à choix multiple.


## Les limites du théorème

Comme tout théorème, 
la garantie de validité du vote du surprenamment populaire
repose sur des hypothèses,
et son degré de validité en pratique va être fortement dépendant
du degré de validité des hypothèses.

En premier lieu, il faut bien sûr supposer que nos sondés sont honnêtes.
S'ils nous racontent n'importe quoi,
ou s'ils cherchent à nous tromper,
alors on risque de conclure ce qu'ils veulent qu'on conclut.
Dès lors, si on veut valoriser l'expertise 
via le principe de popularité soupçonnée 
dans des applications avec de véritables enjeux,
ou sur Internet où les trolls pullulent,
comme par exemple sur Tournesol,
il va falloir envisager des solutions pour sécuriser le scrutin.

Ensuite, comme dans toute affaire de sondage,
il y a une affaire de fluctuations statistiques.
En particulier, en supposant T vrai,
selon les hypothèses du modèle,
chaque sondé a une estimation bayésienne de la proportion de pro-T.
Mais comme on effectue un sondage, 
la proportion parmi les sondés peut différer de la proportion envisagée par le sondé.
Il va donc falloir en particulier que l'erreur d'échantillonnage soit faible,
comparé à la marge d'erreur tolérable du scrutin,
qui va être directement liée à la différence 
entre la proportion de pro-T dans T vrai,
et celle dans T-faux,
selon les différents sondés.

On peut souligner une hypothèse d'indépendance des signaux.
Cependant, celle-ci n'est pas si fondamentale.
Techniquement, si les sondés étaient bayésiens,
on pourrait la contourner en leur demandant :
imaginez que votre postérieur sur T soit en fait un a priori,
et que vous ne sachiez rien d'autre que cet a priori.
Quelle proportion de pro-T prédiriez-vous ?

Non, vous le voyez venir, un énorme problème avec le théorème,
c'est qu'il nécessite de supposer les sondés bayésiens.
Autrement dit, on suppose que les sondés appliquent systématiquement
les lois des probabilités pour déterminer si T est vrai,
mais aussi pour estimer les proportions probables de pro-T parmi les sondés.
Or clairement, nous autres humains sommes extrêmement loin d'avoir 
la faculté de raisonner de manière conforme aux lois des probabilités.

Mais ce n'est pas tout.
Après tout, même en supposant les sondés bayésiens,
ce serait trop beau s'il suffisait d'effectuer un sondage par popularité insoupçonnée
pour obtenir des réponses quasi-conclusives,
y compris à propos de prédictions futures.


## Est-ce que ça marche en pratique ?




## Conclusion

TBD.

