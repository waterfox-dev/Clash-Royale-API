import csv
import json 
import io
from os import execv, read

class Calculator(object):

    @staticmethod
    def get_average(element_list : list):

        occurence_dict = {}
        percent_dict   = {}
        total          = 0

        for element in element_list :
            for value in element :
                total += 1
                if value in occurence_dict.keys():
                    occurence_dict[value] += 1
                else:
                    occurence_dict[value] = 1
            
        for key in occurence_dict :
            percent_dict[key] = (occurence_dict[key]*100/total, occurence_dict[key])
        return percent_dict
    
    @staticmethod
    def count_victory(data_array : list, percent_dict = dict):

        victory_count = {}
        victory_stat  = {}
        victory_total = 0

        for keys in percent_dict :
            victory_count[keys] = 0
            for team in data_array :
                if keys in team and team[-1] == 'True':
                    victory_count[keys] += 1
                    victory_total += 1

        for key in victory_count :
            victory_stat[key] = {
                "count of battles" : percent_dict[key][1],
                "count of victories" : victory_count[key],
            }
            try :
                victory_stat[key]["percent of victories"] = int(victory_count[key]*100/percent_dict[key][1])
            except ZeroDivisionError :
                victory_stat[key]["percent of victories"] = 0
        return victory_stat
