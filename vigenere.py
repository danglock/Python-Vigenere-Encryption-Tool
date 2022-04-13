#!/usr/bin/env python
# encoding:utf-8

"""
Utilisation des commandes :

    Pour chiffrer :
        ./vigenere.py -k "key"

    Pour chiffrer le contenu d'un fichier
        ./vigenere.py -k "key" -i "InputFile.txt"

    Pour chiffrer le contenu d'un fichier ainsi que préciser un chemin de sortie
        ./vigenere -k "key" -i "InputFile.txt" -o "OutputFile.txt"
"""

import argparse

example_text = "example: python vigenere.py -k 'VotreClefDeCryptage' -EF FileToEncrypt.txt -OF output.txt\n"

parser = argparse.ArgumentParser(
    description="Permet de réaliser différentes commandes de chiffrement par substitution polyalphabétique",
    epilog=example_text)

# Définir une description pour les arguments

parser.add_argument("-k", "--key", metavar="", required=False, help="Définir une clé")
# Argument permettant de définir la clé de chiffrement
parser.add_argument("-e", "--encrypt", metavar="", required=False, help="Définir un texte à chiffrer.")
# Argument permettant de définir le texte à chiffrer
parser.add_argument("-EF", "--encryptFile", metavar="", required=False, help="Définir un fichier à chiffrer.")
# Argument permettant de chiffrer le texte d'un fichier
parser.add_argument("-d", "--decrypt", metavar="", required=False, help="Définir un texte à déchiffrer.")
# Argument permettant à déchiffrer un texte
parser.add_argument("-DF", "--decryptFile", metavar="", required=False, help="Définir un fichier à déchiffrer.")
# Argument permettant à déchiffrer le texte d'un fichier
parser.add_argument("-OF", "--outputFile", metavar="", required=False, help="Définir un fichier de sortie.")
# Argument permettant de sauvegarder le résultat d'une commande dans un fichier

args = parser.parse_args()


def code(key):
    if key.islower():  # Si la lettre est une majuscule
        return ord(key) - 97  # Retourne le caractère ascii relatif
    if key.isupper():  # Si la lettre est une majuscule
        return ord(key) - 65  # Retourne le caractère ascii relatif


def encrypt(cle, plaintext):
    # Création d'une fonction "encrypt" avec options "cle" (clé de chiffrement) et "plaintext" (text à chiffrer)

    j = 0  # Initialisation d'un compteur de lettres
    ciphertext = ""  # Initialisation d'un message chiffré

    for letters in plaintext:  # Pour chaque lettre du texte à chiffrer :
        if letters.islower():  # Si la lettre est une minuscule :
            ciphertext += chr(((ord(letters) - 97 + code(
                cle[j])) % 26) + 97)  # Chiffrer la lettre et l'ajouter à la suite du texte chiffré
            j += 1  # Ajouter 1 au compteur
        if letters.isupper():  # Si la lettre est une minuscule :
            ciphertext += chr(((ord(letters) - 65 + code(
                cle[j])) % 26) + 65)  # Chiffrer la lettre et l'ajouter à la suite du texte chiffré
            j += 1  # Ajouter 1 au compteur
        if j == len(cle):  # Si le compteur est égal à la longueur de la clé :
            cle += cle  # Ajouter la clé à la clé (cela permet d'avoir une clé plus petite que le texte)
        if not letters.isalpha():  # Si la lettre n'est pas entre a et z (caractères spéciaux)
            ciphertext += letters
            # Alors, nous n'opérons aucun chiffrement et ajoutons simplement le caractère au texte chiffré

    return ciphertext  # Finalement, on retourne le texte chiffré


def decrypt(cle, ciphertext):
    # Création d'une fonction "decrypt" avec options "cle" (clé de chiffrement) et "ciphertext" (text chiffré)

    j = 0  # Initialisation d'un compteur de lettres
    textauclaire = ""  # Initialisation d'un text claire

    for letters in ciphertext:  # Pour chaque lettre du texte à chiffrer :
        if letters.islower():  # Si la lettre est une minuscule :
            textauclaire += chr(
                ((ord(letters) - 97 - code(cle[j])) % 26) + 97)  # Déchiffrer la lettre et l'ajouter au text claire
            j += 1  # Ajouter 1 au compteur
        if letters.isupper():  # Si la lettre est une majuscule :
            textauclaire += chr(
                ((ord(letters) - 65 - code(cle[j])) % 26) + 65)  # Déchiffrer la lettre et l'ajouter au text claire
            j += 1  # Ajouter 1 au compteur
        if j == len(cle):  # Si le compteur est égal à la longueur de la clé
            cle += cle  # Ajouter la clé à la clé (cela permet d'avoir une clé plus petite que le texte)
        if not letters.isalpha():  # Si la lettre n'est pas entre a et z (caractères spéciaux)
            textauclaire += letters
            # Alors, nous n'opérons aucun chiffrement et ajoutons simplement le caractère au texte chiffré

    return textauclaire  # Finalement, on retourne le text claire


