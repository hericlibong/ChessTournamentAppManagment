# Chess Game OffLine Software

![picture_chess](media/chess.png)

## Table des Matières
I.  [Présentation](#i-présentation)
II. [Initialisation du projet](#ii-initialisation-du-projet)
   - [Windows](#windows)
   - [MacOS et Linux](#macos-et-linux)
III. [Générer un rapport flake8](#iii-générer-un-rapport-flake8)
IV. [Options des menus](#iv-options-des-menus)
   - [Menu principal](#menu-principal)
   - [Rapports](#rapports)


## I - Présentation

Chess Game OffLine Software est une application desktop développée en Python destinée à la gestion de tournois d'échecs hors ligne. Cette application permet aux organisateurs de tournois d'échecs de créer, gérer et suivre le déroulement de leurs événements en toute simplicité. Le logiciel permet à l'utilisateur de créer de tournois, d'inscrire des joueurs, de gérer les rounds, des joueurs et d'afficher les résultats. Les données sont sauvegardées au format json dans `util/data/tournaments.json` et `util/data/players.json`.  

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
pip install -r requirements.txt
```

6. Allez dans le dossier de l'application:
```
ChessTournamentAPP
```

7. Lancez l'application :

```
python main.py
```

## III - Générer un rapport flake8

Pour générer un rapport flake8 afin de vérifier la conformité du code aux standards de codage Python, utilisez la commande suivante :

```
flake8 --format=html --htmldir=flake-report
```

Ouvrir `index` dans le dossier `flake-report` 

![flake8_report](media/flake8.png)


## IV - Options des menus



Le menu principal offre plusieurs options pour gérer le tournoi :

### Menu principal et gestion tournoi

![menu_principal](media/menu_principal_tournament.png)


###  Gestions des Joueurs

![menu_joueur](media/menu_player.png)

### Rapports

Le menu des rapports permet d'accéder aux résultats :



![rapports](media/rapport.png)









