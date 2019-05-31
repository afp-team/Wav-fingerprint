import numpy as np
import scipy.signal as sig
from scipy.io import wavfile
import matplotlib.pyplot as plt

fs_rate, data = wavfile.read('Bello.wav')

lenght = len(data.shape)  # długość wymiarów tablicy
data = data.astype(float)
if lenght == 2:
    data = data.sum(axis=1) / 2


f, t, Sxx = sig.spectrogram(data, fs=fs_rate, window=np.hamming(2048), nperseg=2048, noverlap=1536, scaling='spectrum', mode='magnitude')

plt.figure(figsize=(16,8))
plt.pcolormesh(t, f, 20 * np.log10(Sxx))
plt.xlabel('czas [s]')
plt.ylabel('częstotliwość [Hz]')
plt.title('Spektrogram dźwięku klarnetu')
plt.ylim(0, 8000)
plt.colorbar()
plt.show()

amplituda_spektrogramu = 20* np.log10(Sxx)
Suma = sum(amplituda_spektrogramu)
Suma_2 = sum(Suma)
print("suma:",Suma_2)