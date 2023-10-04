## Create GitHub issues from a template
-----------------------------------------


```python
import requests
import json

GITHUB_API_URL = "https://api.github.com/repos/owner/repo/issues"

AWS_RESOURCES = [
    # (resource_name, service_code, metrics_link)
    ("ec2", "AmazonEC2", "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html"),
    ("s3", "AmazonS3", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-dimensions.html"),
    ("rds", "AmazonRDS", "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html")
]

# pricing_link = "https://aws.amazon.com/" + resource_name + "/pricing/"
TEMPLATE = """
Cost calculations for AWS {resource_name} is either missing or incorrect

## Describe the solution you'd like

A checklist for cost calculation of each resource
- [ ] Fetch price info using AWS SDK price module using `{service_code}` service code and appropriate filters.
- [ ] Get flat price map using util function `GetPriceMap` from [utils.go](https://github.com/tailwarden/komiser/blob/develop/providers/aws/utils/utils.go)
- [ ] Using {resource_name} client fetch the resource objects [Docs AWS service Go SDK](https://docs.aws.amazon.com/sdk-for-go/api/service/{resource_name}/)
- [ ] Fetch usage metrics using AWS SDK cloudwatch module [AWS usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.html) [{resource_name} metrics]({metrics_link})
- [ ] Calculate the cost according to {resource_name} AWS documentation [Link to AWS {resource_name} pricing]({pricing_link})

For inspiration take a look at [AWS Lambda](https://github.com/tailwarden/komiser/blob/develop/providers/aws/lambda/functions.go)
"""

def create_github_issue(owner, repo, title, body):
    headers = {
        "Authorization": "Bearer token"
    }

    data = {
        "title": title,
        "body": body,
        "labels": ["hacktoberfest", "good first issue", "help wanted", "enhancement", "feature", "aws"]
    }

    # Check if an issue with the same title already exists
    existing_issues = requests.get(GITHUB_API_URL.format(owner=owner, repo=repo), headers=headers)
    existing_issue_titles = [issue["title"] for issue in existing_issues.json()]
    
    if title not in existing_issue_titles:
        response = requests.post(
            GITHUB_API_URL.format(owner=owner, repo=repo),
            headers=headers,
            data=json.dumps(data)
        )

        if response.status_code == 201:
            print(f"GitHub issue created for AWS {resource_name} resource.")
        else:
            print(f"Failed to create GitHub issue for AWS {resource_name} resource: {response.status_code}")
    else:
        print(f"GitHub issue with title '{title}' already exists. Skipping creation.")

def main():
    """Creates GitHub issues for the AWS resources in the list."""

    for resource_name, service_code, metrics_link in AWS_RESOURCES:
        template = TEMPLATE

        pricing_link = "https://aws.amazon.com/" + resource_name + "/pricing/"

        template = template.format(
            resource_name=resource_name, service_code=service_code,
            metrics_link=metrics_link, pricing_link=pricing_link
        )

        print(template)

        create_github_issue(title=f"Cost calculations for AWS {resource_name} is missing or incorrect", body=template)

if __name__ == "__main__":
    main()

```