if __name__ == '__main__':

    if args.key and not (args.encrypt or args.encryptFile or args.decrypt or args.decryptFile):
        print("L'argument -k doit être accompagné d'au moins 1 des arguments suivants: -e, -E, -d, -D")

    elif args.key and args.encrypt:  # Si l'utilisateur choisit -k et -e
        print("Encrypted data =", encrypt(args.key, args.encrypt))
        # Chiffrer le contenu de l'argument "-e" avec la clé et afficher le résultat

        if args.outputFile:  # Si l'utilisateur choisit l'argument -OF
            vigenere_output = open(args.outputFile, mode="w")  # Créer un fichier avec open()
            vigenere_output.write(encrypt(args.key, args.encrypt))  # Écrire le résultat dans le fichier
            print(f"Encrypted to: {args.outputFile}")  # Avertir l'utilisateur du bon déroulement de l'opération
            vigenere_output.close()  # Fermer le fichier

    elif args.key and args.encryptFile:  # Si l'utilisateur choisit -k et -EF
        print(f"\nOuverture du fichier : {args.encryptFile}")  # Afficher le nom du fichier en cours d'ouverture
        source_file = open(args.encryptFile, mode="r")  # Ouvrir le fichier avec open en mode lecture
        content = source_file.read()  # Stocker le contenu du fichier dans la variable content
        print(
            f"Le contenu du fichier est : {content}\nLe contenu chiffré est : {encrypt(args.key, content)}")
        # Afficher le contenu du fichier original ainsi que son contenu une fois chiffré

        if args.outputFile:  # Si l'utilisateur choisit l'argument -O
            vigenere_output = open(args.outputFile, mode="w")  # Créer un fichier avec open()
            vigenere_output.write(encrypt(args.key, content))  # Écrire le résultat dans le fichier
            print(f"Encrypted to: {args.outputFile}")  # Avertir l'utilisateur du bon déroulement de l'opération
            vigenere_output.close()  # Fermer le fichier

        source_file.close()  # Fermer le fichier source

    elif args.key and args.decrypt:  # Si l'utilisateur choisi -k et -d
        print("Decrypted data =", decrypt(args.key, args.decrypt))
        # Déchiffrer le contenu de l'argument "-d" avec la clé et afficher le résultat

        if args.outputFile:  # Si l'utilisateur a choisi l'argument -OF
            vigenere_output = open(args.outputFile, mode="w")  # Créer un fichier avec open()
            vigenere_output.write(encrypt(args.key, args.decrypt))  # Écrire le résultat dans le fichier
            print(f"Encrypted to: {args.outputFile}")  # Avertir l'utilisateur du bon déroulement de l'opération
            vigenere_output.close()  # Fermer le fichier

    elif args.key and args.decryptFile:  # Si l'utilisateur choisi -k et -DF
        print(f"\nOuverture du fichier : {args.decryptFile}")  # Afficher le nom du fichier en cours d'ouverture
        source_file = open(args.decryptFile, mode="r")  # Ouvrir le fichier avec open en mode lecture
        content = source_file.read()  # Stocker le contenu du fichier dans la variable content
        print(
            f"Le contenu du fichier est : {content}\nDecrypted data = {decrypt(args.key, content)}")
        # Afficher le contenu du fichier, le déchiffrer avec la clé et afficher le résultat

        if args.outputFile:  # Si l'utilisateur choisit l'argument -OF
            vigenere_output = open(args.outputFile, mode="w")  # Créer un fichier avec open()
            vigenere_output.write(decrypt(args.key, content))  # Écrire le résultat dans le fichier
            print(f"Decrypted to: {args.outputFile}")  # Avertir l'utilisateur du bon déroulement de l'opération
            vigenere_output.close()  # Fermer le fichier

        source_file.close()  # Fermer le fichier source

    else:
        print(
            "Mauvaise utilisation de la commande !\n")
        # En cas d'erreur de frappe / commande inconnue etc.... (tout ce qui n'aurait pas fonctionné)
        parser.print_help()

# Author : danglock 'ЯΛłКФ#1106', AlexGirardin 'AlexioShow#1167'.
