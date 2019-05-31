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
import Ramki

fs_rate, data = wavfile.read("Classic_128.wav")
sample = wave.open("Classic_128.wav")
liczba_kanalow = len(data.shape)
#print("Liczba kanałów: ", liczba_kanalow)
parametry = sample.getparams()
print("Parametry pliku oryginalnego:   ", parametry)
liczba_ramek = sample.getnframes()
#print("liczba ramek: ", liczba_ramek)
music = pyglet.resource.media("Classic_128.wav")
music.play()

fs_rate_deg, data_deg = wavfile.read("Classic_8.wav")
sample_deg = wave.open("Classic_8.wav")
liczba_kanalow_deg = len(data_deg.shape)
# print("Liczba kanałów_deg: ", liczba_kanalow_deg)
parametry_deg = sample_deg.getparams()
print("Parametry pliku zdegradowanego: ", parametry_deg)
liczba_ramek_deg = sample_deg.getnframes()
# print("liczba ramek_deg: ", liczba_ramek_deg)
#music = pyglet.resource.media("Classic_8.wav")
#music.play()

import os
os.system("cls")
class main():

    def __init__(self):
        print("Initialization:")
    def __del__(self):
        print("End!")
    def main(self,data, fs_rate, data_deg, fs_rate_deg):

        lenght = len(data.shape)  # długość wymiarów tablicy
        data = data.astype(float)
        if lenght == 2:
            data = data.sum(axis=1) / 2

        lenght_deg = len(data_deg.shape)  # długość wymiarów tablicy
        data_deg = data_deg.astype(float)
        if lenght_deg == 2:
            data_deg = data_deg.sum(axis=1) / 2

        Ramki.ramki.podzial(self,data, liczba_ramek, fs_rate, data_deg, liczba_ramek_deg, fs_rate_deg)

start = main()
start.main(data, fs_rate, data_deg, fs_rate_deg)

