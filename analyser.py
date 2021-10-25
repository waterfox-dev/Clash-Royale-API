from src.calculator import Calculator

import matplotlib.pyplot as plt
import numpy as np
import csv


with open('team_result.csv', 'r', encoding='UTF8') as file :
    reader = csv.reader(file)
    reader_list = list(reader)
    percent_result = Calculator.get_average(reader_list.copy())
    victory_result = Calculator.count_victory(reader_list.copy(), percent_result)

print("Test")