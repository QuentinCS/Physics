#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 18:28:39 2022

@author: quentin
"""

# Script pour l'extraction des valeurs des coefficients d'atténuation et d'absorption pour différents matériaux
# avec des classe objet 
# Choisi l'énergie 
# Données du NIST: https://www.nist.gov/pml/x-ray-mass-attenuation-coefficients

import fonction as f


# Création des classe pour les différents matériaux 

Eau = f.Data("Données/eau", "Eau")
Air = f.Data("Données/air", "Air")
Tissus_mou = f.Data("Données/soft_tissue", "Tissus mou")
Os = f.Data("Données/bone", "Os")
Poumon = f.Data("Données/lung", "Poumon")
PMMA = f.Data("Données/pmma", "PMMA")

Aluminium = f.Data("Données/aluminium", "Aluminium")
Argon = f.Data("Données/argon", "Argon")
Cuivre = f.Data("Données/cu", "Cuivre")
Fer = f.Data("Données/fer", "Fer")
Plomb = f.Data("Données/plomb", "Plomb")
Zinc = f.Data("Données/zinc", "Zinc")


# Plot des coefficients 
Eau.print()

# Extraction du coefficient d'atténuation pour l'eau 
Eau.get_mu(0.14)

# Extraction du coefficient d'absorption pour l'eau 
Eau.get_muen(0.14)
