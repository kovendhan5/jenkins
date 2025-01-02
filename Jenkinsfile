pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/kovendhan5/jenkins.git'
            }
        }
        stage('Build') {
            steps {
                bat 'mvn clean install'
            }
        }
        stage('Test') {
            steps {
                bat 'mvn test'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t kovendhan-jenkins .'
            }
        }
        stage('Deploy to Staging') {
            steps {
                bat 'docker run -d -p 8081:8080 --name staging-container kovendhan-jenkins'
            }
        }
        stage('Deploy to Production') {
            steps {
                input 'Deploy to production?'
                bat 'docker stop staging-container && docker rm staging-container'
                bat 'docker run -d -p 8080:8080 --name production-container kovendhan-jenkins'
            }
        }
    }
}
