# -*- coding: utf-8 -*-
"""
Created on Tue May 15 2015

@author: Christian Monstein
"""

import astropy.io.fits as pf
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm


files = 'BLEN7M_20110730_063002_25.fit'

plt.rcParams.update({'font.size': 18})

hdu = pf.open(files)
#print(hdu.info()) # FIT-file structure

dB = hdu[0].data/255.0*2500.0/25.4 # conversion digits -> dB
mini_dB = np.min(dB) # find lowest value
rel_dB = dB-mini_dB # set background 0

freqs = hdu[1].data['Frequency'][0] # extract freqeuncy axis
time  = hdu[1].data['Time'][0] # extract time axis [sec]

extent = (time[0], time[-1], freqs[-1], freqs[0])

plt.imshow(rel_dB, aspect = 'auto', extent = extent, cmap=cm.jet)
## cm.PRGn, cm.hot, cm.cool, cm.bone, cm.binary, cm.spectral, cm.jet
plt.xlabel('Time [s]')
plt.ylabel('Frequency [MHz]')
plt.title('FIT file Bleien with frequecy table export')

cbar = plt.colorbar()
cbar.ax.set_ylabel('dB above background')

plt.show()

# Write frequencies to a local ASCII-file
c = np.array([freqs]).T
np.savetxt('frequencies.txt', c, fmt='%f')

# Write frequencies in reversed order  to a local ASCII-file
reversed_c = np.array([freqs]).T[::-1]
np.savetxt('frequencies_reversed.txt', reversed_c, fmt='%f')

#plt.figure()
#spectrum = rel_dB[:,:]
#plt.xlim(5,85)
#plt.ylim(0,30)
#plt.plot(freqs,spectrum, color="red",  linewidth=2.5, linestyle="-")
#plt.xlabel('Frequency [MHz]')
#plt.ylabel('Intensity [dB]')
#plt.title('FIT file "BLEN7M_20110730_064502_25.fit". Single spectrum.')
#plt.show()

# time axis
time = pf.open(files)[1].data[0][0]
date = pf.open(files)[0].header['DATE-OBS']
start_time = float(pf.open(files)[0].header['TIME-OBS'].split(":")[0])*60*60 + float(pf.open(files)[0].header['TIME-OBS'].split(":")[1])*60 + float(pf.open(files)[0].header['TIME-OBS'].split(":")[2])  
ut = (time + start_time)/3600

#print(ut)

plt.figure()
lightcurve = rel_dB[167,:]
lightcurve = lightcurve - min(lightcurve)
plt.plot(ut,lightcurve, color="blue",  linewidth=1.5, linestyle="-")
plt.xlabel('Tempo (hora)')
plt.ylabel('Intensidade (dB)')
#plt.title('FIT file "BLEN7M_20110730_054503_25.fit". Single lightcurve at channel 84 (566.18798828125 MHz).')
plt.show()

