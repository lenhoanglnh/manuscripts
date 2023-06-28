# Le point de vue de Lê Nguyên Hoang

Les algorithmes génératifs sont capables de prouesses spectaculaires.
OpenAI et Midjourney ont permis à des centaines de millions d'utilisateurs
de prendre la mesure de tout ce que ces outils pouvaient leur apporter à l'échelle individuelle.
Rapidement, les blogs et les réseaux sociaux se sont remplis de contenus 
avec des titres comme "9 façons d'améliorer votre productivité avec ChatGPT"
ou "comment utiliser ChatGPT pour gagner beaucoup d'argent".
Derrière cette posture individualiste vis-à-vis des technologies,
se cache cependant une inattention dangereuse 
aux enjeux sociétaux et à la réutilisation de ces outils par des acteurs malveillants.

Or dans le contexte socio-politique actuel du numérique, 
avec des mouvements sociaux qui se répètent dans de nombreux pays,
la prolifération des cyberattaques et le retour de la guerre en Europe,
il faut redouter les effets secondaires négatifs des technologies,
et la manière dont elles peuvent être transformées en cyberarmes.
A delà des avantages individuels, il est urgent de penser
les algorithmes génératifs, et l'intelligence artificielle dans sa généralité,
de manière *adversariale*.

## Appliquer les lois déjà existantes

Les législateurs n'ont pas attendu les algorithmes génératifs pour imposer un cadre légal
à la collecte, au stockage et au traitement automatisé de l'information.
Le règlement général sur la protection des données (RGPD) est ainsi entré en vigueur en 2018,
et régule ces différentes opérations.
En 2022, sa mise en pratique à ainsi conduit à une sanction de 20 millions d'euros à l'encontre de Clearview AI pour collecte et utilisation de données biométriques sans base légale, 
et absence de prise en compte satisfaisante et effective des droits des personnes[^clearview_ai].
Puis, en 2023, ce fut au tour de Meta de recevoir une amende record de 1,2 milliards de dollars,
pour transfert de données d'Européens vers les États-Unis[^meta_rgpd].

[^clearview_ai]: https://www.cnil.fr/fr/reconnaissance-faciale-sanction-de-20-millions-deuros-lencontre-de-clearview-ai
[^meta_rgpd]: https://www.lemonde.fr/pixels/article/2023/05/22/meta-condamne-a-une-amende-record-de-1-2-milliard-d-euros-par-le-regulateur-irlandais-des-donnees-personnelles_6174333_4408996.html

Sachant que Google a reconnu que la moitié des données d'entraînement de PaLM, 
l'un de ses algorithmes génératifs, 
est composée de conversations sur les réseaux sociaux[^palm],
il semble y avoir de quoi fortement douter de la conformité des algorithmes génératifs avec le RGPD.
D'autant que, à maintes reprises, il a été montré que ces algorithmes mémorisent ces données d'entraînement[^memorization]. 
Voilà qui a conduit Samsung à interdire l'utilisation des algorithmes génératifs à une partie de ses employés[^samsung_interdiction], 
après que plusieurs d'entre eux ont révélés des secrets industriels à ChatGPT[^samsung_erreur]. 
Même Microsoft appelle ses employés à faire attention à leur utilisation de cet algorithme génératif[^microsoft_chatgpt], 
tandis que Google demande aux siens de ne pas utiliser le code généré par Google Bard[^google_bard].

