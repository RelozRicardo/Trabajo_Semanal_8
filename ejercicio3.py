#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:27:44 2024

@author: ricardo
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot


##############################################################################
# INTEGRADOR CON PERDIDAS
##############################################################################
w0 = 1
qq = np.sqrt(2)/2

my_tf = TransferFunction( [0.9 , 0], [1 , -0.1] )

plt.close('all')
bodePlot(my_tf, fig_id=1 )
pzmap(my_tf, fig_id=2) #Z plane pole/zero plot
GroupDelay(my_tf, fig_id=3)
