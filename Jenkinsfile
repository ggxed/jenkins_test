 pipeline {
    agent {
       label "deploy"
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
