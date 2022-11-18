# This program extracts some details of matches played at FIFA 2010 Worldcup
# You may need to install BeautifulSoup to run this file on your machine
# See https://www.crummy.com/software/BeautifulSoup/bs4/doc/ for details

from sys import stdin
import math
import sys
import random
import requests
import os
from bs4 import BeautifulSoup

def getTeamName(team):
    name = team.find('span',class_='t-nText').get_text()
    return name

url = "www.fifa.com/worldcup/archive/southafrica2010/matches/"


r  = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data,"html.parser")

results = soup.find_all('div', class_="mu result")
output = open('matches.txt','w')

for match in results:
    home_team = getTeamName(match.find('div',class_="t home"))
    away_team = getTeamName(match.find('div',class_="t away"))

    # Ivory Coast is listed as "CÃ´te d'Ivoire" in one match. Fixing it
    if away_team == "CÃ´te d'Ivoire":
        away_team = "Ivory Coast"
    score = match.find('span',class_="s-scoreText").get_text()
    
    score = score.split("-")
    home_score = score[0]
    away_score = score[1]

    match_stats = home_team +":"+ away_team +":" +home_score+":"+away_score
    print(match_stats)
    output.write(match_stats+"\n")

output.close()
