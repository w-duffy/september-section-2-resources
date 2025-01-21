"""
This is the full script.

It requires you to install the GH CLI tool if you want to use it.
https://cli.github.com/

Please be cautious if you choose to use this.
Do not rm -rf your operating system 🙏
"""

import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        exit(1)


repo_name = input("Enter the name of the repo to create: ")

if not repo_name.strip():
    print("You must provide a repository name.")
    exit(1)

github_username = '<YOUR_GH_USER_NAME_HERE>'  ## Replace this

run_command("git init && git add . && git commit -m 'Initial commit'")

## You could also add an input to toggle between private/public
run_command(f"gh repo create {repo_name} --private")

run_command(
    f"git remote add origin https://github.com/{github_username}/{repo_name}.git"
)

run_command("git checkout -b main")

run_command("git push -u origin main")

print(f"Repository {repo_name} has been created and initialized successfully.")
