#!usr/bin/python3

#==============================================================Exercice 1=====================================================================

def appartient(c: str, ch: str) -> bool:
    """
    Fct qui vérifie si un caractère appartient à la chaine
     -c: caractère à vérifier
     -ch: chaine de caractère
    """

    for caractère in ch:
        if caractère == c:
            return True
        else:
            continue

    return False

#print(appartient("b", "bonjour"))
#==============================================================Exercice 2=====================================================================

def est_voyelle_min(caractère: str) -> bool:
    """
    Fct qui vérifie si un caractère est une voyelle en minuscule:
     -caractère: caractère à vérifier
    """
    voyelles ="aeiouy"

    return appartient(caractère, voyelles)

#print(est_voyelle_min("b"))

#==============================================================Exercice 3=====================================================================

def est_voyelle_maj(caractère: str) -> bool:
    """
    Fct qui vérifie si un caractère est une voyelle en majuscule:
     -caractère: caractère à vérifier
    """
    voyelles_maj = "AEIOUY"

    return appartient(caractère, voyelles_maj)

#print(est_voyelle_maj("a"))

#==============================================================Exercice 4=====================================================================

def est_voyelle(caractère: str) -> bool:
    """
    Fct qui vérifie si un caractère est une voyelle:
     -caractère: caractère à vérifier
    """

    if est_voyelle_min(caractère) or est_voyelle_maj(caractère):
        return True
    else:
        return False

#print(est_voyelle("b"))

#==============================================================Exercice 5=====================================================================


def compte_voyelle(chaine: str) -> bool:
    """
    Fct qui compte le nombre de voyelles au sein d'une chaine:
     -chaine: la chaine de caractère
    """
    compteur = 0

    for c in chaine:
        if est_voyelle(c):
            compteur += 1

    return compteur

#print(compte_voyelle("aeibp"))

#==============================================================Exercice 6======================================================================

def est_majuscule(caractère: str)-> bool:
    """
    Fct qui vérifie si un caractère est en majuscule:
     -caractère: caractère à vérifier
    """

    for c in range(ord("A"), ord("Z")):
        if ord(caractère) == c:
            return True

    return False

#==============================================================Exercice 7=====================================================================

def est_minuscule(caractère: str)-> bool:
    """
    Fct qui vérifie si un caractère est en minuscule:
     -caractère: caractère à vérifier
    """

    for c in range(ord("a"), ord("z")):
        if ord(caractère) == c:
            return True

    return False

#==============================================================Exercice 8=====================================================================

def est_lettre(caractère: str)-> bool:
    """
    Fct qui vérifie si le caractère est une lettre:
     -caractère: caractère à vérifier
    """

    if est_majuscule(caractère) or est_minuscule(caractère):
        return True

    return False

#print(est_lettre(","))

#==============================================================Exercice 9=====================================================================

def compte_maj(chaine: str)-> str:
    """
    Fct qui compte le nombre de majuscules au sein d'une chaine:
     -chaine: chaine à vérifier
    """
    compteur = 0

    for c in chaine:
        if est_majuscule(c):
            compteur += 1

    return compteur

#print(compte_maj('ILovePython'))

#==============================================================Exercice 10===================================================================

def compte_min(chaine: str)-> str:
    """
    Fct qui compte le nombre de minuscules au sein du mdp:
     -chaine: le mdp à vérifier
    """
    compteur = 0

    for c in chaine:
        if est_minuscule(c):
                compteur += 1

    return compteur

#print(compte_min("C'eSTUNTEST"))

def compte_int(chaine: str)-> str:
    """
    Fct qui compte le nombre de chiffres au sein du mdp:
     -chaine: le mdp à vérifier
    """
    compteur = 0

    for c in chaine:
        if c >= "1" and c <= "9":
                compteur += 1

    return compteur

