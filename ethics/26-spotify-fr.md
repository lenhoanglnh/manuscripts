# L'album silencieux à 20 000$

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
pour augmenter leur temps d'écoute,
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
il existe une parade que Deezer a récemment décidé d'adopter,
et qui est un principe fondamental de notre recherche en sécurité des intelligences artificielles.
Aujourd'hui, on va parler de la théorie mathématique des IA équitables et sécurisées,
que mes nombreux co-auteurs et moi avons développée depuis 7 ans,
qu'on a peaufiné et optimisé notamment sur la plateforme Tournesol.  
https://www.deezer-blog.com/how-much-does-deezer-pay-artists/


## Market-Centric versus User-Centric

Alors, la manière dont les recettes de Spotify sont distribuées est très opaque,
et il y a des arrangements spécifiques pour les grands artistes,
qui passent notamment par les grands labels de disque 
comme Warner Music, Sony Music ou Universal Music.  
https://www.theverge.com/2015/5/19/8621581/sony-music-spotify-contract

Mais une composante clairement majeure de la redistribution des recettes Spotify aux artistes
est un système parfois appelé le Market-Centric Payment System.
En gros, dans ce système, les abonnements des consommateurs sont tous collectés 
et regroupés dans un pot commun.
Puis, chaque artiste est rémunéré à hauteur de son temps d'écoute total,
relativement aux temps d'écoutes des autres artistes.

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

D'ailleurs, ce hack fut même organisé et facilité par l'application Eternify,
développée par un autre groupe de musique en protestation 
avec le manque de protection des petits artistes.  
https://www.theverge.com/2015/6/23/8830029/eternify-spotify-loop-payments

Pour contrer cette faille du système de paiement,
Deezer va passer à un système de paiement dit "User-Centric".
Selon ce système, les abonnements des utilisateurs ne sont plus regroupés.
Chacun de ses abonnements est répartis, 
en fonction uniquement des temps d'écoute par l'utilisateur en question.  
https://www.deezer-blog.com/how-much-does-deezer-pay-artists/

En plus d'empêcher la triche par fausses écoutes,
ce système très simple et naturel semble aussi plus équitable.
La répartition des recettes dépend en effet alors bien moins des très gros consommateurs.
En fait, avec le système User-Centric, chaque utilisateur contrôle parfaitement
quels artistes seront financés par ses abonnements.
"Pay who you play", comme disent Deezer.

Malheureusement, contrairement à Deezer, 
Spotify et Apple sont plus réticents à changer de systèmes.  
https://www.digitalmusicnews.com/2022/08/02/streaming-payouts-user-centric-payment-system-market-share-payment-system/

Et il semble qu'il pourrait y avoir une raison très malsaine derrière cette réticence.
En effet, bien conscients qu'ils pouvaient hacker leur succès musical,
des gros artistes pourraient avoir payé les services du cybercrime,
pour automatiser les fausses écoutes et faire gonfler les chiffres des tubes de ces artistes.
Pour se rendre compte à quel point c'est malsain, 
je vous invite vivement à lire cette enquête glaçante de Philippe Astor,
qui décrit toute une industrie.  
https://musiczone.substack.com/p/le-big-hold-up-des-faux-streams

Ce phénomène est particulièrement insidieux, 
sachant à quel point l'apparence de succès est un facteur majeur du succès en musique,
comme l'a montré Mehdi Moussaid dans une excellente vidéo Fouloscopie.  
https://tournesol.app/entities/yt:ppSrAHoGwrI

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
qui est clairement en parti pris pour le statu quo et les idées les plus populaires...  
https://tournesol.app/entities/yt:IVqXKP91L4E

Pour se rendre compte de l'inadéquation de l'hypothèse i.i.d., 
il suffit d'en revenir au cas de Spotify.
Le pot commun des temps d'écoute représente en fait très mal l'usage de Spotify.
Mais surtout, tout mettre dans un même pot revient à survaloriser
les utilisateurs qui ont une consommation abusive de Spotify,
et à ignorer ceux qui en ont une consommation plus raisonnée.
Mais surtout, il suffit dès lors d'écouter plus pour davantage influencer
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

Eh bien, on aura fourni une solution très propre, 
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

En fait, le système User-Centric est en gros un cas particulier de notre article.
Dans ce cas, chaque utilisateur a un vecteur d'écoute, 
qui assigne un nombre d'heures d'écoute par artiste.
Au lieu de prendre directement la moyenne de ces heures d'écoutes,
on normalise ces heures d'écoute, 
en divisant par le nombre total d'heures d'écoute de l'utilisateur.

Autrement dit, on prend le vecteur d'écoute colinéaire de norme unitaire,
avec une petite précision : la norme considérée ici est la norme L1, pas la norme euclidienne L2.
Puis chaque utilisateur tire la distribution des heures d'écoute avec ce vecteur normalisé.
La somme des vecteurs normalisés détermine alors la répartition des recettes
selon le système User-Centric !

NB: La somme des gradients est ici directement le résultat final, 
pas le gradient à intégrer dans une étape d'apprentissage.

Alors, en termes d'incitatifs, la normalisation L1 n'est pas tip top.
Elle est même moins bien que la norme L2, en un certain sens.
Typiquement, si vous trouvez qu'un artiste est sous-payé par rapport à un autre,
notamment parce que les autres utilisateurs l'écoutent moins,
vous pourriez vouloir effectuer des fausses écoutes pour ce premier artiste,
alors que dans votre usage quotidien vous écoutez les deux autant.

NB: Encore une fois, ce que je dis là est approximatif, et surtout illustratif,
mais la L1 a tendance en effet à favoriser les "Dirac" sur une coordonnée.

En fait, la normalisation qui a les meilleures propriétés en termes d'incitatifs,
c'est la normalisation L infini, qui est intimement liée à la médiane par coordonnée.
Si on l'appliquait à Spotify ou Deezer, 
cette normalisation revient à vous demander, pour chaque artiste, 
si vous pensez qu'il devrait être payé plus ou moins qu'il ne l'est actuellement.
Chaque utilisateur tire alors la recette de l'artiste vers le haut ou vers le bas.

Alors, ceci pose d'autres problèmes, 
sachant que si on applique ceci naïvement au cas de Spotify et Deezer,
on va en fait calculer une sorte de temps d'écoute médian, 
qui sera quasiment toujours égal à zéro.
Bref. Il ne faut pas faire cela naïvement.

Mais chez Tournesol, on a beaucoup travaillé pour faire tout cela aussi intelligemment que possible,
et ça nous a conduit à développer depuis 3 ans 
une toute nouvelle théorie des votes sécurisés et équitables,
qui tient désormais dans plusieurs articles de recherche,
et qu'on continue à améliorer tous les jours,
notamment en cherchant à intégrer de volition, de vote bayésien ou encore de démocratie liquide.

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
Infomaniak reverse 2000 CHF de donation à l'Association Tournesol.
Merci beaucoup à eux pour ce partenariat.


# Conclusions

Si je récapitule, on a vu aujourd'hui que, très souvent,
les statistiques étaient aggrégées et des décisions importantes, 
avec parfois des milliards en jeu,
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
comme l'économie des artistes indépendants dans le cas des plateformes de streaming.

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
si vous souhaitez faire profiter vos équipes de nos services.



