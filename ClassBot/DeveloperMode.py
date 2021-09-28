import os.path
from ClassBot import *
import json


def Populate():
    data = {'Function': []}
    data['raid'].append({
        'raid' : '0.5',
        'evoca': '0.5',
        'accept': '0.5',
        'chiudi': '0.5',
        'morte': '0.5',
        'rerun':'0.5',
        'no_shard': '0.5'
    })
    data['pvp'].append({
        'pvp' : '0.5',
        'play': '0.5',
        'accetta': '0.5',
        'defeat': '0.5',
        'cittadina': '0.5',
        'no_shard': '0.5'
    })
    data['people'].append({
        'gaunt': '0.5',
        'accept': '0.5',
        'play': '0.5',
        'no_shard': '0.5'
    })

    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)



