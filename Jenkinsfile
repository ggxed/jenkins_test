pipeline {
    agent {
       label "мастер"
    }
    tage("Build") {
       steps {
          // Just print a Hello, Pipeline to the console
          echo "Hello, Pipeline!"
          // Compile a Java file. This requires JDKconfiguration from Jenkins
          py test_Main.py     
          py test_Main 
          sh "ls -ltr"
       }
    }
} 
