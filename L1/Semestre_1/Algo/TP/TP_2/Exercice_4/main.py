#!usr/bin/python3

from nmb_jours import nb_jours_annee

def main():
     année = int(input("Quelle année souhaitez-vous convertir ? "))

     print(nb_jours_annee(année))

if __name__ == "__main__":
    main()
