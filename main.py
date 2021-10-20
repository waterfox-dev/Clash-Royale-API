from os import read
from src.player import Player
from src.calculator import Calculator

from datetime import datetime

import json 
import csv

#Loading Player
waterfox = Player('RUR8R28PR')

battle_result = waterfox.battles()
number_result = len(battle_result)
win_total     = 0
los_total     = 0

for i in range(number_result):
    
    win = None 
    if battle_result[i]['team'][0]['trophyChange'] > 0 :
        win_total += 1
        win = True
    else:
        los_total += 1
        win = False

    with open('team_result.csv', 'a+', encoding='UTF8', newline='') as file :
        writer = csv.writer(file, delimiter = ',')
        card_list = []

        for element in battle_result[i]['team'][0]['cards']:
            card_list.append(element["name"])

        card_list.append(win)
        writer.writerow(card_list)


with open('algo_result.csv', 'a', encoding='UTF8') as file :
    writer = csv.writer(file)
    writer.writerow([str(datetime.now()), win_total, los_total, number_result])


