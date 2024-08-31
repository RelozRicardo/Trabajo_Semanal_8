#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:27:44 2024

@author: ricardo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:31:02 2024

@author: ricardo
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

from pytc2.sistemas_lineales import group_delay, analyze_sys, plot_plantilla
from pytc2.general import print_latex, print_subtitle, a_equal_b_latex_s

##############################################################################
# ejercicio 2 A
##############################################################################
w0 = np.pi*500
qq = np.sqrt(2)/2
alfa = 1

#my_tf = TransferFunction( [0.8 , 0 , 1], [1 , 0 , 0.8] )
#my_tf = TransferFunction( [1 , 0,0,0 , alfa] , [1-alfa , 0,0,0 , alfa-1] )
my_tf = TransferFunction( [1+alfa , 0,0,0 , alfa+1] , [1 , 0,0,0 , alfa])

plt.close('all')
bodePlot(my_tf, fig_id=1 )
pzmap(my_tf, fig_id=2) #Z plane pole/zero plot
GroupDelay(my_tf, fig_id=3)


# Visualizamos su respuesta en frecuencia
#figaxes = analyze_sys(my_tf, ['TF'])
