pipeline {
  agent any
  environment {
    IMAGE_NAME     = 'glowskin-backend'
    CONTAINER_NAME = 'glowskin_backend'
  }
  stages {
    stage('Clonar Repositorio') {
      steps {
        git branch: 'main',
            url: 'https://github.com/TU_USUARIO/glowskin-ci.git'
      }
    }
    stage('Instalar Dependencias') {
      steps {
        sh 'pip install -r backend/requirements.txt'
      }
    }
    stage('Ejecutar Pruebas') {
      steps {
        sh 'pytest backend/tests/ -v --junitxml=results.xml'
      }
      post {
        always { junit 'results.xml' }
      }
    }
    stage('Construir Imagen Docker') {
      steps {
        sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ./backend'
      }
    }
    stage('Desplegar Contenedores') {
      steps {
        sh 'docker-compose down || true'
        sh 'docker-compose up -d --build'
      }
    }
  }
  post {
    success { echo 'Pipeline exitoso' }
    failure { echo 'Pipeline fallido - revisar logs' }
  }
}
