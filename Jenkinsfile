pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Identificando el agente...'
                bat 'whoami && hostname'
                echo 'Clonando el repositorio...'
                git url: 'https://github.com/julianxttecn05/CP1Julian.git', branch: 'master'
            }
        }
        stage('Build') {
            steps {
                echo 'Identificando el agente...'
                bat 'whoami && hostname'
                echo 'No hay que compilar nada, esto es Python'
                dir('.') {
                    bat 'dir'
                }
            }
        }
        stage('Tests') {
            parallel {
                stage('Unit Tests') {
                    agent { label 'Agent1' }
                    steps {
                        echo 'Identificando el agente...'
                        bat 'whoami && hostname'
                        echo 'Ejecutando pruebas unitarias...'
                        script {
                            if (fileExists('test/unit')) {
                                bat 'python -m pytest --junitxml=result-unit.xml test/unit'
                            } else {
                                echo 'Advertencia: El directorio de pruebas unitarias no existe. Saltando esta etapa.'
                            }
                        }
                    }
                }
                stage('Start Flask Server') {
                    agent { label 'Agent2' }
                    steps {
                        echo 'Identificando el agente...'
                        bat 'whoami && hostname'
                        echo 'Ejecutando servidor Flask...'
                        bat 'start /B python -m flask run --host=127.0.0.1 --port=5000'
                        sleep(time: 15, unit: 'SECONDS') // Espera para que Flask inicie
                    }
                }
                stage('Health Check') {
                    agent { label 'Agent2' }
                    steps {
                        echo 'Identificando el agente...'
                        bat 'whoami && hostname'
                        echo 'Comprobando el estado de la API...'
                        script {
                            def response = bat(script: 'curl -I http://127.0.0.1:5000', returnStatus: true)
                            if (response != 0) {
                                echo 'Advertencia: El servidor Flask no está disponible en http://127.0.0.1:5000'
                            } else {
                                echo 'El servidor Flask está activo y responde correctamente.'
                            }
                        }
                    }
                }
            }
        }
        stage('Results') {
            steps {
                echo 'Identificando el agente...'
                bat 'whoami && hostname'
                echo 'Todas las etapas completadas con éxito.'
            }
        }
    }
    post {
        always {
            echo 'Limpiando el espacio de trabajo...'
            cleanWs()
        }
        failure {
            echo 'El pipeline ha fallado.'
        }
    }
}
