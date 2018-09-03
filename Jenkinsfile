pipeline {
  agent any
  stages {
    stage('initialize') {
      steps {
        bat 'java -version dir'
      }
    }
  }
  environment {
    maven = 'Maven 3.3.9'
    jdk = 'jdk8'
  }
}