from django.shortcuts import render
import requests
import random
import os
# Create your views here.

TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')

def index(request):
    selected_repos = []
    while (len(selected_repos) == 0):
        random_page = random.randint(0, 100000000)
        response = requests.get('https://api.github.com/repositories', 
        params={'since': random_page}, headers={'Authorization': f"token {TOKEN}"})
        data = response.json()
        if (response.status_code == 200):
            random_repos = random.sample(data, 10)
            for i in range(0, 10):
                print(i)
                r = requests.get(random_repos[i]['url'])
                d = r.json()
                if (r.status_code != 200):
                    break
                if (d['stargazers_count'] >= 10):
                    random_repos[i]['stars'] = d['stargazers_count']
                    random_repos[i]['watchers'] = d['watchers_count']
                    random_repos[i]['forks'] = d['forks_count']

                    lr = requests.get(d['languages_url'])
                    random_repos[i]['languages'] = list(lr.json().keys())              
                    selected_repos.append(random_repos[i])
                    break
        else:
            break
    if (len(selected_repos) == 0):
        error = "Rate Limit Reached!!"
        repo = {}
    else:
        error = ""
        repo = selected_repos[0]
    return render(request, "repos/index.html", {'repo': repo, 'error': error})