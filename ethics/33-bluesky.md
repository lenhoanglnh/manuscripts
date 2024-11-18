# Les réseaux sociaux décentralisés (Bluesky, Mastodon, PeerTube...)

Si vous suivez la vulgarisation scientifique sur les réseaux sociaux,
vous avez sans doute observé un X-ode récent de Twitter vers d'autres plateformes,
en particulier vers Bluesky.
Si vous avez pour compris le jeu de mot, j'ai parlé de X-ode. X-ode...

Bref. En tout cas, oui, je fais partie de cette vague, 
notamment sous l'impulsion de Philoxime.
Bien sûr, cette immigration dans le ciel bleu est en partie un geste contestataire 
contre le probable futur directeur du Département de l'Efficacité Gouvernementale des US,
une personne qui est propriétaire de la plateforme Twitter qu'il a renommée X,
et qu'il a transformée en une [arme électorale](https://tournesol.app/entities/yt:dk9_m48rQVg) 
pour le futur Président Donald Trump.

Mais pour certains, il s'agit aussi et surtout d'adopter enfin un réseau social décentralisé,
plutôt qu'un réseau social entièrement contrôlé par un géant du numérique,
voire par un milliardaire étranger.
Et oui, Bluesky, mais aussi des plateformes comme Mastodon et PeerTube,
ce sont des plateformes décentralisées par conception.
Autrement dit, dès leur naissance, 
ces plateformes visaient à éviter une concentration de pouvoir dans l'espace informationnel.

Mais est-ce là vraiment une bonne idée de décentraliser les réseaux sociaux ?
Quelles sont les véritables garanties d'une décentralisation des réseaux sociaux ?
Y a-t-il des risques que cela amplifie le chaos informationnel ?
Quelles sont les chances que, au contraire, 
cette décentralisation protège nos démocraties 
du cyber-harcèlement, de la désinformation et de la haine ?
Et puis, d'abord, comment fonctionnent ces réseaux sociaux décentralisés ?
Qu'est-ce que ça signifie pour un réseau social d'être décentralisé ?
Et puis, Bluesky et compagnie sont-ils vraiment décentralisés ?

Aujourd'hui, on essaie de faire le point sur toutes ces questions,
pour mieux comprendre les enjeux démocratiques 
d'une décentralisation des réseaux sociaux.


## Retour aux emails

Pour commencer, revenons loin, très loin en arrière, 
dans les années 1970, 
avec les débuts d'internet.
L'une des premières applications de la connexion de réseaux de machines à travers le monde,
c'est le courrier électronique, aussi connue sous le nom de courriel ou d'email.
La solution devenue standard dans les années 1980 combine plusieurs protocoles,
avec des acronymes comme SMTP, POP et IMAP.

En gros, ce qu'il se passe en général,
c'est que les machines des utilisateurs vont servir de clients mails,
notamment s'ils utilisent des applications comme Thunderbird ou GNOME Evolution.
Le problème, c'est que ces clients mails ne sont pas toujours allumés et connectés à Internet.
Du coup, lorsque quelqu'un envoie un email à un utilisateur,
l'email ne peut pas tomber directement dans le client mail du destinataire.

Il sera en général stocké sur un serveur mail,
comme gmail, protonmail, kmail, ovh ou encore caramail.
Ah caramail... like cette vidéo si t'es assez vieux pour avoir connu cette belle époque !
Ce serveur mail va aussi être en charge de renvoyer un accusé de réception à l'envoyeur,
de sorte que celui-ci sache si l'envoi a échoué,
et s'il y a donc lieu d'essayer de le renvoyer.
Le protocole SMTP, pour Simple Message Transfer Protocol, se charge de tout ça.

Maintenant, quand on veut accéder à nos emails,
nos clients mails vont alors demander au serveur mail
de nous envoyer tous les emails qu'il ne nous a pas encore envoyé.
Et si on utilise le protocole POP, pour Post Office Protocol,
alors le serveur mail va aussi supprimer ces emails :
dans ce cas, le serveur mail sert avant tout de relai.
Mais ça, ce n'est pas pratique si on veut accéder à nos emails depuis plusieurs machines,
ou si on a peur de perdre nos emails le jour où notre serveur mail tombera en panne.
Du coup, on peut préférer le protocol IMAP,
pour Internet Message Access Protocol,
où le serveur mail conserve nos mails,
et les redistribue aux différents clients mails qui souhaite les télécharger.

