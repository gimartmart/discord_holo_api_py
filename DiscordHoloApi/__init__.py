import requests

def random(arg:str):
    resp  = requests.get(f'http://discord-holo-api.ml/api/{arg}')
    if resp.status_code == 404:
        print("Error! This tag does not exist!\nAll Tags: 404, anal, art, ask, avatar, baka, bite, bj, blowjob, boobs, cry, cuddle, cum, dance, ego, ero, erofeet, erok, erokemo, eroyuri, feed, feet, feetg, fox_girl, futanari, glare, hentai_gif, highfive, holo, holoero, hololewd, hug, kemonomimi, kiss, kuni, les, lewd, lick, loli, meow, neko, ngif, nom, pat, poke, pressf, punch, pussy, pwankg, sex, slap, slappope, smug, solo, tickle, tits, trap, waifu, wallpaper, wasted, wink, woof, yuri")
        return None
    if resp.status_code == 200:
        return resp.json() ["url"]



