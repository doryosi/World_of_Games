pipeline {

    agent any
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
