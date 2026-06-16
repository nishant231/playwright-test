pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }
        stage('Browser Tests') {
            parallel {
                stage('Chrome') {
                    steps {
                        echo 'Running tests on Chrome...'
                    }
                }
                stage('Firefox') {
                    steps {
                        echo 'Running tests on Firefox...'
                    }
                }
                stage('Safari') {
                    steps {
                        echo 'Running tests on Safari...'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }
    }
}
