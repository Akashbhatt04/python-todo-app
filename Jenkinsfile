pipeline {
    agent any
    environment {
        SONARQUBE_ENV = 'LocalSonar'
        SONAR_SCANNER = 'SonarScanner'
    }

    triggers {
        cron('H 10 * * *') // Daily at 10 AM
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Akashbhatt04/python-todo-app.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile todo.py'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    sh "${tool SONAR_SCANNER}/bin/sonar-scanner"
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.pyc', fingerprint: true
            }
        }

        stage('Cleanup') {
            steps {
                cleanWs()
            }
        }
    }
}
