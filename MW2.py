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
from python_speech_features import mfcc
from scipy.spatial import distance
import numpy as np
import scipy.signal as sig
from scipy.io import wavfile
import matplotlib.pyplot as plt
from python_speech_features import mfcc


fs_rate, data = wavfile.read("Classic_128_fast_5.wav")
fs_rate_deg, data_deg = wavfile.read("Classic_128.wav")
sample = wave.open("Classic_128.wav")
liczba_kanalow = len(data.shape)
print("Liczba kanałów: ", liczba_kanalow)
parametry = sample.getparams()
print("Parametry: ", parametry)
liczba_ramek = sample.getnframes()
print("liczba ramek: ", liczba_ramek)
#music = pyglet.resource.media("Orginal.wav")
#music.play()


lenght = len(data.shape)  # długość wymiarów tablicy
data = data.astype(float)
if lenght == 2:
    data = data.sum(axis=1) / 2

fragment_data = data[4000:6048]
#print("fragment: ",fragment_data)
widmo = fragment_data / np.max(np.abs(data))
#print("widmo: ", widmo)
widmo_data = 10 * np.log10(np.abs(np.fft.rfft(widmo * np.hamming(2048))) / 1024)
f = np.fft.rfftfreq(2048, 1 / fs_rate)

Czestotliwosc = []
Amplituda = []
for i,x in enumerate(widmo_data):
    if f[i] <= 20000:
        Czestotliwosc.insert(i,f[i])
        Amplituda.insert(i,widmo_data[i])

for a,m in enumerate(Amplituda):
    suma = 0
    suma = suma + Amplituda[a]
#print("suma: ",suma)
spectrall_roll_off = (sum(Amplituda)/len(Amplituda)) * 0.85
print("suma:",spectrall_roll_off)
#print("spectrall roll off: ",spectrall_roll_off)

#for i, x in enumerate(widmo_data):
    #widmo_data[i] = round(x, 2)
#for a,m in enumerate(widmo_data):
    #if m >= spectrall_roll_off:
        #amplituda = widmo_data[0:a]
    #print("amp: ",a,m)

minimalna_amplituda_calego_widma = min(Amplituda)


plt.plot(Czestotliwosc, Amplituda)
plt.xlim(0, Czestotliwosc[-1])
plt.ylim(minimalna_amplituda_calego_widma, 0)
plt.xlabel('częstotliwość [Hz]')
plt.ylabel('amplituda widma [dB]')
plt.title('Widmo instrumentu')
plt.show()

#f = (-spectrall_roll_off) * fs_rate / 2048
#print("f: ",f[25])
#freq = fftshift(widmo)
#print("freq: ",freq)
##############


for i, x in enumerate(Amplituda):
    #widmo_data[i] = round(x, 0)
    if (Amplituda[i] <=spectrall_roll_off+1) & (Amplituda[i] >=spectrall_roll_off-1):
        spectrall_roll_off_amp = Amplituda[i]
        freq_spectrall_roll_off = i




print("Wartość amplitudy: ",spectrall_roll_off,spectrall_roll_off_amp,"dB" )
#print("Komórka czestotliwości granicznej: ",freq_spectrall_roll_off)
print("Częstotliwość graniczna: ",f[freq_spectrall_roll_off],"Hz")
#print("Częstotliwość podstawowa: ",maksima[0])
print("Suma amplitud: ",suma)

minimalna_amplituda = min(Amplituda[0:freq_spectrall_roll_off])

plt.plot(Czestotliwosc, Amplituda)
plt.xlim(0, Czestotliwosc[freq_spectrall_roll_off])
plt.ylim(minimalna_amplituda, 0)
plt.xlabel('częstotliwość [Hz]')
plt.ylabel('amplituda widma [dB]')
plt.title('Widmo')
plt.show()
suma_spectrall_centroid = 0

suma_spectrall_centroid_roll_off = 0
for i,x in enumerate(Amplituda):
    if i <= freq_spectrall_roll_off:
        suma_spectrall_centroid_roll_off = suma_spectrall_centroid_roll_off + (Amplituda[i] * Czestotliwosc[i])
spectrall_centroid_rol_off = suma_spectrall_centroid_roll_off / sum(Amplituda)

suma_spectrall_centroid = 0
for i,x in enumerate(Amplituda):
    suma_spectrall_centroid = suma_spectrall_centroid + (Amplituda[i] * Czestotliwosc[i])
spectrall_centroid = suma_spectrall_centroid / sum(Amplituda)

print("suma_spectrall_centroid:",spectrall_centroid,spectrall_centroid_rol_off)


f, t, Sxx = sig.spectrogram(data[0:2048], fs=fs_rate, window=np.hamming(2048), nperseg=2048, noverlap=1536, scaling='spectrum', mode='magnitude')

plt.figure(figsize=(16,8))
plt.pcolormesh(t, f, 20 * np.log10(Sxx))
plt.xlabel('czas [s]')
plt.ylabel('częstotliwość [Hz]')
plt.title('Spektrogram dźwięku klarnetu')
plt.ylim(0, 20000)
plt.colorbar()
plt.show()

amplituda_spektrogramu = 20* np.log10(Sxx)
Suma = sum(Sxx)
Suma_2 = sum(Suma)
print("suma:",Suma_2)

for i in range(0, len(Amplituda)):
    dst = distance.euclidean(Czestotliwosc[i], Amplituda[i])

print("dst:",dst)
#20044.999595154335

import math
ilosc_probek = 2048
prog = max(Amplituda)-5

ponad = (Amplituda >= prog).astype(np.int)
pochodna = np.diff(ponad)
poczatki = np.where(pochodna == 1)[0] + 1
konce = np.where(pochodna == -1)[0] + 1
f_euklides = [-100]
indeks = []
for poczatek, koniec in zip(poczatki, konce):
    p = np.argmax(Amplituda[poczatek:koniec]) + poczatek
    a, b, c = Amplituda[p - 1:p + 2]
    k = 0.5 * (a - c) / (a - 2 * b + c)
    f_euklides.append((p + k) * fs_rate / ilosc_probek)

    indeks.append(p)
f_euklides.append(-100)
amp_euklides = [-100,-100]
for i, x in enumerate(indeks):
    amp_euklides.insert(i + 1, Amplituda[indeks[i]])

print(amp_euklides)
print(f_euklides)
print("a",amp_euklides[amp_euklides.index(max(amp_euklides)) + 1])

if amp_euklides[amp_euklides.index(max(amp_euklides)) + 1] == -100:
    od_1 = 1
else:
    od_1 = math.sqrt((pow(abs((max(Amplituda) - 5) - max(amp_euklides)), 2) +
                      pow(f_euklides[amp_euklides.index(max(amp_euklides)) + 1] -
                          f_euklides[amp_euklides.index(max(amp_euklides))], 2)))
print("od_1",od_1)
if amp_euklides[amp_euklides.index(max(amp_euklides)) - 1] == -100:
    od_2 = 1
else:
    od_2 = math.sqrt((pow(abs((max(Amplituda) - 5) - max(amp_euklides)), 2) +
                  pow(f_euklides[amp_euklides.index(max(amp_euklides)) - 1] -
                      f_euklides[amp_euklides.index(max(amp_euklides))], 2)))

print("od_2",od_2)





