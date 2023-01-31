#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:39:35 2023

@author: quentin
"""

import pandas as pd
import numpy as np

def get_factor(Dataframe, pas, d, d_eff, size):
    print("Fantôme %.f :"%(size))
    print("Facteur : %.2f\n"%(Dataframe.loc[int((d-min(d_eff))/pas)]['Coefficient 32cm']))

# Récupération des données 
Data_32 = pd.read_excel('SSDE_coefs.xlsx', sheet_name="32 cm")
d_eff_32 = Data_32['Diamètre effectif (cm)'].values*10
coef_32 = Data_32['Facteur'].values*10

Data_16 = pd.read_excel('SSDE_coefs.xlsx', sheet_name="16 cm")
d_eff_16 = Data_16['Diamètre effectif (cm)'].values*10
coef_16 = Data_16['Facteur'].values*10

D_eff_32 = np.linspace(min(d_eff_32), max(d_eff_32), 10000)
coef_32 = np.interp(D_eff_32, d_eff_32, coef_32)
pas_32 = (max(D_eff_32) - min(D_eff_32))/10000

D_eff_16 = np.linspace(min(d_eff_16), max(d_eff_16), 10000)
coef_16 = np.interp(D_eff_16, d_eff_16, coef_16)
pas_16 = (max(D_eff_16) - min(D_eff_16))/10000

Data = pd.DataFrame()
Data['Diamètre effectif 32cm'] = D_eff_32*0.1
Data['Diamètre effectif 16cm'] = D_eff_16*0.1
Data['Coefficient 32cm'] = coef_32*0.1
Data['Coefficient 16cm'] = coef_16*0.1

# Choix du diamètre (cm, 1 chiffre après la virgule) 
Diamètre = 26.4

# Extraction des facteurs correspondant (fantôme de 32cm ou 16cm)
get_factor(Data, pas_32, Diamètre*10, D_eff_32, 32)
get_factor(Data, pas_16, Diamètre*10, D_eff_16, 16)

