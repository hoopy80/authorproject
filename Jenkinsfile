pipeline{
        agent any
        stages{
            stage('Make directory')
		{
                steps{
                    sh "mkdir ~/authorproject-test"
                }
            }
            stage('Make Files'){
		    
                steps{
                    sh "touch ~/authorproject-test/file1 ~/authorproject-test/file2"
                }
            }
        }
}
