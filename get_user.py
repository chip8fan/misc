import json
import os
import subprocess
import sys
import datetime
repos = json.loads(subprocess.run(f"gh repo list -L {sys.maxsize} --json name,createdAt {sys.argv[1]}".split(), capture_output=True, text=True).stdout)
if os.path.isdir(sys.argv[1]) == False:
    os.mkdir(sys.argv[1])
os.chdir(sys.argv[1])
for repo in repos:
    if datetime.datetime.strptime(str(repo['createdAt']).split("T")[0], "%Y-%M-%d") < datetime.datetime.strptime(sys.argv[2], "%Y-%M-%d"):
        os.system(f"git clone https://github.com/{sys.argv[1]}/{repo['name']}")
        os.chdir(repo['name'])
        latest_commit = subprocess.run(f'git log --until="{sys.argv[2]}"'.split(), capture_output=True, text=True).stdout.split("\n")[0].split("commit ")[1]
        os.system(f"git checkout {latest_commit}")
        os.chdir("..")