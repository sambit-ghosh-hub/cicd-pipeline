from github import Github
import time
import os

g = Github("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") #change this to your own token

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
  