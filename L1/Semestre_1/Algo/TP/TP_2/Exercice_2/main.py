#!usr/bin/python3

from note import mention

def main():
    note = float(input("Quelle est la note ? "))
    resultat = mention(note)

    print(resultat)

if __name__ == "__main__":
    main()
