#!usr/bin/python3

from annee_bis import annee_bissextile

def main():
     année = int(input("Quelle année souhaitez vous tester ? "))

     print(annee_bissextile(année))

if __name__ == "__main__":
    main()