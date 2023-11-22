pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps{
                checkout scmGit(branches: [[name: '*/automation']], extensions: [], userRemoteConfigs: [[credentialsId: '1d80c116-490e-4138-a941-375a1fdb3de8', url: 'https://github.com/Suresh1925/automation.git']])
            }
        }
        stage('build'){
            steps{
                git branch: 'automation', credentialsId: '1d80c116-490e-4138-a941-375a1fdb3de8', url: 'https://github.com/Suresh1925/automation.git'
                bat 'python Suresh.py'
            }
        }
    }
}