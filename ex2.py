# Étape 1 : Définir la liste des villes avec leurs coordonnées (latitude, longitude)
villes = [("Paris", (45548, -55665)),("Sousse", (5458, 88)),("Nabel", (5848548, 21549))
]

# Étape 2 : Afficher chaque ville avec ses coordonnées
print("Liste des villes et leurs coordonnées :")
for ville,coordonnees in villes:
    print(f"{ville} : Latitude = {coordonnees[0]}, Longitude = {coordonnees[1]}")

# Étape 3 : Afficher uniquement les latitudes
print("\nLatitudes des villes :")
for  ville,coordonnees in villes:
    print(coordonnees[0])

# Étape 4 : Calculer et afficher la latitude moyenne
somme_latitudes=0
for ville in villes:
    somme_latitudes =somme_latitudes+ coordonnees[0]
moyenne_latitude = somme_latitudes / len(villes)

print(f"\nLatitude moyenne : {moyenne_latitude}")
