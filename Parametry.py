from __future__ import print_function
import Lista
import numpy as np
import scipy.signal as sig
from python_speech_features import mfcc
import numpy
import math
class parametry():

    def parameters(self,data, fragment_data, fs_rate, ilosc_probek, data_deg, fragment_data_deg, fs_rate_deg, ilosc_probek_deg, komorka,
                   lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,lista_7,lista_8,lista_9,lista_10,lista_11,lista_12,lista_13,lista_14,lista_15,lista_16):
# FFT
        #print("fragment: ",fragment_data)
        widmo = fragment_data / np.max(np.abs(data))
        #print("widmo: ", widmo)
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
            #widmo_data[i] = round(x, 0)
            if (Amplituda[i] <=spectrall_roll_off+1) and (Amplituda[i] >=spectrall_roll_off-1):
                spectrall_roll_off_amp = x
                freq_spectrall_roll_off = i

        #print("Wartość amplitudy 85%: ",spectrall_roll_off,"dB" )
        #print("Minimalna amplituda widma: ", minimalna_amplituda_calego_widma)
        #print("Częstotliwość minmalnej amplitudy: ", czestotliwosc_minimalnej_amplitudy)
        #print("Maksymalna amplituda widma: ", maksymalna_amplituda_calego_widma)
        #print("Częstotliwość maksymalnej amplitudy: ", czestotliwosc_maksymalnej_amplitudy)
        #print("Suma amplitud: ", suma)
        #print("Częstotliwość graniczna: ", f[freq_spectrall_roll_off], "Hz")
        #print("Amplituda częstotliwości granicznej: ", spectrall_roll_off_amp)
        #print("Komórka czestotliwości granicznej: ",freq_spectrall_roll_off)

# Zero crossing
        zero_crossing_rate_counter = 0  # licznik przejsc przez zero
        for i in range(0, len(fragment_data) - 1):
            if fragment_data[i] * -1 > 0 and fragment_data[i + 1] > 0:
                zero_crossing_rate_counter += 1
        zero_crossing_rate = zero_crossing_rate_counter / len(fragment_data)
# RMS
        rms = max(Amplituda) * 0.707
        suma = sum(Amplituda)

# Euclides distance
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

# Spektrogram
        f, t, Sxx = sig.spectrogram(fragment_data, fs=fs_rate, window=np.hamming(ilosc_probek),
                                                nperseg=ilosc_probek, noverlap=ilosc_probek * 0.75,
                                                scaling='spectrum', mode='magnitude')

        # plt.figure(figsize=(16, 8))
        # plt.pcolormesh(t, f, 20 * np.log10(Sxx))
        # plt.xlabel('czas [s]')
        # plt.ylabel('częstotliwość [Hz]')
        # plt.title('Spektrogram dźwięku klarnetu')
        # plt.ylim(0, 20000)
        # plt.colorbar()
        # plt.show()

        Suma_listy_amp_spektrogramu = sum(Sxx)
        Suma_amp_spektrogramu = sum(Suma_listy_amp_spektrogramu)

# Spectrall centroid
        suma_spectrall_centroid_roll_off = 0
        for i,x in enumerate(Amplituda):
            if i <= freq_spectrall_roll_off:
                suma_spectrall_centroid_roll_off = suma_spectrall_centroid_roll_off + (Amplituda[i] * Czestotliwosc[i])
        spectrall_centroid_rol_off = suma_spectrall_centroid_roll_off / sum(Amplituda)

        suma_spectrall_centroid = 0
        for i,x in enumerate(Amplituda):
            suma_spectrall_centroid = suma_spectrall_centroid + (Amplituda[i] * Czestotliwosc[i])
        spectrall_centroid = suma_spectrall_centroid / sum(Amplituda)

#MFCC
        def calculate_nfft(samplerate, winlen):
            window_length_samples = winlen * samplerate
            nfft = 1
            while nfft < window_length_samples:
                nfft *= 2
            return nfft
        fft_size = calculate_nfft(fs_rate,0.025)
        mfcc_org = mfcc(fragment_data, fs_rate, winlen=0.025, winstep=0.01, numcep=13, nfilt=26, nfft=fft_size,lowfreq=0,
                    highfreq=20000, preemph=0.97, ceplifter=22, appendEnergy=True,winfunc=lambda x: numpy.ones((x,)))

        suma_list_mfcc = sum(mfcc_org)
        suma_mfcc = sum(suma_list_mfcc)

