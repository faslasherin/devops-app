pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'faslasherin/devops-app:1.0'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source repository...'
            }
        }

        stage('Test') {
            steps {
                echo 'Setting up environment and executing Pytest...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }

        stage('Build & Push') {
            steps {
                echo 'Compiling image and deploying to Docker Hub...'
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', 
                                                      usernameVariable: 'DOCKER_USER', 
                                                      passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                            echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USER" --password-stdin
                            docker build -t ${DOCKER_IMAGE} .
                            docker push ${DOCKER_IMAGE}
                        '''
                    }
                }
            }
        }
    }
}
