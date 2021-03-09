pipeline {
    agent {
       label "worker"
    }
    stages {
       stage("connect") {
          steps {
            script {
                println 'hello'
                sh "make image push"
            }
          }
       }
    }
}
