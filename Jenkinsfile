pipeline {
  agent any
  stages {
    stage('Test') {
      steps { sh 'python3 test_app.py' }
    }
    // TODO (lesson 4): stage('Build') -> docker build -t devops-practice:${BUILD_NUMBER} .
    // TODO (lesson 4): stage('Push')  -> push to Docker Hub using a Jenkins credential (never hard-code it)
    // TODO (lesson 6): stage('Deploy') -> kubectl set image deployment/devops-practice app=...:${BUILD_NUMBER}
  }
}
