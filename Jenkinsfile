pipeline {
    agent {
       label "deploy"
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
