#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:16:32 2022

@author: quentin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Coefficient:
    def __init__(self, file_medium, name, rho=1):
        
        # Variables
        self.file_medium = file_medium+'.xlsx'
        self.name = name
        self.rho = rho
        self.Nb = 100000
        
        # Extraction des données
        self.Data = pd.read_excel(self.file_medium, sheet_name="Feuil1")
        self.energy = self.Data['Energy (MeV)'].values*1e3
        self.att = self.Data['µ/ρ (cm2/g)'].values
        self.en = self.Data['µen/ρ (cm2/g)'].values
        

        # Interpolation
        self.e_int = np.linspace(min(self.energy), max(self.energy), self.Nb)
        self.mu_rho = np.interp(self.e_int, self.energy, self.att)
        self.mu_rho_en = np.interp(self.e_int, self.energy, self.en)
        self.pas = (max(self.energy) - min(self.energy))/self.Nb

        self.df_data = pd.DataFrame()
        self.df_data["Energy (keV)"] = self.e_int
        self.df_data["mu_rho (cm2/g)"] = self.mu_rho
        self.df_data["mu_rho_en (cm2/g)"] = self.mu_rho_en
        
        if rho != None:
           self.mu = self.mu_rho * rho
           self.mu_en = self.mu_rho_en * rho
           self.df_data["mu (cm^-1)"] = self.mu
           self.df_data["mu_en (cm^-1)"] = self.mu_en
               
    # Fonctions
    def get_medium(self):
        return self.energy_medium
    def get_name(self):
        return self.name
    def get_mu_rho(self, en):
        return self.df_data.loc[int((en-min(self.energy))/self.pas)]['mu_rho (cm2/g)']
    def get_mu_rho_en(self, en):
        return self.df_data.loc[int((en-min(self.energy))/self.pas)]['mu_rho_en (cm2/g)']
    def get_mu(self, en):
        if self.rho != None:
            return self.df_data.loc[int((en-min(self.energy))/self.pas)]['mu']
        else:
            print("Erreur: mu non disponible, masse volumique pour '%s' non renseignée"%(self.name))
    def get_mu_en(self, en):
        if self.rho !=0:
            return self.df_data.loc[int((en-min(self.energy))/self.pas)]['mu_en']
        else:
            print("Erreur: mu non disponible, masse volumique pour '%s' non renseignée"%(self.name)) 
    def print_mu_rho(self, en):
        print(self.df_data.loc[[int((en-min(self.energy))/self.pas)], ["Energy (keV)", 'mu_rho (cm2/g)']])
    def print_mu_rho_en(self, en):
        print(self.df_data.loc[[int((en-min(self.energy))/self.pas)], ['mu_rho_en (cm2/g)']])
    def print_mu(self, en):
        if self.rho != None:
            print(self.df_data.loc[[int((en-min(self.energy))/self.pas)], ['mu']])
        else:
            print("Erreur: mu non disponible, masse volumique pour '%s' non renseignée"%(self.name))
    def print_mu_en(self, en):
        if self.rho !=0:
            print(self.df_data.loc[[int((en-min(self.energy))/self.pas)], ['mu_en']])
        else:
            print("Erreur: mu non disponible, masse volumique pour '%s' non renseignée"%(self.name))
            
    # Atténuation des rayons x à travers d (en cm) du milieu 
    def attenuation(self, energie, d):
        atte = self.df_data.loc[int((energie-min(self.energy))/self.pas)]['mu (cm^-1)']
        return np.exp(-atte*d)
    
    def plot(self):
        plt.rcParams["figure.figsize"] = [10.0, 10.0]
        plt.rcParams["figure.autolayout"] = True
        fig, ax1 = plt.subplots()
        att = ax1.plot(self.e_int, self.mu_rho, label="$\u03BC/\u03C1$ ($cm^2 g^{-1}$)", color='red')
        plt.title("%s"%(self.name), fontsize=20)
        plt.xlabel("Energie (keV)", fontsize=15)
        plt.ylabel("$\u03BC/\u03C1$ ($cm^2 g^{-1}$)", fontsize=10)
        plt.yscale('log')
        plt.xscale('log')
        ax2 = ax1.twinx()
        en = ax2.plot(self.e_int, self.mu_rho_en, label="$\u03BC_{en}/\u03C1$ ($cm{-1}$)", color='navy')
        plt.ylabel("$\u03BC_{en}/\u03C1$ ($cm^2 g^{-1}$)", fontsize=10)
        plt.yscale('log')
        plt.xscale('log')
        
        # Légende 
        lns = att + en
        labels = [l.get_label() for l in lns]
        plt.legend(lns, labels, loc=0, fontsize=15)

    def plot_mu(self):
        plt.figure(figsize=(10, 10)) 
        plt.plot(self.e_int, self.mu_rho, label=self.name)
        plt.title("Coefficients d'atténuation massique $\u03BC/\u03C1$")
        plt.xlabel("Energie (keV)")
        plt.ylabel("$\u03BC/\u03C1$ ($cm^2 g^{-1}$)")
        plt.xlim(0.01, 0.2)
        plt.yscale('log')
        plt.xscale('log')
        plt.legend(loc=1)
        plt.show()
    
    def plot_muen(self):
        plt.figure(figsize=(10, 10)) 
        plt.plot(self.e_int, self.mu_rho_en, label=self.name)
        plt.title("Coefficients d'absorption massique $\u03BC_{en}/\u03C1$")
        plt.xlabel("Energie (keV)")
        plt.ylabel("$\u03BC_{en}/\u03C1$ ($cm^2 g^{-1}$)")
        plt.xlim(0.01, 0.2)
        plt.yscale('log')
        plt.xscale('log')
        plt.legend(loc=1)
        plt.show()
    
    # Fonction pour tracer l'atténuation des photons dans la matière
    def plot_attenuation(self, energie, distance=200):
        atte = self.df_data.loc[int((energie-min(self.energy))/self.pas)]['mu (cm^-1)']
        attenuation = []
        Nb = 1000
        d = np.linspace(0, distance, Nb)
        
        p_50 = 0
        p_80 = 0
        for i in range(0, len(d)):
            attenuation.append(np.exp(-atte*d[i]))
            if attenuation[i] >= 0.5:
                p_50 = (i*distance)/Nb
            if attenuation[i] >= 0.2:
                p_80 = (i*distance)/Nb
            
        plt.figure(figsize=(10, 10)) 
        plt.plot(d, attenuation, label=self.name)
        plt.title("Atténuation des photons de %.0f keV dans %s"%(energie, self.name), fontsize=15)
        plt.xlabel("Distance (mm)", fontsize=15)
        plt.ylabel("Atténuation (%)", fontsize=15)
        plt.axvline(x=p_50, color='orange', linestyle='--', linewidth=1, label="50%% : %0.1f mm"%(p_50))
        plt.axvline(x=p_80, color='red', linestyle='--', linewidth=1, label="20%% : %0.1f mm"%(p_80))
        plt.grid()
        #plt.ylim(0, 1.2)
        #plt.yscale('log')
        #plt.xscale('log')
        plt.legend(loc=1, fontsize=15)
        plt.show()
        
        