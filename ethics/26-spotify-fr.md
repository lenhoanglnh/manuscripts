# Spotify a payé leur silence

En 2014, un groupe de musique appelé Vulpeck, a gagné 20 000$ avec un album inattendu,
intitulé Sleepify.
Et pour bien vous rendre compte du style musical très particulier de Sleepify,
je vais vous le jouer maintenant, malgré les risques d'infraction au droit d'auteur.

[Awkward silence]

Oui vous avez bien entendu.
Cette album à 20 000$ n'est autre que du silence.  
https://www.theguardian.com/music/2014/jul/25/vulpeck-the-band-who-made-20000-from-their-silent-spotify-album

Alors, techniquement, je crois que je vous ai passé la chanson "Zzzz",
et je ne suis pas sûr qu'elle soit la plus représentative de l'album.
Je crois que "Zzzzzzzzz" est peut-être plus représentative,
même si ce n'est pas tout à fait ma préférée de l'album...  
https://en.wikipedia.org/wiki/Sleepify

Mais comment est-ce possible que ce silence soit aussi lucratif ?
Eh bien, comme vous l'avez deviné, 
ce n'est pas parce que les abonnés de Spotify
ont payé pour écouter du silence plutôt que de la musique.
Ce qu'il s'est passé, 
c'est que le groupe Vulpeck a demandé à ses fans d'écouter ce silence en permanence,
y compris pendant la nuit,
pour augmenter leur nombre d'écoutes,
et récupérer ainsi de plus grandes recettes via le système de paiement de Spotify.
Vulpeck a exploité la faille des fausses écoutes.  
https://www.youtube.com/watch?v=KXvncV79LXk

En fait, aujourd'hui, on va voir que ces fausses écoutent sont désormais un enjeu
qui représente littéralement des milliards de dollars  
https://www.lemonde.fr/economie/article/2021/06/09/spotify-deezer-apple-amazon-le-streaming-musical-toujours-en-croissance_6083448_3234.html  
alors que la fraude massive par fausse écoute est devenue une économie importante
qui biaise toute l'offre musicale,
au profit des escrocs, désormais professionnalisés et puissants, qui exploitent.  
https://www.vice.com/en/article/gv5xbx/i-built-a-botnet-that-could-destroy-spotify-with-fake-listens

Mais surtout, pour contrer la fraude, 
il existe une parade, que Deezer cherche notamment à adopter depuis 2016 -
mais sa mise en application traîne -
et qui est un principe fondamental de la recherche en sécurité des intelligences artificielles,
que des collègues et moi avons formalisé dans un article publié en 2022.
Aujourd'hui, on va parler de la théorie mathématique des IA équitables et sécurisées,
que mes nombreux co-auteurs et moi avons développée depuis 7 ans,
qu'on a peaufiné et optimisé notamment sur la plateforme Tournesol.  
https://www.deezer-blog.com/how-much-does-deezer-pay-artists/


## Market-Centric versus User-Centric

Alors, la manière dont les recettes de Spotify sont distribuées est très opaque,
et il y a des arrangements spécifiques avec certains ayant-droits puissants,
notamment les grandes maisons de disque comme Warner Music, Sony Music ou Universal Music,
par opposition notamment aux indépendants.  
https://www.theverge.com/2015/5/19/8621581/sony-music-spotify-contract

Mais une composante clairement majeure de la redistribution des recettes Spotify
est un système parfois appelé le Market-Centric Payment System.
En gros, dans ce système, les abonnements des consommateurs sont tous collectés 
et regroupés dans un pot commun.
Puis, chaque ayant-droit est rémunéré à hauteur de son nombre d'écoutes total,
relativement aux nombres d'écoutes des autres ayant-droits.

Techniquement, une écoute set la lecture d'une piste audio d'au moins 30 secondes,
ce qui explique pourquoi les chansons de l'album Sleepfy de VUlpeck font toutes 31 secondes,
et pourquoi les musiques sur ces plateformes ont tendance à se raccourcir.

Et le problème, c'est que, comme on l'a vu, 
ce système permet aux utilisateurs de manipuler aisément les recettes des artistes, 
pour favoriser les artistes qu'ils préfèrent.
Est-ce que vous voyez pourquoi ?

