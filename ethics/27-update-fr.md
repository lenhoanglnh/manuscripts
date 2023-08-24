# Les algorithmes de Tournesol

Cet été, on a beaucoup bossé sur Tournesol, 
et on a mis en ligne de nouveaux algorithmes 
avec de meilleures propriétés mathématiques,
et qui s'appuient sur des principes philosophiques plus justifiés.
Et on a documenté tout ça dans un article de recherche,
disponible gratuitement et librement sur la plateforme ArXiV.

Si vous êtes curieux de savoir comment mêler mathématiques de très haut niveau,
machine learning, philosophie morale et science politique, 
le tout incarné dans un projet extrêmement concret et déployé,
bah, je vous invite à vous plonger dans la lecture de cet article.

Mais comme je sais qu'il y en aura très certainement au moins parmi vous
qui préfère une présentation audiovisuelle des avancées qu'on a effectuées,
je vous propose de vous expliquer les grandes lignes des algorithmes de Tournesol
dans la vidéo d'aujourd'hui.
Et je vais essayer de faire une présentation digeste, 
ce qui signifie que je vais malheureusement devoir simplifier à outrance des aspects techniques,
et même être parfois volontairement imprécis, voire légèrement erroné, dans les explications.

Allez, c'est parti !


## Tournesol

Avant de parler des algorithmes, faisons un rapide point sur le projet Tournesol,
pour ceux parmi vous qui n'en auraient pas encore entendu parler.
Tournesol, c'est une plateforme libre et open source, 
développée par l'Association à but non lucratif du même nom,
portée par une équipe de bénévoles absolument fantastiques,
notamment Aidan, Louis, Adrien et d'autres.
J'ai l'honneur d'être co-fondateur et président de cette association ; 
mais pour être clair, je n'en suis pas et prévois de ne jamais en devenir salarié.
En fait, l'Association n'a pour l'instant qu'un seul salarié,
qui est un développeur absolument fantastique,
mais dont le salaire est loin d'être garanti sur la durée.

Aujourd'hui, on a la chance d'avoir le support d'Infomaniak,
qui fournit gratuitement des services informatiques à l'Association Tournesol,
et qui sponsorise cette vidéo en effectuant des dons à l'Association.
Encore une fois, je ne suis qu'un bénévole dans cette histoire !
Infomaniak est LE service Cloud par excellence en Suisse,
et se démarque de la concurrence pour son éthique et sa souveraineté,
par opposition à d'autres services américains ou chinois.
Je vous conseille en particulier la kSuite d'Infomaniak,
avec notamment kMail, kDrive ou kMeet, parmi tant d'autres solutions sur le web.


Le but de la plateforme, c'est de proposer une solution technique
au problème fondamental de la gouvernance des intelligences artificielles 
qui me semblent être de loin les plus influentes d'aujourd'hui,
à savoir non pas ChatGPT et MidJourney, 
qui n'ont finalement qu'une influence limitée sur la géopolitique mondiale,
mais davantage les IA de recommandation de TikTok, Instagram, Snapchat, Twitter ou YouTube,
qui déterminent quelles informations auront l'attention du plus grand nombre,
et quelles informations seront noyées dans un océan de surabondance informationnelle.

En particulier, pour de nombreuses causes, 
comme l'éducation, la santé publique, le changement climatique, la cybersécurité
la lutte contre la corruption ou les droits humains,
l'attention de la population générale, ou celle de de population experte ou dirigeante,
est critique pour protéger des millions, voire des milliards de vies humaines.
On l'a vu avec le COVID, la canicule, la compromission de Microsoft Cloud,
le Qatar et le Marocgate ou encore les génocides des Rohingyas, des Ouïghours ou du Tigré.
L'inattention à de telles menaces civilisationnelles est extrêmement dangereuse.

