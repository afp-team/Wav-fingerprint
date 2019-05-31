import numpy as np
import wave
import scipy.io.wavfile as wavfile


buffer_size = 1024



wf = wave.open("Bell.wav")
print("wf:",wf)
no_of_channels = wf.getnchannels()
sample_width = wf.getsampwidth()
frame_rate = wf.getframerate()
no_of_frames = wf.getnframes()


fs_rate, data = wavfile.read("Bell.wav")
print("data",data)
lenght = len(data.shape)  # długość wymiarów tablicy
data = data.astype(float)
if lenght == 2:
    data = data.sum(axis=1) / 2

# plik do stworzenia tablicy
str_data = wf.readframes(buffer_size)

wave_data=np.frombuffer(str_data, dtype = np.int16)
data_array = np.array(wave_data)
print("data",data)
print("wf",data_array)
# ZERO CROSSING RATE
zero_crossing_rate_counter = 0     # licznik przejsc przez zero
for i in range(0, len(data_array) - 1):
    if data_array[i] * -1 > 0 and data_array[i + 1] > 0:
        zero_crossing_rate_counter += 1

zero_crossing_rate = zero_crossing_rate_counter/len(data_array)
print(zero_crossing_rate_counter)
#########################################
#Połowa tych bibliotek nie jest potrzebna jakby co.

#zero_zrossing_rate_counter - dokładna liczba przejść przez 0
#zero_zrossing_rate - przejścia przez zero podzielone przez
 #liczbe wszystkich próbek (w ramce). Taki 'uśredniony' parametr,
#zawsze między zero a 1.