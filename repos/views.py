from django.shortcuts import render
import requests
import random
# Create your views here.

def index(request):
    random_page = random.randint(0, 100000)
    response = requests.get('https://api.github.com/repositories', params={'since': random_page})
    data = response.json()
    random_repos = random.sample(data, 5)
    del_cols = ['']
    for i in range(0, 5):
        url = random_repos[i]['url']
        r = requests.get(url)
        d = r.data()
    return render(request, "repos/index.html")