Vu le rôle prédominant qu'ont acquis les IA de recommandation 
dans l'exposition informationnelle répétée des milliards d'internautes humains,
il me semble qu'il est désormais vain d'espérer combattre cette inattention
sans s'attaquer à la conception, à l'éthique et à la sécurité de ces IA.
Malheureusement, comme le révèlent notamment les Facebook Files,
au sujet desquels je vous invite vivement de vous informer si vous doutez du rôle des IA,
la gouvernance hégémonique de ces IA par des entreprises privées est en train d'empêcher
tout contre-pouvoir démocratique sur le comportement usuel de ces IA surpuissantes­.

Ceci étant dit, même si la société civile pouvait modifier ces IA,
il lui serait aujourd'hui extrêmement difficile d'en proposer une gouvernance collaborative et sécurisé.
Le projet Tournesol cherche justement à modifier cet état de fait,
en permettant une gouvernance collaborative, sécurisée et en temps réel des IA de recommandation.
En particulier, Tournesol permet à n'importe lequel parmi vous de contribuer,
pour faire en sorte que l'IA de recommandation de Tournesol promeuve les vidéos
que vous jugez préférables à recommander massivement au grand public,
typiquement parce qu'il s'agit de vidéos d'intérêt public.

Enfin, ça, c'est dans les grandes lignes.
Car quand on rentre dans les détails de comment une telle IA devrait se modifier
suite à l'ajout de jugements d'un utilisateur sur Internet,
on tombe très vite sur des questions fondamentales de la science de l'information,
comme la sécurité, l'équité, la transparence, l'interprétabilité
ou encore l'accessibilité de la gouvernance des systèmes d'information.

Eh bien, après maintenant 3 ans de travail sur les algorithmes de Tournesol,
on a fait énormément de progrès sur ces questions, et c'est le sujet de cette vidéo -
même si on est encore extrêmement loin d'avoir une solution pleinement satisfaisante !


# Les droits de vote

Sur Tournesol, n'importe quelle contribution de n'importe quel contributeur influencera les scores, 
et donc les recommandations faites par Tournesol.
Ceci revient à dire que le système est sans permission, ou permissionless en anglais.
Cependant, pour se protéger des faux comptes contrôlés par des vagues de trolls,
il nous faut bien sûr limiter l'influence des comptes pas suffisamment certifiés.
C'est ainsi pour des raisons de sécurité que, sur Tournesol,
certains comptes n'auront parfois qu'un petit droit de vote.
On parle de résilience aux attaques Sybil, 
du nom d'un livre sur les troubles dissociatifs de l'identité.  
https://fr.wikipedia.org/wiki/Attaque_Sybil

Pour obtenir cette résilience Sybil, 
Tournesol s'appuie sur deux données de certification : 
la résilience Sybil du nom de domaine de l'adresse email de l'utilisateur 
et les parrainages entre utilisateurs.

Ainsi, Tournesol a dressé une liste de noms de domaine de confiance comme @epfl.ch ou @inria.fr.
La particularité de ces noms de domaine, c'est que, d'après l'Association Tournesol, 
il semble difficile pour des entités malveillantes 
de contrôler un grand nombre de messageries électroniques avec ces noms de domaines.
Et ça, c'est bien sûr par opposition à @gmail.com ou @proton.me,
puisqu'il suffit de quelques clics pour créer une messagerie de la sorte.

Voilà qui permet d'assigner une pré-confiance à certains comptes Tournesol.
Le parrainage permet ensuite de tracer un graphe orienté.
Tournesol propose ensuite de diffuser la confiance à travers ce réseau,
à l'aide d'un nouvel algorithme appelé LipschiTrust,
qui est une variante plus sécurisée de l'algorithme PageRank qui a fait la fortune de Google.  
https://tournesol.app/entities/yt:6jK9bFWE--g

Cette confiance est ensuite convertie en droits de vote sur chaque vidéo de la manière suivante :
Tournesol calcule d'abord la confiance totale des contributeurs à la vidéo.
Puis, on va s'autoriser à assigner légèrement plus de droits de votes.
Cet excédent est réparti entre les comptes qui manquent de confiance.

Voilà qui garantit que l'impact cumulé des comptes douteux sera toujours limité, 
tout en permettant d'intégrer les jugements de ces comptes autant que n'importe qui d'autres
dans les cas où ces comptes qui manquent de confiance sont en fait peu nombreux.


