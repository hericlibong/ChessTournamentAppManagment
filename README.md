# Chess Game OffLine Software

![picture_chess](chess.png)

## Table des Matières
1. [Présentation](#i-présentation)
2. [Initialisation du projet](#ii-initialisation-du-projet)
   - [Windows](#windows)
   - [MacOS et Linux](#macos-et-linux)
3. [Générer un rapport flake8](#iii-générer-un-rapport-flake8)
4. [Options des menus](#iv-options-des-menus)
   - [Menu principal](#menu-principal)
   - [Rapports](#rapports)
5. [Exemples d'affichage](#v-exemples-daffichage)

## I - Présentation

Chess Game OffLine Software est une application desktop développée en Python destinée à la gestion de tournois d'échecs hors ligne. Cette application permet aux organisateurs de tournois d'échecs de créer, gérer et suivre le déroulement de leurs événements en toute simplicité. Grâce à son interface intuitive et ses fonctionnalités complètes, le logiciel offre une expérience utilisateur optimale pour la gestion des rounds, des joueurs et des résultats.

## II - Initialisation du projet

### Windows, MacOs, Linux

Pour installer et lancer le logiciel sous Windows, suivez ces étapes :

1. Clonez le dépôt GitHub :

 ```
https://github.com/hericlibong/ChessTournamentApp_p4.git
```

2. Naviguez dans le dossier du projet :

```
ChessTournamentApp_p4
```

3. Installez un environnement virtuel :
  ```
  python -m venv venv
  ```

4. Activez l'environnement virtuel :

- Sur Windows :
  ```
  venv\Scripts\activate
  ```
- Sur MacOS/Linux :
  ```
  source venv/bin/activate
  ```

5. Installez les dépendances :

```
pip install requirements.txt

```

6. Lancez l'application :

```
python main.py
```

## III - Générer un rapport flake8

Pour générer un rapport flake8 afin de vérifier la conformité du code aux standards de codage Python, utilisez la commande suivante :

```
flake8 --format=html --htmldir=flake-report
```

Ouvrir `index` dans le dossier `flake-report` 

![flake8_report](flake8.png)


## IV - Options des menus

### Menu principal

Le menu principal offre plusieurs options pour gérer le tournoi :

![menu_principal](menu_principal.png)

### Rapports

Le menu des rapports permet d'accéder à divers statistiques et résultats :

![rapports](rapports.png)

## V - Exemples d'affichage

Voici quelques exemples de l'interface utilisateur et des fonctionnalités du logiciel :

![exemple_affichage](exemple_affichage.png)