# Dynamic
        mean = sum(Amplituda) / len(Amplituda)
        dynamic = max(Amplituda) / mean

        Amplituda_roll_off = []
        for i, x in enumerate(Amplituda):
            if i <= freq_spectrall_roll_off:
                Amplituda_roll_off.insert(i, Amplituda[i])

        mean_roll_off = sum(Amplituda_roll_off) / len(Amplituda_roll_off)
        dynamic_roll_off = max(Amplituda_roll_off / mean_roll_off)

#### Zdegradowany plik, parametry:

# FFT
        widmo_deg = fragment_data_deg / np.max(np.abs(data_deg))
        #print("widmo: ", widmo)
        widmo_data_deg = 10 * np.log10(np.abs(np.fft.rfft(widmo_deg * np.hamming(ilosc_probek_deg))) / 1024)
        f_deg = np.fft.rfftfreq(2048, 1 / fs_rate_deg)

        Czestotliwosc_deg = []
        Amplituda_deg = []
        for i,x in enumerate(widmo_data_deg):
            if f_deg[i] <= 20000:
                Czestotliwosc_deg.insert(i,f_deg[i])
                Amplituda_deg.insert(i,widmo_data_deg[i])

        spectrall_roll_off_deg = (sum(Amplituda_deg)/len(Amplituda_deg)) * 0.85

        minimalna_amplituda_calego_widma_deg = min(Amplituda_deg)
        maksymalna_amplituda_calego_widma_deg = max(Amplituda_deg)
        for i,x in enumerate(Amplituda_deg):
            if minimalna_amplituda_calego_widma_deg == Amplituda_deg[i]:
                czestotliwosc_minimalnej_amplitudy_deg = Czestotliwosc_deg[i]
            if maksymalna_amplituda_calego_widma_deg == Amplituda_deg[i]:
                czestotliwosc_maksymalnej_amplitudy_deg = Czestotliwosc_deg[i]

        freq_spectrall_roll_off_deg = 0
        spectrall_roll_off_amp_deg = 0
        for i,x in enumerate(Amplituda_deg):
            #widmo_data[i] = round(x, 0)
            if (Amplituda_deg[i] <= spectrall_roll_off_deg + 1) and (Amplituda_deg[i] >= spectrall_roll_off_deg - 1):
                spectrall_roll_off_amp_deg = x
                freq_spectrall_roll_off_deg = i


        #print("Wartość amplitudy 85%_deg: ",spectrall_roll_off_deg,"dB" )
        #print("Minimalna amplituda widma_deg: ", minimalna_amplituda_calego_widma_deg)
        #print("Częstotliwość minmalnej amplitudy_deg: ", czestotliwosc_minimalnej_amplitudy_deg)
        #print("Maksymalna amplituda widma_deg: ", maksymalna_amplituda_calego_widma_deg)
        #print("Częstotliwość maksymalnej amplitudy_deg: ", czestotliwosc_maksymalnej_amplitudy_deg)
        #print("Suma amplitud_deg: ", suma_deg)
        #print("Częstotliwość graniczna_deg: ", f_deg[freq_spectrall_roll_off_deg], "Hz")
        #print("Amplituda częstotliwości granicznej_deg: ", spectrall_roll_off_amp_deg)
        #print("Komórka czestotliwości granicznej_deg: ",freq_spectrall_roll_off_deg)

# Zero crossing
        zero_crossing_rate_counter_deg = 0  # licznik przejsc przez zero
        for i in range(0, len(fragment_data_deg) - 1):
            if fragment_data_deg[i] * -1 > 0 and fragment_data_deg[i + 1] > 0:
                zero_crossing_rate_counter_deg += 1

        zero_crossing_rate_deg = zero_crossing_rate_counter_deg / len(fragment_data_deg)  # rodzaj uśredniania

# RMS
        rms_deg = max(Amplituda_deg) * 0.707
        suma_deg = sum(Amplituda_deg)

