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

Czestotliwosc = []
Amplituda = []
for i,x in enumerate(widmo_data):
    if f[i] <= 20000:
        Czestotliwosc.insert(i,f[i])
        Amplituda.insert(i,widmo_data[i])

spectrall_roll_off = (sum(Amplituda)/len(Amplituda)) * 0.85
suma = sum(Amplituda)

minimalna_amplituda_calego_widma = min(Amplituda)
maksymalna_amplituda_calego_widma = max(Amplituda)

for i,x in enumerate(Amplituda):
    if minimalna_amplituda_calego_widma == x:
        czestotliwosc_minimalnej_amplitudy = Czestotliwosc[i]
    if maksymalna_amplituda_calego_widma == x:
        czestotliwosc_maksymalnej_amplitudy = Czestotliwosc[i]

freq_spectrall_roll_off = 0
spectrall_roll_off_amp = 0
for i,x in enumerate(Amplituda):
    if (Amplituda[i] <=spectrall_roll_off+1) and (Amplituda[i] >=spectrall_roll_off-1):
        spectrall_roll_off_amp = x
        freq_spectrall_roll_off = i

plt.plot(Czestotliwosc, Amplituda)
plt.xlim(0, Czestotliwosc[-1])
plt.ylim(minimalna_amplituda_calego_widma, 0)
plt.xlabel('częstotliwość [Hz]')
plt.ylabel('amplituda widma [dB]')
plt.title('Widmo instrumentu')
plt.show()

for i, x in enumerate(Amplituda):
    if (Amplituda[i] <=spectrall_roll_off+1) & (Amplituda[i] >=spectrall_roll_off-1):
        spectrall_roll_off_amp = Amplituda[i]
        freq_spectrall_roll_off = i

minimalna_amplituda = min(Amplituda[0:freq_spectrall_roll_off])

plt.plot(Czestotliwosc, Amplituda)
plt.xlim(0, Czestotliwosc[freq_spectrall_roll_off])
plt.ylim(minimalna_amplituda, 0)
plt.xlabel('częstotliwość [Hz]')
plt.ylabel('amplituda widma [dB]')
plt.title('Widmo')
plt.show()
mean = sum(Amplituda) / len(Amplituda)
dynamic = max(Amplituda) / mean

Amplituda_roll_off = []
for i, x in enumerate(Amplituda):
    if i <= freq_spectrall_roll_off:
        Amplituda_roll_off.insert(i, Amplituda[i])

mean_roll_off = sum(Amplituda_roll_off) / len(Amplituda_roll_off)
dynamic_roll_off = max(Amplituda_roll_off / mean_roll_off)