En abusant de fausses écoutes pour les artistes que vous préférez, 
par exemple en ouvrant un onglet Spotify, en mutant l'onglet 
et en jouant la musique de ces artistes,
vous pouvez augmenter artificiellement le temps d'écoute de ces artistes,
en laissant typiquement tourner en boucle pendant toute la nuit.
Autrement dit, c'est comme si vous aviez plus de droit de vote sur la redistribution des recettes,
en écoutant davantage Spotify.

Alors, depuis le cas Vulpeck, les services de streaming ont des algorithmes anti-fraudes,
qui détectent et annulent les tentatives grossières de manipuler le système de paiement.
Mais bien sûr, les fraudeurs se sont adaptés, 
et ils ont maintenant largement automatisé l'écoute des contenus, 
tout en la rendant suffisamment réaliste pour ne pas se faire détecter.  
https://musiczone.substack.com/p/le-big-hold-up-des-faux-streams

Je vous invite vivement à lire cette enquête glaçante de Philippe Astor,
qui décrit toute une industrie de la fausse écoute,
que le journaliste qualifie de "mafia",
dont certains très grands artistes semblent être des clients.  
https://musiczone.substack.com/p/le-big-hold-up-des-faux-streams

D'ailleurs, ce hack fut même organisé et facilité par l'application Eternify,
développée par un autre groupe de musique en protestation 
avec le manque de protection des petits artistes.  
https://www.theverge.com/2015/6/23/8830029/eternify-spotify-loop-payments

Pour contrer cette faille du système de paiement,
Deezer va passer à un système de paiement dit "User-Centric".
Selon ce système, les abonnements des utilisateurs ne sont plus regroupés.
Chacun de ses abonnements est répartis, 
en fonction uniquement des écoute de l'utilisateur en question.  
https://www.deezer-blog.com/how-much-does-deezer-pay-artists/

En plus d'empêcher la triche par fausses écoutes,
ce système très simple et naturel semble aussi plus équitable.
La répartition des recettes dépend en effet alors bien moins 
de ce qu'écoute les très gros consommateurs des plateformes de streaming.
En fait, avec le système User-Centric, 
chaque utilisateur contrôle qui sera financé par ses abonnements.
L'utilisateur ne rémunère que celles et ceux qu'il écoute.
"Pay who you play", comme dit Deezer.

Malheureusement, malgré des bonnes volontés chez Deezer
qui appellent à adopter le système User-Centric depuis 2016,
Deezer n'a pas encore transitionné vers ce système.
Quant à eux, Spotify et Apple sont plus réticents à changer de systèmes.  
https://www.digitalmusicnews.com/2022/08/02/streaming-payouts-user-centric-payment-system-market-share-payment-system/

Et il y a une raison simple à cela.
Ce changement de système revient à redistribuer les richesses différemment,
ce qui entraînera inéluctablement des gagnants et des perdants.
Selon une simulation du Centre National de la Musique,
le rock et la pop y gagneraient, au détriment du rap et du hip hop.  
https://cnm.fr/en/studies/impact-of-online-music-streaming-services-adopting-the-ucps/

Une étude de chercheurs de l'Université de Hambourg confirme cela,
avec notamment une perte estimée à près 90 millions d'euros 
pour le hip hop et le rap allemand,
par opposition à des gains importants pour le rock, le metal et le classique.
https://link.springer.com/article/10.1007/s11747-022-00875-6

Mais du coup, certaines grandes maisons de disque pourraient y perdre !
Et comme celles-ci ont un pouvoir de marché particulièrement important,
et qu'elles peuvent menacer les plateformes de streaming de les quitter,
le statu quo semble difficile à faire évoluer...

Ce phénomène est particulièrement insidieux, 
sachant à quel point l'apparence de succès est un facteur majeur du succès en musique,
comme l'ont montré Salganik, Dodds et Watts en 2006,  
https://www.science.org/doi/10.1126/science.1121066  
dans une expérience répliquée par Mehdi Moussaid dans une excellente vidéo Fouloscopie.  
https://tournesol.app/entities/yt:ppSrAHoGwrI

En particulier, en manipulant les algorithmes de recommandation,
l'impression de succès peut être boosté, et peut ainsi permettre un succès effectif.
Un journaliste affirme ainsi avoir reçu une offre.
Pour 12 000 euros, une agence de publicité lui promettait 1 millions de vues sur YouTube.
Dans un contexte où la fraude est facile et peu combattue,
l'argent fait le succès... qui fait lui-même beaucoup d'argent !  
https://musiczone.substack.com/p/le-big-hold-up-des-faux-streams

