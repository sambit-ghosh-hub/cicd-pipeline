# CI/CD script for deploying a flask app

This script is designed to run every 5 mins with cron job and Check the dev branch of the flask app for new commits every 5 mins and deploy new commit if it happens within those 5 mins.

We use pygithub to get status of repo