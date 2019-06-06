from __future__ import print_function
import scipy.io.wavfile as wavfile
import numpy as np
import wave

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
print("Parametry pliku zdegradowanego: ", parametry_deg, "\n")
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

# Stgnał oryginalny:

fragment_data = data[round(liczba_ramek / 2) : round(liczba_ramek / 2) + 2048]
ilosc_probek = len(fragment_data)
widmo = fragment_data / np.max(np.abs(data))
widmo_data = 10 * np.log10(np.abs(np.fft.rfft(widmo * np.hamming(ilosc_probek))) / 1024)
f = np.fft.rfftfreq(2048, 1 / fs_rate)

Czestotliwosc = []
Amplituda = []
for i,x in enumerate(widmo_data):
    if f[i] <= 20000:
        Czestotliwosc.insert(i,f[i])
        Amplituda.insert(i,widmo_data[i])

spectrall_roll_off = (sum(Amplituda)/len(Amplituda)) * 0.85
suma = sum(Amplituda)

freq_spectrall_roll_off = 0
spectrall_roll_off_amp = 0
for i, x in enumerate(Amplituda):
    if (Amplituda[i] <=spectrall_roll_off+1) & (Amplituda[i] >=spectrall_roll_off-1):
        spectrall_roll_off_amp = Amplituda[i]
        freq_spectrall_roll_off = i



mean = sum(Amplituda) / len(Amplituda)
dynamic = max(Amplituda) / mean

Amplituda_roll_off = []
for i, x in enumerate(Amplituda):
    if i <= freq_spectrall_roll_off:
        Amplituda_roll_off.insert(i, Amplituda[i])

mean_roll_off = sum(Amplituda_roll_off) / len(Amplituda_roll_off)
dynamic_roll_off = max(Amplituda_roll_off / mean_roll_off)

print("Dynamika oryginalnego użytecznego sygnału:", dynamic_roll_off)
print("Dynamika oryginalnego całego sygnału:", dynamic, "\n")

# Sygnał zdeggradowany:

fragment_data_deg = data_deg[round(liczba_ramek_deg / 2) : round(liczba_ramek_deg / 2) + 2048]
ilosc_probek_deg = len(fragment_data_deg)
widmo_deg = fragment_data_deg / np.max(np.abs(data_deg))
widmo_data_deg = 10 * np.log10(np.abs(np.fft.rfft(widmo_deg * np.hamming(ilosc_probek_deg))) / 1024)
f_deg = np.fft.rfftfreq(2048, 1 / fs_rate_deg)

Czestotliwosc_deg = []
Amplituda_deg = []
for i,x in enumerate(widmo_data_deg):
    if f_deg[i] <= 20000:
        Czestotliwosc_deg.insert(i,f_deg[i])
        Amplituda_deg.insert(i,widmo_data_deg[i])

spectrall_roll_off_deg = (sum(Amplituda_deg)/len(Amplituda_deg)) * 0.85

freq_spectrall_roll_off_deg = 0
spectrall_roll_off_amp_deg = 0

for i, x in enumerate(Amplituda_deg):
    if (Amplituda_deg[i] <=spectrall_roll_off_deg + 1) & (Amplituda_deg[i] >=spectrall_roll_off_deg - 1):
        spectrall_roll_off_amp_deg = Amplituda_deg[i]
        freq_spectrall_roll_off_deg = i

mean_deg = sum(Amplituda_deg) / len(Amplituda_deg)
dynamic_deg = max(Amplituda_deg) / mean_deg

Amplituda_roll_off_deg = []
for i, x in enumerate(Amplituda_deg):
    if i <= freq_spectrall_roll_off_deg:
        Amplituda_roll_off_deg.insert(i, Amplituda_deg[i])

mean_roll_off_deg = sum(Amplituda_roll_off_deg) / len(Amplituda_roll_off_deg)
dynamic_roll_off_deg = max(Amplituda_roll_off_deg / mean_roll_off_deg)

print("Dynamika zdegradowanego użytecznego sygnału:", dynamic_roll_off_deg)
print("Dynamika zdegrodowanego całego sygnału:", dynamic_deg)
