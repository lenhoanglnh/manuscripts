# L'incroyable prédiction de fin du monde de Laplace

Dans l'histoire des mathématiques, 
il y a eu peu de débats aussi rocambolesques et mouvementés
que celui sur la stabilité du système solaire.
Pendant plus de trois siècles, 
des générations de génies, de Newton à Villani,
en passant par Euler, Lagrange, Laplace, Poincaré, Kolmogorov et Laskar, entre autres, 
ont enchaîné les approximations, les erreurs,
les théorèmes positifs presque conclusifs, 
les théorèmes négatifs presque conclusifs, 
et même les appels à Dieu,
souvent en réussissant à convaincre leurs contemporains,
mais en échouant presque systématiquement face à l'épreuve du temps.

Peu de conclusions mathématiques sont restées aussi longtemps instables
que celles qui cherchaient à trancher la question de la stabilité du système solaire.
Et ce n'est pas Mathador, auteur d'une excellente vidéo à ce sujet, qui me contredira !

Franck : Ah non, je ne vais pas te contredire.
C'est vraiment l'un des sujets mathématiques les plus passionnants que j'ai traités.

On reparle de ton excellent récit de l'histoire de cette question en fin de vidéo !
Moi ce qui va m'intéresser dans cette histoire, 
c'est un élément que je t'ai demandé de laisser de côté, 
pour que j'y consacre une vidéo à part entière,
à savoir une prédiction faite par, non pas Newton, pas Euler, pas Lagrange, pas Poincaré,
Revient en arrière... Oui ! Lui. Laplace.

Laplaaaaace !!

Comme on va le voir, Laplace avait fait en 1814 une prédiction tellement folle,
qui lui-même la reniait, pour de très bonnes raisons.
Cependant, si on adapte sa prédiction à une découverte du début de la première moitié du 20e siècle,
et si on déroule les arguments de Laplace,
on en vient à effectuer à peu près la même conclusion
que celle des mathématiques les plus célébrées du 21e siècle, 
à savoir les prédictions de Laskar.
Et le plus fou, c'est que ces arguments de Laplace ne font absolument pas intervenir la physique !

Mais pour comprendre les arguments du Laplace de 1814, 
il nous faut revenir quelques décennies en arrière­.

# Le principe de Laplace (a.k.a. la formule de Bayes)

En 1774, un jeune Laplace de 25 ans écrit l'une de ses premières contributions scientifiques,
intitulée "Mémoire sur la probabilité des causes par les événements".
Cet écrit de 38 pages est une véritable révolution, non seulement mathématique,
mais surtout épistémologique à mes yeux.
Car derrière ces apparences mathématiques, 
ce titre soulève clairement une question fondamentale de la philosophie.
Que doit-on penser des causes d'un événement, lorsque cet événement est observé ?
Si un patient a un symptôme d'une maladie, peut-on conclure qu'il a la maladie ?
Si un homme meurt après être vacciné, est-ce à cause de sa vaccination ?

Pour répondre à ces questions, Laplace propose dans ce mémoire un Principe fondateur.
Je cite : "Si un événement peut être produit par un nombre n de causes différentes,
les probabilités de l'existence de ces causes prises de l'événement sont entre elles
comme les probabilités de l'événement prises de ces causes,
et la probabilité de l'existence de chacune d'elles est égale à la probabilité de l'événement prise de cette cause,
divisée par la somme de toutes les probabilités de l'événement prises de chacune de ces causes."

Bon, je vais le reconnaître, l'écriture de Laplace est loin d'être la plus limpide qui soit.
Et j'ai personnellement dû relire ce principe plusieurs fois pour le comprendre ;
mon bagage mathématique et les exemples qui suivent dans le Mémoire
m'ont d'ailleurs été d'une aide vitale.
Du coup, je vais me permettre de reformuler Laplace (déso Pierre-Simon).

Ce que dit Laplace, c'est que plus une cause prédit l'événement observé,
plus elle devient relativement plus crédible, 
par rapport à une cause qui prédit mal l'événement observé.
En fait, la formulation formelle de ce que dit Laplace,
c'est ni plus ni moins la fameuse formule de Bayes,
dont je crois vous avoir déjà un peu parlé...

NB : En fait, pris littéralement, 
le principe énoncé par Laplace en 1774 
est restreint à des a prioris uniformes.
Excusons cette erreur de jeunesse.
L'Essai Philosophique de 1814,
et plus encore sa version révisée en 1840,
seront beaucoup plus complètes,
et définiront une véritable formule de Bayes.

Ainsi, si la mort de l'homme vacciné s'explique par d'autres causes bien plus probables,
il reste peu probable que sa vaccination en soit une cause probable.  
https://tournesol.app/entities/yt:79G5FwAhBDA

