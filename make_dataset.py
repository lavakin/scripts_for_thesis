#!/usr/bin/env python3

from chemicals.critical import critical_data_Yaws
from chemicals import CAS_from_any, Tb
import numpy as np
import pandas as pd
from pysmiles import read_smiles
import pickle
import networkx as nx
from calculate_indices import *


chemicals = pd.read_pickle("smiles.pickle")
funct_dict = {'wiener':Path.wiener,'sum_connectivity':Connectivity.sum_connectivity,'randic':Connectivity.randic,'balaban':Path.balaban, 'szeged':Path.szeged, 'revised szeged':Path.revised_szeged,'detour':Path.detour,'harary':Path.harary,'wiener_hosoya':Matching.wiener_hosoya}

dataset = {'molecule':[], 'boiling point':[],'wiener':[],'sum_connectivity':[],'randic':[],'balaban':[], 'szeged':[], 'revised szeged':[],'detour':[],'harary':[], 'path_walk_ratio 1.1':[],'path_walk_ratio 1.2':[],'path_walk_ratio 2.1':[],'path_walk_ratio 2.2':[], 'estrada 2':[],'estrada 4':[],'markov 2':[],'markov 4':[],'wiener_hosoya':[], 'line estrada 2':[],'line estrada 4':[]}

i = 0
for index, row in chemicals.iterrows(): 
    G = read_smiles(row["smiles"], explicit_hydrogen=True)
    atoms = set([x[1] for x in G.nodes(data='element')])
    if atoms.issubset({'C','H'}) and not nx.is_tree(G):
        try:
            boiling_point =  Tb(CAS_from_any(row['chemicals']))
        except(ValueError):
            continue
        if boiling_point == None or len(G)==1:
            continue
        dataset['boiling point'].append(boiling_point)
        for funct_name,funct in funct_dict.items():
            dataset[funct_name].append(funct(G))
        dataset['molecule'].append(row['chemicals'])
        dataset['path_walk_ratio 1.1'].append(Walk.path_walk_ratio1(G,2))
        dataset['path_walk_ratio 1.2'].append(Walk.path_walk_ratio1(G,3))
        dataset['path_walk_ratio 2.1'].append(Walk.path_walk_ratio2(G,2))
        dataset['path_walk_ratio 2.2'].append(Walk.path_walk_ratio2(G,3))
        dataset['estrada 2'].append(Walk.estrada(G,2))
        dataset['estrada 4'].append(Walk.estrada(G,4))
        dataset['markov 2'].append(Walk.markov(G,2))
        dataset['markov 4'].append(Walk.markov(G,4))
        dataset['line estrada 2'].append(Walk.line_estrada(G,2))
        dataset['line estrada 4'].append(Walk.line_estrada(G,4))
        i+=1
        if i%20:
            print(i)

original_df = pd.DataFrame(dataset)
print(original_df)
original_df.to_pickle("pickles/cycles_H.pickle")