# Transformer des comparaisons en scores

Pour estimer la recommandabilité des différentes vidéos YouTube,
Tournesol s'appuie sur un jugement comparatif des contributeurs,
parce que ceux-ci nous semblent plus fiables que des jugements par vidéo.
Par ailleurs, de tels jugements répondent davantage à la question fondamentale de Tournesol,
qui fait dans un ensemble de 4 recommandations à chaque utilisateur de l'extension Tournesol,
disponible sur Firefox, Chrome et Edge,
à chaque fois que celui-ci ouvre la page YouTube.com.
En effet, la question fondamentale n'est alors pas de savoir si une vidéo est bien ;
c'est davantage de savoir quelles vidéos devraient plus souvent apparaître dans le rectangle jaune.

Ceci étant pour répondre à cette question, 
Tournesol s'appuie sur le calcul de scores pour chaque vidéo, à partir des comparaisons.
Il nous faut donc une façon de transformer des comparaisons en scores.

Et alors, il y a peut-être des utilisateurs de Twitter parmi vous qui se souviennent de mon tweet,
où j'annonçais de manière cryptique une découverte magnifique que mon collègue Julien Fageot et moi
avions alors faites.
Et bien, cette découverte concerne justement cette transformation de comparaisons en scores,
via en fait un formalisme assez général et très élégant qu'on a nommé "Generalized Bradley-Terry",
et qu'on a décrit dans un autre article de recherche, également disponible sur ArXiV,
et qui a reçu de plus les contributions des excellents Sadegh Farhadkhani et Oscar Villemaud.  
https://twitter.com/le_science4all/status/1666199278841212928  
https://arxiv.org/abs/2308.08644

Parmi les nombreuses propriétés remarquables de cette famille de transformation de comparaisons en scores,
il y a la monotonicité que Julien a démontrée,
qui garantit que, si vous accentuez votre préférence de A contre B,
ça va nécessairement améliorer le score de A -
ça paraît tout bête, mais il se trouve que les modèles que nous avions avant l'été n'avaient pas cette propriété,
et que ceci avait conduit plusieurs contributeurs de Tournesol, y compris moi-même,
à juger les vidéos de manières malhonnêtes sur la plateforme...
En gros, avant, une comparaison trop extrême avait en fait moins d'impacts,
si bien que pour descendre une mauvaise vidéo de manière efficace,
on évitait de lui mettre des comparaisons extrêmes. 
Cette ère de malhonnêteté est heureusement révolue !

Ainsi, à l'aide de ces nouveaux algorithmes, 
les comparaisons d'un contributeur sont transformées en scores du contributeur,
que vous pouvez d'ailleurs afficher, si le contributeur les a rendus publics,
en allant directement à l'adresse tournesol.app/users/[username]/recommendations.
Voici par exemple mes top recommandations.

Il y aurait bien sûr beaucoup plus à dire sur la merveilleuse structure mathématique
que Julien et moi avons découverte,
mais je vais laisser tout ça pour une prochaine vidéo.


# Agréger les scores des différents contributeurs

Pour que la gouvernance de Tournesol soit vraiment collaborative,
il faut bien évidemment agréger les avis des différents contributeurs.
Mais s'il y a bien une chose qu'on a appris en développant Tournesol,
et que j'avais déjà un peu exploré dans la série sur la démocratie,
c'est que les mathématiques de l'agrégation d'avis conflictuels sont extrêmement complexes,
surtout si l'on veut faire cela de manière éthique et sécurisée, dans un contexte "sparse".

Ainsi, d'un point de vue éthique, une telle agrégation se doit d'éviter les pièges
des jugements parisiens et marseillais.
C'est littéralement le nom que je donne au problème fondamental
de la comparabilité de jugements de différents contributeurs dans mes conférences académiques.