Armé de son nouveau principe épistémologique,
Laplace s'attaque à une généralisation du fameux problème d'induction de Hume.  
https://tournesol.app/entities/yt:ptJm_otaR5k  
Imaginons que le soleil se lève tous les jours.
Peut-on alors prédire qu'il se lèvera encore demain ?

Laplace va modéliser ce problème par un autre problème plus abstrait.
Imaginez une urne opaque, contenant un très grand nombre de billets noirs et blancs.
Vous tirez un à un un certain nombre de billets.
Imaginez avoir retiré p billets blancs et q billets noirs.
Quelle est la probabilité que le prochain billet tiré de l'urne soit blanc ?

Clairement, le cas particulier où q = 0 décrit le problème de Hume,
où un billet blanc est un jour où le soleil s'est levé,
et où p est alors le nombre de fois que le soleil s'est levé.
Quelle est dans ce cas la probabilité que le soleil se lèvera demain ?

# La loi de succession de Laplace

Pour répondre à cette question, 
Laplace propose d'appeler x la fraction inconnue de billets blancs dans l'urne.
Puis, il considère un a priori uniforme sur x : 
tout ce qu'il sait, c'est que x est entre 0 et 1,
et il considère a priori qu'une valeur x autour de 0.5 
est aussi probable qu'une valeur autour de 0.99.

Notez que x peut alors être considéré comme la cause de chaque événement observé,
à savoir des couleurs des billets tirés.
Le problème est alors bien un problème d'induction :
il s'agit de déterminer la probabilité des causes, à savoir des valeurs de x,
par les événements, à savoir les nombres p et q de billets blancs et noirs tirés.

Pour cela, comme l'explique le principe de Laplace,
il nous faut d'abord estimer les probabilités des événements par les causes.
Autrement dit, sachant x, quelle est la probabilité de tirer p billets blancs et q billets noirs ?
Il s'agissait là d'une question classique, déjà répondue par Pascal puis Bernouilli.
Je ne vais pas rentrer dans les détails,
mais la réponse est de la forme f(p,q) x^p (1-x)^q,
où f(p,q) est ce qu'on appelle un coefficient binomial, 
qu'on note parfois \binom{p+q}{p} et qu'on lit "p parmi p+q".
Mais ces détails importent peu.

Désormais, pour déterminer la probabilité d'une cause x par les événement p,q,
il nous faut comparer ce terme à la somme des termes similaires pour les autres causes possibles x'.
Comme il y a une infinité de valeurs possibles de x',
plutôt qu'une somme classique, il va nous falloir utiliser une somme continue,
qu'on appelle "intégrale" dans le jargon mathématique.

Ainsi la probabilité d'une cause x sachant p et q
est donné par f(p,q) x^p (1-x)^q / \int f(p,q) y^p (1-y)^q dy,
où j'ai juste remplacé symboliquement la lettre x' par la lettre y.
Notez que les coefficients binomiaux s'annulent, 
si bien que la probabilité de x est simplement x^p (1-x)^q / \int y^p (1-y)^q dy.
En fait, le dénominateur est une constante indépendante de x,
et ne dépend uniquement que de p et q,
si bien que cette probabilité s'écrit plus simplement x^p (1-x)^q / une fonction B(p, q).
De nos jours, cette probabilité est connue sous le nom de "loi Bêta".

NB : La loi Bêta est super chouette, notamment car elle est la conjuguée de la Bernouilli.
Autrement dit, si vous observez des données selon une loi de Bernouilli,
dont le paramètre est une variable aléatoire qui suit une loi Bêta,
alors le postérieur bayésien sera encore une loi Bêta.

Si la cause est x, alors la probabilité de tirer un billet blanc sera égale à x,
puisque x est la fraction de billets blancs dans l'urne.
Mais chaque cause x n'a qu'une probabilité x^p (1-x)^q / B(p, q).
Pour connaître la probabilité de tirer un billet blanc,
Laplace propose de cumuler les probabilités selon les différentes causes possibles,
ce qui nous donne une probabilité \int x * P[x|p,q] dx = \int x^{p+1} (1-x)^q dx / B(p, q).

Et alors, je vous passe les détails de calculs, que Laplace a fait soigneusement.
Mais la conclusion de tout ça, c'est que la probabilité de tirer un autre billet blanc
selon les principes laplaciens est (p+1)/(p+q+2).
Cette formule est ce qu'on appelle désormais la "loi de succession de Laplace".
Et comme l'explique très bien 3Blue1Brown, 
elle s'est retrouvée au coeur de nombreuses applications, notamment sur le web.  
https://tournesol.app/entities/yt:8idr1WZ1A7Q

# La prédiction stellaire de Laplace

