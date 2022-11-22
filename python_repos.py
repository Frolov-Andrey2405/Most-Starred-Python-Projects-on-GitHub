import requests

# Creating an API call AND saving the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Saving the API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Analyzing repository information
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

# Analysis of the first repository
repo_dict = repo_dicts[0]
print(f'\nKeys: {len(repo_dict)}')

print('\nSelected information about each repository:\n')
for repo_dict in repo_dicts:
    print(
        "#----------------------------------------------#",
        f"\nName: {repo_dict['name']}",
        f"\nOwner: {repo_dict['owner']['login']}",
        f"\nStars: {repo_dict['stargazers_count']}",
        f"\nRepository: {repo_dict['html_url']}",
        f"\nCreated: {repo_dict['created_at']}",
        f"\nUpdated: {repo_dict['updated_at']}",
        f"\nDescription: {repo_dict['description']}",
        "\n#----------------------------------------------#\n")

# Processing results
print(response_dict.keys())
