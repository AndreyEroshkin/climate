#!/usr/bin/env python
# coding: utf-8



import numpy as np
import CoolProp.CoolProp as CP
import matplotlib.pyplot as plt

def plot_id (ax=None):
    if ax is None:
        ax = plt.gca()
    Tdbvec = np.linspace(-30, 50)+273.15

    # Lines of constant relative humidity
    for RH in np.arange(0.001, 1, 0.1):
        W = CP.HAPropsSI("W","R",RH,"P",101325,"T",Tdbvec)
        plt.plot(W,Tdbvec-273.15, color='k', lw = 0.5)

    # Saturation curve
    W = CP.HAPropsSI("W","R",1,"P",101325,"T",Tdbvec)
    plt.plot(W, Tdbvec-273.15,  color='k', lw=1.5)

    # Lines of constant Vda
    for Vda in np.arange(0.69, 0.961, 0.01):
        R = np.linspace(0.001,1)
        W = CP.HAPropsSI("W","R",R,"P",101325,"Vda",Vda)
        Tdb = CP.HAPropsSI("Tdb","R",R,"P",101325,"Vda",Vda)
        plt.plot(W, Tdb-273.15, color='b', lw=1.5 if abs(Vda % 0.05) < 0.001 else 0.5)

    # Lines of constant wetbulb
    for Twb_C in np.arange(-16, 33, 2):
        if Twb_C == 0:
            continue
        R = np.linspace(0.001, 1)
        print(Twb_C)
        Tdb = CP.HAPropsSI("Tdb","R",R,"P",101325,"Twb",Twb_C+273.15)
        W = CP.HAPropsSI("W","R",R,"P",101325,"Tdb",Tdb)
        plt.plot(W, Tdb-273.15, color='r', lw=1.5 if abs(Twb_C % 10) < 0.001 else 0.5)

    plt.ylabel(r'Dry bulb temperature $T_{\rm db}$ ($^{\circ}$ C)')
    plt.xlabel(r'Humidity Ratio $W$ (kg/kg)')
    plt.xlim(0, 0.030)
    plt.ylim(-30, 55)
    return ax


