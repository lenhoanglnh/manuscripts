# Une astuce bayésienne pour identifier l'expertise

Une heure de streaming Netflix en 4k pollue plus 
que manger un repas de viande rouge, vrai ou faux ?
Imaginez que, pour répondre à cette question, 
vous fassiez appel au vote du grand public,
qui répond vrai à 70%, et faux à 30%.
Faut-il suivre l'avis de la majorité ?

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
que les affirmations bien plus populaires que ceux qu'on croit
ont tendance à être souvent juste ---
en tout cas dans un monde où les humains réfléchissent correctement,
ou plutôt, conformément aux lois des probabilités.


## Le vas simplifié où la popularité insoupçonnée révèle une vérité

Pour bien comprendre 
pourquoi une affirmation bien plus populaire qu'on le croit
a de bonnes chances d'être vraie,
je vous propose de commencer par le cas mathématique le plus simple.

Imaginons donc une théorie T et sa négation non-T,
qui correspond à dire que T est faux.
Supposons maintenant que les humains sont tous des bayésiens,
qui partent du même a priori.
Ce cas, comme on l'a déjà vu dans des vidéos passées,
s'analyse très bien avec un curseur de Turing sur une droite graduée.

Quand le curseur tend à gauche, sa veut dire qu'on juge T plus crédible.
Et quand le curseur tend à droite, on juge T moins crédible.
Au milieu, au zéro de la droite, T est aussi crédible que non-T,
ce qui revient à dire que la probabilité de T est de 50%.
Si le curseur de Turing est un bit à gauche,
T devient 2 fois plus crédible que non-T,
ce qui revient à dire qu'il y a une cote de 2 contre 1 pour T contre non-T,
ou encore que la probabilité de T est 2 / (2+1) = 2 tiers.
Si le curseur est 3 bits à droite,
alors non-T est 2^3 bits fois plus crédible que T,
ce qui revient à dire qu'il y a une cote 8 contre 1 pour non-T contre T,
ou dit autrement 1 contre 8 pour T contre non-T.
Et ça, ça correspond à une probabilité de T égale à 1/(1+8) = 1 neuvième.

Comme on l'a vu, le curseur doit être placé initialement quelque part,
ce qui correspond à la croyance commune à propos de T,
en l'absence de toute expertise.
On parle alors de crédence a priori, c'est-à-dire avant tout apprentissage.

Mais maintenant, certains vont recevoir certaines informations,
d'autres vont recevoir d'autres information,
parfois qui n'ont rien à voir avec T.
Imaginons qu'il existe deux types de signaux,
qu'on va appeler pro-T et anti-T.

Ceux qui vont recevoir le signal pro-T vont naturellement mettre à jour leurs crédences,
et vont déplacer leur curseur de Turing en direction de T.
Les autres, qui reçoivent donc le signal anti-T, vont se déplacer vers non-T.

Imaginons maintenant un multivers avec deux branches distinctes, 
l'une où T est vrai, et l'autre où T est faux.
Remarquez que les gens qui reçoivent le signal pro-T 
croient davantage qu'on est dans la branche T-vrai,
que ce ne n'est le cas pour les gens qui ont reçu le signal anti-T.
Mais du coup, ils imaginent que les pro-T imaginent davantage
que les autres ont eux aussi reçu pro-T.
Ils imaginent pro-T davantage populaire, que les anti-T ne l'imaginent.

Par ailleurs, dans la branche T-vrai,
on s'attend à une certaine fraction de gens qui reçoivent pro-T,
et à une autre fraction qui reçoivent anti-T.
Idem pour la branche T-faux.

Cependant, un théorème bayésien assez simple à démontrer,
c'est que dans la branche T-vrai,
il y aura en espérance plus de gens qui reçoivent pro-T,
que dans la branche T-faux.
Plus précisément, la probabilité de recevoir pro-T sachant T-vrai
est plus grande que celle de recevoir pro-T sachant T-faux.

Mais donc, dans T-vrai comparé à T-faux,
comme les pro-T sont plus nombreux,
la réponse pro-T sera aussi davantage populaire.


## Le théorème général



## Les limites du théorème



## Conclusion


