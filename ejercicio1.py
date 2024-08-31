#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:31:02 2024

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
# FILTRO DE MEDIA MOVIL
##############################################################################

all_sys = []
all_sys_desc = []

w0 = 1
qq = np.sqrt(2)/2

my_tf = TransferFunction( [1/3 , 0 , 0 , -1/3], [1, -1, 0,0] )

all_sys += [my_tf]
all_sys_desc += ['N=3']

my_tf = TransferFunction( [1/4 , 0 , 0 , -1/4], [1, -1, 0,0,0] )

all_sys += [my_tf]
all_sys_desc += ['N=4']

my_tf = TransferFunction( [1/5 , 0 , 0 , -1/5], [1, -1, 0,0,0,0] )

all_sys += [my_tf]
all_sys_desc += ['N=5']
    
# Visualizamos su respuesta en frecuencia
figaxes = analyze_sys(all_sys, all_sys_desc)
