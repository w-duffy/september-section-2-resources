###################################################
## Automating GH Repo Creation Easily with Python
## alias eod='python ~/eod/eod.py'

## For the fully complete script see full_script.py
###################################################


###################################################
###################################################
## Intro Example -- Creating a new directory
###################################################

# dir_name = input("What do you want your directory to be called?\n")
# subprocess.run(f"mkdir {dir_name}", shell=True)
# subprocess.run("cd test", shell=True)
# subprocess.run(f"touch ./{dir_name}/test.py", shell=True)

## Basic GH Actions
# commit_message = input("what do you want your commit message to be?\n")
# subprocess.run("git init", shell=True)
# subprocess.run("git add .", shell=True)
# subprocess.run(f"git commit -m '{commit_message}'", shell=True)



###################################################
###################################################
## Below is what we completed in class.

## The full version is in full_script.py
###################################################
import subprocess

list_of_actions=[
'git init',
'git add .',
'git commit -m "first commit"',
'git branch -M main',
'git remote add origin git@github.com:{your_gh_user_name}/something-new-for-class.git', # Change this line
'git push -u origin main',
]

# print('git commit -m '"first commit"'[:-15]) # Slicing off "firstcommit"

# some_string = 'git commit -m "first commit"'
# commit_message = input("Whats your commit message?\n")
# print(some_string.replace("first commit", commit_message))  ## showing str.replace()

for command in list_of_actions:
    if(command == 'git commit -m "first commit"'):
        commit_message = input("Whats your commit message?\n")
        subprocess.run(f'{command[:-15]} {commit_message}')
        break
    subprocess.run(command, shell=True)
