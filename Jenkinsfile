
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out VoltX source code'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install pytest
                '''
            }
        }

        stage('Run Automated Tests') {
            steps {
                sh '''
                    .venv/bin/python -m pytest -v
                '''
            }
        }
    }

    post {
        success {
            echo 'VoltX CI Pipeline completed successfully!'
        }

        failure {
            echo 'VoltX CI Pipeline failed. Check the test results.'
        }
    }
}

