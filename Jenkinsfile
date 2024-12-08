pipeline {
    agent any
    
    stages {
        stage('getcode'){
            steps {
                git 'https://github.com/julianxttecn05/CP1Julian.git'
            }
        }
        
        stage('build'){
            steps {
                echo 'No hay que compilar nada, esto es pyhon'
                bat "dir"
            }
        }
        
        stage('tests'){
            parallel{
                stage('unit') {
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE'){
                            bat '''
                                set PYTHONPATH=%WORKSPACE%
                                python -m pytest --junitxml=result-unit.xml test\\unit
                            '''
                                    
                        }
                                
                    }
                }
                        
                stage('rest') {
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE'){
                            bat '''
                                set FLASK_APP=app\\api.py
                                start flask run
                                timeout 5
                                curl http://127.0.0.1:5000/health || exit 1
                                start java -jar C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\wiremock-standalone-3.10.0.jar --port 9090 --root-dir C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\O24\\pipeline1\\test\\wiremock
                                timeout 5
                                curl http://127.0.0.1:9090/__admin || exit 1
                                set PYTHONPATH=%WORKSPACE%
                                python -m pytest --junitxml=result-rest.xml test\\rest 
                            '''
                            
                        }    
                    }
                }
            }
        }
        
        stage('results'){
            steps{
                junit 'result*.xml'
            }
        }
    }
}
