#!usr/bin/python3

from conversion_temp import celsius_to_fahr

def main():
    celsius = float(input("Quelle température souhaitez-vous convertir ? "))

    celsius_to_fahr(celsius)

    return 0

if __name__ == "__main__":
    main()
