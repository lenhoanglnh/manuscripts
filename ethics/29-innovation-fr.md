# Peut-on innover sans mettre la planète en danger ? (oui*)

Imaginez qu'une nouvelle rumeur sur l'état de santé d'un dirigeant d'une superpuissance se propage.
Vous êtes journalistes, et vous ressentez la pression de parler de cet événement.
Mais les éléments que vous collectez sont à la fois nombreux et peu fiables.
Faut-il communiquer sur les faits nouveaux à votre disposition ?
Ou vaut-il mieux éviter le sujet dont tout le monde parle, 
quitte à faire moins de vues,
mais avec un risque bien moindre d'effectuer des erreurs ?

Si cette situation devient de plus en plus le quotidien des journalistes,
elle révèle toutefois un problème plus fondamental sur le traitement de la nouveauté.
De manière intuitive, plus on cherche le nouveau,
plus on risque de commettre et de valider des erreurs.
Mais à l'inverse, plus on évite l'erreur, 
moins on est capable de s'adapter à la nouveauté, voire de mener l'innovation.

Aujourd'hui, on va voir que cette tension entre nouveauté et fiabilité 
est en fait une thématique fondamentale de la science de l'information,
où elle est connue davantage sous le nom de dilemme "liveness" versus "safety",
que je vous propose de traduire par "innovation" versus "sécurité".
Bon, ce sont des traductions approximatives, mais elles capturent bien la nature du dilemme.  
https://en.wikipedia.org/wiki/Safety_and_liveness_properties

On va voir en particulier un problème très précis,
où l'on a démontré que, de manière formelle, innovation et sécurité sont incompatibles ;
et on verra en quoi le Bitcoin, cette cryptomonnaie devenue célèbre,
sacrifie un peu de sécurité, 
contrairement aux algorithmes qu'a notamment proposé Leslie Lamport,
chercheur en informatique et lauréat du prestigieux prix Turing.

Mais surtout, comme on le verra, 
la tension fondamentale a des conséquences profondes,
non seulement sur la qualité de l'information journalistique ou même scientifique,
mais aussi et surtout sur la sécurité du développement des technologies,
dans un monde où l'innovation est érigée en tant que priorité absolue,
et où la sécurité est une préoccupation très secondaire.
De manière plus générale, la science de l'information nous informe sur un arbitrage fondamental 
qu'il nous faut faire entre le choix de la sécurité et celui de l'innovation.

Ceci étant dit, on verra aussi que, en pratique, 
il y a des subtilités importantes dans cet arbitrage.
En particulier, la sécurité exige aussi énormément d'innovations,
notamment quand le statu quo est désastreux ;
comme c'est le cas en cybersécurité 
ou pour atténuer drastiquement les conséquences dramatiques du changement climatique.


## Sécuriser et innover : mission impossible ?

Imaginez un média qui doit déterminer si un événement a eu lieu dans une zone de guerre.
Pour cela, ses nombreux journalistes, qui collectent des informations disparates,
doivent se coordonner, en s'envoyant des messages.
Supposez que le média a le seuil suivant : 
si le nombre de journalistes confirmant l'événement dépasse ceux qui le contestent,
alors on considère l'événement vrai, et on publie un article à son sujet.

Il y a toutefois deux difficultés.
La première, c'est que les journalistes sont dans des lieux difficiles, 
ont parfois d'autres priorités que confirmer l'information en question,
et le réseau téléphonique passe parfois très mal.
Ainsi, il peut se passer des jours, 
entre le moment où un journaliste veut vous confirmer l'événement,
et le moment où vous recevrez effectivement le message.

La deuxième, c'est que les journalistes sont en premières lignes du conflit,
et il peut leur arriver à tout moment d'être kidnappé. 
Voire pire.
Dès lors, vous pourriez perdre toute nouvelle de ces journalistes.

Quelles procédures faut-il alors suivre pour valider l'information ?

L'exemple que j'ai donné ici est en fait une illustration 
d'un problème plus fondamental de la science de l'information répartie,
appelé le *problème du consensus*.
Formellement, ce problème imagine plusieurs machines 
qui communiquent via un réseau globalement fiable,
mais qui subit régulièrement des délais de réponse imprévisibles et incontrôlés,
et où au moins une machine peut tomber en panne à tout moment.
On parle de réseau asynchrone avec risque de panne.
Est-il alors possible pour les machines fonctionnelles
d'agréger les informations accessibles des différentes autres machines,
et ainsi aboutir à une validation consensuelle de l'information ?

