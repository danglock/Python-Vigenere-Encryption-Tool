# Python Vignere Encryption Tool
Le chiffrement Vigenère.
Un code Open Source permettant d'effectuer un chiffrement par substitution polyalphabétique.

## Installation
**Prérequis :** [python](https://www.python.org/downloads/)

### Windows
[Télécharger le repository](https://github.com/danglock/V.E.T-Vigenere-Encryption-Tool/archive/refs/heads/main.zip)
### UNIX/Linux
Télécharger le repository avec la commande suivante :
```bash
git clone https://github.com/danglock/Python-Vigenere-Encryption-Tool.git
```
Entrer dans le repository
```bash
cd Python-Vigenere-Encryption-Tool
```  

Rendre le fichier exécutable
```bash
chmod +x vigenere.py
```

## Usage

**Attention !**, veuillez **remplacer** ``./vigenere.py`` par ``python vigenere.py`` dans le cadre d'une utilisation sous **OS Windows**.

Voici la commande permettant d'effectuer un chiffrement Vigenère :
```
./vigenere.py -k "key"
```

Chiffrer un text :
```bash
./vignere.py -k "key" -e "TextToEncrypt"
```

Chiffrer le contenu d'un fichier, puis préciser un chemin de sortie :

```bash
./vignère -k "key" -E "InputFile.txt" -O "OutputFile.txt"
```
***
## A propos

Ce script à été développé dans un cadre d'étude de l'interpréteur python et du chiffrement. Nous déclinons toutes responsabilités quant à une utilisation malintentionnée.

Message destiné aux élèves de l'EPSIC : Si vous utilisez ce code dans le cadre d'un examen, vous pouvez vous en inspirer mais ne pas le copier

**Auteur :** danglock

**Date :** 08.04.2022
