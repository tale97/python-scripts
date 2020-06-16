# This is a simple webscrapper that calculates the average and total time of game played by a LoL player on OP.GG

import requests
from bs4 import BeautifulSoup as bs
import argparse

username = 'Bánh Canh Cá Lóc'
opgg_url = f'https://na.op.gg/summoner/userName={username}'
opgg_req = requests.get(opgg_url)

soup = bs(opgg_req.content, 'html.parser')

gameLengths = soup.find_all('div', class_='GameLength')


def timeInSeconds(s):
    hasM = False
    hasS = False
    mIndex, sIndex, spaceIndex = 0, 0, 0
    for i in range(len(s)):
        if s[i] == 'm':
            hasM = True
            mIndex = i
        if s[i] == 's':
            hasS = True
            sIndex = i
        if s[i] == ' ':
            spaceIndex = i
    minute = int(s[:mIndex])
    second = int(s[spaceIndex+1:sIndex])
    return second + minute*60

    if not hasM or not hasS:
        print(s)


GameLengthsInSecond = []

for gameLength in gameLengths:
    GameLengthsInSecond.append(timeInSeconds(gameLength.string))

totalGameLengthInSecond = sum(GameLengthsInSecond)
averageGameLengthInSecond = totalGameLengthInSecond//len(GameLengthsInSecond)


def formatTime(t):
    minute = t//60
    second = t - (t//60)*60
    hour = 0
    if minute >= 60:
        hour = minute//60
        minute = minute - hour*60
    return "{}m {}s".format(minute, second) if hour == 0 else "{}h {}m {}s".format(hour, minute, second)


print("Average Game Length: {}".format(formatTime(averageGameLengthInSecond)))
print("Total Game Length: {}".format(formatTime(totalGameLengthInSecond)))
