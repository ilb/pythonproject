pipeline {
    agent any

    environment {
       APPNAME = "pythonproject"
    }

    parameters {
        booleanParam(
            name: "RELEASE",
            description: "Build a release from current commit.",
            defaultValue: false)
    }

    stages {
        stage ('Build') {
            when {
                expression { !params.RELEASE }
            }
            steps {
                sh '/opt/bin/pyupdate-remote.sh ${APPNAME}'
                sh '/opt/bin/pyinstall-remote.sh ${APPNAME}'
            }
        }

        stage ('Release') {
            when {
                expression { params.RELEASE }
            }
            steps {
                sh '/opt/bin/pyupdate-remote.sh ${APPNAME}'
                sh '/opt/bin/pyinstall-remote.sh ${APPNAME}'
                sh '/opt/bin/pypublish-remote.sh ${APPNAME}'
            }
        }
    }
}