def compte_symbole(chaine: str)-> int:
    """
    Fct qui compte le nombre de symboles autorisés au sein du mdp:
     -chaine: mdp
    """
    compteur = 0

    for c in chaine:
        if c == "+" or c == "-" or c == "@" or c == "?" or  c == "!" or  c == "*" or c == "$":
            compteur += 1
        elif c == '"' or c == "#" or c >= "%" and c <= ")" or c == "'" or c == "." or c == "/" or c >= ":" and c <= ">" or c >= "[" and \
          c <= "`" or c >= "{" and c <= "~":
            return 0
    
    return compteur

#print(compte_symbole("aee+@{"))

def teste_mdp(password: str)-> bool:
    """
    Fct qui vérifie si le mdp:
            .A une longueur >= 8
            .Contient au moins une minuscule
            .Contient au moins une majuscule
            .Contient au moins un chiffre
            .Contient au moins un symbole parmi: +,-,@,?,!,*,$

     -password: Le mot de passe à vérifier
    """

    if len(password) >= 7 and compte_min(password) >= 1 and compte_maj(password) >= 1 \
        and compte_int(password) >= 1 and compte_symbole(password) >= 1:
        return True

    return False

#print(teste_mdp("abracadabra?"))

#==============================================================Exercice 11=====================================================================

def copie_sauf_car(chaine: str, caractère: str)-> str:
    """
    Fct qui copie une chaine, sans le caractère sélectionné
     -chaine: chaine à recopier
     -caractère: caractère à ne pas recopier
    """

    cpy_str = ""

    for c in chaine:
        if c != caractère:
            cpy_str += c

    return cpy_str

#print(copie_sauf_car("bonjour", "o"))

#==============================================================Exercice 12=====================================================================

def copie_sauf_plusieurs_car(chaine: str, chaine_x_cpy: str)-> str:
    """
    Fct qui copie une chaine, sans les caractère sélectionné
     -chaine: chaine à recopier
     -chaine_x_cpy: les caractères à ne pas recopier
    """

    cpy_str = ""

    for c in chaine:
        if c not in chaine_x_cpy:
            cpy_str += c

    return cpy_str

#print(copie_sauf_plusieurs_car("bonjour", "jdo"))

#==============================================================Exercice 13=====================================================================

def remplace(chaine: str, car_a_edit:str, car_remplacement:str)-> str:
    """
    Fct pour recopier une chaine en remplacant un caractère sélectioné par un autre souhaité
     -chaine: chaine à recopier
     -car_a_edit: caractère à remplacer
     -car_remplacement: caractère de remplacement
    """

    cpy_str = ""

    for c in chaine:
        if c == car_a_edit:
            cpy_str += car_remplacement
        else:
            cpy_str += c

    return cpy_str

#==============================================================Exercice 14=====================================================================

def min_to_maj(caractère: str)-> str:
    """
    Fct qui convertir une minsucule en majuscule
     -caractère: caractère à convertir
    """

    if est_minuscule(caractère):
        return chr(ord(caractère) - 32)

    return caractère

#print(min_to_maj("a"))

#==============================================================Exercice 15=====================================================================

def maj_to_min(caractère: str)-> str:
    """
    Fct qui convertir une majuscule en minuscule
     -caractère: caractère à convertir
    """

    if est_majuscule(caractère):
        return chr(ord(caractère) + 32)

    return caractère

#print(maj_to_min("c"))

#==============================================================Exercice 16=====================================================================

def majuscules(chaine: str)-> str:
    """
    Fct pour faire passer toute une chaine en majuscule
     -chaine: chaine de caractères à convertir
    """

    cpy_str = ""

    for c in chaine:
        cpy_str += min_to_maj(c)

    return cpy_str

#print(majuscules("IAMTheBest"))

def minuscules(chaine: str)-> str:
    """
    Fct pour faire passer toute une chaine en minuscule
     -chaine: chaine de caractères à convertir
    """

    cpy_str = ""

    for c in chaine:
        cpy_str += maj_to_min(c)

    return cpy_str

#print(minuscules("ILovePython"))