Ce problème a tout à coup pris la lumière des projecteurs,
lorsqu'on s'est rendus compte que sa résolution permettrait de concevoir une monnaie décentralisée, 
comme le Bitcoin.
En effet, l'un des problèmes est l'émission de transactions incompatibles.
Par exemple, si j'ai 100 Bitcoins, 
je pourrais demander à certaines machines de valider le transfert des 100 Bitcoin à Pierre,
et à d'autres machines de valider le transfert des 100 Bitcoin à Jacques.
Clairement, vu que je n'ai que 100 Bitcoins, 
ces deux opérations ne devraient pas être validées toutes les deux.
Mais comment le réseau de machines peut-il valider l'une sans valider l'autre ?

Et bien, ça va peut-être vous surprendre, 
mais le théorème de Fischer, Lynch et Paterson de 1985 prouve que c'est impossible.
Aucun algorithme distribué ne peut garantir la validation consensuelle de l'information
dans un réseau asynchrone avec une panne potentielle.  
https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf

Et, bon, la preuve de ce théorème est très technique,
donc je vais pas en parler dans cette vidéo.
Mais intuitivement, 
c'est parce qu'il y aura toujours des suites d'événements qui repousseront l'indécision,
et après lesquelles il restera impossible pour n'importe quelle machine 
de résoudre les ajouts conflictuels à l'état des faits enregistrés,
en garantissant que cette résolution sera conforme aux résolutions faites par les autres machines.

Mais alors, est-ce que le Bitcoin fonctionne vraiment ?

Eh bien, pour bien répondre à cette question,
il est utile de distinguer deux propriétés différentes d'un algorithme,
à savoir d'un côté sa liveness, que j'ai donc proposé d'appeler "innovation",
et de l'autre sa safety, que j'ai traduit en "sécurité".
Dans notre cas, l'innovation consiste à valider une information ; 
à ajouter une nouvelle information au système.
La sécurité consiste à garantir que l'information validée est bien cohérente avec le système ---
comme par exemple ne pas impliquer une dépense de Bitcoins inexistants,
ou une information en fait largement rejetée par le réseau de journalistes.

Historiquement, c'est en fait davantage la propriété d'innovation 
qui fut sacrifiée par les chercheurs du domaine.
En 1998, Leslie Lamport, qui remportera plus tard le prestigieux Prix Turing,
proposa une solution appelée Paxos qui garantissait la sécurité,
mais qui pouvait ne pas valider les nouveautés ;
des garanties d'innovation peuvent toutefois être fournies pour des réseaux plus fiables,
qui satisfont notamment l'hypothèse d'asynchronie partielle.  
https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf

La Blockchain, cette solution algorithmique derrière le Bitcoin,
a en revanche légèrement sacrifié la sécurité.
En effet, avec le Bitcoin, 
une transaction validée par certaines machines du système peut être plus tard rejetée
par ces mêmes machines,
notamment si l'on observe une grande fourchette dans la liste des transactions acceptées ;
et d'ailleurs, en 2016, 
une autre cryptomonnaie appelée Ethereum a volontairement effectué un "hard fork",
une opération qui consiste à annuler des opérations passées.  
https://en.wikipedia.org/wiki/Ethereum

Je vous renvoie vers la vidéo que j'ai faite à ce sujet pour plus d'informations.  
https://tournesol.app/entities/yt:l9CWjEExtbo

Et ce n'est peut-être finalement pas si anodin que,
même lorsqu'il s'agit de gérer des centaines de milliards de dollars,
beaucoup ont préféré sacrifié la sécurité à l'innovation ---
d'autant que la sécurité de la finance dépend d'un grand nombre de régulations invasives,
auxquelles les cryptomonnaies échappent complètement,
ce qui facilite la fraude, le blanchiment d'argent et les trafics de marchandises illégales.

> Si vous préférez utiliser un numérique plus éthique et responsable,
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


## Freiner l'innovation au nom de la sécurité

