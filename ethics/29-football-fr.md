# Une IA pour arbitrer le football ?

Peut-on envisager un arbitrage du football entièrement automatisé ?

Depuis plusieurs années, l'arbitrage du football s'est beaucoup modernisé,
en exploitant les nouvelles technologies de l'information,
notamment pour la goal-line technologie, 
qui permet de savoir si le ballon a franchi la ligne de but,  
https://tournesol.app/entities/yt:m17ERc-kQhQ  
et pour la règle du hors-jeu, 
dont les lignes sont maintenant tracées à l'aide de nombreuses caméras et d'algorithmes.  
https://tournesol.app/entities/yt:C164kYMGV1A

OK, mais ça, ça paraît être les applications "faciles" 
des technologies de l'information à l'arbitrage au football.
Après tout, dans ces deux cas, tout se joue exclusivement sur un problème d'information :
le ballon-a-t-il entièrement franchi la ligne ou non ?
Et l'attaquant était-il devant le dernier défenseur au moment de la passe de son coéquipier ?

Mais intuitivement, on pourrait se dire que l'arbitrage du football recèle une dose de subjectivité,
dès lors qu'il s'agit de juger si une main est licite,
ou si une faute doit être sifflée.
Dès lors, l'information semble insuffisante.
Il semble nécessaire d'y ajouter une dose de jugement humain,
ce qui pourrait suggérer que l'IA n'est pas applicable à ces cas,
et donc à l'arbitrage général du football.

Mais est-ce vraiment le cas ? La subjectivité est-elle suffisante pour rejeter l'usage des IA ?

## Qu'est-ce qu'une faute ?

Pour qu'un algorithme applique les lois du football,
on pourrait être tenté de lui faire tout simplement lire ces lois de football,
et de les faire respecter à la lettre.
Coment ces lois définissent-elles les fautes, qui donnent lieu à un coup franc direct ?

Eh bien, on peut les lire,
puisqu'elles sont rendues publiquement accessibles 
par le Conseil international du football association,
ou IFAB en anglais.

Je cite la loi 12.1 : 
"Un coup franc direct est accordé si, de l’avis de l’arbitre, 
un joueur commet l’une des fautes suivantes de manière imprudente, inconsidérée ou violente :
- charge un adversaire ;
- saute sur un adversaire ;
- donne ou essaie de donner un coup de pied à l’adversaire ;
- bouscule un adversaire ;
- frappe ou essaie de frapper un adversaire (y compris un coup de boule) ;
- tacle un adversaire ou lui dispute le ballon ;
- fait ou essaie de faire trébucher un adversaire."  
https://www.theifab.com/fr/laws/latest/fouls-and-misconduct/#introduction

Clairement, ces lois vont être difficiles à encoder dans un algorithme.
En premier lieu, "l'avis de l'arbitre" est explicitement mis en valeur.
Autrement dit, selon l'IFAB, la décision revient avant tout à une interprétation par l'arbitre.
Et d'ailleurs,cela peut paraître fort insatisfaisant.
Si l'avis de l'arbitre va à l'encontre de celui de tous les observateurs,
et sachant qu'il peut être corrompu par la pression du public ou des avances financières,
comme cela a été le cas par le passé,  
https://en.wikipedia.org/wiki/Match_fixing_in_association_football  
est-ce vraiment l'avis d'un arbitre humain imparfait et corruptible qui doit faire foi ?

Mais surtout, la loi utilise des critères qui sont beaucoup plus difficiles à modéliser et à trancher,
que ceux qui sont utilisés pour déterminer si le ballon a franchi la ligne de buts,
ou si un joueur est en position de hors-jeu.
En effet, on trouve dans la loi des mots comme "imprudente", "inconsidérée", "violente".
Sachant que le football reste un sport de contact où les charges et bouscules sont en fait souvent licites,
comment tracer la frontière entre les interventions de la sorte qui sont "considérées"
et celles qui seraient "inconsidérées".
Comment un algorithme est censé considérer le mot "considéré" ? #MesTasDeMetas

## L'apprentissage par jurisprudence

