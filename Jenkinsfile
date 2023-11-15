pipeline {
agent {
        docker {
            // Use a Docker image with Python and Pip
            image 'python:3.8'
        }
    }


    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }
}
}