Si le théorème d'impossibilité de Fischer, Lynch et Paterson 
n'a bien entendu qu'un champ d'application limité,
la décomposition des propriétés désirables en "sécurité" et "innovation" 
est devenue un standard de la recherche en informatique ---
enfin, surtout dans les domaines de l'informatique où la sécurité n'est pas complètement ignorée !
La sécurité dit en gros "rien de (trop) mauvais ne peut survenir",
alors que l'innovation dit en gros "quelque chose de bien finira par être fait" ;
mais bien sûr le "mauvais" et le "bien" restent à définir, en fonction du problème considéré.

D'ailleurs, l'un des algorithmes au coeur de Tournesol, à savoir l'algorithme Mehestan,
qui a été accepté à publication dans la prestigieuse conférence AISTATS 2024,
arbitre justement la tension entre sécurité et innovation.  
https://arxiv.org/abs/2202.08656

En l'occurence, l'innovation exige grosso modo 
que les scores représentent fidèlement les jugements des contributeurs qui se sont exprimés,
tandis que la sécurité exige que chaque contributeur n'a qu'un faible impact sur les scores Tournesol,
pour éviter la manipulabilité des recommandations Tournesol par une poignée d'acteurs.
Très concrètement, dans le code de Tournesol, 
un paramètre appelé "résilience Lipschitz" effectue l'arbitrage entre innovation et sécurité.

De façon plus terre-à-terre, la sécurité exige de dépenser du temps, de l'énergie et de l'argent
pour évaluer, auditer et décortiquer les systèmes qu'on développe ;
alors que l'innovation consiste à sans cesse remplacer les systèmes existants,
avec souvent peu d'attention aux nombreux dispositifs de sécurité mis en place pour les sécuriser.

Et malheureusement, surtout dans le contexte actuel de courses à la spectacularité des IA,
l'innovation est aujourd'hui beaucoup plus lucrative que la sécurité,
tout en exigeant beaucoup moins de compétences.
Ce n'est d'ailleurs pas un hasard si le motto original de Facebook est "Move fast and break things",
qu'on peut traduire par "innover vite et casser ce qui existe" ;
un archétype d'une posture de dédain envers la sécurité.  

L'informatique n'est d'ailleurs pas le seul champ de nos sociétés 
à avoir basculé vers un excès d'innovation.
En sciences, par exemple, la prime à la nouveauté est immense ;
alors que ceux qui vont vérifier la fiabilité des publications acceptées 
ne gagnent presque aucune valorisation.
Les cas les plus frappants sont bien sûr les cas de fraudes scientifiques,
comme celles de Francesca Gino et Dan Ariely,
qui ont non seulement for fortune, mais aussi obtenu un prestige académique exceptionnel.  
https://tournesol.app/entities/yt:d2Tm3Yx4HWI

Mais même sans en aller jusque là,
tous les chercheurs s'accordent sur la présence d'un énorme biais dans le système académique,
qui favorise les découvertes "statistiquement significatives" et surprenantes,
aux dépens de la fiabilité de la recherche effectuée,
ce qui a conduit à une terrifiante crise de la réplicabilité.  
https://tournesol.app/entities/yt:NOnGn6Bq09o  
En plus du fameux diction "publish or perish" ; qu'on pourrait renommer "innove ou meurt".
Vraiment pas les meilleures instructions pour garantir la fiabilité de l'information...

Et bien entendu, le monde des médias est aussi une victime de l'innovation, 
aux dépens de la sécurité.
Surtout avec Internet, les IA de recommandation offrent une prime majeure à la nouveauté,
ce qui pousse les médias à sans cesse relayer des informations nouvelles,
sans prendre le temps nécessaire pour vérifier la fiabilités de ces nouvelles.

Mais s'il y a un domaine dans lequel la course à l'innovation me paraît terrifiante,
c'est surtout le développement des technologies de l'information, et en particulier des IA.
Et je ne suis pas le seul à trouver que cette course met en danger la sécurité.
Le gouvernement chinois cherche lui aussi à freiner le développement des IA,
en exigeant des développeurs qu'ils montrent la vérité, non seulement de ce que les IA disent,
mais aussi de toutes les données d'entraînement des IA --- une tâche virtuellement impossible !  
https://www.reuters.com/technology/chinas-slow-ai-roll-out-points-its-tech-sectors-new-regulatory-reality-2023-07-12/

