from __future__ import print_function
import scipy.io.wavfile as wavfile
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
zero_crossing_rate_counter = 0  # licznik przejsc przez zero
for i in range(0, len(fragment_data) - 1):
    if fragment_data[i] * -1 > 0 and fragment_data[i + 1] > 0:
        zero_crossing_rate_counter += 1
zero_crossing_rate = zero_crossing_rate_counter / len(fragment_data)

print("Ilość przejśc przez zero dla sygnału oryginalnego:", zero_crossing_rate_counter, "\n")

# Sygnał zdegradowany:

fragment_data_deg = data_deg[round(liczba_ramek_deg / 2) : round(liczba_ramek_deg / 2) + 2048]
zero_crossing_rate_counter_deg = 0  # licznik przejsc przez zero
for i in range(0, len(fragment_data_deg) - 1):
    if fragment_data_deg[i] * -1 > 0 and fragment_data_deg[i + 1] > 0:
        zero_crossing_rate_counter_deg += 1
zero_crossing_rate_deg = zero_crossing_rate_counter_deg / len(fragment_data_deg)

print("Ilość przejśc przez zero dla sygnału zdegradowanego:", zero_crossing_rate_counter_deg)

#dodać przebieg sygnału w dziedzinie czasu