[^palm]: https://web.archive.org/web/20230103115317/https://arxiv.org/abs/2204.02311
[^memorization]: [https://www.usenix.org/system/files/sec21-carlini-extracting.pdf](https://www.usenix.org/system/files/sec21-carlini-extracting.pdf), [https://petsymposium.org/popets/2023/popets-2023-0070.pdf](https://petsymposium.org/popets/2023/popets-2023-0070.pdf), [https://arxiv.org/abs/2304.05197](https://arxiv.org/abs/2304.05197)
[^samsung_interdiction]: https://www.lemonde.fr/pixels/article/2023/05/02/samsung-interdit-l-utilisation-de-chatgpt-a-une-partie-de-ses-employes_6171774_4408996.html
[^samsung_erreur]: https://global.techradar.com/fr-fr/news/les-employes-de-samsung-ont-commis-une-grosse-erreur-en-utilisant-chatgpt
[^microsoft_chatgpt]: https://www.businessinsider.com/chatgpt-microsoft-warns-employees-not-to-share-sensitive-data-openai-2023-1?r=US&IR=T
[^google_bard]: https://www.businessinsider.com/chatgpt-microsoft-warns-employees-not-to-share-sensitive-data-openai-2023-1?r=US&IR=T

Au delà du danger évident d'espionnage des dissidents et de la presse, 
qui menace gravement la lutte contre la corruption et les abus de pouvoir,
et au delà des risques pour les secrets industriels et la cybersécurité des clients,
l'enjeu est ici aussi l'application des lois déjà existantes.
Les algorithmes génératifs sont-ils actuellement tolérés malgré leur non-conformité probable avec le RGPD ?
Et si la loi déjà en vigueur ne s'applique pas, 
peut-on faire confiance à l'application des lois futures, 
comme l'AI Act et le Cyber Resilience Act, parmi d'autres ?
En particulier, les appels aux régulations futures ne sont-ils pas 
une façon de dévier l'attention des lois déjà existantes, 
et déjà probablement violées ?

En fait, ce que le cas des algorithmes génératifs révèle surtout, 
c'est l'inadéquation des dispositifs mis en place pour faire appliquer les lois existantes.
Les entreprises privées se sont ainsi permises de déployer massivement des technologies intrusives,
et empêchent les parties civiles de démontrer leur non-conformité,
simplement en rendant extrêmement opaques la conception de ces technologies.
Tant que des moyens conséquents ne seront pas mis en oeuvre 
pour faire appliquer les lois existantes,
le numérique restera un lieu de non-droit,
c'est-à-dire un espace où le droit ne s'applique pas.
En particulier, pour espérer rétablir les droits humains,
il semble urgent d'adopter la *présomption de non-conformité*,
qui exige des concepteurs qu'ils démontrent la conformité de leurs produits
pour obtenir le droit de commercialisation,
comme cela est le cas dans les industries matures 
comme l'aviation, la pharmaceutique et l'agroalimentaire.

## Dépendance et sobriété numérique

La régulation des algorithmes est cependant souvent brandie comme un épouvantail,
qui freinera l'émergence de grandes entreprises numériques européennes.
Si cette critique a clairement ses propres limites 
(une entreprise européenne est-elle vraiment plus digne de confiance, 
si elle est par conception hors de tout contrôle démocratique ?),
elle soulève toutefois le problème plus établi de la dépendance numérique.
En particulier, il est urgent de considérer que les fournisseurs de services informatiques
peuvent un jour devenir des menaces dangereuses pour leurs clients.
Or, la plupart des entreprises européennes sont déjà extrêmement dépendantes 
des services informatiques de Google, Microsoft ou Amazon, parmi d'autres.
Si ces entreprises cessent leur activité sur le territoire européen, 
parce qu'elles ont subi une cyberattaque
ou parce que le gouvernement américain l'exige pour faire pression sur l'Europe,
alors la survie de tout le tissu économique européen sera menacée.

Pire encore, des solutions numériques émergentes viennent de pays autoritaires,
à l'instar du modèle de langue Falcon conçu par l'entreprise Émirati *Technology Institute Innovation* (TII), 
et néanmoins promue par Hugging Face[^hugging_face_falcon].
Dès lors, la dépendance numérique devient un enjeu de géopolitique
et de droits humains,
d'autant que ces pays autoritaires sont souvent eux-mêmes connus
pour leur participation active à l'énorme marché du cybercrime[^perlroth],
dont le budget total était estimé à 6000 milliards de dollars par an en 2021[^cybercrime_senat].
Rappelons ainsi que, le Parti Communiste Chinois a interrompu un contrat avec Alibaba,
parce que des chercheurs d'Alibaba ont rapporté la vulnérabilité critique log4j à Oracle,
plutôt que de d'abord la partager avec les autorités chinoises[^log4j].
Si ces chercheurs avaient collaboré avec ces autorités,
de nombreuses infrastructures de nombreuses entreprises auraient été facilement hackées
par le cybercrime chinois.

[^hugging_face_falcon]: https://huggingface.co/blog/falcon
[^perlroth]: https://thisishowtheytellmetheworldends.com
[^cybercrime_senat]: https://www.senat.fr/rap/r20-678/r20-6780.html
[^log4j]: https://cybernews.com/news/log4j-saga-china-suspends-deal-with-alibaba-cloud-over-log4j-reporting/

En fait, les experts en cybersécurité appellent souvent à réduire les fonctionnalités des algorithmes,
afin de réduire la *surface d'attaque*,
ce qui est l'exact opposé de l'approche généraliste des algorithmes génératifs.
C'est ce qu'on pourrait appeler le principe de *sobriété numérique*.
Typiquement, intégrer une domotique connectée, 
c'est augmenter notre dépendance numérique
en les nombreux hardwares et softwares qui composent cette domotique connectée.
De la même manière, chaque nouvel outil de la suite Google,
chaque importation d'un module python[^calicarpa]
et chaque nouvel appel à l'API d'un tiers 
est une vulnérabilité additionnelle.
La meilleure cyberdéfense, c'est éviter les *bloatwares*,
c'est-à-dire l'ajout d'outils numériques de faible utilité,
mais qui pourraient un jour devenir le vecteur d'attaque fatale aux systèmes d'information.
En cela, les algorithmes génératifs à tout faire sont des catastrophes pour la cybersécurité[^jailbreak_multimodal].

[^calicarpa]: https://calicarpa.com
[^jailbreak_multimodal]: https://arxiv.org/abs/2306.13213

Pour augmenter la robustesse des entreprises, 
il est urgent d'imposer des régulations 
qui favoriseront la sobriété numérique de toutes les entreprises,
surtout celles qui ne sont pas par nature des entreprises technologiques.
Pour cela, la régulation est en fait un atout.
Or, de façon très préoccupante, 
la Commission Européenne semble avoir cédé au lobby d'OpenAI,
une entreprise américaine pourtant largement reconnue 
pour ses très faibles standards de transparence et de sécurité.
En tout cas, elle a amendé l'AI Act 
pour tolérer les algorithmes génératifs avec un moindre contrôle
que celui exigé pour les IA à « haut risque »[^time_openai_eu].

[^time_openai_eu]: https://time.com/6288245/openai-eu-lobbying-ai-act/

## Cyberarnaques et cyberguerres

Ceci étant dit, dans le contexte de tensions géopolitiques croissantes,
ainsi que celui de croissance rapide de l'industrie du cybercrime,
la plus grande préoccupation à avoir autour des algorithmes génératifs 
semble surtout résider dans leur utilisation massive à venir par des acteurs malveillants.
En particulier, de nombreuses cyberarnaques, 
comme les attaques par phishing ou l'impersonnification de proches,
semblent dangereusement optimisables et automatisables 
notamment par l'exploitation d'algorithmes génératifs Open Source[^scam].

[^scam]: https://www.youtube.com/watch?v=U2r1MJk85Zo

L'un des aspects les plus critiques de la cyberguerre est la guerre de l'information,
dans laquelle des organisations parfois surprenantes, privées ou publiques, sont déjà engagées.
MediaPart a par exemple révélé l'investissement du Paris Saint Germain dans des campagnes de dénigrement,
y compris envers ses propres joueurs comme Kylian Mbappé[^psg].
De la même manière, la guerre en Ukraine a mis en lumière toute l'importance de la propagande russe,
à la fois sur le sol russe[^russo_russe], sur le continent africain[^russie_afrique] et dans les démocraties occidentales[^propagande_russe_us].
Comme l'ont révélé les enquêtes #StoryKillers de Forbidden Stories[^storykillers],
ces opérations de désinformation s'appuient désormais massivement sur des technologies numériques,
notamment pour automatiser la création et la gestion de faux comptes[^team_jorge],
et pour ainsi amplifier certains messages 
tout en réduisant la recommandation d'autres messages[^eliminalia].
Les algorithmes génératifs semblent vouer à amplifier drastiquement 
les capacités de l'industrie de la désinformation 
à automatiser et crédibiliser les créations et les activités des faux comptes
qui opèrent ces manipulations de l'écosystème informationnel mondial.
Malheureusement, les réponses des institutions dirigeantes jusque là sont désespérément inappropriées[^avisa_partners],
ce qui risquent d'aggraver significativement le déclin démocratique actuel déjà terrifiant[^vdem].

[^psg]: https://www.mediapart.fr/journal/france/121022/revelations-sur-l-armee-numerique-du-paris-saint-germain
[^russo_russe]: https://theconversation.com/putins-propaganda-is-rooted-in-russian-history-and-thats-why-it-works-184197
[^russie_afrique]: https://www.dw.com/en/russia-targets-africa-with-propaganda-machine/a-63916836
[^propagande_russe_us]: https://www.nytimes.com/2022/02/25/technology/russia-supporters.html
[^storykillers]: https://forbiddenstories.org/story-killers/
[^team_jorge]: https://forbiddenstories.org/story-killers/team-jorge-disinformation/
[^eliminalia]: https://forbiddenstories.org/story-killers/the-gravediggers-eliminalia/
[^avisa_partners]: https://www.linforme.com/banque-finance/article/avisa-partners-va-aider-l-union-europeenne-a-lutter-contre-la-desinformation_695.html
[^vdem]: https://www.v-dem.net/documents/29/V-dem_democracyreport2023_lowres.pdf

Une dernière préoccupaion à mentionner est l'utilisation des algorithmes génératifs
pour la fabrication d'armes, en particulier de cyberattaques.
De nombreuses cyberattaques ont ainsi déjà été conçues via ChatGPT[^zero_day_chatgpt][^chatgpt_attacks].
Il est alors particulièrement préoccupant de savoir que le Président de TII, 
l'entreprise derrière l'algorithme génératif Falcon,
est aussi le fondateur et directeur de DarkMatters, 
une autre entreprise Émirati spécialisée dans les cyber-attaques 
et sous enquête par le FBI, 
suite au recrutement de nombreux hackers ex-NSA[^darkmatters].
Sachant à quel point, de l'aute côté, les cyberdéfenses sont à la traîne[^perlroth],
il faut craindre que de nombreux systèmes critiques pourront être mis à genoux
par le cybercrime armé d'algorithmes génératifs,
y compris nos banques, nos hôpitaux et nos réseaux électriques.

[^zero_day_chatgpt]: https://www.forcepoint.com/blog/x-labs/zero-day-exfiltration-using-chatgpt-prompts
[^chatgpt_attacks]: https://www.csoonline.com/article/3694931/5-ways-threat-actors-can-use-chatgpt-to-enhance-attacks.html
[^darkmatters]: https://www.reuters.com/article/us-usa-spying-raven-specialreport-idUSKCN1PO19O

## Au-delà des algorithmes génératifs

Si, comme on l'a vu, il y a de nombreuses raisons de se méfier des mauvaises utilisations des algorithmes génératifs,
et s'il y a donc certainement lieu d'être beaucoup plus intransigeant 
sur la sécurité de ces systèmes, 
l'indépendance vis-à-vis de ces outils vulnérables 
et l'application des lois déjà existantes,
il ne faut toutefois pas perdre de vue 
que les algorithmes génératifs ne jouent encore qu'un rôle mineur
dans notre écosystème informationnel.

En particulier, la cybersécurité de nombreux outils numériques est déjà désespérément déficiente,
y compris celle des contrôleurs de systèmes critiques[^insécurité].
Par ailleurs, les intelligences artificielles les plus lucratives 
et les plus influentes d'aujourd'hui ne sont pas des algorithmes génératifs.
Il s'agit bien plus des IA de recommendation et de ciblage publicitaire, 
au coeur du modèle d'affaire et des revenus pharaoniques de Google, Meta et TikTok
et avec des conséquences dramatiques 
pour la qualité de l'information, la santé mentale des utilisateurs 
et les incitations à la surconsommation polluante,
ou des IA d'investissements financiers comme Aladdin de BlackRock,
qui contrôlerait plus de 20 mille milliards de dollars d'investissement.
Il y a malheureusement une inattention alarmante 
à la conception, à la sécurité et aux conséquences socio-économiques de ces IA,
qui pourtant déterminent tant les sujets qui auront l'attention des démocraties,
et l'identité des bénéficiaires d'investissement importants.
Plus encore que les algorithmes génératifs,
ce sont sans doute ces IA qu'il faudrait urgemment beaucoup plus strictement encadrer.

[^insécurité]: https://arxiv.org/abs/2303.12340