Laplace nous fournit ainsi une solution au problème de Hume.
Quelle est la probabilité que le soleil ce lève encore demain ?
Il suffit de compter le nombre de jours p où il s'est levé jusque là,
puis de faire le calcul (p+1)/(p+q+2), avec q = 0, donc (p+1)/(p+2).
Dès lors, la probabilité qu'il ne se lève pas,
et donc qu'un cataclysme stellaire empêche ce qui peut nous paraître inévitable,
sera donné par 1/(p+2).
En particulier, si la probabilité que le soleil ne se lève pas est en effet 1/(p+2),
et si chaque prochain lever de soleil est statistiquement indépendant des précédents,
alors il faut s'attendre à ce que le soleil s'arrête de se lever, dans environ p+2 jours.

Si vous pensez que ces calculs de Laplace sont farfelus, vous n'êtes pas les seuls !
Laplace même les avait effectués, 
en prenant l'hypothèse religieuse selon laquelle l'histoire aurait commencé il y a 5000 ans,
soit 1 826 213 jours,
ce qui l'amène à conclure que "il y a 1 826 214 à parier contre un qu'il se lèvera encore demain".
Ou dit autrement, le soleil pourrait s'arrêter de se lever dans 5000 ans.
Mais il se précipite ensuite d'ajouter :
"Mais ce nombre est incomparablement plus fort pour celui qui 
connaissant par l’ensemble des phénomènes le principe régulateur des jours et des saisons, 
voit que rien dans le moment actuel ne peut en arrêter le cours."  
https://fr.wikisource.org/wiki/Essai_philosophique_sur_les_probabilit%C3%A9s/1b

Autrement dit, selon Laplace, sachant les connaissances de la physique de son époque,
les prédictions de sa modélisation du problème de Hume ne doivent pas être 
prises pour argent comptant.
D'une certaine manière, en disant cela, Laplace ne fait qu'appliquer sa théorie des probabilités !
En effet, on a plus de données que la simple observation du soleil ;
l'observation des trajectoires des planètes du système solaire nous a notamment conduit 
aux lois de la gravité universelle de Newton.
Ignorer ces autres données pour effectuer une prédiction serait irrationnelle.

D'autant que Laplace n'est pas le savant le plus clairement croyant de l'histoire,
et il y a de bonnes chances qu'il ne croyait même pas à l'hypothèse religieuse
selon laquelle l'histoire n'a que 5000 ans.

Mais donc, y a-t-il lieu de complètement rejeter l'argument bayésien de Laplace ?

Eh bien, peut-être pas. 
En premier lieu, on peut l'ajuster à l'état des connaissances modernes.
On sait maintenant que le système solaire est en fait vieux de 5 milliards d'années ;
de sorte que le soleil s'est levé 5 milliards de fois 365 jours de suite.
Et donc, on serait amenés à prédire que le soleil pourrait arrêter de se lever
dans environ 5 milliards d'années, 
voire même qu'il est peu probable que le soleil se lève encore dans 50 milliards d'années.

Et ça... bah ça ressemble beaucoup à la conclusion de la vidéo de Mathador !

[Extrait de vidéo de Mathador sur Laskar]

D'autant que l'instabilité du système solaire n'est que l'une des causes possibles
de cette prédiction insensée du modèle laplacien !
D'autres arguments fondés sur l'énergie noire prédisent 
une expansion fatale de l'espace-temps, appelée Big Rip, 
dans 22 milliards d'années.
Voilà deux arguments qui montrent que les ordres de grandeur de 
l'incroyable prédiction de la fin du monde de Laplace sont tous sauf complètement déraisonnables.  
https://arxiv.org/abs/astro-ph/0302506

En tout cas, ils semblent être bien plus qu'une simple coïncidence littéralement cosmique.

# Conclusion

Alors, que retenir de cette coïncidence cosmique ?
Y a-t-il vraiment des choses à retenir pour nous autres humains, et nos vies quotidiennes ?
Et bien, oui, certainement, 
car le modèle laplacien est beaucoup plus général que son application cosmique.

En particulier, le principe qui consiste à supposer qu'un événement vieux de X années
va probablement perdurer pendant encore X années
semble relativement fiable, et extrêmement applicable à de nombreux cas d'applications.
Il est même utilisé explicitement dans le show-business 
où il est connu sous le nom de "effet de Lindy",
et possède de nombreuses justifications, listées notamment dans mon livre #LaFormuleDuSavoir.

Même si, comme tout bayésien, il ne faut pas s'arrêter à ce principe,
et bien considérer toutes les données à notre disposition pour bien raisonner.
Un bayésien doit prendre en compte l'ensemble de ses connaissances pour affiner ses prédictions.

Et dans le cas de la stabilité du système solaire, 
je fais en particulier avant tout confiance aux prédictions de Laskar ;
même si elles se trouvent être conformes à celles de Laplace !

