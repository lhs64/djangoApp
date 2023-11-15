pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8.12'
    }

    tools {
        // Define the Python tool with the specified version
           jdk "${PYTHON_VERSION}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies using pip
                    sh "python -m pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run Django tests or other commands
                    sh "python manage.py test"
                }
            }
        }

        // Add more stages as needed (e.g., deployment, additional testing)

    }

    post {
        success {
            echo 'All stages passed. Job successful!'
        }
        failure {
            echo 'One or more stages failed. Job failed!'
        }
    }
}
