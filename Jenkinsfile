pipeline {
  stages {
    stage("Build") {
       steps {
          // Just print a Hello, Pipeline to the console
          echo "Hello, Pipeline!"
          // Compile a Java file. This requires JDKconfiguration from Jenkins
          python test_Main.py     
       }
   }
   // And next stages if you want to define further...
 } // End of stages
} // End of pipeline



