
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