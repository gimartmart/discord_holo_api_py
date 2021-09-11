import requests

core = requests.get(f'http://discord-holo-api.ml/api')
core = core.json()
core = core["requests"]
def random(arg:str):
    resp  = requests.get(f'http://discord-holo-api.ml/api/{arg}')
    if arg not in core:
        return f"Error! This tag does not exist!\nAll Tags: {core}"
    
    elif resp.status_code == 200:
        return resp.json()["url"]
def stats():
    stat  = requests.get(f'http://discord-holo-api.ml/api/stats')
    stat = str(stat.json())
    return stat

def tags():
    return core

