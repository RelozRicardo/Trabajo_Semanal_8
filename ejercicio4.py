#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:30:47 2024

@author: ricardo
"""

from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

##############################################################################
# FILTRO ELIMINA CONTINUA
##############################################################################
w0 = 1
qq = np.sqrt(2)/2

my_tf = TransferFunction( [1 , -1], [1 , -0.9] )

plt.close('all')
bodePlot(my_tf, fig_id=1 )
pzmap(my_tf, fig_id=2) #Z plane pole/zero plot
GroupDelay(my_tf, fig_id=3)
