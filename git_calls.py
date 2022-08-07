import requests
import os

# access_token = "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" The 'token' environment variable is the GitHub Personal
# Access Token. How to creat GitHub Personal Access Token ->
# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

access_token = os.getenv("token")
repo_languages = []
languages = "https://api.github.com/repos/hasiya/Jet-Drive_Off-DB/languages"
repos = "https://api.github.com/users/hasiya/repos"
response = requests.get("https://api.github.com/users/hasiya/repos", auth=("hasiya",access_token))
for r in response.json():
    lan = {}
    name = r["name"]
    l_str = f"https://api.github.com/repos/hasiya/{name}/languages"
    lans = requests.get(l_str, auth=("hasiya",access_token))

    lan[name] = lans.json()
    repo_languages.append(lan)
print(repo_languages)
print(len(repo_languages))
