#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:16:32 2022

@author: quentin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Data:
    def __init__(self, file_medium, name):
        
        # Variables
        self.file_medium = file_medium+'.xlsx'
        self.name = name
        self.Nb = 1000
        
        # Extraction des données
        self.Data = pd.read_excel(self.file_medium, sheet_name="Feuil1")
        self.energy = self.Data['Energy (MeV)'].values
        self.att = self.Data['µ/ρ (cm2/g)'].values
        self.en = self.Data['µen/ρ (cm2/g)'].values

        # Interpolation
        self.e_int = np.linspace(min(self.energy), max(self.energy), self.Nb)
        self.mu = np.interp(self.e_int, self.energy, self.att)
        self.mu_en = np.interp(self.e_int, self.energy, self.en)
        self.pas = (max(self.energy) - min(self.energy))/self.Nb

        self.df_data = pd.DataFrame()
        self.df_data["Energy"] = self.e_int
        self.df_data["mu"] = self.mu
        self.df_data["mu_en"] = self.mu_en
        
        
        
    # Fonctions
    def get_medium(self):
        return self.energy_medium
    def get_name(self):
        return self.name
    def get_mu(self, en):
        print(self.df_data.loc[[int(en/self.pas)], ['mu']])
    def get_muen(self, en):
        print(self.df_data.loc[[int(en/self.pas)], ['mu_en']])

    def print(self):
        plt.rcParams["figure.figsize"] = [10.0, 10.0]
        plt.rcParams["figure.autolayout"] = True
        fig, ax1 = plt.subplots()
        att = ax1.plot(self.e_int, self.mu, label="$\u03BC/\u03C1$ ($cm^2 g^{-1}$)", color='red')
        plt.title("%s"%(self.name), fontsize=20)
        plt.xlabel("Energie (MeV)", fontsize=15)
        plt.ylabel("$\u03BC/\u03C1$ ($cm^2 g^{-1}$)", fontsize=10)
        plt.yscale('log')
        plt.xscale('log')
        ax2 = ax1.twinx()
        en = ax2.plot(self.e_int, self.mu_en, label="$\u03BC_{en}/\u03C1$ ($cm{-1}$)", color='navy')
        plt.ylabel("$\u03BC_{en}/\u03C1$ ($cm^2 g^{-1}$)", fontsize=10)
        plt.yscale('log')
        plt.xscale('log')
        
        # Légende 
        lns = att + en
        labels = [l.get_label() for l in lns]
        plt.legend(lns, labels, loc=0, fontsize=15)

    def print_mu(self):
        plt.figure(figsize=(10, 10)) 
        plt.plot(self.e_int, self.mu, label=self.name)
        plt.title("Coefficients d'atténuation $\u03BC/\u03C1$")
        plt.xlabel("Energie (MeV)")
        plt.ylabel("$\u03BC/\u03C1$ ($cm^2 g^{-1}$)")
        plt.xlim(0.01, 0.2)
        plt.yscale('log')
        plt.xscale('log')
        plt.legend(loc=1)
        plt.show()
    
    def print_muen(self):
        plt.figure(figsize=(10, 10)) 
        plt.plot(self.e_int, self.mu_en, label=self.name)
        plt.title("Coefficients d'absorption $\u03BC_{en}/\u03C1$")
        plt.xlabel("Energie (MeV)")
        plt.ylabel("$\u03BC_{en}/\u03C1$ ($cm^2 g^{-1}$)")
        plt.xlim(0.01, 0.2)
        plt.yscale('log')
        plt.xscale('log')
        plt.legend(loc=1)
        plt.show()