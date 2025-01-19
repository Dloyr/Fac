#!usr/bin/python3

from durées import difference_durees

j_1 = int(input("Combien de jours souhaitez-vous convertir pour la première durée ? "))
h_1 = int(input("Combien d'heures souhaitez-vous convertir pour la première durée ? "))
m_1 = int(input("Combien de minutes souhaitez-vous convertir pour la première durée ? "))
print(" ")
j_2 = int(input("Combien de jours souhaitez-vous convertir pour la deuxième durée ? "))
h_2 = int(input("Combien d'heures souhaitez-vous convertir pour la deuxième durée ? "))
m_2 = int(input("Combien de minutes souhaitez-vous convertir pour la deuxième durée ? "))
print(" ")

difference_durees(j_1, h_1, m_1, j_2, h_2, m_2)