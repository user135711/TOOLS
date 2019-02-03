#!/usr/bin/python3

from config import HOMEDIR

catlist = ['Malicious', 'VPN', 'Adult', 'Drugs', 'Guns', 'DynDNS', 'Ads', 'SocialMedia']

combinefiles = []

def Combine():
    for cat in catlist:
        with open('config.py', 'r') as config:
            for line in config:
                if ('{}=1'.format(cat.upper()) in line):
                    combinefiles.append('{}.domains'.format(cat))

    with open('{}/BL.domains'.format(path), 'w+') as BL:
        for files in combinefiles:
            with open('{}/{}'.format(HOMEDIR, files), 'r+') as files:
                for line in files:
                    BL.write(line)


                 
