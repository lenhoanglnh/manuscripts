# Les mathématiques de l'argument d'autorité #DébattonsMieux

Si une autorité vous dit de la croire, 
faut-il ignorer tout ce que vous pensiez et adhérer entièrement à ce qu'elle dit ?

Concrètement, imaginez que vous pariez à 40% 
que Kamala Harris battra Donald Trump 
et deviendra la prochaine Présidente des États-Unis ?
Mais imaginez qu'un de vos amis a beaucoup plus suivi l'actualité 
l'élection présidentielle américaine,
et qu'il vous dit que, selon lui, cette probabilité est 60%,
sans aucune justification.
Que devez-vous maintenant croire ?

Aujourd'hui, on va voir les réponses que nous fournit le bayésianisme,
et voir les conséquences non seulement sur le degré de validité de l'argument d'autorité,
mais aussi sur ce à quoi ressemblerait un débat entre des individus rationnels.
Spoiler alert, ces individus, en tout cas s'ils sont bayésiens,
ont une manière extrêmement étrange de débattre,
qui devraient beaucoup nous informer sur la manière dont nous devrions débattre.


## Le théorème de l'argument d'autorité

Commençons par un théorème bayésien.

Théorème : 
Si vous êtes bayésien,
si vous supposez qu'une autorité a eu accès aux mêmes données que vous et à plus encore,
si vous êtes sûr que l'autorité parle de manière honnête,
si vous pensez qu'une autorité est aussi bayésienne avec le même a priori que vous,
alors vous devez croire tout ce que l'autorité dit.

Autrement dit, l'argument d'autorité est un théorème.
Il dit que, si vous voulez être rationnels au sens du bayésianisme,
et si une autorité que vous jugez strictement plus informée que vous,
si vous pensez qu'elle est honnête,
et si vous pensez que l'autorité est bayésienne,
alors il vous faut croire pleinement tout ce qu'elle vous raconte.

Alors bien sûr, il faut supposer que l'autorité est plus informée que vous,
ce qui nécessite un peu d'humilité épistémique.
Mais bon, je suis sûr que même les plus prétentieux parmi vous
reconnaîtrez qu'il existe au moins certains sujets à propos desquels
il existe des personnes bien plus informées que vous.
Allez... Avouez...

La deuxième hypothèse peut être plus questionnable.
Clairement, certaines autorités ne devraient pas être supposées complètement et toujours honnêtes,
notamment quand elles sont connues pour être mêlées à des affaires de corruption,
ou lorsqu'elles ont des conflits d'intérêt évidents.
Cependant, autour de vous, j'imagine qu'il y a tout de même des personnes,
que vous jugez être honnêtes avec vous,
au moins à propos de certains sujets.

Enfin, la troisième hypothèse est clairement la plus douteuse.
Il vous faut supposer que l'autorité raisonne correctement,
ou plus exactement qu'elle se conforme aux lois des probabilités.
Ou, au moins, que sa conclusion est approximativement celle des lois des probabilités.
En général, ce ne sera pas le cas ;
après tout, le bayésianisme requiert des calculs déraisonnables,
qui sont clairement inaccessibles à nos crétins de cerveaux de primates.
Cependant, ne nous sous-estimons pas complètement.
Quand les données sont suffisamment univoques,
nous sommes tout à fait capables d'aboutir à des conclusions similaires à celle du bayésien.
Même les physiciens parmi nous !

Bref. Les hypothèses du théorème de l'argument d'autorité sont loin
d'être valides dans tous les cas où une autorité s'exprime.
Cependant, il semble bel et bien qu'il y a des cas,
et même qu'il arrive souvent,
que nous parlions à des personnes de notre entourage
dont il est raisonnable de penser qu'elles sont plus informées sur un sujet donné,
qu'elles sont honnêtes quand elles en parlent,
et que leurs conclusions sont approximativement celles du bayésianisme.

Et bien, dans ce cas, selon le bayésianisme,
l'argument d'autorité est valide :
il vous faut au moins approximativement croire ces personnes à propos de ce sujet donné,
même avant que celles-ci ne vous fournissent une quelconque explication.

Pensez-y, la prochaine fois que vous parlerez à un statisticien, 
un défenseur des droits humains,
un guide de montagne ou un plombier de confiance.
Ou lorsqu'un ami bien plus informé que vous affirme 
que la probabilité de victoire de Kamala Harris est de 60%.

