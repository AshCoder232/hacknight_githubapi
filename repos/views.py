from django.shortcuts import render
import requests
import random
# Create your views here.

def index(request):
    selected_repos = []
    while (len(selected_repos) < 5):
        random_page = random.randint(0, 100000)
        response = requests.get('https://api.github.com/repositories', params={'since': random_page})
        data = response.json()
        random_repos = random.sample(data, 5)
        for i in range(0, 5):
            r = requests.get(random_repos[i]['url'])
            d = r.json()
            if (d['stargazers_count'] >= 10):
                random_repos[i]['stars'] = d['stargazers_count']
                random_repos[i]['watchers'] = d['watchers_count']
                random_repos[i]['forks'] = d['forks_count']

                lr = requests.get(d['languages_url'])
                random_repos[i]['languages'] = list(lr.json().keys())              
                selected_repos.append(random_repos[i])
    return render(request, "repos/index.html")