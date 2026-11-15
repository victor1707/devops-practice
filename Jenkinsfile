pipeline {
  agent any
  stages {
    stage('Test') {
      steps { sh 'python3 test_app.py' }
    }
    stage('Deploy nginx') {
      steps {
        // kubeconfig is a Jenkins "Secret file" credential, never committed to GitHub
        withCredentials([file(credentialsId: 'kind-kubeconfig', variable: 'KUBECONFIG')]) {
          sh '''
            /snap/bin/kubectl apply -f k8s/nginx.yaml
            /snap/bin/kubectl wait --for=condition=Ready pod/nginx --timeout=120s
            /snap/bin/kubectl get pod nginx -o wide
          '''
        }
      }
    }
    // TODO (lesson 4): stage('Build') -> docker build -t devops-practice:${BUILD_NUMBER} .
    // TODO (lesson 4): stage('Push')  -> push to Docker Hub using a Jenkins credential (never hard-code it)
    // TODO (lesson 6): stage('Deploy') -> kubectl set image deployment/devops-practice app=...:${BUILD_NUMBER}
  }
}
