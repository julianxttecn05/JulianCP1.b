pipeline {
    agent none
    stages {
        stage('Get Code') {
            agent { label 'shared-agent' }
            steps {
                git 'https://github.com/julianxttecn05/JulianCP1.b.git'
                bat 'whoami'
                bat 'hostname'
                echo "Workspace: ${WORKSPACE}"
                stash includes: '**', name: 'source-code'
            }
        }

        stage('Unit and Coverage') {
            agent { label 'test-agent' }
            stages {
                stage('Unit Tests') {
                    steps {
                        unstash 'source-code'
                        bat '''
                        set PYTHONPATH=.
                        pytest --junitxml=result-unit.xml test\\unit
                        '''
                        junit 'result*.xml'
                    }
                }
                stage('Code Coverage') {
                    steps {
                        unstash 'source-code'
                        bat '''
                        coverage run --branch --source=app --omit=app\\__init__.py,app\\api.py -m pytest test\\unit
                        coverage xml
                        '''
                        cobertura coberturaReportFile: 'coverage.xml',
                                  lineCoverageTargets: '100,0,95',
                                  branchCoverageTargets: '100,0,90',
                                  onlyStable: false
                    }
                }
            }
        }
    }
}
