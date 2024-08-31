#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:30:47 2024

@author: ricardo
"""

import sympy as sp
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# Gráficos interactivos
# %matplotlib ipympl
# Gráficos estáticos
#%matplotlib inline

from pytc2.sistemas_lineales import group_delay, analyze_sys, plot_plantilla
from pytc2.general import print_latex, print_subtitle, a_equal_b_latex_s

from sympy import symbols, Matrix
from sympy import init_printing

from scipy.signal import TransferFunction
import matplotlib.pyplot as plt

# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot
##############################################################################
# FILTRO ECUALIZADOR DE FASE 1ER ORDEN
##############################################################################
all_sys = []
all_sys_desc = []
w0 = 1
qq = np.sqrt(2)/2

Dval = ([-0.5, -0.25 , -0.1,0.1, 0.25 , 0.5])

for D in Dval:    
    
    R = -D/(D+2)    
    my_tf = TransferFunction( [R , 1], [1 , -R] )
    
    all_sys += [my_tf]
    all_sys_desc += ['D={:3.2f} f$'.format(D)]
    
# Visualizamos su respuesta en frecuencia
figaxes = analyze_sys(all_sys, all_sys_desc)