import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://github.com/trending"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_trending_repos(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    repo_list = []
    repositories = soup.find_all("article", class_="Box-row")

    for repo in repositories:
        repo_name = repo.find("h2").text.strip().replace("\n", "").replace(" ", "")
        repo_url = "https://github.com" + repo.find("h2").find("a")["href"]
        repo_desc = repo.find("p").text.strip() if repo.find("p") else "No description"

        repo_list.append({"Repository": repo_name, "URL": repo_url, "Description": repo_desc, })

    return repo_list

data = get_trending_repos(URL)
df = pd.DataFrame(data)
df.to_csv("Class-5/assignment_code/task_3/github_trending.csv", index=False)
print("Data saved to github_trending.csv")
