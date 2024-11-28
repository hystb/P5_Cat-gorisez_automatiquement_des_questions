# Catégorisation Automatique de Questions - Projet P5

Ce projet vise à développer une API capable de suggérer automatiquement des tags pertinents pour des questions posées sur des plateformes telles que Stack Overflow.  
L'objectif est d'aider les utilisateurs, notamment les nouveaux, à catégoriser efficacement leurs questions en proposant des tags appropriés basés sur le contenu de la question.

---

## Objectifs du Projet

- Développer une API qui reçoit une question en entrée et retourne des tags suggérés.
- Utiliser des techniques de traitement du langage naturel (NLP) et des modèles d'apprentissage automatique pour la classification.
- Fournir une solution évolutive et facilement intégrable dans d'autres systèmes.

---

## Structure des Dossiers

- **`flask_app/`** : Contient le code source de l'API développée avec Flask.
    - **`app.py`** : Script principal pour lancer l'application Flask.
    - **`load.py`** : Module pour le chargement des données et des modèles.
    - **`model.py`** : Définition du modèles de machine learning.
    - **`tests.py`** : Scripts de tests pour valider le bon fonctionnement de l'API.
	- **`models/mlb_500T.pkl`** : Afin de convertir la reponse du model en text.
- **`model_training/`** : Notebooks pour l'entraînement des modèles de machine learning.
    - **`notebooks`** : Notebooks Jupyter pour l'exploration et l'expérimentation.
- **`frontend/`** : Code source du frontend de l'application.
    - **`index.html`** : Page d'accueil de l'application.
    - **`static/`** : Fichiers statiques tels que CSS, JavaScript, images.
- **`nginx/`** : Configuration pour le serveur Nginx.
    - **`nginx.conf`** : Fichier de configuration principal pour Nginx.
- **`docker/`** : Fichiers liés à la conteneurisation du projet avec Docker.
- **`docker-compose.yml`** : Fichier pour orchestrer les conteneurs Docker.
- **`.github/`** : Configurations pour les workflows GitHub Actions.
    - **`workflows/`** : Définit les workflows CI/CD pour le projet.
- **`.gitignore`** : Liste des fichiers et dossiers à ignorer par Git.
---

## Installation et Lancement de l'API avec Docker Compose

1. **Cloner le dépôt :**
    ```bash
    git clone https://github.com/hystb/P5_Cat-gorisez_automatiquement_des_questions.git
    cd P5_Cat-gorisez_automatiquement_des_questions
    ```

2. **Construire et lancer les conteneurs :**
    ```bash
    docker compose up --build
    ```

    Cela téléchargera les images nécessaires, construira les conteneurs et démarrera l'application.

3. **Accéder à l'application :**

    Une fois les conteneurs en cours d'exécution

    ```
    http://localhost
    ```

4. **Arrêter les conteneurs :**
    ```bash
    docker compose down
    ```

## Packages

	scikit-learn==1.3.1
	scipy==1.9.3
	cloudpickle==2.2.1
	mlflow==2.7.1
	numpy==1.25.2
	packaging==23.2
	psutil==6.1.0
	pandas==2.1.1
	tensorflow==2.14.0
	tensorflow-hub==0.13.0
