# TP TDD - Poker 

* **Validité des entrées :** Le programme suppose que les données en entrée sont valides. Il n'y a pas de vérification pour rejeter des formats invalides ou des cartes qui n'existent pas.
* **Doublons :** Le programme suppose qu'il n'y a pas de triche et donc qu'il n'y a aucune carte en double distribuée entre le plateau et les mains des joueurs.
* **Ordre de sortie :** La fonction `best_hand` renvoie les 5 meilleures cartes. L'ordre de ces cartes dans la liste de retour dépend de la combinaison trouvée : les cartes qui forment la combinaison principale sont évaluées en premier (par exemple, pour un carré, on renvoie la valeur de la carte en 4 exemplaires, puis le kicker).

## Lancement des tests
La commande pour lancer la suite de tests est :
python -m unittest test_poker.py