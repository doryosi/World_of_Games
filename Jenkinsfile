pipeline {

    agent any
    environment{
    DOCKERHUB_CREDENTIALS = credentials('doryosisinay-dockerhub')
    }
    stages {
        stage('Checkout') {
            steps {
              checkout([$class: 'GitSCM',
                branches: [[name: '*/master']],
                userRemoteConfigs: [[url: 'https://github.com/doryosi/World_of_Games']]])
              git "https://github.com/doryosi/World_of_Games"
          }
        }
        stage('Build'){
            steps{
                sh "docker build -t doryosisinay/world_of_games:WOG ."
                }
            }
        stage('Run'){
            steps{
                sh "docker-compose up -d"
                }
            }
        stage('Test'){
            steps{
                sh "python3 MainScore.py"
                sh "python3 tests/e2e.py"
                }
            }
        stage('Login'){
            steps{
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
            }
        stage('Push'){
            steps{
                sh "docker push doryosisinay/world_of_games:WOG"
                }
            }
        }
    post{
        always{
            sh "docker logout"
        }
    }
}
