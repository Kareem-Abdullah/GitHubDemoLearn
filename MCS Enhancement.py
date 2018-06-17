# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:11:45 2018

@author: kabdullah
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
from matplotlib.backends.backend_pdf import PdfPages
from pylab import *
ser=np.genfromtxt("MCS Enhancement.csv", delimiter=',',dtype=float)
print(ser[:,1])

plt.figure()
plt.plot(ser[:,0], ser[:,1],linewidth=2.5 , ls='solid' , animated='True')
#plt.ylim((0,1.02))
plt.grid(True, linestyle='--', linewidth=1, which='major')
#plt.legend(['High MCS Penetration for the top 10% Busy Cells'], loc='best')
plt.title("UL Throughput Enhancement after MCS Adjustment")
plt.xlabel("Monitored Days")
plt.ylabel("High MCS Pentration (%)", fontsize='large')
savefig('MCS.pdf', bbox_inches='tight')
plt.show()