# Bibliothèque Numérique DIT

## Présentation

La Bibliothèque Numérique DIT est une application développée dans le cadre de l'examen DevOps du Dakar Institute of Technology (DIT).

L'application repose sur une architecture microservices permettant de gérer :

- Les livres
- Les utilisateurs
- Les emprunts
- Les retards

Le projet met en œuvre les technologies DevOps suivantes :

- Docker
- Docker Compose
- Jenkins
- GitHub
- PostgreSQL

---

## Fonctionnalités

### Gestion des Livres

- Ajouter un livre
- Modifier un livre
- Supprimer un livre
- Consulter les livres
- Rechercher par titre, auteur ou ISBN

### Gestion des Utilisateurs

- Créer un utilisateur
- Consulter un profil
- Modifier un utilisateur
- Supprimer un utilisateur
- Gérer les types :
  - Étudiant
  - Professeur
  - Personnel administratif

### Gestion des Emprunts

- Emprunter un livre
- Retourner un livre
- Consulter l'historique
- Détecter les retards
- Calculer automatiquement :
  - la date limite
  - les jours restants
  - les jours de retard

### Tableau de Bord

- Nombre de livres
- Nombre d'utilisateurs
- Nombre d'emprunts
- Nombre total de retards

---

## Technologies

### Backend

- Python
- FastAPI
- SQLAlchemy

### Frontend

- HTML
- CSS
- JavaScript

### Base de Données

- PostgreSQL

### DevOps

- Docker
- Docker Compose
- Jenkins
- Git
- GitHub

---

## Architecture du Projet

bibliotheque-microservices/
├── backend-livres/
├── backend-utilisateurs/
├── backend-emprunts/
├── frontend/
├── docker-compose.yml
├── Jenkinsfile
└── README.md

---

## Installation

Cloner le projet :

git clone https://github.com/WAF-DIT/bibliotheque-microservices.git
cd bibliotheque-microservices

Construire les images :

docker compose build

Démarrer les services :

docker compose up -d

Arrêter les services :

docker compose down

---

## Accès aux Services

Frontend : http://localhost:3000

API Livres : http://localhost:8000/docs

API Utilisateurs : http://localhost:8001/docs

API Emprunts : http://localhost:8002/docs

PgAdmin : http://localhost:8080

---

## Pipeline Jenkins

Le pipeline Jenkins permet :

- Récupération du code depuis GitHub
- Exécution du Jenkinsfile
- Vérification de l'intégration du projet
- Construction des images Docker

Pipeline défini dans : Jenkinsfile

---

## Dépôt GitHub

https://github.com/WAF-DIT/bibliotheque-microservices.git

---

## Auteur

Projet réalisé dans le cadre de l'examen DevOps du Dakar Institute of Technology (DIT).

Groupe 4 – Année 2025-2026
