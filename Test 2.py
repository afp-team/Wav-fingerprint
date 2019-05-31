
Amplituda_deg = [1,2,3]
suma_deg = 0
for a, m in enumerate(Amplituda_deg):

    suma_deg = suma_deg + Amplituda_deg[a]
print(suma_deg)


def spectral_centroid(Amplituda):
    suma_mianownik = 0.0
    for i,x in enumerate(Amplituda):
        suma_mianownik = suma_mianownik + (Amplituda[i] * -1)
    f = 10.75
    suma_licznik = 0.0
    temp = 0.0
    for each in Amplituda:
        temp = f * (each * -1)
        suma_licznik = suma_licznik + temp
        f = f + 21.5

    spectral_centroid = suma_licznik/suma_mianownik

spectral_centroid(Amplituda)