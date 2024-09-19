# Cette équation est une backdoor de la NSA



## Les courbes elliptiques

y² = x³ + ax + b

y² = x³ + ax² + x (Montgomery, ECDSA 25519)

Des courbes réelles, des quasi-courbes rationnelles, des surfaces complexes...
et des points dans les corps finis.


## Une courbe elliptique est un groupe

Définition géométrique

Dérivation algébrique

Sous-groupe cyclique


## Diffie-Hellman

x P

y P 

xy P

Hash(xy P)


## Chiffrement à clé public

x^-1^ (m (x P))

x^-1^ peut se calculer à l'aide de l'algorithme de Schoof 
(pour compter l'ordre du groupe)
et en choisissant x^-1^ tel que x^-1^ x = 1 [ordre].


## La backdoor de la NSA

Q^x = P^(ex)

(Q^x)^s = P^(esx) = (P^(es))^x

