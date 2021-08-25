import requests

def random(arg:str):
    resp  = requests.get(f'http://discord-holo-api.ml/api/{arg}')
    if resp.status_code == 404:
        print("Error! This tag does not exist!\nAll Tags: art, ask, bite, cry, cuddle, dance, ego, glare, highfive, hug, kiss, lick,\nnom, pat, poke, pressf, punch, sex, shoot, slap, slappope, smug, suicide, tickle, wasted, wink")
        return None
    if resp.status_code == 200:
        return resp.json() ["url"]