De même, Samsung a interdit l'utilisation des algorithmes génératifs par ses employés,  
https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/  
tandis que Microsoft a appelé ses employés à faire attention à l'information fournie à ChatGPT,  
https://www.businessinsider.com/microsoft-tells-employees-not-to-share-sensitive-data-with-chatgpt-2023-1?op=1&r=US&IR=T  
et que Google a appelé les siens à se méfier de l'information fournie par Google Bard.  
https://www.theregister.com/2023/06/19/even_google_warns_its_own/

Et pourtant, malgré toutes ses inquiétudes chez les puissants du monde numérique,
les démocraties échouent encore à protéger la population contre les travers de l'innovation.
Elles autorisent encore, par exemple, 
SnapChat sur les téléphones de millions d'enfants dont beaucoup de moins de 13ans,
alors que de nombreux articles révèlent que son IA banalise la pédophilie auprès de mineurs.   
https://www.washingtonpost.com/technology/2023/03/14/snapchat-myai/

Et il y aurait une solution très simple pour à la fois freiner drastiquement l'innovation,
garantir la légalité des outils du numérique et protéger beaucoup mieux la société :
exiger la présomption de non-conformité.

[Extrait Infrarouge]  
https://www.rts.ch/emissions/infrarouge/13916241-intelligence-artificielle-a-quel-saint-se-vouer.html

À l'heure où l'Europe s'arme légalement, 
avec notamment l'AI Act, le Cyber Resilience Act et le Digital Services Act,
le grand défi restera la mise en application des lois,
pour non seulement protéger la population, 
mais aussi les entreprises clientes de technologies très mal sécurisées.  
https://hal.science/hal-03605110/document

Vouloir ralentir l'intégration précipitée des intelligences artificielles 
est même une position majoritaire dans la population américaine,
d'après un sondage du Artificial Intelligence Policy Institute.
En fait, même parmi les 21% d'enthousiastes de l'IA du sondage,
la majorité ne souhaite pas accélérer leur développement,
puisqu'ils sont au total que 8% a vouloir cette accélération.
https://theaipi.org/poll-shows-overwhelming-concern-about-risks-from-ai-as-new-institute-launches-to-understand-public-opinion-and-advocate-for-responsible-ai-policies/

Même son de cloche chez les experts, 
en tout cas chez ceux qui ne gagnent pas des millions grâce à ce développement précipité.  
https://futureoflife.org/open-letter/pause-giant-ai-experiments/  
https://www.forbes.com/sites/nicolesilver/2023/06/06/artificial-intelligence-regulation-why-experts-are-calling-for-slowing-down-ai-ai-series-4-of-5/

En particulier, il est urgent d'exiger, légalement ou contractuellement, 
que les produits commercialisés respectent des standards,
comme ceux décrits par le National Institute of Standard of Technology, ou NIST,
dans son rapport sur la sécurité du machine learning publié en janvier 2024.  
https://csrc.nist.gov/pubs/ai/100/2/e2023/final

D'ailleurs, un truc chouette dans ce rapport,
c'est que 5 des 9 articles listés comme étant l'état de l'art des solutions
de sécurisation des algorithmes contre les attaques par empoisonnement,
qui représentent la plus grande menace industrielle selon les praticiens,
sont des articles publiés par des co-fondateurs de mon entreprise Calicarpa,
qui peut proposer à vos organisations du conseil en IA et en sécurité de l'IA.  
https://www.calicarpa.com/

Jusque là, toutefois, beaucoup de gouvernements valorisent encore davantage l'innovation,
voire l'urgence à accélérer dans la digitalisation et l'adoption de produits étrangers,
et ignorent, volontairement ou non, les nombreux problèmes de cybersécurité 
que l'innovation effrénée implique inéluctablement.  
https://www.lemonde.fr/sciences/article/2024/02/13/intelligences-artificielles-les-mille-et-une-facons-de-les-faire-derailler_6216264_1650684.html

En fait, à l'instar du changement climatique, 
l'une des principles pistes pour améliorer radicalement la sécurité numérique est la sobriété.
Comme tous les experts vous le diront, 
chaque ajout de fonctionnalités à un système d'information augmente sa surface d'attaque,
c'est-à-dire le nombre de possibilités pour les attaquants de compromettre les systèmes d'information.

Un exemple particulièrement clair de sobriété numérique 
est la recommandation d'un comité de 14 chercheurs en cybersécurité 
sur le futur du vote aux États-Unis.
Je cite :