Plus généralement, la manière dont les activités des utilisateurs sont aggrégées 
est un aspect critique pour la sécurité et l'équité, et donc l'éthique, des systèmes ainsi conçus.
Et tout ce que je dis là dans le cas de la redistribution des recettes Spotify, Apple et Deezer,
s'applique tout autant au cas du machine learning...


## Le lien avec le machine learning

Dans quasiment tous les livres, les cours, les articles et les séminaires de machine learning,
vous trouverez l'hypothèse d'un pot commun de données,
et l'objectif d'apprendre de l'ensemble de ce pot commun.
Ou pire encore, ce pot commun est parfois remplacé par une mystique "distribution de données",
dont les données utilisées pour entraîner les algorithmes seraient tirées
de manière indépendante et identiquement distribuée.

Comme j'en ai parlé dans une vidéo précédente, 
cette hypothèse dite "i.i.d." est l'une des plus irréalistes et des plus dangereuse 
des hypothèses "standards" en machine learning - 
l'autre hypothèse dangereusement politisée étant l'objectif de généraliser les données collectées,
qui est clairement un parti pris pour le statu quo et les idées les plus populaires...  
https://tournesol.app/entities/yt:IVqXKP91L4E

Pour se rendre compte de l'inadéquation de l'hypothèse i.i.d., 
il suffit d'en revenir au cas de Spotify.
Le pot commun des temps d'écoute représente en fait très mal l'usage de Spotify.
Mais surtout, tout mettre dans un même pot revient à survaloriser
les utilisateurs qui ont une grosse consommation de Spotify,
et à ignorer ceux qui en ont une consommation plus occasionnelle.
Ainsi, il suffit dès lors d'écouter plus pour davantage influencer
la redistribution des recettes de Spotify.

Autrement dit, on peut identifier deux failles, l'une d'équité et l'autre de sécurité.
La faille d'équité est ce que je vais appeler le biais d'activité.
Les utilisateurs plus actifs ont un pouvoir disproportionné,
comparativement aux utilisateurs moins actifs.
Et notez que le problème ici n'est pas restreint aux plateformes de streaming musical.
Tout projet participatif est exposé au risque de biais d'activité,
y compris les débats politiques,
et des mécanismes comme le vote sont souvent critiques pour le corriger.

L'autre faille, de sécurité, est l'incitation aux activités factices.
Armés de fermes de trolls ou de bots,
les acteurs malveillants peuvent acquérir un pouvoir disproportionné,
et prendre le contrôle sur le système en place.  
https://tournesol.app/entities/yt:x22oI81jyTQ  
Et ça, pour toute application populaire et déployée sur le web,
il faut absolument se rendre compte que c'est la norme.
Pour rappel, l'industrie du cybercrime, c'est estimé à 6000 milliards de dollars,
soit 4 fois plus que Google, Apple, Facebook, Amazon et Microsoft combinés !  
https://tournesol.app/entities/yt:QprkRP-Dylo

Ces deux problèmes, biais d'activité et incitation aux activités factices, 
sont déjà alarmants dans le cas des algorithmes de langage,
qui en l'absence de fine-tuning et de prépompts,  
https://tournesol.app/entities/yt:dDhTMIao-fM  
ou lorsque le fine-tuning et le préprompt sont inadaptés pour un prompt d'un utilisateur,
vont se mettre à parler comme le font les comptes les plus actifs sur les réseaux sociaux,
ou comme les campagnes de désinformation le font.  
https://tournesol.app/entities/yt:vYb3rB0jU70

Ils deviennent toutefois plus catastrophiques encore dans le cas des IA les plus puissantes du monde,
à savoir les algorithmes de recommandation de YouTube, TikTok et Instagram,
qui décident tant de l'exposition informationnelle répétée de milliards d'humains sur terre.  
https://tournesol.app/entities/yt:utWMGi8HTjY  
Même si ces IA sont souvent conçues avec des hypothèses moins naïves que l'hypothèse i.i.d.,
elles subissent un énorme biais d'activité,
surtout lorsqu'elles favorisent les contenus en #Trending,
et sont clairement extrêmement vulnérables aux fermes de trolls et de bots,  
https://tournesol.app/entities/yt:8gH-sYnJez4  
notamment parce que la création de compte y est très facile,
et sans doute désormais très largement automatisables, 
via les algorithmes génératifs comme ChatGPT et MidJourney.  
https://tournesol.app/entities/yt:QprkRP-Dylo

