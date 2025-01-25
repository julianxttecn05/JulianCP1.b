pipeline {
    agent any
    stages {
        stage('Get Code') {
            steps {
                // Obtener código del repo
                git 'https://github.com/julianxttecn05/JulianCP1.b.git'
                bat 'dir'
                echo WORKSPACE
            }
        }
        stage('Unit') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {
                    bat '''
                    set PYTHONPATH=.
                    pytest --junitxml=result-unit.xml test\\unit
                    '''
                    junit 'result*.xml'
                }
            }
        }


        stage('Coverage') {
            steps {
                bat '''
                coverage run --branch --source=app --omit=app\\__init__.py,app\\api.py -m pytest test\\unit
                coverage xml
                '''
                catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {
                    cobertura coberturaReportFile: 'coverage.xml', 
                              conditionalCoverageTargets: '100,0,90', 
                              lineCoverageTargets: '100,0,95',
                              onlyStable: false
                }
            }
        }
        
        stage('rest') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '''
                    set FLASK_APP=app\\api.py
                    start /B flask run
                    ping -n 10 127.0.0.1 > nul
                        start java -jar C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\wiremock-standalone-3.10.0.jar --port 9090 --root-dir C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\O24\\pipeline1\\test\\wiremock
                        
                        ping -n 10 127.0.0.1
                        
                        python -m pytest --junitxml=result-rest.xml test\\rest 
                    '''
                }
            }
        }        

        stage('Static') {
            steps {
                bat '''
                python -m flake8 --exit-zero --format=pylint app > flake8.out
                '''
                recordIssues tools: [flake8(name: 'Flake8', pattern: 'flake8.out')], 
                             qualityGates: [[threshold: 8, type: 'TOTAL', unstable: true], 
                                            [threshold: 10, type: 'TOTAL', unstable: false]]
            }
        }

        stage('Security') {
            steps {
                bat '''
                    bandit --exit-zero -r . -f custom -o bandit.out --msg-template "{abspath}:{line}: [{test_id}] {msg}"
                '''
                recordIssues tools: [pyLint(name: 'Bandit', pattern: 'bandit.out')], 
                             qualityGates: [
                                 [threshold: 2, type: 'TOTAL', unstable: true], 
                                 [threshold: 4, type: 'TOTAL', unstable: false]
                             ]
            }
        }

        stage('Performance') {
            steps {
                bat '''
                    set FLASK_APP=app\\api.py
                    start /B flask run
                    ping -n 10 127.0.0.1 > nul
                    C:\\Users\\julia\\Downloads\\apache-jmeter-5.6.3\\apache-jmeter-5.6.3\\bin\\jmeter -n -t test\\jmeter\\CP1B.jmx -f -l flask.jtl
                '''
                perfReport sourceDataFiles: 'flask.jtl'
            }
        }


    }
}

