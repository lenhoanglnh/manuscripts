# Contrôler une supercalculatrice avec une armée de fourmis

Imaginez qu'une supercalculatrice d'une entreprise privée 
prétend effectuer des milliards de milliards d'opérations,
et que l'entreprise affirme que les calculs concluent 
que la probabilité que la gauche gagne l'élection présidentielle de 2027
est égale à 35%
Comment savoir si la supercalculatrice a bien effectué correctement
les milliards de milliards d'opération, 
et que l'entreprise a bien rapporté les résultats de ce calcul ?

Bien sûr, il suffirait de refaire à notre tour ces milliards de milliards d'opération.
Mais supposons que ces opérations soient faits à la suite et donc de manière non-parallèle,
et qu'on ne dispose que de machines capables de faire un milliard d'opérations par seconde.
Comme le calcul n'est pas parallélisable,
on sera forcément limité par la vitesse de la machine la plus rapide à notre disposition ;
et il nous faudra alors un milliard de secondes, soit 31 ans,
pour venir à bout de la vérification des calculs.
Clairement, on aura mieux fait d'attendre 2027 
pour savoir si la gauche gagnera l'élection présidentielle.

À moins que...
Certes le calcul n'est pas parallélisable.
Mais se pourrait-il que sa vérification le soit ?
Est-ce qu'une foule de vérificateurs faibles peut vérifier
les opérations d'une superintelligence ?

Eh bien, aujourd'hui,
on va voir comment des milliards de machines peuvent être combinées,
et vérifier les opérations de la supercalculatrice
en quelques secondes ou quelques minutes,
avec toutes sortes d'astériques à mettre dans cette affirmation... * ** ***

* En fait, non, car il faut un "témoin"

** Techniquement, la supercalculatrice pourrait juste envoyer ce témoin

