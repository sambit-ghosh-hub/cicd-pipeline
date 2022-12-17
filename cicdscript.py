from github import Github
import time
import os
import datetime
import pytz
from datetime import datetime as dt

g = Github("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")

repo = g.get_repo("sambit-ghosh-hub/flask-hello-world")

dev_branch = repo.get_branch("dev")

latest_sha = dev_branch.commit.sha

commit = repo.get_commit(sha=latest_sha)

committime = commit.commit.author.date
print("Latest commit at:",committime)

now = dt.now(pytz.timezone('GMT'))
print("Time Now:",now)

timediff = now - committime
timediffmins = timediff.total_seconds() / 60

if timediffmins < 5:
 print("New Commit Found! Deploying new commit...")
 os.system(".\pullanddeploy.bat")
else:
 print("No new Commits in last 5 mins")