Et alors, il y a beaucoup de surcouches de cryptographie pour sécuriser tout cela,
notamment des histoires de TLS, de DKIM, voire de PGP...
mais oublions tout cela pour aujourd'hui.

En principe, il n'y a nul besoin d'utiliser un service d'une entreprise privée.
Vous pourriez très bien acheter votre propre machine, 
la laisser constamment allumer,
et lui demander de jouer le rôle de votre serveur mail.
C'est en cela que le protocole email est très décentralisé.

Bref. Tout ça est un peu technique,
mais si je prends le temps de vous en parler,
c'est parce qu'il s'agit d'un archétype de protocole décentralisé,
qui montre toutefois bien les limites de la décentralisations.
Et oui, parce qu'il y a de bonnes chances pour que vous qui regardez cette vidéo,
vous n'utilisez en fait ni le protocole POP, ni le protocole IMAP,
notamment parce que vous ne disposez même pas d'un client mail.
C'est typiquement le cas si vous accédez à vos emails via un navigateur web,
comme Google Chrome, Microsoft Edge, Safari ou encore Mozilla Firefox.
Dans ce cas, les mails sont envoyés à votre navigateur,
et toute la gestion des nouveaux mails reçus est directement faite
par votre serveur mail.

Et comme, de plus, il y a finalement une poignée d'acteurs
qui sont abondamment utilisés comme serveurs mails,
le protocole SMTP/POP/IMAP s'est centralisé,
avec désormais une gestion centralisée des emails sur gmail ou outlook.
Il y a même de bonnes chances 
que les emails de votre entreprise sont en fait eux aussi gérés 
par l'un des géants du numérique,
si bien que la malveillance ou le hack massif d'un de ces géants 
pourraient compromettre toutes les communications d'un très grand nombre d'entreprise.

