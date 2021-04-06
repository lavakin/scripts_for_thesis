from chemicals.critical import critical_data_Yaws
from chemicals import CAS_from_any, Tb
import numpy as np
import pandas as pd
from pysmiles import read_smiles
import pickle
import networkx as nx
from calculate_indices import *


chemicals = pd.read_pickle("smiles.pickle")
i = 0
for index, row in chemicals.iterrows(): 
    G = read_smiles(row["smiles"], explicit_hydrogen=False)
    atoms = set([x[1] for x in G.nodes(data='element')])
    if atoms.issubset({'C','H'}):
        try:
            boiling_point =  Tb(CAS_from_any(row['chemicals']))
        except(ValueError):
            continue
        if boiling_point == None or len(G)==1:
            continue
        print(row['smiles'])
        Matching.wiener_hosoya(G)
        i+=1
        
        print(i)
