# Add label to GitHub issues conditionally
-------------------------------------------

The following code adds "hacktoberfest" label to all open issues with "good first issue" label.
```python
import requests
import json

username = "Azanul"
token = "secret token"
repository_owner = "owner"
repository_name = "repo"

# Create a session with GitHub credentials
session = requests.Session()
session.auth = (username, token)

# Get the list of issues with the "good first issue" label
url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/issues"
params = {
    "labels": ["good first issue"],
    "state": "open",
    "page": 1
}

response = session.get(url, params=params)
while True:
    response = session.get(url, params=params)
    params["page"] += 1
    if response.status_code == 200:
        issues = json.loads(response.text)

        for issue in issues:
            label_names = [label["name"] for label in issue["labels"]]
            if issue["state"] != "open" or "hacktoberfest" in label_names:
                continue

            issue_number = issue["number"]
            labels_url = f"{url}/{issue_number}/labels"
            label_data = ["hacktoberfest"]

            response = session.post(labels_url, json=label_data)
            if response.status_code == 200:
                print(f"Added 'hacktoberfest' label to issue #{issue_number}")
            else:
                print(f"Failed to add 'hacktoberfest' label to issue #{issue_number}")
        
        if len(issues) < 30:
            print("All issues fetched")
            break

    else:
        print(f"Failed to retrieve issues for {params}")
        break

session.close()

```
