import requests


def get_request_token(client_id: str, client_secret: str, request_token: str) -> str:
    if not client_id:
        raise ValueError('The client_id has to be supplied!')
    if not client_secret:
        raise ValueError('The client_secret has to be supplied!')
    if not request_token:
        raise ValueError('The request token has to be supplied!')
    if not isinstance(client_id, str):
        raise ValueError('The client_id has to be a string!')
    if not isinstance(client_secret, str):
        raise ValueError('The client_secret has to be a string!')
    if not isinstance(request_token, str):
        raise ValueError('The request token has to be a string!')

    base_url = 'https://github.com/login/oauth/access_token?'
    auth = f'client_id={client_id}&client_secret={client_secret}&code={request_token}'
    url = base_url + auth
    headers = {
        'accept': 'application/json'
    }

    res = requests.post(url, headers=headers)
    data = res.json()
    access_token = data['access_token']
    return access_token


def get_user_data(access_token: str) -> dict:
    if not access_token:
        raise ValueError('The access token has to be supplied!')
    if not isinstance(access_token, str):
        raise ValueError('The access token has to be a string!')

    access_token = f'token {access_token}'
    url = 'https://api.github.com/user'
    headers = {
        "Authorization": access_token
    }

    resp = requests.get(url=url, headers=headers)

    user_data = resp.json()
    return user_data


def get_user_repos(repos_url: str, access_token) -> list:
    if not repos_url:
        raise ValueError('The repos_url has to be supplied!')
    if not isinstance(repos_url, str):
        raise ValueError('The repos_url has to be a string!')
    if not access_token:
        raise ValueError('The access token has to be supplied!')
    if not isinstance(access_token, str):
        raise ValueError('The access token has to be a string!')

    access_token = f'token {access_token}'
    url = 'https://api.github.com/user/repos'
    headers = {
        "Authorization": access_token
    }

    resp = requests.get(url=url, headers=headers)
    repos = resp.json()
    return repos


def get_repo_languages(repos: list, access_token: str) -> list:
    repos_languages_list = []
    repo_langs = {}
    total_lan_use = {'total': 0}
    for r in repos:
        if 'languages_url' in r:
            lan = {}
            name = r['name']
            url = r['languages_url']
            langs = requests.get(url)
            repo_langs = langs.json()
            for l in repo_langs:
                if l not in total_lan_use:
                    total_lan_use[l] = repo_langs[l]
                else:
                    total_lan_use[l] += repo_langs[l]
                total_lan_use['total'] += repo_langs[l]
            lan[name] = repo_langs
            repos_languages_list.append(lan)

    return repos_languages_list


def get_langs(langs_url: str, headers: dict) -> dict:
    langs = requests.get(langs_url)
    return langs.json()
