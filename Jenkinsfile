pipeline {
    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                echo 'Récupération du code source'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Construction image Docker'
                sh 'docker build -t backend-livres ./backend-livres'
            }
        }

        stage('Verify Docker') {
            steps {
                echo 'Vérification Docker'
                sh 'docker ps'
            }
        }
    }

    post {

        success {
            echo ' Déploiement réussi'
        }

        failure {
            echo ' Échec du pipeline'
        }

        always {
            echo 'Pipeline terminé'
        }
    }
}