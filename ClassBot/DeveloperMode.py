import os.path
from ClassBot import *
import json
import logging


def Populate():
    # check if there isnt a data.json
    file = os.path.isfile("data.json")
    logging.debug(f"data.json = {file}")
    if file is True: # To edit cause i need this to debug
        f = open("data.json", "w")
        data = {'Function':[{
            'raid':[{
                'raid':'0.5',
                'evoca':'0.5',
                'accept':'0.5',
                'chiudi': '0.5',
                'morte': '0.5',
                'rerun':'0.5',
                'no_shard': '0.5'
            }],
            'pvp':[{
                'pvp': '0.5',
                'play': '0.5',
                'accetta': '0.5',
                'defeat': '0.5',
                'cittadina': '0.5',
                'no_shard': '0.5'
            }],
            'gauntlet':[{
                'gaunt': '0.5',
                'accept': '0.5',
                'play': '0.4',
                'no_shard': '0.5'
            }],
            'nynx_trial':[{
                'trial': '0.5',
                'accept': '0.5',
                'play': '0.4',
                'no_shard': '0.5'
            }],
            'gvg':[{
                'gvg':'0.5',
                'play' :'0.5',
                'select':'0.5',
                'accept':'0.5',
                'no_shard':'0.5'
            }],
            'expedition':[{
                'enter':'0.5',
                'accept':'0.5',
                'cittadina':'0.5'
            }],
            'invasion':[{
                'invasion': '0.5',
                'accept': '0.5',
                'play': '0.4',
                'no_shard': '0.5'
            }]
        }
        ]}

        json.dump(data,f, indent=4)
        f.close



