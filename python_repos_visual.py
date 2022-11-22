import requests

# --------------------------------
from plotly.graph_objs import Bar
from plotly import offline
# --------------------------------

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
repo_links, stars, labels = [], [], []

# Adding active links to the diagram
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href= '{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # Adding prompts
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)

# Building a visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {
            'width': 1.5,
            'color': 'rgb(25, 25, 25)',
        }
    },
    'opacity': 0.6,
}]

layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {
    'data': data,
    'layout': layout,
}
offline.plot(fig, filename='python_repos.html')
