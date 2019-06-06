from __future__ import print_function
import scipy.io.wavfile as wavfile
import numpy as np
import wave
import math

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

Czestotliwosc = []
Amplituda = []
for i,x in enumerate(widmo_data):
    if f[i] <= 20000:
        Czestotliwosc.insert(i,f[i])
        Amplituda.insert(i,widmo_data[i])
prog = max(Amplituda) - 5
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
amp_euklides = [-100, -100]

for i, x in enumerate(indeks):
    amp_euklides.insert(i + 1, Amplituda[indeks[i]])

if amp_euklides[amp_euklides.index(max(amp_euklides)) + 1] == -100:
    dst_1 = 1
else:
    dst_1 = math.sqrt((pow(abs((max(Amplituda) - 5) - max(amp_euklides)), 2) +
                      pow(f_euklides[amp_euklides.index(max(amp_euklides)) + 1] -
                          f_euklides[amp_euklides.index(max(amp_euklides))], 2)))

if amp_euklides[amp_euklides.index(max(amp_euklides)) - 1] == -100:
    dst_2 = 1
else:
    dst_2 = math.sqrt((pow(abs((max(Amplituda) - 5) - max(amp_euklides)), 2) +
                      pow(f_euklides[amp_euklides.index(max(amp_euklides)) - 1] -
                          f_euklides[amp_euklides.index(max(amp_euklides))], 2)))

print("Pierwszy dystans Euklideswy sygnału oryginalnego:", dst_1)
print("Drugi dystans Euklideswy sygnału oryginalnego:", dst_2)

# Sygnał zdegradowany

Czestotliwosc_deg = []
Amplituda_deg = []
for i,x in enumerate(widmo_data_deg):
    if f_deg[i] <= 20000:
        Czestotliwosc_deg.insert(i,f_deg[i])
        Amplituda_deg.insert(i,widmo_data_deg[i])

prog = max(Amplituda_deg) - 5
ponad = (Amplituda_deg >= prog).astype(np.int)
pochodna = np.diff(ponad)
poczatki = np.where(pochodna == 1)[0] + 1
konce = np.where(pochodna == -1)[0] + 1
f_euklides_deg = [-100]
indeks_deg = []

for poczatek, koniec in zip(poczatki, konce):
    p = np.argmax(Amplituda_deg[poczatek:koniec]) + poczatek
    a, b, c = Amplituda_deg[p - 1:p + 2]
    k = 0.5 * (a - c) / (a - 2 * b + c)
    f_euklides_deg.append((p + k) * fs_rate / ilosc_probek_deg)
    indeks_deg.append(p)

f_euklides_deg.append(-100)
amp_euklides_deg = [-100, -100]

for i, x in enumerate(indeks_deg):
    amp_euklides_deg.insert(i + 1, Amplituda[indeks_deg[i]])

if amp_euklides_deg[amp_euklides_deg.index(max(amp_euklides_deg)) + 1] == -100:
    dst_1_deg = 1
else:
    dst_1_deg = math.sqrt((pow(abs((max(Amplituda_deg) - 5) - max(amp_euklides_deg)), 2) +
                      pow(f_euklides_deg[amp_euklides_deg.index(max(amp_euklides_deg)) + 1] -
                          f_euklides_deg[amp_euklides_deg.index(max(amp_euklides_deg))], 2)))
#print("org".dst_1)
if amp_euklides_deg[amp_euklides_deg.index(max(amp_euklides_deg)) - 1] == -100:
    dst_2_deg = 1
else:
    dst_2_deg = math.sqrt((pow(abs((max(Amplituda_deg) - 5) - max(amp_euklides_deg)), 2) +
                      pow(f_euklides_deg[amp_euklides_deg.index(max(amp_euklides_deg)) - 1] -
                          f_euklides_deg[amp_euklides_deg.index(max(amp_euklides_deg))], 2)))

print("Pierwszy dystans Euklideswy sygnału zdegradowanego:", dst_1_deg)
print("Drugi dystans Euklideswy sygnału zdegradowanego:", dst_2_deg)