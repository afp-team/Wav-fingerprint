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
print("Lista:")
lista = ["WjakWokal.wav","Bass.wav","Bell.wav","CasinoPiano.wav","Sax.wav","12Gtr.wav"]
for a, x in enumerate(lista):
    print(a,x)
def lista_startowa(): #menu
    sound = input("Podaj sciezke dzwiekowa:")
    print("'6' zamyka program")
    int_sound=int(sound)
    wczytywanie_wava(int_sound)

def wczytywanie_wava(int_sound):
    if int_sound >= 0 and int_sound <= 5:
        fs_rate, data = wavfile.read(lista[int_sound]) #returns numpy array with a data-type determined from the file
        sample = wave.open(lista[int_sound])
        liczba_kanalow = len(data.shape)
        print("Liczba kanałów: ", liczba_kanalow)
        parametry = sample.getparams()
        print("Parametry: ", parametry)
        music = pyglet.resource.media(lista[int_sound])
        music.play()
        funkcja_FFT(fs_rate,data)
        lista_startowa()
    elif int_sound < 0 or int_sound > 6:
        print("Nie intnieje sciezka dzwiekowa o takim numerze")
        lista_startowa()
    else:
        print("Koniec")



def funkcja_FFT(fs_rate,data):
    lenght = len(data.shape)  # długość wymiarów tablicy
    data = data.astype(float)  # zmienia na typ float
    if lenght == 2:
        data = data.sum(axis=1) / 2  # sumowanie wierszami

    N = data.shape[
        0]  # liczba wierszy, próbek----0≤k<N/2 . Tak więc obliczanie FFT polega na kolejnym dzieleniu próbek na ciągi parzyste
    secs = N / float(fs_rate)  # czas
    Ts = 1 / fs_rate  # sprópkowanie w czasie, okres=1/f
    t = scipy.arange(0, secs, Ts)  # czas od 0 do secs co Ts/ generacja przedziału
    print("Czas ścieżki: ", secs)
    FFT = abs(fft(data))  # wartosc bezwzgledna
    FFT_side = FFT[range(N // 2)]  # one side FFT range

    freqs = scipy.fftpack.fftfreq(data.size, t[1] - t[0])
    freq = freqs[range(N // 2)]  # one side frequency range
    fft_f_side = np.array(freq)

    #print(FFT_side)
    for min_f, fft_value in enumerate(FFT_side):
        if fft_value > 100000000:
            #print("element:", min_f)
            minfft = fft_value
            #print("fft", minfft)
            break

    FFT_side = FFT_side[::-1]

    for max_f, fft_value in enumerate(
            FFT_side):  # enumerate () dodaje licznik do iteracji i zwraca ją (wylicza obiekt), zaczynamy od fft_side max_f=>enumerate; x wartość w FFT_side
        if fft_value > 100000000:
            #print("element:", max_f)
            maxfft = fft_value
            #print("fft", maxfft)
            break

    print("Min. Hz: ", fft_f_side[min_f])
    fft_f_side = fft_f_side[::-1]
    print("Max. Hz: ", fft_f_side[max_f])

    FFT_side = FFT_side[::-1]
    p = plt.plot(freq, abs(FFT_side), "b")
    plt.xlabel('Częstotliwość (Hz)')
    plt.ylabel('Amplituda widma')
    plt.title("Widmo sygnalu")
    plt.show()

    fragment_data = data[30000:32048]
    widmo = fragment_data / np.max(np.abs(data))
    widmo_data = 20 * np.log10(np.abs(np.fft.rfft(widmo * np.hamming(2048))) / 1024)
    f = np.fft.rfftfreq(2048, 1 / fs_rate)
    plt.plot(f, widmo_data)
    plt.xlim(0, 10000)
    plt.ylim(-90, 0)
    plt.xlabel('częstotliwość [Hz]')
    plt.ylabel('amplituda widma [dB]')
    plt.title('Widmo instrumentu')
    plt.show()

    fragment_data = data[30000:32048]
    widmo = fragment_data / np.max(np.abs(data))
    widmo_data = 20 * np.log10(np.abs(np.fft.rfft(widmo * np.hamming(2048))) / 1024)
    f = np.fft.rfftfreq(2048 , 1/fs_rate)
    plt.plot(f, widmo_data)
    plt.xlim(0, 10000)
    plt.ylim(-40, 0)
    plt.xlabel('częstotliwość [Hz]')
    plt.ylabel('amplituda widma [dB]')
    plt.title('Widmo instrumentu')
    plt.show()

    def maksima_widma(widmo, prog, rozmiar_okna, fs_rate):
        ponad = (widmo >= prog).astype(np.int)
        pochodna = np.diff(ponad)
        poczatki = np.where(pochodna == 1)[0] + 1
        konce = np.where(pochodna == -1)[0] + 1
        maksima = []
        for poczatek, koniec in zip(poczatki, konce):
            p = np.argmax(widmo[poczatek:koniec]) + poczatek
            a, b, c = widmo[p - 1:p + 2]
            k = 0.5 * (a - c) / (a - 2 * b + c)
            maksima.append((p + k) * fs_rate / rozmiar_okna)
        print("maksima", maksima)
        return maksima

    maksima = maksima_widma(widmo_data, -40, 2048, fs_rate)
    for m in maksima:
        print('f = {:8.3f}, współczynnik = {:5.2f}'.format(m, m / maksima[0]))
        print("f= ",m)
lista_startowa()


