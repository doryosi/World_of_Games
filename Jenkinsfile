pipeline {
    agent any
    environment{
    DOCKERHUB_CREDENTIALS = credentials('doryosisinay-dockerhub')
    USER = "doryosi"
    PROJ_NAME = "World_of_Games"
    PROJ_BRANCH = "master"
    IMAGE = "WOG_Web_App"
    NODE_NAME = "WOG_Node"
    PORT = "5001"
    FLASK_SERVER_URL = "http://127.0.0.1:${PORT}"
    }
    stages {
        stage('Checkout') {
            steps {
              checkout([$class: 'GitSCM',
                branches: [[name: "*/$PROJ_BRANCH"]],
                userRemoteConfigs: [[url: "https://github.com/$USER/$PROJ_NAME"]]])
              git "https://github.com/$USER/$PROJ_NAME"
          }
        }
        stage('Build docker image'){
            steps{
                sh "docker-compose build"
                }
            }
        stage('Run'){
            steps{
                sh "docker-compose up -d"
                }
            }
        stage('Test'){
            steps{
                sh "docker-compose exec web python3 e2e.py"
                }
            }
        stage('Login'){
            steps{
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
            }
        stage('Push'){
            steps{
                sh "docker compose push"
                }
            }
        }
    post{
        always{
            sh "docker compose down -v"
            sh "docker image rm $USER/$PROJ_NAME"
            sh "docker logout"
        }
    }
}
