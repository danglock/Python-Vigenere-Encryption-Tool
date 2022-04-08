# V.E.T - Vignere Encryption Tool
Le chiffrement Vigenère.
Un code Open Source permettant d'effectuer un chiffrement par substitution polyalphabétique.

## Installation
**Prérequis :** [python](https://www.python.org/downloads/)

### Windows
[Télécharger le repository](https://github.com/danglock/V.E.T-Vigenere-Encryption-Tool/archive/refs/heads/main.zip)
### UNIX/Linux
Télécharger le repository avec la commande suivante :
```bash
git clone 
```
Rendre le fichier exécutable
```bash
chmod +x vigenere.py
```

***
## Usage

**Attention !**, veuillez **remplacer** ``./vigenere.py`` par ``python vigenere.py`` dans le cadre d'une utilisation sous **OS Windows**.

Voici la commande permettant d'effectuer un chiffrement Vigenère :
```
./vigenere.py -k "key"
```

Chiffrer le contenu d'un fichier. (si aucun chemin de sortie n'est spécifié, alors le fichier de sortie se trouvera dans le même répertoire que celui d'entrée) :
```bash
./vignere.py -k "key" -i "InputFile.txt"
```

Chiffrer le contenu d'un fichier, puis préciser un chemin de sortie :

```bash
./vignère -k "key" -i "InputFile.txt" -o "OutputFile.txt"
```
***
## A propos

Ce script à été développé dans un cadre d'étude de l'interpréteur python et du chiffrement. Nous déclinons toutes responsabilités quant à une utilisation malintentionnée.

**Auteur :** danglock

**Date :** 08.04.2022