"À ce jour, Internet (ou n'importe quel réseau connecté à Internet) ne devrait pas être utilisé
pour l'envoi de bulletins de vote remplis.
De plus, le vote par Internet ne devrait pas être utilisé dans le futur,
jusqu'au jour où, si ce jour arrive, des garanties très robustes de sécurité et de vérifiabilité
sont développées et mises en place,
sachant qu'aucune technologie connue ne garantit le secret, la sécurité et la vérifiabilité
d'un bulletin rempli transmis via Internet."

> At the present time, the Internet (or any network connected to the Internet) 
> should not be used for the return of marked ballots. 
> Further, Internet voting should not be used in the future 
> until and unless very robust guarantees of security and verifiability are developed and in place, 
> as no known technology guarantees the secrecy, security, and verifiability 
> of a marked ballot transmitted over the Internet.  
> https://nap.nationalacademies.org/catalog/25120/securing-the-vote-protecting-american-democracy

Voilà un jugement extrêmement radical, mais aussi extrêmement bien informé.
Et ce ne sont pas les exemples récents de spywares surpuissants comme Pegasus ou Predator,
capables d'infiltrer et de prendre le contrôle de nombreux téléphones,
qui vont pousser ces chercheurs à réviser leur jugement.
Voter avec des appareils potentiellement hackés,
c'est encourir le risque que des élections présidentielles soient complètement manipulées
par des logiciels malveillants contrôlés par des puissances autoritaires.

Et sachant les profits monumentaux du réseau tentaculaire du cybercrime ---
on parle de dizaines de milliers de milliards de dollars par an ---  
https://www.weforum.org/agenda/2023/06/cyber-insurance-security-cybercrime/  
il faut s'attendre à ce que les journalistes dissidents ne soient pas les seules cibles
de ces spywares ;
pour peu que votre entreprise a un chiffre d'affaire supérieur au millier d'euros,
elle est une cible qui intéressera bien au moins quelqu'un dans ce marché noir.

Bref. Si vous voulez vous protéger des vols de données, des vols de mots de passe, 
des vols d'accès à vos réseaux sociaux, à vos emails et à vos banques,
réduisez drastiquement le nombre d'applications que vous avez sur vos téléphones
et les informations sensibles que vous partagez sur Slack ou WhatsApp,
ainsi que le nombre d'extensions que vous avez dans vos navigateurs web
ou dans vos IDE comme Microsoft VS Code,
surtout sur vos machines de travail professionnel.
Plus généralement, limitez votre confiance en les appareils numériques que vous utilisez.
Ces machines pourraient en fait être devenus des espions d'une puissance étrangère.
Faites très attention aux secrets que vous partagez avec elles.


## Les "boules noires"

Alors, jusque là, j'ai donné l'impression que la quête effrénée de l'innovation allait
à l'encontre de notre sécurité et de la sécurité de nos civilisations.
C'est d'une certaine manière l'argument défendu par Nick Bostrom,
dans son article terrifiant sur l'hypothèse du monde vulnérable,
et dont Monsieur Phi a dédié une excellente vidéo,
qui est dans le top de tous les temps sur Tournesol.  
https://tournesol.app/entities/yt:GuTgfnkILGs

À chaque fois qu'on innove,
on extrait d'une urne imaginaire des innovations une boule,
sans connaître au préalable la couleur de cette boule ;
or il n'y a pas de raison de penser que l'urne ne contient que des boules de la bonne couleur.
Certaines boules pourraient être "noires",
c'est-à-dire des boules très dangereuses pour l'humanité ;
du type bombe nucléaire facilement constructible, 
nouvelles ressources fossiles ultra-efficaces et ultra-polluantes, 
kit de créations de pandémie, ou encore IA incontrôlables.

Bon j'ai un peu envie de dire que l'IA incontrôlable, on y est déjà très largement...
En tout cas si on parle d'IA démocratiquement incontrôlable.  
https://tournesol.app/entities/yt:lYXQvHhfKuM

Mais du coup, plus on tire rapidement de nouvelles boules de l'urne,
ce qui grâce au progrès technologique, est de plus en plus le cas,
plus la probabilité de tirer une boule noire est grande.
En accélérant l'innovation, l'humanité court en fait probablement à sa propre perte.