Or malheureusement, une telle malveillance ou un tel hack massif,
ce n'est asbolument pas de la science-fiction. 
L'analyse automatisée de vos emails par les géants du numérique est systématique
(après tout gmail vous propose des autocomplétions et des réponses automatisées),
et [Microsoft a subi un hack majeur à l'été 2023](https://tournesol.app/entities/yt:v66YDx7U6V0),
qui a conduit à un [rapport incendiaire](https://www.cisa.gov/resources-tools/resources/CSRB-Review-Summer-2023-MEO-Intrusion)
de l'agence américaine de cybersécurité, le CISA,
où l'on peut lire que "Microsoft ne sait pas comment ses systèmes ont été infiltrés
et si les vulnérabilités utilisées ont été corrigées".
Autrement dit, le hack n'est pas un événement isolé dans le temps ;
les attaquants chinois sont très probablement encore dans les systèmes critiques de l'entreprise.

Aussi piratable qu'un PC Windows.

Et malheureusement, décentraliser l'email moderne est loin d'être trivial,
notamment parce que les protocoles modernes sont en fait horriblement complexes,
avec notamment toutes sortes de blacklists pour combattre la pandémie de spams.
En gros, votre serveur fait-maison a de bonnes chances d'être bloqué par Gmail ou outlook...
Et comme l'intérêt des emails, c'est d'envoyer des messages à d'autres,
qui pour beaucoup sont sur ces plateformes,
en pratique, c'est vraiment compliqué de décentraliser les emails aujourd'hui.
C'est le piège de l'effet de réseau.

En fait, à moins que vous ne soyez un professionnel qui utilise des clés PGP
et qui ne parle qu'à d'autres professionnels qui utilisent eux aussi des clés PGP,
ce qui est mon cas avec les co-fondateurs de mon entreprises d'ailleurs,
je vous recommande fortement de privilégier des solutions de messagerie modernes comme Signal,
qui est libre, open-source et fournit du chiffrement bout-à-bout,
pour envoyer des messages sensibles à vos contacts.
Même si Signal n'est pas lui-même un système centralisé,
il a au moins l'avantage d'être "zero-trust", 
dans le sens où une compromission de Signal paralyserait la messagerie,
mais ne permettrait pas à l'attaquant d'accéder à vos messages,
car ils sont chiffrés de bout-à-bout.

En tout cas, il s'agit d'un avertissement important :
les forces du marché et la tentation de la centralisation 
pour simplifier la résolution des problèmes de cybersécurité
plannent systématiquement sur tout protocole a priori décentralisé,
ce qui peut conduire à l'adoption de solutions qui sont en fait très mal sécurisées,
notamment car elles concentrent les risques sur un petit nombre de systèmes d'information.


## Mastodon, ActivityPub et le Fediverse

Mais donc, à quel point ce risque est-il présent pour les réseaux sociaux décentralisés ?
Est-ce que Mastodon est vraiment une solution pour décentraliser les réseaux sociaux ?

Pour essayer de répondre à cette question,
il va me falloir expliquer un peu le protocole ActivityPub
sur lequel repose Mastodon, mais aussi PeerTube et Threads,
le nouveau réseau social de Facebook inspiré de Twitter.

ActivityPub a été [standardisé](https://www.w3.org/TR/activitypub/#social-web-working-group) 
en 2018 par le World Wide Web Consortium, ou W3C.
Et comme pour les emails, tout utilisateur va avoir un client,
qui va être typiquement son navigateur web ou une application sur son téléphone,
et va s'appuyer sur un serveur ActivityPub constamment connecté
pour envoyer et recevoir des messages au reste du monde.
Par exemple, j'ai créé un compte ActivityPub 
à [mastodon.social/@lenhoang](https://mastodon.social/@lenhoang),
ce qui signifie que je fais confiance au serveur mastodon.social
pour gérer mes envois et mes réceptions de messages ActivityPub.

Ce serveur ActivityPub va en particulier gérer 2 boîtes :
une boîte d'envoi de messages, ou outbox,
et une boîte de réception de messages, ou inbox.
Et comme pour les emails, 
à chaque fois que l'utilisateur voudra consulter un fil d'actualité,
il retirera des messages de l'inbox.
Et s'il veut publier des contenus, il enverra dans l'outbox.

Le gros du travail, c'est encore une fois le serveur ActivityPub qui va l'effectuer.
En particulier, il va devoir maintenir l'inbox,
en faisant régulièrement une requête aux autres serveurs ActivityPub
qui gèrent les publications des comptes auxquels l'utilisateur est abonné.
Il peut bien sûr potentiellement y ajouter des requêtes à d'autres serveurs ActivityPub,
comme ceux qui sont spécialisés dans l'analyse des tendances.
Et à l'inverse, quand vos contenus sont dans votre outbox,
ils seront livrés à tous ceux qui se sont abonnés à vous,
au moment où leurs serveurs ActivityPub mettent à jour leur inbox.

Pour ceux qui connaissent, cette opération est très similaire aux flux RSS,
qui vous permettre d'obtenir 
toutes les nouvelles publications d'un journal ou d'une chaîne YouTube,
en appelant directement le serveur qui publie ces contenus,
et donc sans passer par un serveur mail ou un serveur ActivityPub.
L'un des ajouts, c'est une sémantique pour permettre naturellement
le like, le partage et le commentaire à des publications antérieures,
en faisant référence à ces publications antérieures.

Comme pour les emails, en principe, 
chacun pourrait concevoir son serveur ActivityPub,
ce qui fait de ce protocole un protocole décentralisé.
Mais en pratique, ce n'est pas si simple.
Et oui, on a vu que la difficulté du serveur mail personnel,
c'est de réussir à ne pas se faire bloquer par les autres serveurs mails.
Eh bien, dans ActivityPub, un serveur ActivityPub peut bloquer d'autres.

Et ce n'est pas un hasard.
Il y a déjà des [dizaines de milliers de serveurs ActivityPub](https://instances.social/list/advanced#lang=&allowed=&prohibited=&min-users=&max-users=).
Mais du coup, dans le tas, il faut s'attendre à ce que certains soient malveillants,
et puissent par exemple vouloir inonder le réseau de spams.
Et d'ailleurs, cela peut ne pas être malveillant !
Avec Threads dans ActivityPub, 
les petits serveurs ActivityPub risquent d'avoir bien du mal 
à suivre ce qu'il se passe sur Thread...

Mais surtout, dans le tas, il y aura inéluctablement des serveurs
qui hébergent toutes sortes de contenus problématiques,
comme du cyber-harcèlement, de la désinformation et des appels à la haine,
voire du traffic de drogues, d'armes et d'humains.

Mais du coup, c'est même une fonctionnalité du protocole 
que de permettre aux modérateurs d'un serveur ActivityPub A
de bloquer entièrement d'autres serveurs ActivityPub B.
Mais si vous utilisez le serveur A, 
vous ne pourrez du coup plus recevoir les messages du serveur B.
En fait, le système ActivityPub, 
il est en quelque sorte davantage féodal que décentralisé,
dans le sens où les terrains des seigneurs peuvent communiquer,
mais ils peuvent aussi être bloqués.
L'espace informationnelle dans ActivityPub est ainsi naturellement morcelé,
ou du moins morcelable.

Alors, il n'est pas non plus complètement féodal,
puisque vous pouvez facilement déménager dans un autre serveur C,
voire vous pouvez créer votre propre serveur ActivityPub.
Cependant, ce transfert de compte d'un serveur à l'autre est nécessairement un peu radical.
Et ça, c'est en fait parce que votre serveur concentre beaucoup de tâches.
Ce serveur gère non seulement vos inbox et vos outbox,
mais aussi du coup tout votre historique et vos clés cryptographiques 
pour authentifier vos messages,
ainsi que, comme on l'a vu, les serveurs ActivityPub à qui vous pouvez parler
et ceux que vous pouvez écouter.

Autrement dit, ActivityPub n'a pas super bien appliqué
le principe de cloisonnement avec moindre privilège,
dont on vous parle dans le "Guide de Survie au Cybercrime en Entreprise",
co-écrit avec Romain du Marais et préfacé par Guillaume Poupard.


## Bluesky et le Protocole AT

En 2019, bien avant le rachat par le futur bras droit de Trump, 
Twitter a exploré la décentralisation de sa plateforme.
C'est ainsi qu'est né le projet Bluesky,
et surtout le développement du protocole AT.
Ah 2019... c'était un peu l'âge d'or de l'éthique des algorithmes.

En 2021, sous le poids de la menace du modèle d'affaire de Twitter,
le projet Bluesky fut incorporé sous une entreprise indépendante, appelée "Bluesky Social",
avec un statut "d'entreprise d'intérêt pour la société", ou Benefit corporation en anglais.
En pratique, ça exige uniquement d'ajouter l'objectif d'intérêt pour la société
dans les statuts de l'entreprise,
et il y a clairement des risques d'ethics washing derrière ce genre d'appellation.

Mais au delà des mots, le projet Bluesky a vraiment coupé les ponts avec Twitter,
en effectuant des levées de fonds alternatives,
et en exigeant une énorme transparence dans le développement.
C'est ainsi qu'est né non seulement le protocole AT,
mais aussi le code open source de Bluesky sous licence libre MIT.
Bluesky, c'est vraiment une entreprise née des frustrations d'employés de Twitter
du manque de sécurité et d'éthique de la plateforme,
et avec un engagement bien plus que seulement officiel
dans la conception d'un réseau social au service de la société.

En particulier, de manière remarquable,
Bluesky a beaucoup plus cherché à découper les différentes fonctionnalités
qu'on attend d'un réseau social,
et les a confié à des modules différents,
en exigeant un maximum de portabilité.

Autrement dit, ce protocole correspond beaucoup plus 
aux appels au [pluralisme algorithmique](https://www.lemonde.fr/idees/article/2024/09/25/pour-le-pluralisme-algorithmique_6332830_3232.html),
comme le fait une tribune publiée dans Le Monde,
dont vous pourrez trouver une traduction sur [aiforensics.org](https://aiforensics.org/algopluralism),
et dont la liste des signataires inclut l'Assocation Tournesol.

Plus précisément, le protocole AT considère trois types de serveurs :
les PDS, les relais et les AppView.
Les PDS, pour Personal Data Server, sont un peu l'équivalent des serveurs mail.
Chaque utilisateur peut avoir son propre PDS, 
qui enregistra les données personnelles de l'utilisateur,
notamment tout ce que l'utilisateur publie

> Alors, pour être précis, ce serveur contient une indexation de vos données ;
> vos images et vidéos sont généralement sauvegardées dans un autre serveur,
> optimisé pour le stockage de gros fichiers.

Les relais, eux, vont effectuer le gros du travail.
Ils vont régulièrement lire les informations publiques des PDS des utilisateurs,
et les organiser pour qu'elles soient ensuite prêtes à être accédées.
Enfin, les AppViews vont accéder aux informations des relais,
pour les afficher sur le téléphone ou l'ordinateur d'un utilisateur.

Autrement dit, les tâches de publication, d'aggrégation des publications
et d'affichage chez les utilisateurs ont été segmentées :
et ça, ça veut dire que si un serveur de stockage de vos données vous paraît louche,
vous pouvez uniquement modifier ce PDS,
qui a vraiment été conçu pour être portable,
tout en préservant l'utilisation normale du réseau social.
De même si les relais ignorent systématiquement les comptes que vous voulez suivre,
vous pouvez demander à votre AppView de récupérer ses données chez un autre relai.

Enfin, si vous n'aimez pas l'interface de votre AppView,
si vous trouvez qu'il manque de fonctionnalités à la TweetDeck,
ou si vous souhaitez un algorithme de recommandation spécifique,
vous pouvez utilisez une autre AppView.

Le protocole AT envisage même l'ajout de deux autres types de serveurs :
d'un côté les serveurs d'étiquetage des contenus publiés, 
typiquement en charge d'évaluer 
si un message est un discours de haine, de cyberharcèlement ou de désinformation ;
et de l'autre les serveurs de création de fils d'actualité,
qui vont filtrer les contenus et surtout sélectionner ceux qui vont être recommandés.

Et puis, bien sûr, je n'ai ici que survoler le protocole AT,
mais il y a bien sûr beaucoup de nombreux autres aspects importants
que je ne vais pas prendre le temps de détailler.
Ceci étant dit, en théorie, 
même si le protocole AT est clairement une avancée remarquable,
on est encore loin de l'idéal de l'algorithmique répartie,
qui garantirait à un utilisateur aucune gêne occasionnée,
même si certains composants du réseau deviennent tout à défaillants,
voire malveillants, typiquement parce qu'ils ont été piratés par des malfaisants.

Mais surtout, en pratique, jusque là en tout cas,
si le protocole AT a été conçu pour permettre un réseau social très décentralisé,
force est de constater que BlueSky est encore assez incontournable,
et qu'il gère en fait tous les services identifiés,
à savoir le PDS, le relai, l'étiquetage, la création de fils et l'AppView.
Donc il va falloir attendre encore un peu pour voir dans quelles mesures
le protocole AT définit vraiment un réseau social décentralisé.


## De nouvelles fonctionnalités

Pour l'instant, Mastodon et Bluesky disposent d'un nombre limité de fonctionnalités,
notamment si on le compare à des alternatives comme Twitter.
Et je veux vraiment insister sur le fait que c'est une excellente chose.
Comme on en parle dans le Guide de Survie au Cybercrime,
l'un des principes opérationnels fondamentaux de la cybersécurité,
c'est la sobriété numérique.
Plus vos outils numériques seront sobres,
et moins ils seront bourrés,
bourrés de fonctionnalités mais bourrés aussi de potentielles vulnérabilités
que des attaquants pourront exploiter pour ces outils.
Il faut absolument réduire la *surface d'attaque*.

Néanmoins, ces protocoles permettent déjà de nouvelles fonctionnalités.
Les protocoles ActivityPub et AT étant partiellement interopérables,
sur Mastodon, il est possible en principe de concevoir des comptes
qui vont être conçus pour relayés des informations publiées sur Bluesky,
et vice-versa.
On parle de "Bridge" entre les protocoles.
Cependant, ces Bridges ne seront pas parfaits, 
certaines opérations dans l'un des protocoles 
ne pouvant pas tout à fait être traduits dans l'autre.
Et surtout, jusque là, aucune solution ne semble être solidement maintenue ;
par exemple Bridgy Fed n'est maintenue que par le seul Ryan Barrett,
ce qui soulève des préoccupations en termes de continuité de la maintenance,
voire en terme de compromission potentielle.

De même des AppViews alternatives peuvent accéder aux données des relais AT,
et c'est le cas en particulier de deck.blue,
qui rappellera TweetDeck à ceux qui connaissent.
Cependant, là encore, méfiance méfiance,
deck.blue est maintenu par l'unique [Giladsio](https://patreon.com/deckblue/about),
ce qui questionne la pérennité et la sécurité de cette solution.

Par ailleurs, sur Bluesky,
vous avez la possibilité pour chacun de créer des "starter packages",
c'est-à-dire une liste de comptes Bluesky que vous pourrez suivre.
Plus généralement, pour vous lancer sur Bluesky,
je vous invite à cliquer sur le profil d'un utilisateur actif que vous aimez bien,
et à voir la liste des personnes que cet utilisateur suit.

Une autre fonctionnalité chouette de Bluesky,
qui montre bien qu'elle a été pensée par des anciens des équipes de sécurité de Twitter,
c'est la possibilité d'être détaché d'une citation.
Ainsi, comme sur Twitter, 
vous pouvez partager un message publié et y ajouter un commentaire.
Cependant, sur Twitter, si cette action est souvent utilisée pour sourcer une information,
ou pour diffuser une tendance amusante,
elle l'est aussi trop souvent pour faire des [appels à la meute](https://tournesol.app/entities/yt:P0YB40z7RJ0),
en encourageant typiquement la haine envers la personne citée.
Pour éviter cette troisième utilisation sans compromettre les deux premières,
Bluesky permet à la personne citée de forcer le détachement de son message.

Par ailleurs, Mastodon et Bluesky proposent tout deux 
une solution de vérification de compte à partir d'une preuve de contrôle d'un site web.
Typiquement, si vous voulez garantir que vous êtes bien Lê Nguyên Hoang,
vous pourriez prouver que vous contrôlez bien le site [Science4All](https://science4all.org),
car il y a suffisamment d'éléments sur des sites sérieux 
qui font le lien entre Lê Nguyên Hoang et ce site.
Et pour y arriver, Mastodon et Bluesky vous proposent le défi suivant :
intégrer au site Science4All.org une mention des comptes Mastodon et Bluesky
que vous prétendez posséder.
C'est ce que j'ai fait, et c'est pour ça que sur Bluesky par exemple,
vous verrez que mon arobase est @science4all.org.

Sur Bluesky, en plus de faire ça avec son site [scienceetonnante.com](https://scienceetonnante.com),
David Louapre a également prouvé qu'il contrôlait la chaîne YouTube Science Étonnante,
en ajoutant à la description de la chaîne son compte Bluesky ;
et d'ailleurs je l'ai copié, en en faisant de même avec ma chaîne YouTUbe.

Sauf que bien sûr, ceci marche uniquement si vous disposez d'un site,
ou d'un compte sur un autre réseau social,
qui est de notoriété suffisante.
En particulier, on est malheureusement encore très loin d'une preuve de citoyenneté,
et plus loin encore d'une preuve de citoyenneté 
avec potentiellement divulgation nulle d'identité,
qui serait un peu le Saint-Graal pour être authentifié en ligne de manière anonyme.
Cependant, le protocole AT me semble parfaitement approprié pour inclure ce genre d'informations.

Les protocoles ActivityPub et AT ont par ailleurs introduit des mécanismes de modération,
des outils bien entendu indispensables pour gouverner adéquatement les réseaux sociaux,
et éviter la violation des lois existantes sur le harcèlement et l'appel à la haine.
Sur ActivityPub, la modération est avant tout effectuée au niveau des serveurs ActivityPub,
non seulement en supprimant éventuellement des contenus publiés sur ces serveurs,
mais aussi en bloquant éventuellement les flux venant de certains autres serveurs ActivityPub.

Dans le protocole AT, 
l'idée est davantage de permettre à différentes entités de poser une étiquette, 
aussi appelée label,
sur des contenus publiés.
Le [relai Bluesky](https://docs.bsky.app/docs/advanced-guides/moderation#global-label-values) 
peut par exemple imposer le label `!hide`,
qui cachera les contenus aux AppViews qui utilisent ce relai.
Mais il peut aussi se contenter d'un label comme `porn`,
qui sera visible des AppViews, 
qui pourront alors décider elles-mêmes de publier ou non le contenu.
D'ailleurs, ces labels ne viennent pas nécessairement du relai Bluesky.
Les utilisateurs peuvent eux-mêmes étiqueter leurs propres publications.

Mais surtout, comme on l'a vu, 
le protocole AT envisage de permettre à des tiers d'ajouter leurs propres étiquettes.
On peut ainsi tout à fait envisager que, à l'avenir,
une plateforme à la Tournesol organise un étiquetage collaboratif,
puis les aggrège en scores Tournesol selon différents critères pour chaque contenu publié,
comme on le fait déjà pour les vidéos YouTube.
En fait, adapter Tournesol à Bluesky serait sans doute déjà d'actualité,
si l'Association Tournesol disposait des moyens humains et financiers suffisants
pour investiguer la gouvernance démocratique des plateformes de micro-blogging.

Bref, en régulant les mécanismes de labels,
en particulier la manière de les assigner 
et la manière dont ils doivent être pris en compte par les AppViews,
on peut tout à fait envsager une gouvernance démocratie 
des réseaux sociaux qui suivent le protocole AT.

Enfin, il y a le problème des messages directs qui
sont assez mal gérés par les protocoles ActivityPub et AT.
En particulier, dans sa [Roadmap 2024](https://docs.bsky.app/blog/2024-protocol-roadmap),
Bluesky reconnaît utilisé un système centralisé pour l'instant.
Ceci étant dit, Bluesky prévoit à terme de développer du chiffrement bout-à-bout,
ou End-to-end encryption,
comme le fait déjà très bien Signal.
Donc je vous recommande d'éviter d'envoyer des messages trop sensibles 
via la messagerie directe de Bluesky, 
et d'utiliser plutôt Signal.


## Les travers de la décentralisation

Quoi qu'il en soit, au cours des dernières années,
il y a eu beaucoup de progrès techniques dans la décentralisation des réseaux sociaux,
ainsi que dans leur adoption,
même si on est très loin de réseaux sociaux complètement décentralisés et massivement utilisés.
Et c'est une excellente chose... non ?

Clairement, les réseaux sociaux prédominants sont très centralisés,
et ceux-ci abusent de leur position dominante,
à travers notamment un [lobbying extrêmement puissant](https://usbeketrica.com/fr/article/ia-pourquoi-il-est-urgent-de-porter-de-l-attention-aux-conflits-d-interet-des-experts-en-ia),
et avec des conséquences géopolitiques,
à l'instar des appels des dirigeants américains 
[à ne pas réguler Twitter en Europe](https://www.independent.co.uk/news/world/americas/us-politics/jd-vance-elon-musk-x-twitter-donald-trump-b2614525.html).
Pire encore, ils sont mêlés à un nombre déraisonnable de scandales,
qui vont de la radicalisation des démocraties vers l'extrême-droite
à la complicité dans des génocides,
en passant par des crises de santé mentale,
des affinités avec des trafics d'humains,
voire du chantage sur le journalisme de pays démocratiques 
comme le Canada et l'Australie.

Vraiment, Google, Facebook, TikTok et compagnie,
ce sont vraiment des entreprises extrêmement sales
qui menancent la viabilité des démocraties.
Ce ne sont absolument pas des entreprises "cools" 
où il est chouette de travailler, 
ou qu'il est souhaitable de copier.

Cependant, est-ce que l'alternative souhaitable,
ce sont vraiment des réseaux sociaux décentralisés ?

Dès 2018, on m'a invité à publier mes vidéos sur Skeptikon.fr,
un serveur ActivityPub qui s'appuie sur le logiciel libre PeerTube.
Mais honnêtement, quand je vois la description de Skeptikon,
avec le mot zététique un peu partout,
ça ne me donne personnellement absolument pas envie.
Il y a déjà eu des dérives sectaires dérangeantes dans le mouvement zététique.
Un réseau social qui s'annonce dédié à ce mouvement,
ça me semble en fait plus inquiétant qu'enthousiasmant.

Or, bien sûr, Skeptikon, 
c'est pourtant très loin d'être la communauté web la plus dérangeante.
Même s'ils n'utilisent pas le protocole ActivityPub,
les plateformes comme BitChute, Gab ou 4Chan sont très largement reconnues 
comme étant des nids de radicalisation d'extrême-droite.

Alors oui, concevoir des réseaux sociaux alternatifs,
c'est permettre à des journalistes et des politiciens de se protéger 
du harcèlement et de la haine,
ce qui est vraiment important.
Mais si les solutions techniques qu'on avance faciliteront également
la radicalisation de bulles idéologiques alimentées par la haine,
il y a de quoi être très dubitatif vis-à-vis de leur intérêt démocratique.
C'est vraiment pour ça que j'ai utilisé le qualificatif "féodal"
pour parler du protocole ActivityPub,
mêm s'il est probablement un peu trop fort.

Dans notre livre "La dictature des algorithmes", co-écrit avec Jean-Lou Fourquet,
un chapitre est dédié à la tension entre centralisation et décentralisation.
Et ce qu'on a écrit, c'est qu'il s'agit d'un problème en fait ancestral,
auquel la Révolution Française a fourni une solution remarquable :
en fait, pour vivre ensemble, il faut avant tout décentraliser la gouvernance,
mais au moins certaines parties de cette gouvernance doivent être appliquées uniformement,
de manière donc centralisée.

Ou dit autrement, la solution semble avant tout résider 
dans un État de droit dont les lois sont décidées démocratiquement :
le contenu des lois est conçu de manière décentralisée,
en tenant compte de l'avis d'un grand nombre de personnes,
afin d'inclure des diversité de points de vues
et d'augmenter radicalement le coût de la corruption de la gouvernance.
Mais une fois les quasi-consensus radicaux identifiés,
et une fois qu'on s'est mis d'accord pour en faire des lois,
il faut qu'il y a une et une seule loi ;
et que cette loi s'applique à tous.

En tout cas, cette vision de décentralisation de la gouvernance de décisions centralisées,
c'est vraiment la raison d'être du projet Tournesol.
Nous pensons que, pour limiter les risques de corruption,
ainsi que pour bien tenir compte de la diversité des points de vue,
il est indispensable de décider collectivement des contenus à amplifier massivement.
Mais une fois les consensus identifié,
il est aussi important que ces contenus qu'il est d'intérêt général de diffuser 
soient effectivement diffusés au plus grand nombre.

Bien sûr, comme on l'a vu, 
cette vision est loin d'être incompatible avec le protocole AT.
Mais pour qu'elle prenne un jour le pas,
il va falloir qu'on ne vise pas uniquement 
la décentralisation et le pluralisme des algorithmes ;
il est aussi indispensable, je pense, d'assujettir ces algorithmes à la voix démocratique.


## Conclusion

Aujourd'hui, on a donc vu que 
les réseaux sociaux pouvaient être beaucoup plus décentralisés
qu'ils ne le sont actuellement,
grâce à des protocoles remarquables, 
notamment le protocole AT utilisé par Bluesky.

Attention toutefois à ne pas tomber dans un techno-solutionnisme,
en se concentrant uniquement sur un aspect technique
de la conception des réseaux sociaux.
En pratique, il y a aussi de nombreuses lois qui régissent l'espace informationnel,
comme les lois sur la diffamation, l'incitation à la haine raciale,
le cyber-harcèlement, la protection des données personnelles ou les droits d'auteur.
Les juristes, les sociologues et le peuple ont aussi un rôle crucial à jouer
pour assainir notre cyberespace et protéger nos démocraties.

À l'inverse, toutefois, 
il faut éviter également le piège du socio-solutionnisme,
par exemple en espérant que le DSA sera magiquement appliqué
ou que les citoyens français vont magiquement abandonner TikTok.
Concrètement aujourd'hui, on manque aussi de nombreuses solutions techniques
pour assujettir notre espace informationnel aux normes démocratiques,
comme la preuve de citoyenneté sans divulgation d'identité,
des solutions pour identifier et promouvoir les consensus radicaus
et des algorithmes résilients à des cyber-attaques.

D'ailleurs, ces derniers sont particulièremment difficiles à concevoir
dans des systèmes décentralisés,
dont les participants peuvent en fait être 
des serveurs de forces étrangères ou du cybercrime.
Il est alors indispensable de concevoir des algorithmes 
qui incluent vraiment l'état de l'art de la cryptographie ;
et c'est justement ce dont je parle dans ma série sur la cybersécurité.
Et si vous avez déjà vu quelques vidéos,
vous savez à quel point le niveau technique requis est très élevé.

Et donc pour finir, j'aimerais avant tout effectuer un appel à l'aide.
Concevoir une démocratie numérique, 
ce qui me semble indispensable pour protéger nos démocraties aujourd'hui très menacées,
c'est malheureusement un énorme chantier extrêmement pluridisciplinaire.
Si on veut se donner les chances de ne pas succomber à des gouvernements autoritaires,
ou à une troisième guerre mondiale,
il est indispensable que tous ceux parmi nous qui le pouvons
donnions au moins un peu d'attention à cette cause.

Et pour cela, il y a une myriade de choses que vous pouvez faire,
comme vous informer davantage à ce sujet,
en parler autour de vous, à vos proches et à vos collègues,
organiser des événements avec des experts de ces questions,
orienter les financements publics et privés vers ces considérations,
ou encore adopter les solutions qui s'approchent le plus d'une démocratie numérique,
comme privilégier Bluesky à Twitter.

En particulier, je crois sincèrement 
que notre projet Tournesol est le plus abouti à ce sujet,
même s'il est lui-même encore extrêmement déficient.
Bluesky a reçu des dizaines de millions de dollars d'investissement
pour concevoir en quelques années le protocole AT et une plateforme minimaliste.
Si on veut une démocratie numérique, 
il va falloir au moins ce genre d'investissements pour y arriver.
En attendant, vous pouvez nous aider de multiples manières :
en évaluant des vidéos sur Tournesol, en contribuant à notre code libre et open source,
en affinant les mathématiques des algorithmes de Tournesol,
ou encore en effectuant des dons à l'Association.

Je vous en remercie profondément d'avance.


