pipeline {
  agent any
  stages {
    stage('initialize') {
      steps {
        bat 'maven install'
      }
    }
  }
  environment {
    maven = 'Maven 3.5.4'
    jdk = 'jdk8'
  }
}