*** Mais en fait OSEF, car le plus intéressant, c'est qu'on peut transformer
cette parallélisation en un SNARK ! 
(Mais ça va prendre encore pas mal de vidéos pour qu'on y arrive...)


## Comment fonctionne une supercalculatrice ?

Pour comprendre comment les opérations de la supercalculatrice peuvent être vérifiés,
prenons d'abord le temps de parler de son fonctionnement.
Alors, bien sûr, on va éviter de plonger dans trop de détails,
parce que, bah, c'est vite très compliqué...

Cependant, de manière très grossière, on peut voir ces opérations
comme celles de machines de Turing,
dont je vous ai parlé à l'ère pré-Covid.
Mais on peut être plus fins que cela.

De manière un peu plus précise, mais toujours très grossière
les supercalculatrices disposent d'un microprocesseur, et d'une mémoire.
Le microprocesseur a lui-même une sorte de mémoire interne,
dont les case mémoires sont appelés des registres.
Par exemple l'ARMv8, introduit en 2011
et qui équipe beaucoup de smartphones modernes,
ainsi que des supercalculatrices comme Fugaku,
possède 31 registres de 64 bits à usage général,
et 32 bits de 128 bits dédiés à des opérations arithmétiques.

À travers des circuits électroniques, et notamment des transistors,
beaucoup de transistors,
les microprocesseurs sont conçus avec un bon nombre
d'opérations entre les registres,
comme copier un registre dans un autre,
ajouter un à un registre,
additioner ou multiplier les contenus de deux registres,
et enregistrer le résultat dans un autre registre,
ou lire une case de la mémoire et l'enregistrer dans un registre,
ou encore écrire la valeur d'un registre dans une case de la mémoire.

L'opération à effectuer est définie par un registre spécial appelé compteur de programmes,
et il est mis à jour automatiquement juste après l'opération à effectuer.
Chaque registre de 64 bits peut contenir un nombre entier entre 0 et 2^64,
ce qui est de l'ordre de 10 milliards de milliards.

> Ça fait beaucoup.

En particulier, ça veut dire qu'on peut utiliser ce registre
pour indexer n'importe quelle case mémoire directement accessible par le microprocesseur ;
les disques durs qui font plus de 10 exaoctets ne courent pas encore les rues !
On peut ainsi utiliser des opérations prédéfinies d'adressage indirect,
pour dire "lit le contenu de la mémoire dont l'adresse est le registre 1 et enregistre le résultat dans le registre 2
ou "écrit le contenu du registre 14 dans la case mémoire dont l'adresse est le contenu du registre 22".

Bon, je simplifie énormément de choses avec ces exemples.
Mais ce qu'il faut retenir, c'est qu'une machine, surtout si elle tourne sur un seul coeur,
c'est vraiment un petit nombre de registres,
avec des opérations entre ces registres,
et une grande mémoire à laquelle la machine peut accéder
via des instructions inscrites dans les registres.

Pour ceux qui se souviennent de la machine de Turing,
les registres et les opérations précodées correspondent à la tête de lecture,
et la bande est désormais optimisée pour des accès directs à des cases mémoires.
En pratique, certaines cases mémoires sont plus rapides d'accès que d'autres,
ce qu'il arrive de modéliser en théorie par une mémoire infinie,
dont la n-ième case peut être accéder en un temps logarithme en n ;
notamment dans le cadre du modèle des machines avec Random Access.

Mais, surtout dans le cadre de la vidéo d'aujourd'hui,
il s'agit de détails qui peuvent obfusquer la complexité déjà importante
de la parallélisation de la vérification du calcul.

En tout cas, c'est assez fou de se dire que,
avec un nombre fini d'opérations prédéfinies sur un petit nombre de registres,
et avec un accès à une mémoire en lecture et écriture par ces registres,
de manière purement mécanique 
--- ou en fait, électroniques, mais vous voyez ce qu je veux dire ---
on obtient des machines capables d'effectuer toutes sortes de traitements informationnels,
des calculs des zéros de la fonction zêta de Riemann à la lecture des vidéos YouTube,
en passant par l'apprentissage des préférences humaines,
la gouvernance algorithmique à la Tournesol et la cryptographie moderne.


## De l'architecture générale du calcul à des circuits logiques

Pour pouvoir étudier plus facilement les calculs 
qui peuvent être effectués par les microprocesseurs modernes et leurs mémoires,
on va d'abord les réduire à une composition d'un petit nombre d'opérations possibles,
un peu comme on peut vouloir réduire la matière 
à un petit nombre de particules élémentaires.

Pour cela, on peut remarquer que, si on faisait une photographie à chaque instant
des états des registres et de la mémoire,
alors ça nous ferait autant de photographies à prendre
qu'il y a eu d'opérations faites par la supercalculatrice,
soit dans notre exemple un milliard de milliards de photographies.
Cependant, on peut aussi remarquer que, 
pour vérifier le calcul de la supercalculatrice,
il suffit de vérifier que, pour passer d'une photo à l'autre,
la supercalculatrice a bien fait les opérations qu'on attendait de lui.

Dès lors, vérifier les calculs de la supercalculatrice,
c'est simplement vérifier que toutes les transitions sont correctes.
Or ce calcul de vérification, il est très simple à paralléliser.
Si on a un milliard de machines à disposition,
on peut donner à chaque machine la tâche de vérifier un milliards de transitions,
et on a aura bien décentraliser la vérification.

Mieux encore, chaque vérification de transition 
correspond à vérifier une opération du microprocesseur,
ce qui peut être fait en copiant-collant les circuits logiques 
qui encodent les opérations du microprocesseur.
De nos jours, ces circuits logiques sont extrêmement complexes ;
mais in fine, ils ne correspondent qu'à des combinaisons entre les bits des registres,
à l'aide d'opération "ET", "OU" et "NON".

Il y a tout de même un petit problème avec cette approche.
Vous le voyez ?
Le problème, c'est qu'il faut aussi vérifier l'intégrité de la mémoire,
d'une photographie à l'autre !
Alors, oui, ça peut là encore être fait à l'aide de circuits logiques ;
en particulier vérifier qu'un bit B de la mémoire n'a pas changé entre t et t+1
peut se calculer en vérifiant (B_t_ ET B_t+1_) OU (NON B_t_ ET NON B_t+1_).
Mais il va nous en falloir énormément, car cette mémoire peut être énorme.
Si la supercalculatrice a effectivement utilisé une case mémoire différente pour chaque opération ;
ça fait un milliard de milliards de cases mémoires 
dont il faut bien vérifier qu'ils n'ont pas été changés d'une photo à l'autre !

Ainsi, on a décentralisé la vérification,
mais la simple tâche de vérifier une transition
peut en fait être insurmontable pour chaque machine de vérification.


## De la RAM à un circuit logique peu profond

Bien entendu, suivre l'évolution de toute la mémoire lors de toutes les transitions,
c'est clairement une approche sous-optimale de la vérification.
Pour clarifier la tâche de vérification,
on peut la décomposer en deux problèmes :
1. Vérifier la cohérence de la mémoire.
2. En supposant la mémoire valide, vérifier chaque transition des états des registres.

Pour y parvenir, on va maintenant considérer 
que les vérificateurs exigent de la supercalculatrice
qu'elle leur envoie un transcript de ses calculs, qu'on appelle parfois la *trace*,
qui liste à chaque instant l'état des registres.
Comme les registres sont en petit nombre,
la trace est un objet 
dont la taille est proportionnelle uniquement à longueur du calcul ;
et donc, si on décentralise la vérification, 
la supercalculatrice aura un nombre suffisamment faible d'information 
à envoyer à chaque vérificateur.

En supposant la mémoire valide, en particulier au moment de lectures,
chaque vérificateur peut aisément vérifier les transitions d'états des registres,
pour chaque portion du transcript.
En fait, il peut le faire en réutilisant les circuits logiques des microprocesseurs.

Clairement, la difficulté de la vérification réside dans la vérification
de la cohérence de la mémoire ;
en particulier du fait que sa lecture retourne
forcément la dernière écriture qui y a été faite ;
y compris lors de son initialisation pour écrire les données du calcul effectué.

Et bien, l'astuce c'est d'exiger de la supercalculatrice
qu'elle nous envoie aussi les opérations,
mais cette fois dans un ordre trié.
Plus précisément, on demande qu'elle classe les opérations en deux catégories :
celles qui font intervenir une écriture ou une lecture en mémoire,
et le reste.
Le reste, elle les met toutes à la fins, dans un ordre quelconque ;
puisque de toute façon ces opérations n'affectent pas la cohérence de la mémoire.

Pour celles qui font intervenir une écriture ou une lecture en mémoire,
on sait qu'elles font en particulier intervenir
l'adresse mémoire à lire ou à laquelle écrire,
ainsi qu'un numéro, qui correspond au numéro de l'opération
dans l'ordre normal des opérations.

Et bien, le tri doit d'abord respecter l'ordre des adresses mémoires,
en mettant en premier les opérations sur les premières cases mémoires,
et ensuite pour une case mémoire donnée,
les opérations doivent être telles 
que les premières opérations à effectuer apparaissent avant.

Étant donné les opérations dans cet ordre,
on peut maintenant très bien paralléliser la vérification de cohérence de la mémoire,
puisqu'on peut déduire la validité d'une opération sur la mémoire
à partir du résultat de l'opération qui la précède.
En effet, si c'est une opération d'écriture, alors rien à vérifier.
Maintenant si c'est une opération de lecture,
et que celle juste avant était une opération d'écriture,
alors la lecture doit donner le résultat inscrit lors de l'écriture juste avant.
Enfin, si c'est une lecture, et si juste avant c'était une lecture,
il faut que ces deux lectures aient donné le même résultat.

De façon remarquable, on peut effectuer 
chaque vérification des opérations sur la mémoire à l'aide d'un circuit logique ;
et on peut vérifier le tri par mémoire également avec un circuit logique ---
ce n'est d'ailleurs pas trivial de faire cela,
je renvoie à ce livre pour plus de détails sur comment y arriver.  
https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.html


## Conclusion

Dans cette vidéo, on a vu comment 
la vérification des calculs d'une supercalculatrice pouvait être décentralisée,
et ainsi effectuée par une foule de vérificateurs faibles.
De façon plus précise encore, 
n'importe quelle suite de T opérations d'une supercalculatrice
par un ensemble de T vérificateurs faibles.
Mieux encore, ces vérificateurs faibles n'ont en fait 
qu'à exécuter à chaque étape les calculs d'un circuit logique,
puis à communiquer un bit d'information à d'autres vérificateurs faibles ;
et le nombre d'étapes nécessaires est beaucoup plus faible que T,
on peut le rendre polylogarithmique en T.

NB : Le temps total de calcul des vérificateurs sera alors O(T log T).
Mais on peut faire mieux, et se ramener à un temps total de calcul en O(T),
tout en ayant O(log T) opérations par vérificateur,
si on s'autorise des affaiblissements du problème de vérification,
qui n'affaibilissent pas pour autant le SNARK qu'on finit par construire !

Bien sûr, ce résultat est avant tout théorique.
Cependant, différents projets, notamment RISC-Zero et Cairo,
cherchent vraiment à identifier des architectures de microprocesseurs
et des circuits associés à ces architectures,
dont la vérification est ainsi rapide avec une armée de vérificateurs,
de sorte à ensuite fournir des preuves de validité du calcul rapidement vérifiables.

NB: RISC est le "R" dans ARM.

De façon plus pragmatique encore,
pour certaines fonctions spécifiques et récurrentes, 
notamment en cryptographie,
des vérifications efficaces des calculs ont déjà été construites.

Ceci étant, sachant qu'il reste nécessaire de disposer d'une armée de vérificateurs, 
ces systèmes de vérification de calcul peuvent sembler n'être que d'une utilité limitée.
Détrompez=vous !
Comme on va le voir, la décomposition que je vous ai présentée aujourd'hui 
n'est en fait qu'une étape de la conception de SNARK,
c'est-à-dire une preuve relativement courte,
capable de convaincre rapidement un unique vérificateur faible
que le résultat du calcul de la supercalculatrice est correct,
comme on en a parlé dans la vidéo précédente.

L'une des nombreuses astuces indispensables pour y arriver
consiste à transformer le circuit logique en un circuit arithmétique,
où l'opération "NON x" est remplacée par l'opération 1-x,
où l'opération "x ET y" est remplacée par xy,
et où l'opération "x OU y" est remplacée par x + y - xy,
Ce faisant, toutes les opérations du circuit logique sur des bits
correspond à une suite d'addition et de multiplication.
Or composer des additions et multiplications,
c'est précisément concevoir des polynomes à plusieurs variables,
qu'étudie la très riche théorie de la géométrie algébrique.

Eh bien, la combinaison des propriétés des nombres de cette théorie
avec la parallélisation de la vérification dont on a parlé aujourd'hui
forme le socle d'une construction très générale de SNARK.
En fait, plus que vérifier le calcul de la supercalculatrice,
cette construction permet de vérifier que la supercalculatrice
connaît des données qui lui ont permis d'obtenir le résultat de son calcul ;
des données qui peuvent typiquement correspondre à des données secrètes d'authentification.

Mais pour en venir là, on va devoir faire des mathématiques fondamentales ;
ce sera le sujet des prochaines vidéos !

