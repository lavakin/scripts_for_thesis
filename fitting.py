#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model
from functions import *
import pandas as pd
from scipy.optimize import curve_fit
import json


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
    plt.plot(chem_index,bp,'o')
    chem_index.sort()
    y = [f(x,*popt) for x in chem_index]
    plt.plot(chem_index,y, 'r-', label=f_name)
    plt.xlabel(index_name)
    plt.ylabel('boiling point')
    plt.legend()
    plt.show()
    
    
chemicals = pd.read_pickle("ch_smiles.pickle")
results = {}
bp = [row["boiling point"] for index, row in chemicals.iterrows()]
for chem_index in chemicals.keys():
    if not (chem_index == "boiling point" or chem_index == "molecule"):
        results[chem_index] = get_rmses([row[chem_index] for index, row in chemicals.iterrows()])

for chem_index,result in results.items():
    function_name = min(result, key= lambda x: result[x])
    plot_best(funct_dict[function_name],[row[chem_index] for index, row in chemicals.iterrows()],function_name,chem_index)
    
print(results)

with open('results.json', 'w') as outfile:
    json.dump(results, outfile)