En fait, la manière dont les arbitres, les professionnels et les amateurs de football
ont appris à distinguer les actions de jeux qui sont des fautes,
de celles qui ne sont pas des fautes,
repose bien plus sur la jurisprudence que sur les lois existantes.
Autrement dit, à force de regarder des matchs de football,
et en particulier des arbitres arbitrer des matchs de football,
on a fini par apprendre à reconnaître les actions où la plupart des arbitres siffleraient,
et à les distinguer des actions où les arbitres ne sifflent pas.
Et c'est certainement bien plus cette apprentissage par expérience,
qui nous a permis de définir dans nos têtes
ce qui constitue une action sanctionnable par un coup franc direct.

Comme finalement beaucoup de choses dans notre quotidien,
nous avons appris ce qui constitue une faute de jeu à partir d'un grand nombre d'exemples,
beaucoup plus qu'à l'aide d'une définition rigoureuse 
que l'on appliquerait à la lettre pour déterminer si une action est une faute de jeu.
Un peu comme les sens des mots courants sont bien plus définis par leur usage,
que par une définition imposée dans un dictionnaire.  
https://tournesol.app/entities/yt:8eY8d0u0gF4

D'ailleurs, pour justifier qu'une action de jeu aurait dû ou n'aurait pas sû être sifflée,
plutôt que de lire la loi,
les commentateurs sportifs vont surtout s'appuyer sur des actions de jeux similaires qui,
dans le passé, ont été jugé différemment.
Autrement dit, leur argument exploite davantage la jurisprudence que la loi.

Mais donc si on veut que quiconque, humain ou machine, sache arbitrer,
dans le sens où si on veut qu'ils arbitrent 
comme la plupart des observateurs s'y attendent,
il va falloir que l'entité arbitre regarde beaucoup de football,
et apprennent ce qui, dans les actions de football, rend les actions sifflables ou non.

Eh bien ça, c'est exactement ce que les algorithmes modernes font.
Les algorithmes dits d'apprentissage, ou de machine learning en anglais,
consistent précisément à généraliser des données observées.
Et comme il y a des kilomètres de bandes vidéos de football,
avec des sifflets d'arbitre,
il semble y avoir largement de quoi concevoir des algorithmes 
qui sauront ce qui fait qu'une action est sifflable, ou non.
C'est pour cela que je m'attends à ce que, dans les années à venir,
l'arbitrage pourra être entièrement automatisable.

Qui plus est, contrairement à l'arbitre humain,
l'arbitre algorithmique pourra exploiter 
tous les angles de vues de toutes les caméras pour prendre sa décision ;
et contrairement à la VAR, sa décision pourra être rendue en une fraction de seconde,
plutôt qu'après plusieurs minutes.

Mais donc, l'arbitrage algorithmique est-il pour demain ?
Peut-on envisager qu'une IA prenne les commandes des matchs de football ?

## Biais et voile d'ignorance

Même si l'IA paraît prendre des décisions raisonnables dans une démonstration
faite par l'entreprise qui la développe,
il faudra absolument que celle-ci soit auditée, testée et décortiquée
par plusieurs entités indépendantes
pour que toutes les parties prenantes du football acceptent de la déployer.

Après tout, qui nous dit que l'IA n'a pas en fait un biais systématique en faveur de certaines équipes ?
Quand on sait à quel point le football italien était sous l'emprise de la corruption,
notamment comme cela a été révélé dans l'affaire Calciopoli, 
n'y a-t-il pas un risque que, en généralisant le passé,
on généralise aussi un arbitrage favorable à deséquipes comme la Juventus et le Milan AC ?  
https://fr.wikipedia.org/wiki/Affaire_Calciopoli  
Et quid des suspicions modernes, par exemple concernant le FC Barcelone ?  
https://www.reuters.com/sports/soccer/barcelona-under-investigation-suspected-bribery-refereeing-case-court-2023-09-28/

