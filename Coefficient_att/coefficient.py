#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 18:28:39 2022

@author: quentin
"""

# Script pour l'extraction des valeurs des coefficients d'atténuation et d'absorption pour différents matériaux
# avec des classe objet 
# Choisir l'énergie (en keV)
# Données du NIST: https://www.nist.gov/pml/x-ray-mass-attenuation-coefficients

import fonction as f
import time

start_time = time.time()

# Création des classe pour les différents matériaux 

Eau = f.Coefficient("Données/eau", "Eau")
Air = f.Coefficient("Données/air", "Air")
Tissus_mou = f.Coefficient("Données/soft_tissue", "Tissus mou")
Os = f.Coefficient("Données/bone", "Os")
Poumon = f.Coefficient("Données/lung", "Poumon")
PMMA = f.Coefficient("Données/pmma", "PMMA")

Aluminium = f.Coefficient("Données/aluminium", "Aluminium")
Argon = f.Coefficient("Données/argon", "Argon")
Cuivre = f.Coefficient("Données/cu", "Cuivre")
Fer = f.Coefficient("Données/fer", "Fer")
Plomb = f.Coefficient("Données/plomb", "Plomb")
Zinc = f.Coefficient("Données/zinc", "Zinc")


# Plot des coefficients 
Eau.plot()

# Extraction du coefficient d'atténuation pour l'eau 
print(Eau.get_mu_rho(140))
Eau.print_mu_rho(140)
Eau.plot_attenuation(140, 50)

# Calcul de l'atténuation (%)
print("Atténuation :", 100*Eau.attenuation(140, 10), "%")

duree = time.time() - start_time
print ('\n \nTotal running time : %5.3g s' % duree)