Imaginez ainsi un excellent contenu qui attire disproportionné des contributeurs parisiens.
Et faisons l'hypothèse complètement imaginaire que 
ces contributeurs parisiens sont victimes d'une maladie qui les poussent à constamment râler,
même lorsque tout va pour le mieux dans le meilleur des mondes.
Si on utilise des agrégations naïves des jugements des contributeurs,
cet excellent contenu pourrait recevoir presque exclusivement des avis négatifs,
non pas parce que le contenu est mauvais,
mais parce qu'il attire des contributeurs qui disposent d'un biais systématique de négativité.

Faisons une autre hypothèse complètement imaginaire.
Imaginez que les contributeurs marseillais sont victimes d'une autre maladie,
qui les poussent à constamment exagérer leurs jugements.
Pour eux, il n'y a pas d'entre deux. 
Un contenu est ou bien excellentissime, ou bien honteusement merdique.
Un contenu correct jugé quasiment exclusivement par de tels contributeurs sera jugé excellentissime,
davantage à cause de la manière dont ceux qui l'ont jugé s'expriment 
qu'à cause de sa qualité intrinsèque.

Youssef Allouah, Oscar Villemaud, Rachid Guerraoui et moi-même avons formalisé ces difficultés,
et ajouté une exigence de sécurité, qu'on appelle depuis la résilience Lipschitz.
Celle-ci exige que chaque contributeur pourra influencer le score d'une vidéo 
d'au plus une quantité proportionnelle à son droit de vote - 
sur Tournesol, ça correspond en gros à 10 points pour un droit de vote unitaire.
Et on a conçu une solution à ce scrutin, 
qu'on a appelée Mehestan, du nom d'un proto-parlement en Iran antique, 
autour de 247 après Jésus-Christ.  
https://arxiv.org/abs/2202.08656

Là encore il y aurait beaucoup plus à dire sur cet algorithme, 
que je présenterai plus en détail dans une prochaine vidéo.
Il s'agit en tout cas, à quelques adaptations près, 
de la manière dont Tournesol a choisi d'agréger les avis de différents contributeurs.


# La présomption de non-recommandabilité

L'un des aspects les plus insatisfaisants des algorithmes pré-estivaux,
c'est qu'ils assignaient un score négatif à de nombreuses excellentes vidéos,
notamment par exemple celles de Science Étonnante,
simplement car celles-ci ne traitent pas d'un sujet 
que les contributeurs de Tournesol jugent très important.
Autrement dit, beaucoup de vidéos recommandables, 
même si elles ne sont peut-être pas les plus recommandables,
donnaient l'impression d'être jugées très négativement.

En fait, ce que nous avons fini par comprendre, 
c'est que le problème résidait davantage dans le fait 
que la vidéo moyenne sur Tournesol avait un score de zéro, 
qui se trouve aussi être le score par défaut, en l'absence de tout jugement.

Notre solution pour corriger le tir est simplement de modifier le score par défaut,
pour qu'il ne corresponde pas à une vidéo moyenne de Tournesol,
mais pour qu'il corresponde davantage à une mauvaise vidéo de Tournesol.
Autrement dit, le score par défaut, égal à zéro, va correspondre 
à une vidéo parmi les 15% les moins bonnes de la plateforme.
En quelques sortes, c'est comme si on instaurait une présomption de positivité
pour 85% des vidéos sur Tournesol.

De façon intéressante, ceci nous a aussi permit de programmer naturellement une présomption de non-recommandabilité,
en fixant un seuil de recommandabilité à 20.
Autrement dit, Tournesol va s'autoriser à recommander une vidéo uniquement si son score dépasse 20.

Ce qui est intéressant, c'est que par construction, pour devenir recommandable,
un contenu va devoir recevoir le jugement de suffisamment de contributeurs.
En effet, chaque contributeur a un droit de vote au plus égal à 1 sur Tournesol.
Or la garantie de résilience Lipschitz fait qu'un droit de vote unitaire ne peut déplacer le score d'une vidéo que de 9.95.
Mais donc 2 droits de votes ne peuvent avoir un effet que de 19.9,
ce qui sera insuffisant pour faire que la vidéo soit jugée recommandable par Tournesol.

