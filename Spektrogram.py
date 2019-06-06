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
import scipy.signal as sig


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

fs_rate_deg, data_deg = wavfile.read("Classic_80.wav")
sample_deg = wave.open("Classic_80.wav")
liczba_kanalow_deg = len(data_deg.shape)
# print("Liczba kanałów_deg: ", liczba_kanalow_deg)
parametry_deg = sample_deg.getparams()
print("Parametry pliku zdegradowanego: ", parametry_deg)
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


fragment_data_deg = data_deg[round(liczba_ramek_deg / 2) : round(liczba_ramek_deg / 2) + 4048 ]
ilosc_probek_deg = len(fragment_data_deg)/2

f_deg, t_deg, Sxx_deg = sig.spectrogram(fragment_data_deg, fs=fs_rate_deg, window=np.hamming(ilosc_probek_deg),
                                        nperseg=ilosc_probek_deg, noverlap=(ilosc_probek_deg) * 0.75,
                                        scaling='spectrum', mode='magnitude')

plt.figure(figsize=(16, 8))
plt.pcolormesh(t_deg, f_deg, 20 * np.log10(Sxx_deg))
plt.xlabel('czas [s]')
plt.ylabel('częstotliwość [Hz]')
plt.title('Spektrogram dźwięku klarnetu')
plt.ylim(0, 20000)
plt.colorbar()
plt.show()

Suma_listy_amp_spektrogramu_deg = sum(Sxx_deg)
Suma_amp_spektrogramu_deg = sum(Suma_listy_amp_spektrogramu_deg)
print(Suma_amp_spektrogramu_deg)

fragment_data = data[round(liczba_ramek / 2) : round(liczba_ramek / 2) + 4048 ]
ilosc_probek = len(fragment_data)/2
f, t, Sxx = sig.spectrogram(fragment_data, fs=fs_rate, window=np.hamming(ilosc_probek),
                            nperseg=ilosc_probek, noverlap=(ilosc_probek) * 0.75,
                            scaling='spectrum', mode='magnitude')

plt.figure(figsize=(16, 8))
plt.pcolormesh(t, f, 20 * np.log10(Sxx))
plt.xlabel('czas [s]')
plt.ylabel('częstotliwość [Hz]')
plt.title('Spektrogram dźwięku klarnetu')
plt.ylim(0, 20000)
plt.colorbar()
plt.show()

Suma_listy_amp_spektrogramu = sum(Sxx)
Suma_amp_spektrogramu = sum(Suma_listy_amp_spektrogramu)
print(Suma_amp_spektrogramu)


