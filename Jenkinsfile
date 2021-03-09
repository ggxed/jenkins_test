pipeline 
{
    agent 
    {
       label 'мастер'
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