# Euklides distance
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

    # Spektrogram
        f_deg, t_deg, Sxx_deg = sig.spectrogram(fragment_data_deg, fs=fs_rate_deg, window=np.hamming(ilosc_probek_deg),
                                                nperseg=ilosc_probek_deg, noverlap=ilosc_probek_deg * 0.75,
                                                scaling='spectrum', mode='magnitude')

        #plt.figure(figsize=(16, 8))
        #plt.pcolormesh(t, f, 20 * np.log10(Sxx))
        #plt.xlabel('czas [s]')
        #plt.ylabel('częstotliwość [Hz]')
        #plt.title('Spektrogram dźwięku klarnetu')
        #plt.ylim(0, 20000)
        #plt.colorbar()
        #plt.show()

        Suma_listy_amp_spektrogramu_deg = sum(Sxx_deg)
        Suma_amp_spektrogramu_deg = sum(Suma_listy_amp_spektrogramu_deg)

# Spectrall centroid
        suma_spectrall_centroid_roll_off_deg = 0
        for i,x in enumerate(Amplituda_deg):
            if i <= freq_spectrall_roll_off_deg:
                suma_spectrall_centroid_roll_off_deg = suma_spectrall_centroid_roll_off_deg + (Amplituda_deg[i] * Czestotliwosc_deg[i])
        spectrall_centroid_rol_off_deg = suma_spectrall_centroid_roll_off_deg / sum(Amplituda_deg)

        suma_spectrall_centroid_deg = 0
        for i,x in enumerate(Amplituda_deg):
            suma_spectrall_centroid_deg = suma_spectrall_centroid_deg + (Amplituda_deg[i] * Czestotliwosc_deg[i])
        spectrall_centroid_deg = suma_spectrall_centroid_deg / sum(Amplituda_deg)

#MFCC
        mfcc_deg = mfcc(fragment_data_deg, fs_rate_deg, winlen=0.025, winstep=0.01, numcep=13, nfilt=26, nfft=fft_size,lowfreq=0,
                    highfreq=20000, preemph=0.97, ceplifter=22, appendEnergy=True,winfunc=lambda x: numpy.ones((x,)))

        suma_list_mfcc_deg = sum(mfcc_deg)
        suma_mfcc_deg = sum(suma_list_mfcc_deg)

# Dynamic
        mean_deg = sum(Amplituda_deg) / len(Amplituda_deg)
        dynamic_deg = max(Amplituda_deg) / mean_deg

        Amplituda_roll_off_deg = []
        for i, x in enumerate(Amplituda_deg):
            if i <= freq_spectrall_roll_off_deg:
                Amplituda_roll_off_deg.insert(i, Amplituda_deg[i])

        mean_roll_off_deg = sum(Amplituda_roll_off_deg) / len(Amplituda_roll_off_deg)
        dynamic_roll_off_deg = max(Amplituda_roll_off_deg / mean_roll_off_deg)



        Lista.listy.Zapis_do_listy(self,rms,minimalna_amplituda_calego_widma,czestotliwosc_minimalnej_amplitudy,czestotliwosc_maksymalnej_amplitudy,suma,f[freq_spectrall_roll_off],spectrall_roll_off_amp,zero_crossing_rate_counter,Suma_amp_spektrogramu,spectrall_centroid,spectrall_centroid_rol_off,suma_mfcc,dst_1,dst_2,dynamic,dynamic_roll_off,
                             rms_deg,minimalna_amplituda_calego_widma_deg,czestotliwosc_minimalnej_amplitudy_deg,czestotliwosc_maksymalnej_amplitudy_deg,suma_deg,f_deg[freq_spectrall_roll_off_deg],spectrall_roll_off_amp_deg,zero_crossing_rate_counter_deg,Suma_amp_spektrogramu_deg,spectrall_centroid_deg,spectrall_centroid_rol_off_deg,suma_mfcc_deg,dst_1_deg,dst_2_deg,dynamic_deg,dynamic_roll_off_deg,
                             komorka,ilosc_probek,lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,lista_7,lista_8,lista_9,lista_10,lista_11,lista_12,lista_13,lista_14,lista_15,lista_16)


        #sql dml scharakteryzować
        #tabelak wyciągnąc imiona nazwiska iq wyższe niż 100





