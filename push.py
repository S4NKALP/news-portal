import os
import subprocess

def push_to_github(repo_path, commit_message):
    os.chdir(repo_path)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push"])

repo_path = r"C:\Users\nurpr\OneDrive\Desktop\Backend\news-portal"
commit_message = "Automated commit message"
push_to_github(repo_path, commit_message)