D'autant que les conditions géopolitiques nécessaires pour protéger l'humanité 
malgré le tirage d'une boule noire sont extrêmement distantes du contexte actuel ;
en pratique, aujourd'hui, on vit dans un monde qui se radicalise, 
avec une haine qui se généralise entre différentes communautés à travers le monde,
une montée de l'autoritarisme et des investissements militaires,
des nouveaux bombardements massifs dans une nouvelle région du monde tous les ans,
et un déclin drastique des démocraties un peu partout, gangrénées par la corruption et le populisme.  
https://www.idea.int/gsod/2023/chapters/global/

Bref. Vraiment pas les conditions géopolitiques optimales pour la découverte
d'une nouvelle arme de destruction massive,
comme une cyber attaque ou une arme nucléaire pas chère.
Dans ce contexte, l'innovation dans certains domaines paraît complètement immorale.
Si le succès d'un domaine réduit drastiquement les coûts de l'enrichissement nucléaire,
ou la faculté à casser le chiffrement sur lequel repose la sécurité des banques et des assurances,
sûrement, il ne faudrait pas vouloir innover dans ce domaine... non ?

Eh bien, aussi effrayant que cela puisse paraître, 
ces réflexions de base de l'impact social de l'innovation sont absentes 
chez énormément d'entrepreneurs, de développeurs et de chercheurs, y compris académiques.
Comme en parle Mr. Phi dans sa vidéo, en Australie, l'entreprise Silex Systems
continue d'investir massivement pour trouver des nouvelles techniques d'enrichissement nucléaire,
et a connu même un gain drastique de son évaluation boursière depuis la guerre en Ukraine.  
https://www.silex.com.au/  
https://www.asx.com.au/markets/company/slx

Et par ailleurs, y compris en France, la recherche publique investit massivement
dans la conception des ordinateurs quantiques,
dont on sait que la principale faculté nouvelle est la capacité à casser la cybersécurité classique,
sur laquelle reposent tant de banques et d'assurances ;
et on donne régulièrement la parole à des chercheurs célébrés qui vantent ces axes de recherche !
Autrement dit, on célèbre ce qui accélère des armes de destruction massives,
qui seront réutilisables par n'importe quelle puissance étatique qui voudrait s'en équiper.

Mais donc, l'innovation est-elle vouée à sacrifier la sécurité de nos sociétés ?


## La bonne et la mauvaise innovation

En pratique, il y a plutôt de nombreuses urnes,
avec différents chercheurs et entrepreneurs qui tirent des boules dans ces différentes urnes.
Et plutôt que d'encourager ces derniers 
à tirer des boules dans l'urne "enrichissement LASER d'uranium",
ou dans l'urne "ordinateur quantique capable de détruire les systèmes d'information mondiaux",
on pourrait envisager de les encourager à tirer dans l'urne
"détection des usines d'enrichissement d'uranium" 
ou dans l'urne "cybersécurité postquantique",
ou encore dans les urnes "efficacité énergétique" et 
"outil de gouvernance démocratique de l'information" ?

Et si, plutôt que célébrer l'innovation aveugle, ou l'innovation pour l'innovation,
on encourageait explicitement et on célébrait l'innovation 
pour protéger les démocraties et les populations ?

La réponse positive à ces questions est ce que Bostrom appelle 
le *principe de développement différentiel*.
Et à bien y réfléchir, ça paraît être une évidence.
Plutôt que de faire de la science pour la science,
ou pire encore, de la science pour l'argent comme c'est malheureusement trop souvent le cas,
notamment via les partenariats publics-privés,
et si on faisait de la science et de l'ingénierie pour protéger la société ?

C'est typiquement ce que s'acharnent à faire les chercheurs et les entreprises en cybersécurité,
qui identifient des failles dans les produits existants 
et proposent des mises à jour pour davantage les sécuriser.
D'ailleurs, j'en profite pour vous rappeler un conseil de base de cybersécurité :
mettez à jour vos logiciels dès qu'on vous en propose une.
L'innovation en cybersécurité peut vous éviter d'énormes ennuis.

C'est pour cela que les discours technophobes simplistes sont ainsi très problématiques,
à l'instar de celui d'Aurélien Barrau,
qui accusent les étudiants de CentraleSupélec d'être le problème,
sont en fait extrêmement gênant.  

> Vous n'êtes pas la solution. Vous êtes le problème.
https://www.youtube.com/watch?v=r9vrU9g893o (5:31)  

