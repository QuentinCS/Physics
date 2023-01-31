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

Eau = f.Coefficient("Données/eau", "Eau", 1)
Air = f.Coefficient("Données/air", "Air", 1.2e-3)
Tissus_mou = f.Coefficient("Données/soft_tissue", "Tissus mou", 1.03)
Os = f.Coefficient("Données/bone", "Os", 1.92)
Poumon = f.Coefficient("Données/lung", "Poumon", 0.26)
PMMA = f.Coefficient("Données/pmma", "PMMA", 1.18)

Aluminium = f.Coefficient("Données/aluminium", "Aluminium", 2.698)
Argon = f.Coefficient("Données/argon", "Argon", 0.001784)
Cuivre = f.Coefficient("Données/cu", "Cuivre", 8.96)
Fer = f.Coefficient("Données/fer", "Fer", 7.874)
Plomb = f.Coefficient("Données/plomb", "Plomb", 11.35)
Zinc = f.Coefficient("Données/zinc", "Zinc", 7.14)


# Plot des coefficients 
Eau.plot()
Plomb.plot()

# Extraction du coefficient d'atténuation pour l'eau 
print(Eau.get_mu_rho(140))
Eau.print_mu_rho(140)

# Plot de l'atténuation dans la matière
#Eau.plot_attenuation(1000)
#Plomb.plot_attenuation(1000)
#Plomb.plot_attenuation(100)


Tissus_mou.plot_attenuation(100)

duree = time.time() - start_time
print ('\n \nTotal running time : %5.3g s' % duree)