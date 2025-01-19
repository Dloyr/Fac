#!usr/bin/python3

from convertion_jhm import convertion_jhm

def main():
    minutes = int(input("Combien de minutes souhaitez-vous convertir ? "))
    convertion_jhm(minutes)

if __name__ == "__main__":
    main()