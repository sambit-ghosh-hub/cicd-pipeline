# CI/CD script for deploying a flask app

This script is designed to run every 5 mins with cron job and Check the 'deploy' branch of the flask app for new commits every 5 mins and deploy new commit if it happens within those 5 mins.

We use pygithub to get status of repo and update our deployed app with newly commited code.

## Instructions

-Set up the flask app repo and this repo in server to be sibling directories.
 ``` 
    parent-directory
    |- flaskapp
    |- cicd-pipeline
 ```
-Set Environment variable called ```GITHUBTOKENCICD``` and put your api token in it.
 On Linux run:
 ```
 export GITHUBTOKENCICD=<your token here>
 ```

-Run cicdscript.py **NOT** cicd.py(This is a pure python implementation without use of cron jobs)

-On linux, in crontab add the following line to set up cron job for every 5 mins:

 ```
 5 * * * * /home/osboxes/<pathtorepo>/cicd-pipeline/run_cicd.sh
 ```

# Targets of the project

1. First create a GitHub repository.
2. Create a development branch
3. Write a "Hello World" flask application.
4. Push this branch.
5. Create a new branch called as deployment from the development branch and push this branch too.
6. Look at the documentation for PyGithub and install it.
7. Write simple script to check for the commit history and their time.
8. Modify this script to check if the commit was done within 5 min from the current time.
9. Write a bash script to:
    a. pull the code from the deployment branch.
    b. Deploy the development branch
10. Modify the python code to execute this bash script if the commit time is not more than 5 min from the current time. You can import os and use os.system() in python to execute the bash script.
11. Write a crontab for 4 min.
12. Write a readme.md file with all your understanding of code.
