# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:33:08 2023

@author: flama
"""

import thermo as th
import numpy as np
import matplotlib.pyplot as plt

prop_gly = "4254-14-2"
eau = "7732-18-5"

T = -3.5 + 273.15 
P = 101325 #on pose l'hypothèse que l'on est à pression atmosphérique dans
#la brasserie

#Mix = th.Mixture((prop_gly, eau), zs = (0.30,0.70), T=T, P=P)
#eau = th.Mixture((prop_gly, eau), zs = (0.0,0.100), T=T, P=P)

temp=np.arange(-10,5,0.1)
k_mel=[]
mu_mel=[]
Cp_mel=[]

for i in range(len(temp)):
  Mix = th.Mixture((prop_gly, eau), zs = (0.30,0.70), T=temp[i]+273.15, P=P)
  k_mel.append(Mix.k)
  mu_mel.append(Mix.mu)
  Cp_mel.append(Mix.Cp)

plt.figure()
plt.plot(temp,k_mel,'g')
plt.xlabel('Température (°C)')
plt.grid(True)
plt.ylabel("Conductivité thermique du mélange de propylène glycol et d'eau (W*K/m)")
plt.title('Conductivité thermique du mélange de refroidissement entre -10°C et 5°C')
plt.show()

plt.figure()
plt.plot(temp,mu_mel,'r')
plt.xlabel('Température (°C)')
plt.grid(True)
plt.ylabel("Viscosité dynamique du mélange de propylène glycol et d'eau (Pa*s)")
plt.title('Viscosité dynamique du mélange de refroidissement entre -10°C et 5°C')
plt.show()

plt.figure()
plt.plot(temp,Cp_mel,'b')
plt.xlabel('Température (°C)')
plt.grid(True)
plt.ylabel("Capacité thermique à pression constante du mélange de propylène glycol et d'eau (J*K/kg)")
plt.title('Capacité thermique à pression constante du mélange de refroidissement entre -10°C et 5°C')
plt.show()


