# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:35:33 2018

@author: startol1
"""
import numpy as np
#Bocket: DBTT= +70°C experimental difference: 
#        ghost lines +126°C vs seg-free +49°C
 


#1 Guioneet
def function_DBTT_Guioneet(Ni,Cu, P):
    dbtt = 36 + 310* Ni**2 * Cu + 368*(Cu-0.08) + 2328*(P-0.008)
    return dbtt


def function_DBTT_RSEMcode2010(Ni,Cu, P,f):
    dbtt = 15.8*(1+ 35.7 *max(0,(P-0.008))+6.6* max(0,(Cu - 0.08))+5.8*Ni**2*Cu)*f**0.59
    return dbtt

sign = lambda x: ('+','-')[x < 0]
#
#    wt.%
#     sf      gl
#Ni:  0.72    0.91
#Cu:  0.08    0.14
#P :  0.008   0.022

DBTT_Guioneet_sf=function_DBTT_Guioneet(0.72,0.08,0.008)                       #sf
DBTT_Guioneet_gl=function_DBTT_Guioneet(0.91,0.14,0.022)                       #gl
print('DBTT G : sf = '+str(DBTT_Guioneet_sf)+'°C')
print('DBTT G : sf = '+str(DBTT_Guioneet_gl)+'°C')
print('delta DBTT G : gl-sf = '+str(DBTT_Guioneet_gl-DBTT_Guioneet_sf)+'°C')
print('delta DBTT G : gl-sf = '+str(sign(DBTT_Guioneet_gl-DBTT_Guioneet_sf))+str(np.abs(DBTT_Guioneet_sf-DBTT_Guioneet_gl))+'°C')
