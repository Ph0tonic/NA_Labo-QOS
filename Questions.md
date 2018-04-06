# Labo 3 - Questions

## Ex 1
- Certains routeurs lorsqu'ils sont surchargé et s'ils disposent de la fonctionnalité NAGGLE marquent les pacquets par un flag afin de signaler aux clients que leurs messages passent par des zones surchargées.
- Le client va ensuite automatiquement diminuer son débit et le remonter progressivement

## Ex 2
- Problème de partage des trames
- Guigge de phase très variable
- Baisse de l'efficacité mais augment le temsp de réponse

## Ex 3
Une des 3 possibilités:
- Jeter les pacquets
- ignorer le flag TOS
- supprimer le flag TOS

## Ex 4
- Ralentir le débit montant de cette connexion
- Supprimer des paquets de confirmation

## Ex 5
- Limiter le nombre de ack par exemple en groupant les confirmations comme go back-n
- Priorisation du traffic montant, confirmations

## Ex 6
- Routeur entreprise ne peux pas gérer le traffic plus général qui sera plus important sur le routeur FAI.
- Routeur FAI aura un traffic plus important que le routeur entreprise
- Parce que on peut déjà prioriser notre traffic en interne.

## Ex 7
- SFQ (stochastic fair queuing)
- Non car il va jeter ce qui déborde

## Questions rapport
## Ex 1
- Il envoie tout ce qu'il reçoit et s'il y a un routeur qui est surchargé, il envoie le paquet à un autre routeur

## Ex 2
- Wireshark avec des filtres

## Ex 3
- Prioriser le tcp

## Ex 4
- A faire