Mais alors, que faire ? 
Comment corriger les systèmes d'apprentissage pour qu'ils évitent le biais d'activité
et l'incitation aux activités factices ?

Dans la vidéo précédente, sur les maths des IA démocratiques,
on avait vu un bout de la réponse,
en limitant l'impact maximal d'une donnée.
Mais clairement, ceci est insuffisant, sachant qu'il suffirait alors d'injecter plus de données
pour acquérir plus de droits de votes.  
https://tournesol.app/entities/yt:iy2RZbq7Kn4

Eh bien, avec mes collègues Sadegh Farhadkhani, Oscar Villemaud et Rachid Guerraoui, 
on a fourni une solution très propre, 
et finalement très proche du paiement User-Centric,
dans un article accepté en 2022 à la conférence ultra-prestigieuse ICML,
dont j'avais fait un vlog il y a plusieurs mois.  
https://tournesol.app/entities/yt:8YHFGYh1c6I  
https://proceedings.mlr.press/v162/farhadkhani22b.html


## La solution : isoler les contributions par utilisateur

L'idée centrale de notre solution, c'est d'isoler les données des différents contributeurs,
et de faire en sorte que l'ensemble des données d'un contributeur ait un impact limité
sur l'apprentissage d'un algorithme de machine learning.

Typiquement, le gradient associé à l'ensemble de ces données doit être normalisé,
et rendu de norme égale à 1, avant d'être affecté à l'algorithme d'apprentissage.
Et si on considère une norme euclidienne, on tombe exactement dans le cas de la médiane géométrique.
Autrement dit, de manière approximative, 
il ne faut pas prendre la médiane géométrique des données ;
il faut prendre la médiane géométrique des utilisateurs.

Voilà qui garantit vraiment la propriété d'équité : un votant, une force unitaire !
Et comme on l'a vu, elle est accompagnée de propriétés pas dégueux en termes d'incitations.

Alors, dans le cas du papier ICML, pour des raisons techniques,
et en particulier pour avoir des fonctions localement fortement convexes,
on a rusé et on a remplacé les forces unitaires par des forces quasi-unitaires,
obtenues avec la smooth-L2 putôt que la L2, ce qui a par ailleurs d'autres avantage.
Mais on peut oublier ces détails techniques pour aujourd'hui !

En fait, les systèmes de paiement Market-Centric et User-Centric 
sont intimement liés aux problèmes de robustesse discutés dans notre article.
Dans ces cas, chaque utilisateur a un vecteur d'écoute, 
qui assigne à chaque artiste un vecteur d'écoutes.
Le système Market-Centric est alors équivalent 
à prendre la moyenne des vecteurs d'écoute des abonnés à la plateforme de streaming,
puis à répartir les recettes de manière proportionnelle à ce vecteur d'écoutes.

Mais si vous avez suivi la vidéo précédente,
vous savez très bien que cette solution est mauvaise, car la moyenne est très manipulable,
en exaggérant le vecteur vers les directions qu'on préfère - 
ce qui peut être fait avec les fausses écoutes.

A contrario, le paiement User-Centric est équivalent à d'abord normaliser 
les vecteurs d'écoutes des différents abonnés,
à ensuite prendre la moyenne des vecteurs ainsi normalisés,
et à payer les artistes proportionnellement au vecteur moyen ainsi calculé -
bon techniquement ce ne sont pas les artistes qui sont payés,
mais leurs ayant-droits, typiquement les maisons de disques des artistes.

Et en fait, pour être plus précis, les vecteurs ne sont pas normalisés pour être de norme unitaire 
selon la norme euclidienne, aussi appelée norme L2, 
et qui est la manière usuelle de calculer des distances.
Ils sont de norme unitaire selon la norme L1.
Autrement dit, la somme des coordonnées du vecteur doit être unitaire.

Et alors, cette solution est en effet plus robuste, 
mais elle n'a pas les jolies propriétés d'incitatifs alignés avec l'honnêteté
dont on a beaucoup parlé dans le cas de la médiane géométrique.
En effet, si je suis tout aussi fan de 2 artistes aux succès très différents,
disons le sosie de Lê d'un côté - [extrait de Lê avec son ukulélé] -
et Taylor Swift de l'autre,
mais si je pense que le sosie de Lê est sous-payé, et que Taylor Swift ne l'est pas,
j'ai tout intérêt à mentir dans mon vote, et à voter entièrement pour le sosie de Lê -
par exemple avec des fausses écoutes... 
parce que, bon, c'est quand même un peu chiant d'écouter le sosie de Lê toute la nuit...

