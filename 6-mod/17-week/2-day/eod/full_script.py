"""
This is the full script.

It requires you to install the GH CLI tool if you want to use it.
https://cli.github.com/

Please be cautious if you choose to use this.
Do not rm -rf your operating system 🙏
"""

# import subprocess

# def run_command(command):
#     try:
#         subprocess.run(command, check=True, shell=True)
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred: {e}")
#         exit(1)


# repo_name = input("Enter the name of the repo to create: ")
# repo_name.capitalize
# if not repo_name.strip():
#     print("You must provide a repository name.")
#     exit(1)

# github_username = '<YOUR_GH_USER_NAME_HERE>'  ## Replace this

# run_command("git init && git add . && git commit -m 'Initial commit'")

# ## You could also add an input to toggle between private/public
# run_command(f"gh repo create {repo_name} --private")

# run_command(
#     f"git remote add origin https://github.com/{github_username}/{repo_name}.git"
# )

# run_command("git checkout -b main")

# run_command("git push -u origin main")

# print(f"Repository {repo_name} has been created and initialized successfully.")



import subprocess
import json

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

def run_cmd_return_output(command):
    """Executes a shell command and returns the output."""
    try:
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")
        exit(1)


def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"{RED}An error occurred: {RESET}{e}")
        print(f"{RED}Command output: {RESET}{e.stderr}")
        exit(1)

def create_repo():
    repo_name = input("Enter the name of the repo to create: ")
    repo_name = repo_name.strip()
    if not repo_name:
        print(f"{YELLOW}You must provide a repository name.{RESET}")
        return

    print(f"{CYAN}Creating repository '{repo_name}'...{RESET}")

    run_command("git init && git add . && git commit -m 'Initial commit'")

    ## You could also add an input to toggle between private/public
    privacy_choice = input("Do you want to create a private repository? (yes/no): ").lower()
    private_flag = "--private" if privacy_choice == 'yes' else ""
    run_command(f"gh repo create {repo_name} {private_flag}")

    run_command(
        f"git remote add origin https://github.com/{github_username}/{repo_name}.git"
    )

    run_command("git checkout -b main")

    run_command("git push -u origin main")

    print(f"{GREEN}Repository '{repo_name}' has been created and initialized successfully.{RESET}")

def delete_repo():
    repo_name = input("Enter the name of the repo to delete: ")
    repo_name = repo_name.strip()
    if not repo_name:
        print(f"{YELLOW}You must provide a repository name.{RESET}")
        return

    confirmation = input(f"{YELLOW}Are you sure you want to delete the repository '{repo_name}'? (yes/no): {RESET}").lower()
    if confirmation == 'yes':
        print(f"{CYAN}Deleting repository '{repo_name}'...{RESET}")
        run_command(f"gh repo delete {github_username}/{repo_name} --yes")
        print(f"{GREEN}Repository '{repo_name}' has been deleted.{RESET}")
    else:
        print(f"{BLUE}Deletion of repository '{repo_name}' cancelled.{RESET}")

def list_repos():
    print(f"{CYAN}Listing your repositories...{RESET}")
    output = run_cmd_return_output("gh repo list --public --json name --limit 100")
    repos = json.loads(output)
    for idx, repo in enumerate([repo['name'] for repo in repos], 1):
        print(f"{idx}. {repo}")
    return

github_username = 'w-duffy'

if github_username == '<YOUR_GH_USER_NAME_HERE>':
    print(f"{RED}Please replace '<YOUR_GH_USER_NAME_HERE>' with your actual GitHub username in the script.{RESET}")
    exit(1)


while True:
    print(f"\n{WHITE}Choose an option:{RESET}")
    print(f"{BLUE}1. Create a new repo{RESET}")
    print(f"{BLUE}2. Delete a repo{RESET}")
    print(f"{BLUE}3. See all repos{RESET}")
    print(f"{BLUE}4. Exit{RESET}")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        create_repo()
    elif choice == '2':
        delete_repo()
    elif choice == '3':
        list_repos()
    elif choice == '4':
        print(f"{MAGENTA}Exiting.{RESET}")
        break
    else:
        print(f"{YELLOW}Invalid choice. Please enter a number between 1 and 4.{RESET}")
