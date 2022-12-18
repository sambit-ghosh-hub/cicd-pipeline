from github import Github
import time
import os
import platform
import pytz
from datetime import datetime as dt
from datetime import timezone

token = os.environ.get("GITHUBTOKENCICD")

g = Github(token)

repo = g.get_repo("sambit-ghosh-hub/flask-hello-world") # change to your own repo link

deploy_branch = repo.get_branch("deploy")

latest_sha = deploy_branch.commit.sha

commit = repo.get_commit(sha=latest_sha)

committime = commit.commit.author.date
committime = committime.replace(tzinfo=timezone.utc)

now = dt.now(pytz.timezone('UTC'))

print("Time Now:",now)
print("Latest commit at:",committime)

timediff = now - committime
timediffmins = timediff.total_seconds() / 60

if timediffmins < 5:
 print("New Commit Found! Deploying new commit...")
 if platform.system() == 'Windows':
  os.system(".\batchscripts\pullanddeploy.bat")
 else:
  os.system('cd "$(dirname "$0")";ls -a;cat bashscripts/pullanddeploy.sh')
 
else:
 print("No new Commits in last 5 mins")
