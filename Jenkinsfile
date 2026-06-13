pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'cd /Users/nishantsingh/Downloads/Playwright && source venv/bin/activate && pip install playwright pytest-playwright pytest-html'
            }
        }
        stage('Install Browsers') {
            steps {
                sh 'cd /Users/nishantsingh/Downloads/Playwright && source venv/bin/activate && playwright install chromium'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'cd /Users/nishantsingh/Downloads/Playwright && source venv/bin/activate && pytest tests/test_login.py -k "test_valid_login" --override-ini="addopts=--browser chromium" --headless'
            }
        }
    }
}