Pour contrer les risques de biais systématiques, 
il peut être utile d'exploiter le voile d'ignorance du philosophe John Rawls.
Autrement dit, pour juger si une action de jeu est une faute ou non,
il faudrait idéalement que ce jugement soit le même,
quelles que soient les équipes qui sont opposées.
Ou dit autrement, la décision de siffler faute ne doit pas dépendre
de la couleur des maillots du potentiel fautif et de la potentielle victime.

Ce voile d'ignorance pourrait être explicitement encodé
dans l'entraînement de l'IA arbitre.
Après avoir appris des cas passé,
cette IA pourrait suivre une phase d'entraînement additionnel,
où on lui apprend à fournir les même jugements,
lorsqu'on lui fournit les mêmes images, mais avec des couleurs de maillots modifiés,
voire avec des visages et des morphologies de joueurs modifiés ---
oui car l'IA pourrait avoir appris des choses plus subtiles 
comme "on ne siffle pas les fautes de Messi".

Bref. Le problème des biais doit absolument être traité avec soin.
Mais il ne me semble pas insurmontable.
Le vrai problème des IA arbitres de football est ailleurs.

## Gouvernance et cybersécurité

Sachant à quel point la FIFA est proche de dictatures comme le Qatar et l'Arabie Saoudite,
et sachant à quel point ces pays investissent dans le cybercrime,
il faudrait certainement avoir un oeil constant sur les IA arbitres,
et vérifier qu'elles se comportent de manière satisfaisante ;
et non hackée ou backdoorée par des entités malveillantes.  
https://www.amnesty.org/en/latest/news/2022/11/infantinos-call-to-focus-on-the-football-a-crass-abdication-of-fifas-accountability-for-migrant-worker-abuses/

En fait, l'enjeu fondamental pour que les IA d'arbitrage du football soient éthiques et sécurisées
me semble résider avant tout dans leurs gouvernances.
Qui pourra auditer ces IA ? Le groupe des auditeurs sera-t-il lui-même résilient à la corruption ?
À quelles données à propos des IA auront-ils accès ?
Et surtout, s'ils détectent des comportements indésirables, 
comme un biais systématique en faveur d'une équipe,
de quels recours disposeront-ils pour modifier le comportement des IA ?
Si l'on voit tous que l'IA a commis une erreur grossière,
comment pourra-t-on corriger l'IA, et vérifier que cette correction a bien été faite ?

J'ai envie de dire que, 
tant que des réponses satisfaisantes n'auront pas été fournies à ces questions,
le déploiement d'IA arbitres de football me semble hautement indésirable,
même si la possibilité de concevoir des IA arbitres de football de niveau surhumain est avérée.

Et cet enjeu n'est bien entendu pas restreint aux arbitres de football.
En fait, l'arbitrage du football reste un enjeu bien moindre que 
l'arbitrage entre la recommandation de différents contenus informationnels
à des milliards d'utilisateurs,
dont les IA de TikTok, YouTube et Twitter ont le monopole,
malgré l'absence de tout audit externe, 
ni même la possibilité pour les régulateurs d'analyser correctement ces IA,
fautes d'accès aux codes sources et aux données d'entraînement ou de comportement de ces IA ;
et surtout, malgré les très nombreuses données parcellaires mais déjà extrêmement compromettantes,
auxquels des chercheurs et des journalistes indépendants ont pu avoir accès,
comme les Facebook Files qui montrent qu'un changement de l'IA de Facebook de 2018
a conduit à la radicalisation des médias en quête de vues pour leur survie économique,
avec pour conséquence un déclin des démocraties et une montée de l'autoritarisme à travers le monde.

Bref. Toute précaution qui vous semble indispensable pour la validation d'une IA arbitre de football
devrait vous paraître beaucoup plus critique encore pour les IA arbitres de l'information ;
et la situation actuelle où ces arbitres de l'information sont hors de contrôle
devrait vous paraître absolument inacceptable.

De manière plus générale, nos concitoyens et nos sociétés font beaucoup trop confiance
aux services de géants du numérique qui ne méritent certainement pas un tel niveau de confiance.
Je ne peux que vous encourager à questionner vos fournisseurs de services informatiques,
et à envisager des alternatives plus éthiques, sécurisées et souveraines.

