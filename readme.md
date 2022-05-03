# Python Vigenère Encryption Tool
FR = Le **chiffre de Vigenère** est un système de [chiffrement par substitution](https://fr.wikipedia.org/wiki/Chiffrement_par_substitution "Chiffrement par substitution") polyalphabétique dans lequel une même lettre du message clair peut, suivant sa position dans celui-ci, être remplacée par des lettres différentes, contrairement à un système de chiffrement mono alphabétique comme le [chiffre de César](https://fr.wikipedia.org/wiki/Chiffre_de_C%C3%A9sar "Chiffre de César") (qu'il utilise cependant comme composant).

EN = The **Vigenère cipher** is a method of [encrypting](https://en.wikipedia.org/wiki/Encryption) [alphabetic](https://en.wikipedia.org/wiki/Alphabetic) text by using a series of interwoven [Caesar ciphers](https://en.wikipedia.org/wiki/Caesar_cipher), based on the letters of a keyword. It employs a form of [polyalphabetic substitution](https://en.wikipedia.org/wiki/Polyalphabetic_cipher).

<p align="center">
  <img src="https://iili.io/VAnXQn.md.png" />
</p>

## Prérequis // Requirements

<p>
<p align="center">
<a href="https://www.python.org/downloads/"><img style="display: block; margin-left: auto; margin-right: auto;" src="https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg" alt="W3Schools" width="436" height="139" border="0" />
</a>
</p>

## Installation

<h3><strong>Windows </strong>&nbsp;<img src="https://simpleicons.org/icons/windows.svg" alt="" width="20" height="20" /></h3>

[Télécharger le repository / Download the repository](https://github.com/danglock/V.E.T-Vigenere-Encryption-Tool/archive/refs/heads/main.zip)

<h3><strong>Linux / UX </strong>&nbsp;<img src="https://simpleicons.org/icons/linux.svg" alt="" width="25" height="25" /></h3>

Télécharger le repository avec la commande suivante // Download the repository with the following command  :

```bash
git clone https://github.com/danglock/Python-Vigenere-Encryption-Tool.git
```
Entrer dans le repository // Enter in the repository

```bash
cd Python-Vigenere-Encryption-Tool
```

Rendre le fichier exécutable // Make the file executable

```bash
chmod +x vigenere.py
```

## Utilisation / Use

**Attention !** Veuillez **remplacer** ``./vigenere.py`` par ``python vigenere.py`` lors d'une utilisation sous l'**OS Windows**.
**Warning !** Please replace ``./vigenere.py`` by ``python vigenere.py`` when using **Windows OS.**

Voici la commande permettant d'effectuer un chiffrement Vigenère : // Here is the command to perform a Vigenère encryption :

```
./vigenere.py -k "key"
```

Chiffrer un texte : // Encrypting a text :

```bash
./vignere.py -k "key" -e "TextToEncrypt"
```

Chiffrer le contenu d'un fichier, puis préciser un chemin de sortie : // Encrypt the contents of a file, then specify an output path:

```bash
./vignère -k "key" -EF "InputFile.txt" -OF "OutputFile.txt"
```

## Termes et conditions / Terms and conditions

Ce script a été développé dans un cadre d'étude de l'interpréteur python et du chiffrement. Nous déclinons toutes les responsabilités quant à une utilisation malintentionnée. // This script has been developed to study the python interpreter and encryption. We decline all responsibility for any malicious use. WARNING! THE CODE WILL ONLY RUN IN FRENCH!

------

**Auteur/Author :** danglock

**Contributeur/Contributor :** AlexioShow

**Date :** 08.04.2022
