# Sécuriser les codes nucléaires

Comment prendre la décision de lancer une attaque nucléaire massive ?
Et surtout comment peut-on sécuriser cette prise de décision ?

Clairement, les codes nucléaires sont parmi les secrets les plus critiques au monde.
Si jamais ils se faisaient volés, et si un hacker parvenait à les exploiter
pour déclencher une attaque nucléaire massive,
alors c'est toute l'humanité qui en subirait les conséquences,
avec probablement des milliards de vies humaines perdues,
notamment en cas d'escalades nucléaires et d'hiver nucléaire.

Mais à l'inverse, si ces codes nucléaires sont perdus,
comme cela semble avoir été le cas 
[sous le mandat de Bill Clinton aux États-Unis](https://abcnews.go.com/WN/president-bill-clinton-lost-nuclear-codes-office-book/story?id=11930878),
et si une superpuissance ne dispose plus de faculté de lancer une telle attaque,
et surtout si les adversaires géopolitiques finissaient par le savoir,
alors les équilibres de pouvoir pourraient être bouleversés.

Quelle serait alors une procédure vraiment sécurisée
pour acter la décision d'attaque nucléaire ?

Alors, notez que les véritables protocoles nucléaires sont sous secret défense,
et donc, non seulement je ne les connais pas,
mais même si je les connaissais, 
je n'aurais aucune envie d'en parler publiquement ---
[notamment pour éviter de finir en prison](youtube.com/watch?v=ryW5KGSpsdI).
Ce qui va m'intéresser aujourd'hui, 
c'est uniquement de vous parler de l'état de l'art en cryptographie
pour sécuriser des prises de décision à très haut enjeu,
comme celle d'une attaque nucléaire.


## La décision doit être prise à distante

Alors, bien sûr, si les individus, ou l'unique individu, 
chargés de décider de l'attaque nucléaire peuvent être réunis dans une même pièce,
alors il serait raisonnable de choisir d'acter la décision
suite à une discussion, avec prises de positions claires à voix haute.

Cependant, en pratique, il peut être beaucoup trop compliqué
de réunir les preneurs de décision dans cette pièce,
notamment si le Président est en déplacement dans un pays lointain,
ce qui arrive finalement très souvent.
Dès lors, la décision devra être prise à distance.

En fait, même si les preneurs de décision sont réunis dans une pièce,
il faudra toujours communiquer leur décision,
soit à des opérateurs humains chargés du lancement effectif des missiles nucléaires,
soit à des machines conçues pour automatiser ce lancement.

Quoi qu'il en soit, une décision devra être communiquée à distance.
Sauf qu'une telle communication, ce n'est finalement qu'un signal physique.
Dès lors, se pose la question de l'authentification du signal.
Comment peut-on être sûr que le signal vient bien
de ceux qui sont réellement en charge de la prise de décision ?
Et comment peut-on en particulier empêcher un cybercriminel
de concevoir un signal qui sera interprété comme une décision d'attaque nucléaire
par les personnes ou les machines chargés d'opérer l'attaque ?

De nos jours, on considère très largement qu'il est illusoire
d'espérer compter sur des spécificités physiques du support du signal.
En cryptographie en tout cas, 
on considère que la clé n'est pas d'encoder l'authentification 
dans le support du signal ;
mais qu'il faut au contraire encoder l'authentification
dans le code que le signal transmet.

Et typiquement, 
il va falloir que le signal transmette un mot de passe ultra secret
pour que le signal reçu soit interprété comme la décision d'une attaque nucléaire massive.

Et là, on retrouve le problème du vol ou de la perte de ce mot de passe.
Si les forces armées perdent le mot de passe,
alors ils ne pourront plus déclender l'attaque nucléaire.
Ou, pire encore, imaginons ainsi qu'un espion parvienne à accéder au mot de passe.
Il pourra alors envoyer un signal qui déclenchera l'attaque nucléaire.


## Décider à partir d'un quorum

(f,n)-secure.

n > 3f


## Le secret partagé de Shamir


