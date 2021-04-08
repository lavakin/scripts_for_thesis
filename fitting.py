#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model
from functions import *
import pandas as pd
from scipy.optimize import curve_fit
import json
import sys
import csv

funct_dict = {'logarithm': logarithm , 'linear':linear, 'polynomial 2': poly2, 'power':power_law, 'modified_power':modified_power_law}


def get_rmses(index):
    rmses = {}
    return {funct_name: get_rmse(index, funct) for funct_name,funct in funct_dict.items()}
    
    
def get_rmse(chem_index,function):
    try:
        popt, pcov = curve_fit(function, chem_index, bp)
        return round(math.sqrt(sum([(abs(bp[i]-function(chem_index[i], *popt)))**2 for i in range(len(chem_index))])/len(chem_index)),3)
    except: 
        return 1000
    

def plot_best(f, chem_index, f_name, index_name):
    popt, pcov = curve_fit(f, chem_index, bp)
    plt.plot(chem_index,bp,'.',alpha=0.3)
    chem_index.sort()
    y = [f(x,*popt) for x in chem_index]
    plt.plot(chem_index,y, 'r-', label=f_name)
    plt.xlabel(index_name)
    plt.ylabel('boiling point')
    plt.legend()
    plt.show()
    
def store_best(results):
    with open('csvs/' + sys.argv[1].split('.')[0].split('/')[-1] + '_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["index", "function name", "RMSE"])
        for chem_index,result in results.items():
            function_name = min(result, key= lambda x: result[x])
            score = result[function_name]
            writer.writerow([chem_index,function_name, score])
    
    
    
chemicals = pd.read_pickle(sys.argv[1])
results = {}
bp = [row["boiling point"] for index, row in chemicals.iterrows()]
for chem_index in chemicals.keys():
    if not (chem_index == "boiling point" or chem_index == "molecule"):
        results[chem_index] = get_rmses([row[chem_index] for index, row in chemicals.iterrows()])

"""
for chem_index,result in results.items():
    function_name = min(result, key= lambda x: result[x])
    plot_best(funct_dict[function_name],[row[chem_index] for index, row in chemicals.iterrows()],function_name,chem_index)
"""    
print(results)
store_best(results)
with open('jsons/' + sys.argv[1].split('.')[0].split('/')[-1] + '_results.json', 'w') as outfile:
    json.dump(results, outfile)