> En parlant d'actualités, 
> vous avez peut-être vu l'été dernier l'importance de la cybersécurité
> suite notamment à la panne majeure provoquée par une faille de CrowdStrike.
> Et si vous êtes un peu pointus, 
> vous avez peut-être même vu que Microsoft a été l'objet 
> (d'une faille moins spectaculaire, mais bien plus grave encore)[[https://www.theregister.com/2024/08/14/august_patch_tuesday_ipv6/]]. 
> Si vous ou votre entreprise sentez l'urgence à développer un numérique plus responsable, 
> je vous invite en particulier à vous intéresser à Infomaniak.
> À l'heure où les systèmes d'information sont trop souvent outsourcés à des tiers 
> qui exploitent vos données et les données de vos entreprises pour entraîner des algorithmes génératifs, 
> il est devenu urgent de considérer que Slack, Google Docs ou autre Microsoft Teams sont des spywares en puissance. 
> A contrario, Infomaniak fait un effort majeur pour tout développer de manière souveraine, 
> avec des collaborateurs uniquement en Suisse, un pays beaucoup plus digne de confiance, 
> notamment par opposition aux entreprises américaines soumises au Patriot Act. 
> Vous pouvez profitez gratuitement des services Mail et SwissTransfer d'Infomaniak, 
> et je vous recommande aussi vivement leurs services Web, kMeet ou encore kDrive. 
> Pour chaque vidéo où je les promeus, ce que je fais avec grand plaisir, 
> Infomaniak reverse un don à l'Association Tournesol. 
> Merci beaucoup à eux pour ce partenariat.


## La démonstration

Rappelons le théorème bayésien de l'argument d'autorité.

Théorème : 
Si vous êtes bayésien,
si vous supposez qu'une autorité a eu accès aux mêmes données que vous et à plus encore,
si vous êtes sûr que l'autorité parle de manière honnête,
si vous pensez qu'une autorité est aussi bayésienne avec le même a priori que vous,
alors vous devez croire tout ce que l'autorité dit.

Comment peut-on démontrer cela ?
Une approche la plus classique consiste à modéliser votre connaissance
par un ensemble Omega d'états possible du monde.
Chaque état décrit très précisément tout ce qu'il se passe, et se passera dans le monde.
Ainsi, il n'y a pas juste un état où Harris gagne l'élection présidentielle 2024.
Il y en a énormément.
Dans certains, elle gagne très largement, dans d'autres elle gagne de très peu,
dans d'autres encore personne ne gagne à cause d'une guerre civile,
et dans d'autres encore, Trump se retire de la course avant même l'élection,
et appelle tous ses électeurs à en faire de même pour calmer les tensions nationales,
et protéger avant tout l'intégrité du pays.

Bon, je suis pas sûr de mettre une grande probabilité à cet état du monde...
Justement, a priori,
vous devez assigner à chaque état omega du monde une probabilité p(omega).
Les lois des probabilités imposent alors que la somme des p(omega) doit être égale à 1.
Maintenant, les données D auxquelles vous avez eu accès
vous permettent d'exclure tous les états omega incompatibles avec ces données.
Typiquement, les états omega où Harris ne se présente pas car Biden reste le candidat
ont été exclus de mon ensemble Omega sachant D des états encore plausibles.

Dans cet espace réduit Omega sachant D,
la probabilité de chaque état doit rester la même que dans l'a priori,
à une normalisation multiplicative près introduite pour garantir 
que la somme des probabilités dans Omega sachant D soit bien une loi des probabilités.
Autrement dit, il faut que la somme des p(omega sachant D) soit égale à 1.
Et ça, pour le garantir, il suffit de définir
p(omega sachant D) = p(omega) divisé par la somme des p(omega') pour les omega' compatibles avec D.
Notez que ça peut se réécrire
p(omega sachant D) = p(omega) / p(D),
ou encore
p(omega sachant D) = p(D sachant omega) p(omega) / p(D),
qui n'est autre que la formule de Bayes.

OK. Maintenant, imaginons les calculs de l'autorité.
Celle-ci a accès non seulement à vos données D, mais aussi à d'autres données Delta.
Ceci lui permet de supprimer davantage d'états plausibles,
et ainsi réduire l'espace des états possibles du monde.
Son espace Omega sachant D et Delta est beaucoup plus petit.

Mais vous, vous ne connaissez pas ce Delta.
Vous pouvez simplement imaginez un grand nombre de Delta possibles,
ou même plus précisément tous les sous-ensembles d'états possibles selon l'autorité.
Selon un Delta, l'autorité a cet a posteriori sur les états possibles.
Selon un autre Delta, l'autorité a cet autre a posteriori.

Imaginez maintenant que l'autorité est honnête,
et vous dit que selon elle, 
la probabilité de l'élection de Harris est 60%.
Quel est son a posteriori ? À quoi ressemble son espace Omega sachant D et Delta ?
Difficile à dire.
Après tout, il y a plusieurs manières d'exclure des états pour que,
lorsqu'on prend ensuite la probabilité de l'élection de Harris
dans l'espace ainsi réduit,
on obtient 60%.

Eh bien, nul besoin de trancher.
Ce dont vous pouvez être sûr, si l'autorité est bien bayésienne,
c'est que son espace Omega sachant D et Delta est 
l'un des nombreux espaces où la probabilité de l'élection de Harris est 60%.
Mieux encore, en appliquant les lois des probabilités,
vous assignez différentes probabilités à ces différents espaces.
Mais, toujours selon les lois des probabilités,
si vous voulez estimer quoi que ce soit,
il vous faut prendre la moyenne des estimations dans les différents espaces.

Et du coup, quand il s'agit d'estimer la probabilité de l'élection de Harris,
vous devez prendre la moyenne d'estimations, qui sont toutes égales à 60%.
Cette moyenne est forcément égale à 60%.
Autrement dit, a posteriori, votre crédence en l'élection de Harris est de 60%,
même si l'autorité ne vous a rien dit de plus sur la manière dont elle est arrivée à ce résultat.


## Le débat bayésien

S'il est parfois raisonnable de penser 
que l'autorité est bien plus informée que nous,
en pratique toutefois, dans la plupart des débats,
vous avez certaines informations auxquelles votre interlocuteur n'a pas accès,
et vice-versa.
Comment deux bayésiens avec des données distinctes débattraient ?

En 1982, John Geanakoplos et Heraklis Polemarchakis ont démontré 
qu'une étrange manière de débattre de la probabilité d'élection d'Harris
garantit à nos deux bayésiens d'aboutir inéluctablement 
à une conclusion commune :
il suffit à chacun de dire chacun à son tour la probabilité
qu'il assigne à cet événement.

A priori, on pourrait se dire que c'est idiot.
Est-ce que ça ne serait pas mieux pour eux de dire quels états du monde
leurs données respectives permettent d'exclure ?
Et surtout, est-ce que les bayésiens peuvent vraiment améliorer
leurs représentations mutuelles de l'état du monde,
juste en parlant de la probabilité d'élection d'Harris ?

Eh bien, ça peut paraître étrange, mais oui.
Et si c'est le cas, c'est grâce à un raisonnement,
non seulement sur la probabilité d'élection d'Harris,
mais surtout sur la manière dont l'interlocuteur estime cette probabilité d'élection.
Autrement dit, la clé pour avoir un débat vraiment bayésien,
c'est de beaucoup réfléchir à ce à quoi l'autre pense.

En théorie des jeux, notamment suite aux travaux du père des jeux bayésiens,
le prix Nobel d'économie John Harsanyi,
on parle de croyances d'ordre supérieur.
Ainsi, la croyance d'ordre un, c'est ce qu'on pense de l'élection d'Harris.
La croyance d'ordre deux, c'est qu'on croit à propos de la pensée de l'autre
au sujet de l'élection d'Harris.

Friends: So they know you know, and they don't know Rachel knows

La croyance d'ordre trois, c'est ce qu'on envisage
à propos de la croyance d'autrui
sur notre réflexion au sujet de l'élection d'Harris.

Friends: They don't know that we know that they know.

Et puis, ensuite, il y a la croyance d'ordre quatre,
sur ce qu'on croit de la croyance d'autrui sur ce qu'on croit qu'autrui croit.

Friends: They don't know that we know that they know that we know.

Et oui, ça peut aller très loin ainsi...

Et justement, imaginons Alice et Bob, qui débattent de l'élection de Kamala Harris,
avec ce genre de raisonnements d'ordre supérieur.
Lorsqu'Alice dit 40%, Bob doit se demander quelles données ont pu pousser Alice à dire 40%.
Voilà qui le pousse à supprimer des états possibles du monde.
Mais bien sûr, comme Bob pense avoir des données qu'Alice n'a probablement pas,
il va persister à avoir un biais par rapport à Alice.
Imaginons que ce raisonnement le pousse à dire 60%.

Alice doit alors tenir compte, 
non seulement du fait que les données de Bob l'ont poussé à avoir visiblement
une prédiction supérieure à la sienne,
mais aussi du fait que si Bob persiste à penser 60%,
après avoir tenu compte du fait qu'Alice a dit évaluer à 40% la probabilité d'élection d'Harris.
Voilà qui suggère clairement que Bob a des données très fiables 
pour en arriver à une conclusion aussi distincte de celle d'Alice ;
et qui force donc Alice à modifier ses croyances.
Mais Alice peut néanmoins estimer que, 
dans ce raisonnement Bob sous-estime la fiabilité des données d'Alice ;
autrement dit Alice peut persister à penser que Bob pense incorrectement la pensée d'Alice.
Voilà qui pourrait la pousser à répondre 50%.

Mais maintenant Bob doit conclure qu'Alice pense que Bob pense incorrectement la pensée d'Alice ;
et en particulier Bob doit se dire que les données d'Alice sont plus solides que ce qu'il croyait.
On peut même imaginer que Bob se dise qu'Alice sous-estime même peut-être
à quel point Bob pense incorrectement la pensée d'Alice,
ce qui peut le pousser à penser qu'Alice a davantage raison que lui,
et à répondre 48%.
Et Alice va alors effectuer un raisonnement sur ce qu'elle pense
que Bob pense qu'elle pense sur ce qu'il pense sur sa pensée,
et ainsi de suite.

C'est ce que l'excellente Julia Galef explique excellement dans cette vidéo :
https://tournesol.app/entities/yt:HxUxlVijZQw  

Et dans ette autre vidéo, 
Julia Galef insiste sur le danger de la phrase 
"je ne comprends pas comment on peut croire X".
Plus qu'un aveu d'ignorance,
ce genre de phrases incite surtout à renoncer à l'effort
de réflexion sur les croyances d'ordre supérieure,
pourtant indispensable pour extraire un maximum d'information des interlocuteurs,
et pour déterminer comment échanger au mieux avec eux.  
https://tournesol.app/entities/yt:chALQCm9VgE

A contrario,
de manière remarquable, Geanakoplos et Polemarchakis ont démontré que,
si l'ensemble des possibles est fini,
et si Alice et Bob sont bien bayésiens et effectuent ces raisonnements 
sur les croyances probables des autres,
alors Alice et Bob finiront par dire exactement la même probabilité.
Dès lors leurs estimations postérieures 
sur la probabilité d'élection d'Harris seront les mêmes,
et elle sera bien entendu celles qu'ils affirment publiquement.

Et leur démonstration est très simple :
juste après qu'Alice a donné son estimation,
elle s'attend à ce que Bob a la même estimation qu'elle.
Techniquement, c'est parce que l'a priori est nécessairement l'espérance du postérieur.
Quoi qu'il en soit, si Bob exprime un désaccord,
alors Alice sera néécessairement surprise par cela,
ce qui la forcera à réviser ses croyances ;
et en particulier à supprimer certains états du monde qu'elle pensait encore plausibles.

Dans un cadre plus général,
Scott Aaronson a même démontré que, pour toute erreur epsilon, delta > 0,
après 257 / (delta * epsilon^2) échanges,
et avec une probabilité au moins 1-delta,
les postérieurs d'Alice et Bob diffèreront d'au plus epsilon.  
https://www.scottaaronson.com/papers/agree-econ.pdf

Autrement dit, il suffira d'environ 257 000 échanges pour que,
avec une probabilité au moins 90%,
l'erreur de prédiction entre Alice et Bob soit au plus de 10%.

Bon, ça reste de très longs échanges, 
avec des calculs bayésiens complexes entre chaque échange.
Mais ce que je trouve fascinant dans ce que ce théorème suggère,
c'est que nos débats pourraient être plus informatifs,
si nous faisions nous aussi l'effort intellectuel 
d'intégrer dans nos raisonnements des croyances d'ordre supérieur.

Friends: They don't know that we know that they know that we know.

En particulier, quand une personne vous dit quelque chose qui contredit vos croyances,
quelles sont les raisons pour lesquelles elle en est venu à sa conclusion ?
Cette personne a-t-elle accès à des informations pertinentes et fiables ?
A-t-elle des conflits d'intérêts et des motivations autres 
que le partage honnête de ses croyances ?
Et enfin, son raisonnement a-t-il des chances de conduire à des conclusions similaires,
que celles d'une pure bayésienne,
y compris l'intégration de calculs de croyances d'ordre supérieur ?

Voici des réflexions essentielles pour #DébattonsMieux ;
et en particulier, si vous avez la chance de parler 
à des personnes informées, honnêtes et dont le raisonnement coïncide suffisamment
avec les lois des probabilités,
pensez à intégrer correctement les affirmations de ces personnes.
Si elles sont probablement plus informées que vous,
il y a même lieu de la croire pleinement,
quelles que soient vos croyances antérieures.


## Malfaisance

En pratique, il y a de nombreux débats dont les enjeux sont tels
que la probabilité d'une malveillance ne doit pas être négligée.
Dès lors, il est crucial d'intégrer ce risque avant de conclure.
Malheureusement, de nos jours, 
si nous autres humains sommes extrêmement conscients de ce risque,
dès qu'il s'agit de politique, de guerre ou des nombreux autres sujets
mis massivement en avant par les réseaux sociaux,
c'est beaucoup moins le cas des algorithmes conçus 
pour apprendre des données des réseaux sociaux,
que ce soit les algorithmes de langage et d'images,
ou encore les arbitres de l'information du web 
que sont les algorithmes de recommandation.

Analyser correctement des énormes jeux de données,
dont certaines peuvent être fournies de manière malveillantes,
c'est vraiment le coeur de ma recherche 
et des solutions proposées par mon entreprise Calicarpa,
qui ont notamment été massivement citées par le rapport du
National Institute of Standards of Technologies, ou NIST,
sur la sécurité de l'intelligence artificielle.

Certaines de ces solutions sont même déjà intégrées au projet non-lucratif Tournesol,
cette plateforme de gouvernance démocratique des algorithmes de recommandation,
qui se méfie des comptes peu authentifiés et des données qu'ils fournissent,
sans toutefois les ignorer.
Clairement, toute solution de gouvernance du web devra résoudre ce défi majeur.
Malheureusement, les initiatives fondées 
sur la transparence, la démocratie et la sécurité
sont aujourd'hui très mal financées,
ce qui a conduit à un web tantôt chaotique, tantôt féodal.

En particulier, j'ai l'immense regret de vous annoncer que,
faute de moyens suffisants collectés par notre Association Tournesol,
nous avons dû licencié notre excellent et unique employé,
ou plutôt désormais ex-employé,
ce qui va inéluctablement conduire à un ralentissement drastique
du développement d'une démocratie numérique.

Tout n'est pas perdu pour autant.
Cet employé a fourni un travail d'excellente qualité,
qui a permis à la plateforme d'avoir une base de code robuste,
ce qui va permettre aux nombreux bénévoles de l'Association, notamment moi,
de continuer à contribuer au projet sur nos heures perdues.
Mais surtout, notre Association continue à recevoir près de 2000 euros de dons mensuels.
On n'est en fait pas si loin d'une entrée suffisante,
mais le déficit de 2000 euros par mois depuis près de deux ans
a fini par puiser dans toutes nos réserves.

Quoi qu'il en soit, on a encore besoin de vos dons, 
pour payer des factures récurrentes, 
mais aussi et surtout pour espérer ré-embaucher un jour notre ex-employé,
voire pour obtenir d'autres financements.
D'ailleurs, s'il y en a parmi vous qui souhaitent nous y aider,
notamment des chercheurs, des employés de fondations
ou des personnes actives dans l'économie sociale et solidaire,
votre aide sera bien sûr plus que la bienvenue.

Notre espace informationnel est actuellement en très grave danger,
et il nous faut urgemment développer des solutions 
pour démocratiser et sécuriser la gouvernance de l'espace informationnel.
Et pour en arriver à cette conclusion,
j'espère que vous pensez que je fais de mon mieux pour être informé,
que je vous le dis en toute honnêteté,
et que je fais d'énormes efforts pour être 
aussi conforme aux lois des probabilités que possible.

De quoi suffire à vous convaincre ?

