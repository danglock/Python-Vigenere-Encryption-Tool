#!/usr/bin/env python
#encodinng:utf-8

import argparse # Nous en avons besoin pour gérer les commandes

parser = argparse.ArgumentParser(description="Permet de chiffrer un fichier")

parser.add_argument("-k","--key", metavar="", required=False, help="Definir une clé")
parser.add_argument("-i","--input", metavar="", required=False, help="Definir un text")
parser.add_argument("-d","--decrypt", metavar="", required=False, help="Definir un text")
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
			cle += cle		# ajouter la clé à la clé (cela permet d'avoir une clé plus petite que le texte)
		if not letters.isalpha():		# Si la lettre n'est pas entre a et z (charactères spéciaux)
			ciphertext += letters		# Alors, nous n'opérons aucun chiffrement et ajoutons simplement le charactère au texte chiffré

	return ciphertext	# Finalement, on retourne le texte chiffré


def decrypt (cle, ciphertext):
	def code(j):
		key = cle[j]
		if key.islower():
			return ord(key) - 97
		if key.isupper():
			return ord(key) - 65
	
	j = 0
	textclaire = ""
	
	for letters in ciphertext:
		if letters.islower():
			textclaire += chr(((ord(letters) - 97 - code(j)) % 26) + 97)
			j += 1
		if letters.isupper():
			textclaire += chr(((ord(letters) - 65 - code(j)) % 26) + 65)
			j += 1
		if j == len(cle):
			cle += cle
		if not letters.isalpha():
			textclaire += letters
						
	return textclaire


if __name__ == '__main__':
	#if args.encryp
	
	if args.key and args.input:
		print("Encrypted data =", encrypt(args.key, args.input))
	elif args.key and args.decrypt:
		print("Decrypted data =", decrypt(args.key, args.decrypt))
	else:
		print(encrypt("test", "ok"))
		
