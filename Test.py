from __future__ import print_function
import wave


sample = wave.open("Classic_128.wav")
parametry = sample.getparams()
print("Parametry pliku oryginalnego:   ", parametry)

sample_deg = wave.open("Classic_8.wav")
parametry_deg = sample.getparams()
print("Parametry pliku oryginalnego:   ", parametry_deg)



