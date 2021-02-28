pipeline 
{
    agent 
    {
       label 'pipe'
    }
    stages 
    {

        stage("connect to dockerhub")
       {

          steps
          {
                sh 'make image '
                sh 'make push '

           }
       }

    }

}