Comme je l'avais dit dans la vidéo précédente, s'il faut répartir des budgets,
au moins d'un point de vue sécurité et équité du vote,
et en oubliant la difficulté d'explicabilité pour le plus grand nombre,
la solution que je préconise c'est bien plus la médiane géométrique,
notamment à cause de ses propriétés de robustesse, d'incitatifs alignés avec l'honnêteté
et de localisation dans l'enveloppe convexe des votes reçus.

Mais d'ailleurs, dans le cas particulier du streaming, 
d'autres considérations pourraient aussi entrer en jeu, 
comme ne pas trop valoriser l'avis d'une personne qui n'a fait qu'une écoute dans l'année,
le fait de soutenir les artistes indépendants et de leur garantir un salaire minimum,
quitte potentiellement à limiter les recettes mirobolantes des méga-artistes,
voire le fait de favoriser les auteurs de musique qui améliorent le bien-être des consommateurs,
et qui diffusent des messages positifs pour la société,
aux dépens de ceux qui pourraient appeler à la haine et à la violence, par exemple.

En fait, l'algorithme qui détermine la répartition des recettes des plateformes de streaming,
et plus encore l'algorithme de recommandation qui met en avant certains contenus plutôt que d'autres,
c'est on-ne-peut-plus un objet politique en soi,
qui va déterminer la survie économique des différents créateurs de contenus,
les habitudes de consommation audio d'un demi-milliard d'humains
et les cultures musicales prédominantes aux quatre coins du monde -
quand bien même cet objet politique est sous le contrôle d'entreprises privées.
Et donc, tout ce dont on a parlé dans la série sur la démocratie,
et tout ce dont on a parlé dans cette série sur l'éthique de l'information,
s'applique à ces algorithmes des plateformes de streaming.

Et bien entendu, tout ceci s'applique en particulier à Tournesol,
cette plateforme qui vise à concevoir un algorithme de recommandation sécurisé et éthique,
en s'appuyant sur des principes de gouvernance démocratique.
Et sur Tournesol, justement, l'aggrégation des contributions des contributeurs
s'appuie sur une autre normalisation encore, à savoir la normalisation L infini.
Je ne rentre pas dans trop de détails pour aujourd'hui - on y reviendra -
mais en gros, sur Tournesol, et pour chaque vidéo qu'il ou elle a explicitement jugé,
chaque contributeur va en gros tirer le score de cette vidéo vers le score
qu'il ou elle juge être le score adéquat de la vidéo.

Si on l'appliquait à Spotify ou Deezer, 
cette normalisation revient à vous demander, pour chaque artiste, 
si vous pensez qu'il devrait être payé plus ou moins qu'il ne l'est actuellement.
Chaque utilisateur tire alors la recette de l'artiste vers le haut ou vers le bas -
ce qui n'est pas évident parce qu'on obtient alors une recette totale à reverser
qui n'a a priori rien à voir avec les recettes de ces plateformes -
bon, c'est un problème qui se pose beaucoup moins sur Tournesol,
puisque nous on reverse des scores Tournesol, pas de l'argent.

En fait, même sur Tournesol, 
ce principe de vote par norme L infini ne marche pas du tout
si on l'appliquait naïvement ainsi.
Pour obtenir une démocratie algorithmique satisfaisante,
il nous a fallu développer, depuis maintenant 3 ans,
une toute nouvelle théorie des votes sécurisés et équitables,
qui tient désormais dans plusieurs articles de recherche,
et qu'on continue à améliorer tous les jours,
notamment en cherchant à intégrer de volition, du vote bayésien ou encore de démocratie liquide -
avec dernièrement des progrès assez excitants 
dans la théorie des conversions de comparaisons en scores,
qui s'appuie désormais sur des mathématiques incroyablement élégantes dont j'ai hâte de vous parler.

