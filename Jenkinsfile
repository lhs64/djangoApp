pipeline {
agent any

    environment {
        PYTHONPATH = "${workspace}"
    }
    stages {
        stage('Checkout') {
        steps{
              checkout scm
        }
        }

        stage('Install Dependencies') {
            steps{
                 script {
                    sh 'pip install -r requirements.txt'
                }
                
            }
        }

        stage('Run Tests') {
          steps{
              script {
                    sh 'python manage.py test'
                }
    
          }
        }
}
}
