#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:29:49 2023

@author: quentin
"""

# RX spectum obtained using SpekCalc software (http://spekcalc.weebly.com/)

import matplotlib.pyplot as plt
import numpy as np

def get_data(file):
    
    Data = {}
    
    with open(file) as f:
        lines = f.readlines()
    
    voltage = lines[4].split()[0]
    filtration = lines[8].split()[2]
    
    Data['Voltage'] = voltage
    Data['filtration'] = filtration

    energy = np.zeros(len(lines)-18)
    bin_E = np.zeros(len(lines)-18)

    for i in range(18, len(lines)):
        energy[i-18], bin_E[i-18] = lines[i].split()

    Data['Energy'] = energy
    Data['bin_E'] = bin_E
    
    return Data

# Spectrum as function of the tube voltage
kv_80 = get_data('./Data/spectre_80kv.txt')
kv_90 = get_data('./Data/spectre_90kv.txt')
kv_100 = get_data('./Data/spectre_100kv.txt')
    
plt.figure(figsize=(30, 15))
plt.title('RX spectrum', fontsize=50)
plt.plot(kv_80['Energy'], kv_80['bin_E'], label=f'{kv_80["Voltage"]} kV')
plt.plot(kv_90['Energy'], kv_90['bin_E'], label=f'{kv_90["Voltage"]} kV')
plt.plot(kv_100['Energy'], kv_100['bin_E'], label=f'{kv_100["Voltage"]} kV')
plt.xlabel('Energy (keV)', fontsize=30)
plt.ylabel('dN/dE', fontsize=30)
plt.ylim(0)
plt.xlim(10)
plt.legend(fontsize=25)


# Spectrum as function of the beam filtration 
f_0 = get_data('./Data/spectre_90kv_0mm.txt')
f_1 = get_data('./Data/spectre_90kv_1mm.txt')
f_2 = get_data('./Data/spectre_90kv_2mm.txt')
f_3 = get_data('./Data/spectre_90kv_3mm.txt')
f_4 = get_data('./Data/spectre_90kv_4mm.txt')
f_5 = get_data('./Data/spectre_90kv_5mm.txt')
    
plt.figure(figsize=(30, 15))
plt.title('RX spectrum', fontsize=50)
plt.plot(f_0['Energy'], f_0['bin_E'], label=f'{f_0["filtration"]} mm Al')
plt.plot(f_1['Energy'], f_1['bin_E'], label=f'{f_1["filtration"]} mm Al')
plt.plot(f_2['Energy'], f_2['bin_E'], label=f'{f_2["filtration"]} mm Al')
plt.plot(f_3['Energy'], f_3['bin_E'], label=f'{f_3["filtration"]} mm Al')
plt.plot(f_4['Energy'], f_4['bin_E'], label=f'{f_4["filtration"]} mm Al')
plt.plot(f_5['Energy'], f_5['bin_E'], label=f'{f_5["filtration"]} mm Al')
plt.xlabel('Energy (keV)', fontsize=30)
plt.ylabel('dN/dE', fontsize=30)
plt.ylim(0)
plt.xlim(10)
plt.legend(fontsize=25)