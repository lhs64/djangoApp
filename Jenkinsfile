pipeline {
 agent   {
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
                // Install Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run Django tests
                sh 'python manage.py test'
            }
        }

        // Add more stages as needed
    }
}
