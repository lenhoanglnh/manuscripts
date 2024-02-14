# Les maths des IA démocratiques (version hardcore)

La semaine dernière, j'ai fait une vidéo sur les maths des IA démocratiques...
et beaucoup parmi vous m'ont demandé la version hardcore,
qui présente les grandes lignes de nos preuves mathématiques
qui permettent de comprendre ce qu'implique l'utilisation de la médiane géométrique
en termes d'incitatifs pour les fournisseurs de données d'entraînement 
des algorithmes de machine learning.

Et même si la vidéo n'a en fait pas fait tant de vues, 
comme ça me manque d'expliquer des maths,
je vais m'exécuter et vous parler de notre preuve.
Mais, vous êtes prévenu, ça ne va pas être super simple - 
il va falloir que vous soyez au moins de niveau bac + 1, voire un peu plus.

En particulier, si tout ce qui vous intéresse, 
c'est simplement de comprendre nos théorèmes 
et leurs implications pour la conception d'intelligences artificielles démocratiques,
je vous renvoie vers la vidéo non-hardcore, dont le lien est en description.

OK. On est partis pour parler hardcore !

## Quelques préliminaires à propos de la médiane géométrique

Commençons par définir plus formellement la médiane géométrique.
Pour commencer, on va se placer dans un espace euclidien de dimension d.
Étant donné une famille de V vecteurs $\theta_1$, ..., $\theta_V$ de dimension d, 
famille que je vais noter $\vec \theta$ avec une flèche,
leur médiane géométrique peut être définie comme le vecteur z
qui minimise la somme des distances aux $\theta_v$.
Autrement dit, $GM(\vec \theta) \triangleq \arg\min_z \sum_{v \in [V]} || z - \theta_v ||_2$.



