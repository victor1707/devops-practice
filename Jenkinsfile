pipeline {
  agent any
  stages {
    stage('Test') {
      steps { sh 'python3 test_app.py' }
    }
    stage('Deploy nginx') {
      steps {
        // token = Jenkins "Secret text" credential for the jenkins service account, never committed
        withCredentials([string(credentialsId: 'kind-lab-token', variable: 'TOKEN')]) {
          // shortcut: skips TLS check of the lab cluster; for real clusters pass --certificate-authority
          sh '''
            K="/snap/bin/kubectl --server=https://192.168.29.170:16444 --token=$TOKEN --insecure-skip-tls-verify"
            $K apply -f k8s/nginx.yaml
            $K wait --for=condition=Ready pod/nginx --timeout=120s
            $K get pod nginx -o wide
          '''
        }
      }
    }
    // TODO (lesson 4): stage('Build') -> docker build -t devops-practice:${BUILD_NUMBER} .
    // TODO (lesson 4): stage('Push')  -> push to Docker Hub using a Jenkins credential (never hard-code it)
    // TODO (lesson 6): stage('Deploy') -> kubectl set image deployment/devops-practice app=...:${BUILD_NUMBER}
  }
}
