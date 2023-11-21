# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:33:08 2023

@author: flama
"""

import thermo as th
import numpy as np
import matplotlib.pyplot as plt

#propylène glycole : 4254-14-2 a 30 % 
#eau : 7732-18-5

T = -3.5 + 273.15 
P = 101325

Mix = th.Mixture(('4254-14-2', '7732-18-5'), zs = (0.30,0.70), T=T, P=P)
eau = th.Mixture(('4254-14-2', '7732-18-5'), zs = (0.0,0.100), T=T, P=P)

print('Le CP du mélange est de ', Mix.Cp, 'J/Kg * K ')

print('le k du mélange est de ', Mix.k, 'W/mK ')

print('le H du mélange est de ', Mix.H, 'W/m^2K ')
