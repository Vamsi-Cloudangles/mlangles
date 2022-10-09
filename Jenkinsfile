pipeline{
    agent any

    stages{
        stage("Checkout"){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Vamsi-Cloudangles/Dimond_new.git']]])
            }
        }
        stage("build"){
            steps{
                git branch: 'main', url: 'https://github.com/Vamsi-Cloudangles/Dimond_new.git'
            }
        }
        stage("load_data"){
            steps{
                sh 'python3 load_data.py'
            }
        }
        stage("feature_engineering"){
            steps{
                sh 'python3 feature_engineering.py'
            }
        }
        stage("pre_processing"){
            steps{
                sh 'python3 pre_processing.py'
            }
        }
        stage("model_selection"){
            steps{
                sh 'python3 model_selection.py'
            }
        }
        
    }
    post{
        always{
            emailext body:"summery", subject: "Pipeline Status", to: 'vamsi.muramreddy@cloudangles.com'
        }
    }
}
