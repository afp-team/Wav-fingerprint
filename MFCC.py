from __future__ import print_function
import scipy.io.wavfile as wavfile
import wave
import numpy as np
from python_speech_features import mfcc
import numpy


fs_rate, data = wavfile.read("Classic_128.wav")
sample = wave.open("Classic_128.wav")
liczba_kanalow = len(data.shape)
#print("Liczba kanałów: ", liczba_kanalow)
parametry = sample.getparams()
print("Parametry pliku oryginalnego:   ", parametry)
liczba_ramek = sample.getnframes()
#print("liczba ramek: ", liczba_ramek)
#music = pyglet.resource.media("Classic_128.wav")
#music.play()

fs_rate_deg, data_deg = wavfile.read("Classic_8.wav")
sample_deg = wave.open("Classic_8.wav")
liczba_kanalow_deg = len(data_deg.shape)
# print("Liczba kanałów_deg: ", liczba_kanalow_deg)
parametry_deg = sample_deg.getparams()
print("Parametry pliku zdegradowanego: ", parametry_deg,"\n")
liczba_ramek_deg = sample_deg.getnframes()
# print("liczba ramek_deg: ", liczba_ramek_deg)
#music = pyglet.resource.media("Classic_8.wav")
#music.play()

lenght = len(data.shape)
data = data.astype(float)
if lenght == 2:
    data = data.sum(axis=1) / 2

lenght_deg = len(data_deg.shape)
data_deg = data_deg.astype(float)
if lenght_deg == 2:
    data_deg = data_deg.sum(axis=1) / 2

fragment_data = data[round(liczba_ramek / 2) : round(liczba_ramek / 2) + 2048]
ilosc_probek = len(fragment_data)
widmo = fragment_data / np.max(np.abs(data))
widmo_data = 10 * np.log10(np.abs(np.fft.rfft(widmo * np.hamming(ilosc_probek))) / 1024)
f = np.fft.rfftfreq(2048, 1 / fs_rate)

fragment_data_deg = data_deg[round(liczba_ramek_deg / 2) : round(liczba_ramek_deg / 2) + 2048]
ilosc_probek_deg = len(fragment_data_deg)
widmo_deg = fragment_data_deg / np.max(np.abs(data_deg))
widmo_data_deg = 10 * np.log10(np.abs(np.fft.rfft(widmo_deg * np.hamming(ilosc_probek_deg))) / 1024)
f_deg = np.fft.rfftfreq(2048, 1 / fs_rate_deg)

def calculate_nfft(samplerate, winlen):
    window_length_samples = winlen * samplerate
    nfft = 1
    while nfft < window_length_samples:
        nfft *= 2
    return nfft


fft_size = calculate_nfft(fs_rate, 0.025)
mfcc_org = mfcc(fragment_data, fs_rate, winlen=0.025, winstep=0.01, numcep=13, nfilt=26, nfft=fft_size, lowfreq=0,
                highfreq=20000, preemph=0.97, ceplifter=22, appendEnergy=True, winfunc=lambda x: numpy.ones((x,)))

suma_list_mfcc = sum(mfcc_org)
print(suma_list_mfcc,"\n")

mfcc_deg = mfcc(fragment_data_deg, fs_rate_deg, winlen=0.025, winstep=0.01, numcep=13, nfilt=26, nfft=fft_size,lowfreq=0,
                    highfreq=20000, preemph=0.97, ceplifter=22, appendEnergy=True,winfunc=lambda x: numpy.ones((x,)))

suma_list_mfcc_deg = sum(mfcc_deg)
print(suma_list_mfcc_deg)

wynik = suma_list_mfcc[0] / sum(suma_list_mfcc)
print(wynik)

wynik_2 = suma_list_mfcc_deg[0] / sum(suma_list_mfcc_deg)
print(wynik_2)