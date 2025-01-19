#!/usr/bin/python3

def decomp_facteurs_premiers(n: int)-> list[int]:
    """
    Fonction pour décompter un nombre en facteur premiers

    Argument:
        - n: nombre à décompter

    Retourne: une liste des facteurs premiers
    """
    liste_facteurs = []
    facteur_premiers = 2

    while n != 1:
        if n % facteur_premiers == 0:
            liste_facteurs.append(facteur_premiers)
            n //= facteur_premiers
        else:
            facteur_premiers += 1
    return liste_facteurs


# EXERCICE 2 (res sur fiche faux)

def Heron(a: int, k: int)-> float:
    """
    Fonction de l'algorithme d'Héron d'Alexandrie

    Arguments:
        -a: le nombre
        -k: le nombre d'itération

    Retourne: la racine carrée
    """
    numerateur = 1
    denominateur = 1

    for i in range(k):
        nvx_numerateur = numerateur ** 2 + a * (denominateur ** 2)
        denominateur = 2 * numerateur * denominateur
        numerateur = nvx_numerateur

    return numerateur / denominateur

# EXERCICE 3
base = []

def insere(base: dict[str, any], titre: str, genre: str, duree: int)-> None:
    """
    Permet d'insérer un film au sein du catalogue

    Arguments:
        - base: la liste des films
        - titre: titre du film à ajouter
        - genre: genre du film à ajouter
        - duree: duree du film à ajouter
    """
    if titre not in base:
        base.append(
            {
                "titre": titre,
                "genre": genre,
                "duree": duree
            }
        )

# EXERCICE 4
def film_par_genre(genre: str, base: list[dict[str, str|int]])-> list[str]:
    """
    Affiche tout les films d'un même genre qui sont présent dans le catalogue

    Arguments:
        - genre: le genre des films
        - base: le catalogue de film

    Retourne: une liste de films liés au genre
    """
    liste_film = []

    for film in base:
        if film["genre"] == genre:
            liste_film.append(film["titre"])

    return liste_film

# EXERCICE 5
def base_genre(base: list[dict[str, str | int]]):
    """
    Trie les films dans le catalogues en fonction des genres

    Arguments:
        - base: le catalogue

    Retourne: 
        - le catalogue filtré, sous forme d'un dictionnaire :
            . clé: genre
            . valeur: liste des films lié au genre
    """
    liste_genres = []
    dict_par_genres = {}

    for film in base:
        genre = film["genre"]
        if genre not in liste_genres:
            liste_genres.append(genre)

    for genre in liste_genres:
        if genre not in dict_par_genres:
            dict_par_genres[genre] = film_par_genre(genre, base)

    return dict_par_genres

# EXERCICE 6
def film_plus_long(base: list[dict[str, int | str]]):
    """
    Récupère le film le plus long dans le catalogue

    Argument:
        - base: le catalogue

    Retourne: le titre du film
    """
    duree = 0
    titre = ""

    for film in base:
        if duree <= film["duree"]:
            duree = film["duree"]
            titre = film["titre"]

    return titre

# EXERCICE 7    
def presents(liste_films: list[str], base: list[dict[str, int | str]])-> list[str]:
    """
    film
    """
    films_present = []
    for film in base:
        if film["titre"] in liste_films:
            films_present.append(film["titre"])

    return films_present

#print(presents(["Avatar", "Saw", "Greenland", "Swallow"], base))

# EXERCICE 8

note_film = [
    ("Avatar", 3400000),
    ("007 Spectre", 2450000),
    ("Saw", 1710000),
    ("Hunger Games", 3100000),
    ("Jurassic world 2", 5100000),
    ("Swallow", 2730000)
]

def meilleur_film(note_film: list[tuple[str, int]])-> str:
    note = 0
    titre = ""
    for film in note_film:
        if note <= film[1]:
            note = film[1]
            titre = film[0]

    return titre

print(meilleur_film(note_film))