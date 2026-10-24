import requests

def search_repositories(query, language=None, sort='stars'):
    url = "https://api.github.com/search/repositories"
    
    q = query
    if language:
        q += f" language:{language}"
        
    params = {
        'q': q,
        'sort': sort,
        'order': 'desc',
        'per_page': 10
    }
    
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('items', [])
        else:
            return []
    except requests.exceptions.RequestException:
        return []

def search_issues(query, language=None):
    url = "https://api.github.com/search/issues"
    
    q = f"{query} type:issue state:open label:\"good first issue\""
    if language:
        q += f" language:{language}"
        
    params = {
        'q': q,
        'sort': 'updated',
        'order': 'desc',
        'per_page': 10
    }
    
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('items', [])
        else:
            return []
    except requests.exceptions.RequestException:
        return []