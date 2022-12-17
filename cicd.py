from github import Github
import time
import os

token = os.environ.get("GITHUBTOKENCICD")
g = Github(token) #change this to your own token

repo = g.get_repo("sambit-ghosh-hub/flask-hello-world")#change this to your owm flask app

dev_branch = repo.get_branch("dev")

print(dev_branch.commit.sha)

latest_sha = dev_branch.commit.sha

commit = repo.get_commit(sha=latest_sha)

print(commit.commit.author.date)

while True:
 dev_branch = repo.get_branch("dev")
 print("Checking for new commit...")
 sha = dev_branch.commit.sha

 if sha != latest_sha:
  print("Found new commit. Deploying...")
  latest_sha = sha
  os.system(".\pullanddeploy.bat")
  pass
 
 time.sleep(1*60)
  