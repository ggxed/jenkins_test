pipeline {
    agent {
       label "worker"
    }
    stages {
       stage("connect") {
          steps {
            script {
                sh "make image push"
            }
          }
       }
    }
}
