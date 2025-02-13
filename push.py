import os
import subprocess


def push_to_github(repo_path):
    os.chdir(repo_path)
    commit_message = input("Enter your commit message: ")  # Take input from user
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push"])


repo_path = r"C:\Users\nurpr\OneDrive\Desktop\Backend\news-portal"
push_to_github(repo_path)