Et justement, le sponsor de cette vidéo, Infomaniak, est un fournisseur de service clouds
qui s'appuie sur une souveraineté et une éthique très supérieures 
à celles des concurrents américains qui, à cause du Patriot Act,
se doivent de partager vos données avec les autorités américaines si celles-ci l'exigent.
Autrement dit, ces concurrents américains sont officiellement facilement corruptibles.
A contrario, Infomaniak fait un effort majeur pour tout développer de manière souveraine, 
avec des collaborateurs uniquement en Suisse, un pays beaucoup plus digne de confiance. 
Vous pouvez profitez gratuitement des services Mail et SwissTransfer d'Infomaniak, 
et je vous recommande aussi vivement leurs services Web, kMeet ou encore kDrive. 
Pour chaque vidéo où je les promeus, ce que je fais avec grand plaisir, 
Infomaniak reverse un don à l'Association Tournesol. 
Merci beaucoup à eux pour ce partenariat.

## Présomption de non-conformité

Plus généralement, il me semble que dans le cas du déploiement d'une IA pour arbitrer le football,
tous les entraîneurs, les joueurs, les commentateurs et les supporters de football
seraient unanimes dans l'exigence d'une présomption de non-conformité de cette IA.

Qui nous dit que les propriétaires émiratis de Manchester City,
les propriétaires saoudiens de Newcastle
ou les propriétaires qataris du Paris Saint-Germain n'ont pas inclus des backdoors dans l'IA,
pour que celle-ci siffle plus systématiquement des pénaltys
lors des actions litigieuses et confuses qui favorisent ces équipes ?

Cela m'étonnerait ainsi très fortement 
qu'une IA arbitre de football soit autorisée à la commercialisation,
et à l'utilisation pour les matchs de football,
si, en amont, il n'y aura pas eu suffisamment de procédures d'évaluation
de l'éthique et de la sécurité d'une telle IA.

Mais alors, pourquoi en serait-il autrement des autres IA,
beaucoup plus sophistiquées et géopolitiquement influentes,
qui ont déjà envahi les réseaux sociaux,
qu'il s'agisse de ChatGPT ou de l'IA de recommandation de TIkTok ?
Comment en est-on venu à faire confiance à ces outils numériques qui,
dans le cas du football, soulèveraient probablement des levers de bouclier très légitimes ?
Et que faudrait-il faire pour concevoir des outils numériques vraiment dignes de confiance,
et qui notamment ne seraient pas facilement corruptibles par des entités malveillantes ?

Eh bien, cette dernière question est précisément le grand défi 
que s'est fixé l'Association Tournesol, notre organisation à but non lucratif.
Depuis maintenant plus de trois ans, 
nous avons réuni des expertises en mathématiques, en informatique, en philosophie et en sociologie,
entre autres, pour concevoir une plateforme open-source de gouvernance démocratique et sécurisée 
des IA de recommandation.
Et si l'on s'est donc intéressé surtout aux arbitres de l'information,
nulle doute que nombre des outils qu'on a développés sont aussi applicables à l'arbitrage du football.
Ceci étant dit, il nous reste en fait beaucoup de chemins à effectuer 
pour que la gouvernance algorithmique de Tournesol soit vraiment satisfaisante.
Et pour cela, nous avons besoin de nombreuses formes d'aides,
de vos évaluations de la recommandabilité de différents contenus,
à des dons financiers pour nous permettre de garder notre excellent employé,
en passant par des contributions à la codebase, aux mathématiques des algorithmes de Tournesol,
ou encore à la simple promotion de la plateforme.
Pour toute l'aide que vous pourrez nous fournir,
nous tenons à exprimer d'ores-et-déjà notre extrême gratitude.

Ce n'est qu'à la suite d'une mobilisation générale et de progrès majeurs
dans la sécurité, l'éthique et la gouvernance des IA,
que je pourrais un jour en venir à recommander un arbitrage entièrement par les IA ;
que ce soit du football ou de l'information.