Si tout ceci peut sembler très technique, 
(et malheureusement, c'est en effet très technique),
il me semble vraiment s'agir de préoccupations fondamentales à avoir
au moment de la conception de tout système participatif,
surtout lorsque les enjeux sont aussi massifs que le discours politique en démocratie,
ou la lutte contre les déviances autoritaires.

Mais pour continuer à développer ces outils, 
Tournesol a malheuresement besoin de plus de moyens, financiers et humains.
Le salaire de notre unique développeur n'est pour l'instant assuré que jusqu'à août.
Fort heureusement, nous avons maintenant la chance d'avoir l'aide et le soutien financier d'Infomaniak,
une entreprise éthique dont je suis heureux de vous parler sur Science4All.
À l'heure où les systèmes d'information sont trop souvent outsourcés à des tiers 
qui exploitent vos données et les données de vos entreprises pour entraîner des algorithmes génératifs,
il est devenu urgent de considérer que 
Slack, Google Docs ou autre Microsoft Teams sont des spywares en puissance.
A contrario, Infomaniak fait un effort majeur pour tout développer de manière souveraine,
avec des collaborateurs uniquement en Suisse,
un pays beaucoup plus digne de confiance, 
notamment par opposition aux entreprises américaines soumises au Patriot Act.
Vous pouvez profitez gratuitement des services Mail et SwissTransfer d'Infomaniak,
et je vous recommande aussi vivement leurs services Web, kMeet ou encore kDrive.
Pour chaque vidéo où je les promeus, ce que je fais avec grand plaisir,
Infomaniak reverse un don à l'Association Tournesol.
Merci beaucoup à eux pour ce partenariat.


# Conclusions

Si je récapitule, on a vu aujourd'hui que, très souvent,
les statistiques étaient aggrégées sans se soucier de leurs origines,
et des décisions importantes, avec parfois des milliards en jeu,
sont prises à partir de ces statistiques aggrégées.
J'espère que vous retiendrez qu'il s'agit là en fait d'une très mauvaise façon de faire,
aussi bien sur le plan de l'éthique que sur le plan de la sécurité.
Au lieu de cela, et à l'instar de ce que tout journaliste et scientifique apprend,
pour des questions de sécurité,
il est important de prêter attention aux sources de données, 
et juger la fiabilité des données à la lumière de ces sources.

Malheureusement, faute d'analyse critique de ces aspects,
et parfois poussée par la corruption et l'incitation 
à déployer rapidement des technologies spectaculaires,
les industries ont tendance à déployer rapidement des solutions très insatisfaisantes,
qui peuvent pourtant avoir des conséquences majeures sur des économies entières,
comme l'économie des artistes indépendants dans le cas des plateformes de streaming,
ou, dans le cas de ChatGPT et TikTok,
sur l'économie massive du cybercrime, la cybersécurité du tissu économique,
les capacités cognitives de milliards d'humains et les sujets d'actualité en démocratie.

Il est urgent d'exiger beaucoup plus de sécurité et d'éthique 
dans la conception des systèmes d'information.
En particulier, non, ce n'est pas parce qu'il s'agit d'algorithmes que c'est neutre ou sécurisé.
Faire l'hypothèse i.i.d. et généraliser les données collectées, c'est normaliser le statu quo.
Rien que calculer une moyenne plutôt qu'une médiane, c'est déjà favoriser l'industrie du cybercrime.
 
Malheureusement, l'expertise en mathématiques de la sécurité et de l'éthique est extrêmement rare,
notamment car dès qu'un mathématicien s'y intéresse,
on dit de lui qu'il sort de son champ d'expertise, voire on le traite d'idéologue.
Je parle d'expérience personnelle.

Je ne peux que vous encourager à ne pas laisser ces sujets en suspens,
et à encourager vos proches, vos collègues, vos entreprises et vos régulateurs à en faire de même.
Et pour monter en expertise sur ces sujets critiques,
sachez que notre entreprise Calicarpa, co-fondée par trois experts du domaine,
offre du conseil et de la formation pour vous et vos équipes.
Je vous invite à prendre contact avec moi, 
si vous souhaitez faire profiter vos équipes de nos services,
pour les éviter de tomber dans les nombreux pièges de la cybersécurité des IA,
dont même les ingénieurs de Samsung sont des victimes...  
https://www.lemonde.fr/pixels/article/2023/05/02/samsung-interdit-l-utilisation-de-chatgpt-a-une-partie-de-ses-employes_6171774_4408996.html

Le développement du numérique est aujourd'hui un énorme far west,
qui ne cesse de considérer que les enjeux de sécurité, d'éthique et de gouvernance,
sont secondaires et ne méritent pas une attention centrale.
J'espère que je peux compter sur vous pour ne pas tomber dans ce travers,
et pour faire au moins vos premiers pas 
vers un numérique plus sécurisé, éthique et collaborativement gouverné.


