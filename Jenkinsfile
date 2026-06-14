pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'cd /Users/nishantsingh/Downloads/Playwright && source venv/bin/activate && pip install playwright pytest-playwright pytest-html allure-pytest'
            }
        }
        stage('Install Browsers') {
            steps {
                sh 'cd /Users/nishantsingh/Downloads/Playwright && source venv/bin/activate && playwright install chromium'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'rm -rf /Users/nishantsingh/Downloads/Playwright/allure-results'
                sh 'cd /Users/nishantsingh/Downloads/Playwright && source venv/bin/activate && pytest tests/test_login.py -k "test_valid_login" --override-ini="addopts=--browser chromium" --alluredir=/Users/nishantsingh/Downloads/Playwright/allure-results'
            }
        }
        stage('Upload Report'){
            steps {
                allure([
                    results: [[path: '/Users/nishantsingh/Downloads/Playwright/allure-results']]
                ])

            }
        }
    }
}
