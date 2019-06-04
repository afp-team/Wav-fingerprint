def calculate_nfft(samplerate, winlen):
    window_length_samples = winlen * samplerate
    nfft = 1
    while nfft < window_length_samples:
        nfft *= 2
    return nfft


fft_size = calculate_nfft(fs_rate, 0.025)
mfcc_org = mfcc(fragment_data, fs_rate, winlen=0.025, winstep=0.01, numcep=13, nfilt=26, nfft=fft_size, lowfreq=0,
                highfreq=20000, preemph=0.97, ceplifter=22, appendEnergy=True, winfunc=lambda x: numpy.ones((x,)))

suma_list_mfcc = sum(mfcc_org)
suma_mfcc = sum(suma_list_mfcc)