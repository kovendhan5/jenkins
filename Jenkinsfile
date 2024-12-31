pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/kovendhan5/jenkins.git'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Deploy to Staging') {
            steps {
                sh 'scp target/your-app.jar user@staging-server:/path/to/deploy'
            }
        }
        stage('Deploy to Production') {
            steps {
                input 'Deploy to production?'
                sh 'scp target/your-app.jar user@production-server:/path/to/deploy'
            }
        }
    }
}