NB1: en fait l'effet max en partant de 0 sera de 19.6, 
à cause du "squashing" des scores qui les force à être entre -100 et 100  
NB2: L'effet max est en fait plus complexe à cause d'impacts indirects, notamment sur les scaling des autres contributeurs.

D'ailleurs, il me semble y avoir quelque chose d'en fait très profond 
derrière cette notion de présomption de non-recommandabilité,
surtout à l'ère de la surabondance de l'information,
qui sera de surcroît alimentée par l'explosion des algorithmes génératifs
et l'enrichissement spectaculaire du cybercrime.
Plutôt que de chercher à signaler et retirer le mauvais,
il semble être devenu plus judicieux de permettre la diffusion massive
uniquement pour des contenus qui auront été jugés adéquats à diffuser massivement,
surtout sur des sujets importants comme la santé publique, le changement climatique,
ou le respect des droits humains.

En tout cas, ce sont les scores ainsi calculés qui sont affichés sur le site web de Tournesol,
et via l'extension pour les navigateurs Firefox, Chrome et Edge,
et qui sont utilisés pour déterminer quels contenus devraient être plus souvent recommandés.


# Conclusion

J'espère que la vidéo d'aujourd'hui vous aide à mieux comprendre 
comment Tournesol envisage la sécurité d'une gouvernance collaborative
des IA les plus puissantes du monde moderne.
En particulier, plus que des algorithmes dédiés à la plateforme Tournesol,
les nombreuses difficultés et solutions dont j'ai parlé me semble omniprésentes,
dès lors que l'on cherche à permettre à des internautes de prendre des décisions collectives.
De nombreux projets participatifs en ligne gagneraient ainsi sans doute à s'inspirer de nos travaux,
que ce soit au niveau de la certification des comptes,
de l'inférence des préférences des contributeurs,
de l'aggrégation des avis contraires
ou de la présentation des résultats de l'agrégation.

Ceci étant dit, il serait très erroné de voir en Tournesol une solution complète à la gouvernance algorithmique.
En fait, jusque là, j'ai surtout l'impression qu'on a fait à peine plus que le minimum
pour avoir une solution fonctionnelle et relativement sécurisée.
Mais pour disposer d'une solution vraiment fiable et efficace de gouvernance algorithmique,
de nombreux autres enjeux devront être résolus,
ce qui va nécessiter toujours plus de recherches en amont,
aussi bien sur le plan mathématique,
que sur les plans philosophiques, sociologiques, politiques, juridiques et psychologiques,
comme on en parle notamment dans notre article.  
https://arxiv.org/pdf/2211.01179.pdf

Comme on le disait en 2019, rendre les intelligences artificielles robustement bénéfiques
est un chantier absolument monumental,
qui requiert une pluridisciplinarité 
dont la recherche académique a jusque là été très peu prompte à initier,
et très inefficace à accomplir.
En fait, l'un des grands objectifs à court et moyen terme de Tournesol,
c'est justement d'y parvenir.
Si vous êtes mathématiciens, informaticiens, philosophes, sociologues ou psychologues,
je vous invite à vous intéresser de plus près à notre projet,
et à rejoindre la communauté grandissante de mathématiciens, informaticiens, philosophes, sociologues et psychologues,
parmi d'autres,
à concevoir les fondations d'une gouvernance algorithmique effective, efficace et sécurisée,
et à résoudre les nombreux problèmes aussi bien théoriques que pratiques
qu'une telle gouvernance soulève.

Mais pour y arriver, il nous faut absolument avoir les moyens de continuer à développer Tournesol.
Et pour cela, nous avons besoin de beaucoup d'aides, notamment financières.
En particulier, malgré les dons d'Infomaniak, 
l'Association Tournesol manque de réserves
pour assurer le salaire de notre employé dans les mois à venir.
Pour soutenir et encourager la recherche sur la gouvernance collaborative et sécurisée des algorithmes,
nous vous serions extrêmement reconnaissants de contribuer à nos finances,
via des dons directs à l'Association ou via notre compte KissKissBankBank.
Merci beaucoup d'avance.

