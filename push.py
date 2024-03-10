import requests
import json
import datetime

def create_commit(repo_name, token):
    url = f"https://api.github.com/repos/{repo_name}/git/commits"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "message": f"Automated commit on {datetime.datetime.now()}",
        "committer": {
            "name": "Your Name",
            "email": "your_email@example.com"
        },
        "content": "bXkgbmV3IGZpbGUgY29udGVudHM="
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print("Commit created successfully.")
    else:
        print(f"Failed to create commit: {response.text}")

def main():
    repo_name = "Chiamablessing/AirBnB_clone"
    token = "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"


    for _ in range(50):
        create_commit(repo_name, token)

main()
