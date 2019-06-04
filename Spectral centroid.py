
suma_spectrall_centroid_roll_off = 0
for i,x in enumerate(Amplituda):
    if i <= freq_spectrall_roll_off:
        suma_spectrall_centroid_roll_off = suma_spectrall_centroid_roll_off + (Amplituda[i] * Czestotliwosc[i])
spectrall_centroid_rol_off = suma_spectrall_centroid_roll_off / sum(Amplituda)

suma_spectrall_centroid = 0
for i,x in enumerate(Amplituda):
    suma_spectrall_centroid = suma_spectrall_centroid + (Amplituda[i] * Czestotliwosc[i])
spectrall_centroid = suma_spectrall_centroid / sum(Amplituda)