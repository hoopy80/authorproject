pipeline 
{
    agent none
    stages 
	{
        stage('Build Stage')
		{
           		agent any
            		steps 
			{
				echo 'This is Build part'
			
				sh 'proj.py'
				
            		}
            	
        	}
        stage('Test Stage')
		{
			agent any
			steps
			{
				echo 'This is Test part'
			
				sh 'proj.py'
			}
