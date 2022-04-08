#!/usr/bin/env python
#encodinng:utf-8

import argparse # Nous en avons besoin pour gérer les commandes

parser = argparse.ArgumentParser(description="Permet de chiffrer un fichier")

parser.add_argument("-k","--key", metavar="", required=False, help="Definir une clé")
parser.add_argument("-i","--input", metavar="", required=False, help="Definir un text à chiffrer")
parser.add_argument("-d","--decrypt", metavar="", required=False, help="Definir un text à déchiffer")

args = parser.parse_args()



def encrypt (cle, plaintext):	# Création d'une fonction "encrypt" avec options "cle" et "plaintext"

	def code(j):
		key = cle[j]			# 
		if key.islower():		# Si la lettre est une majuscule
			return ord(key) - 97	# retourne le charactère ascii relatif
		if key.isupper():		# Si la lettre est une majuscule
			return ord(key) - 65	# Retourne le charactère ascii relatif
			
	j = 0 				# Initialisation d'un compteur de lettres
	ciphertext = ""			# Initialisation d'un message chiffré

	for letters in plaintext:							# Pour chaques lettres du texte à chiffrer :
		if letters.islower():							# Si la lettre est une minuscule :
			ciphertext += chr(((ord(letters) - 97 + code(j)) % 26) + 97)	# Chiffrer la lettre et l'ajouter à la suite du texte chiffré
			j += 1								# Ajouter 1 au compteur
		if letters.isupper():								# Si la lettre est une minuscule:
			ciphertext += chr(((ord(letters) - 65 + code(j)) % 26) + 65)		# Chiffrer la lettre et l'ajouter à la suite du texte chiffré
			j += 1									# Ajouter 1 au compteur
		if j == len(cle):		# Si le compteur est égal à la longueure de la clé :
			cle += cle		# Ajouter la clé à la clé (cela permet d'avoir une clé plus petite que le texte)
		if not letters.isalpha():		# Si la lettre n'est pas entre a et z (charactères spéciaux)
			ciphertext += letters		# Alors, nous n'opérons aucun chiffrement et ajoutons simplement le charactère au texte chiffré

	return ciphertext	# Finalement, on retourne le texte chiffré




def decrypt (cle, ciphertext):	# Création d'une fonction "decrypt" avec options "cle" et "ciphertext"

	def code(j):
		key = cle[j]
		if key.islower():
			return ord(key) - 97
		if key.isupper():
			return ord(key) - 65
			
	j = 0				# Initialisation d'un compteur de lettres
	textclaire = ""			# Initialisation d'un text claire
	
	for letters in ciphertext:							# Pour chaques lettres du texte à chiffrer :
		if letters.islower():							# Si la lettre est une minuscule :
			textclaire += chr(((ord(letters) - 97 - code(j)) % 26) + 97)	# Déchiffrer la lettre et l'ajouter au text claire
			j += 1								# Ajouter 1 au compteur
		if letters.isupper():								# Si la lettre est une majuscule :
			textclaire += chr(((ord(letters) - 65 - code(j)) % 26) + 65)		# Déchiffrer la lettre et l'ajouter au text claire
			j += 1									# Ajouter 1 au compteur
		if j == len(cle):		# Si le compteur est égal à la longueur de la clé
			cle += cle		# Ajouter la clé à la clé (cela permet d'avoir une clé plus petite que le texte)
		if not letters.isalpha():		# Si la lettre n'est pas entre a et z (charactère spéciaux)
			textclaire += letters		# Alors, nous n'opérons aucun chiffrement et ajoutons simplement le charactère au texte chiffré
						
	return textclaire	# Finalement, on retourne le text claire



if __name__ == '__main__':
	
	if args.key and args.input:
		print("Encrypted data =", encrypt(args.key, args.input))
		
	elif args.key and args.decrypt:
		print("Decrypted data =", decrypt(args.key, args.decrypt))
		
	else:
		print("Mauvaise utilisation de la commande !\nEssayez python vigenere.py --help")