Dans le cas particulier du problème environnemental,
la plupart des chercheurs et des entrepreneurs sont en fait extrêmement sensibilisés aux risques,
et ont du coup énormément oeuvré pour réduire drastiquement 
l'impact environnemental de nombreux produits encore indispensables 
pour la plupart de nos concitoyens,
comme le logement, le transport et l'alimentation,
de sorte que l'empreinte carbone d'un Français aujourd'hui a chuté 
par rapport à ce qu'elle était il y a un demi-siècle ---
et si la sobriété aide, elle est en fait loin d'en être la principale cause !  
https://ourworldindata.org/co2/country/france  
https://fr.wikipedia.org/wiki/D%C3%A9couplage_(%C3%A9cologie)#/media/Fichier:Absolute-decoupling-Growth-and-falling-emissions-all.png

Bien entendu, l'innovation seule ne nous sauvera pas.
Même en pariant sur d'énormes progrès technologiques, 
les scénarios du GIEC sont très préoccupants.
Cependant, dans le scénario contrafactuel où tout progrès technologique est interrompu,
même en imaginant par un coup de baguette magique une adoption massive d'une sobriété radicale,
la dépendance aux énergies fossiles persistera, 
avec toutes sortes de conséquences dramatiques qui pourraient aller jusqu'à un retour dans le passé,
qui, comme le disent les livres d'histoire,
est rempli de famines, de maladies et de guerres.  
https://tournesol.app/entities/yt:jbkSRLYSojo  
https://tournesol.app/entities/yt:Sm5xF-UYgdg

Malheureusement, en science de l'information, 
jusque là et contrairement aux sciences environnementales, 
nos instances dirigeantes,nos fonds de financement de la recherche, 
notre système académique et nos universités 
ne priorisent pas la recherche de solutions de résilience numérique pour nos sociétés.
Il est encore bien plus facile de trouver un job académique aujourd'hui,
ou plus simplement d'avoir un article de recherche accepté,
si l'on s'intéresse à l'innovation dans des IA sans aucune considération de sécurité,
que si l'on démontre l'impossibilité d'allier innovation et sécurité,
ou si l'on s'intéresse au sujet extrêmement peu lucratif de la gouvernance algorithmique.

D'ailleurs, même avant que je ne quitte l'École Polytechnique Fédérale de Lausanne en Suisse,
des ressources humaines de la ressource allouées à sécuriser la gouvernance algorithmique,
sur laquelle je travaillais,
ont été subitement réaffectées à un projet... de cryptomonnaie.
Est-ce vraiment un tel projet qui va protéger nos sociétés contre les fléaux
de la concentration de richesse, du blanchiment d'argent, de l'évasion fiscale,
de la volatilité financière, du cybercrime ou encore de la corruption ?
Et surtout, est-il moralement justiablement de détourner des moyens de recherche
sur l'éthique des algorithmes vers cet autre projet ?

Ceci étant dit, même si certaines tendances sont désespérantes,
d'autres vont carrément dans le bon sens.
À l'échelle individuelle, au moins, 
de plus en plus de chercheurs parmi vous qui regardez Science4All s'intéressent à Tournesol, 
notre projet d'innovation dans la gouvernance algorithmique sécurisée,
et je suis très fier de pouvoir dire que plusieurs collaborations avec plusieurs laboratoires différents,
y compris avec des chercheurs du MIT, du CNRS et de l'EPFL,
sont en cours, avec déjà des publications acceptées 
notamment dernièrement à la prestigieuse conférence AAAI 2024.  
https://arxiv.org/abs/2308.08644

Et tout ça, c'est aussi beaucoup grâce à tous ceux parmi vous 
qui effectuez des contributions sur Tournesol,
que ce soit via des jugements de recommandabilité comparative de différents contenus,
via de la promotion de Tournesol auprès de vos proches et sur les réseaux sociaux,
ou via des dons financiers absolument critiques pour nous permettre de conserver les services
de notre excellent développeur et unique employé.
Vos contributions nous aident à fédérer une communauté de chercheurs autour d'un projet éthique,
et à piocher des boules, non seulement très certainement blanches,
mais même probablement blanchissantes,
qui aideront ainsi à nous protéger contre les boules noires 
que d'autres chercheurs ne manqueront pas de tirer.

Du fond du coeur et au nom de toute l'équipe de Tournesol, 
je vous en remercie profondément.

