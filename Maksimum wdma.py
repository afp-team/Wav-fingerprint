from __future__ import print_function
from scipy.fftpack import fft
from scipy.io import wavfile
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt
import pyglet
import wave
from scipy.fftpack import fftshift

def maksima_widma(widmo,spectrall_roll_off, rozmiar_okna, fs_rate):
    ponad = (widmo >= spectrall_roll_off).astype(np.int)
    pochodna = np.diff(ponad)
    poczatki = np.where(pochodna == 1)[0] + 1
    konce = np.where(pochodna == -1)[0] + 1
    maksima = []
    for poczatek, koniec in zip(poczatki, konce):
        p = np.argmax(widmo[poczatek:koniec]) + poczatek
        #print("p: ",p)
        a, b, c = widmo[p - 1:p + 2]
        k = 0.5 * (a - c) / (a - 2 * b + c)
        #print("k: ",k)
        maksima.append((p + k) * fs_rate / rozmiar_okna)
    #print("maksima", maksima)
    return maksima

maksima = maksima_widma(Amplituda,spectrall_roll_off, 2048, fs_rate)
for i,x in enumerate(maksima):
    print('Częstotliwość podstawowa = {:8.3f}, współczynnik = {:5.2f}'.format(m, m / maksima[0]))
   #for a, m in enumerate(f):
        # if m >= spectrall_roll_off:
        # amplituda = widmo_data[0:a]
        #print("f ", a, m)

Czestotliwosc_podstwowa = maksima[0]
##############################################

def maksima_widma(widmo, prog, rozmiar_okna, fs_rate):
    ponad = (widmo >= prog).astype(np.int)
    pochodna = np.diff(ponad)
    poczatki = np.where(pochodna == 1)[0] + 1
    konce = np.where(pochodna == -1)[0] + 1
    maksima = []
    for poczatek, koniec in zip(poczatki, konce):
        p = np.argmax(widmo[poczatek:koniec]) + poczatek
        # print("p: ",p)
        a, b, c = widmo[p - 1:p + 2]
        k = 0.5 * (a - c) / (a - 2 * b + c)
        # print("k: ",k)
        maksima.append((p + k) * fs_rate / rozmiar_okna)
    # print("maksima", maksima)
    return maksima
# maksima = maksima_widma(widmo_data, -30, 2048, fs_rate)

#print("Częstotliwość podstawowa: ",maksima[0])