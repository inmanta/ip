pipeline {
    agent any

    options{
        disableConcurrentBuilds()
    }

    environment {
        INMANTA_MODULE_REPO='https://github.com/inmanta/'
        INMANTA_TEST_ENV="${env.WORKSPACE}/env"
    } 

    stages {
        stage('Test') {
            steps {
                sh 'rm -rf $INMANTA_TEST_ENV; python3 -m venv $INMANTA_TEST_ENV; $INMANTA_TEST_ENV/bin/python3 -m pip install -U  inmanta pytest-inmanta; $INMANTA_TEST_ENV/bin/python3 -m pip install -r requirements.txt'
                sh '$INMANTA_TEST_ENV/bin/python3 -m pytest --junitxml=junit.xml -vvv tests'
            }
        }
    }

    post {
        always {
            junit 'junit.xml'
        }
    }
}