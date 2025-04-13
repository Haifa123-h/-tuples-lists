# Exercice 1 : Manipulation de Listes

# 1. Demander le nombre d'étudiants à inscrire
# n = ...
n=int(input("enter number of students: "))
# 2. Créer une liste vide pour stocker les noms
# etudiants = []
etudiants=[]
# 3. Boucle pour saisir les noms des étudiants
# for i in range(...):
    # nom = input(...)
    # ...
for i in range(n):
    name = input(f"Enter student {i + 1}: ")
    etudiants.append(name)
# 4. Afficher la liste des étudiants
print("list is: ")
print(etudiants)
# 5. Afficher la liste triée
etudiants=sorted(etudiants)
print("etudiants after sort: ")
print(etudiants)
# 6. Afficher le nombre total d'étudiants
print("total number is: ",n)
# 7. Demander un nom à supprimer et supprimer s’il est dans la liste
rem=input("enter nom to remove: ")
etudiants.remove(rem)
# 8. Afficher la nouvelle liste
print(etudiants)
