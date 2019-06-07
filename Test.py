from __future__ import print_function
import wave


sample = wave.open("Próbki_zdegradowane/Classic_orchestra_128.wav")
parametry = sample.getparams()
print("Parametry pliku oryginalnego:   ", parametry)

sample_deg = wave.open("Próbki_zdegradowane/Classic_orchestra_80.wav")
parametry_deg = sample.getparams()
print("Parametry pliku oryginalnego:   ", parametry_deg)



