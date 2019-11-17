pipeline {
  agent any
  triggers {
    pollSCM '* * * * *'
    cron 'H H(2-5) * * *'
  }
  options {
    disableConcurrentBuilds()
    checkoutToSubdirectory('ip')
  }

  environment {
      INMANTA_MODULE_REPO='https://github.com/inmanta/'
      INMANTA_TEST_ENV="${env.WORKSPACE}/env"
  }

  stages {
    stage("test"){
      steps{
        script{
          dir('ip'){
            sh """rm -rf $INMANTA_TEST_ENV;
                  python3 -m venv $INMANTA_TEST_ENV;
                  $INMANTA_TEST_ENV/bin/python3 -m pip install -r requirements.txt;
                  $INMANTA_TEST_ENV/bin/python3 -m pip install -U inmanta pytest-inmanta
               """
            sh '$INMANTA_TEST_ENV/bin/python3 -m pytest --junitxml=junit.xml -vvv tests'
          }
        }
      }
    }
  }
  post {
    always{
      always {
            junit 'ip/junit.xml'
        }
    }
  }

}