
class wynik():
    def srednia(self,ilosc_probek,lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,lista_7,lista_8,lista_9,lista_10,lista_11,lista_12,lista_13,lista_14,lista_15,lista_16):
        if ilosc_probek > 2048 or ilosc_probek < 2048:
            print("Róźnica1 RMS               : ", lista_1)
            print("Róźnica2 min amp           : ", lista_2)
            print("Róźnica3 f min amp         : ", lista_3)
            print("Róźnica4 MFCC              : ", lista_4)
            print("Róźnica5 f amx amp         : ", lista_5)
            print("Róźnica6 suma              : ", lista_6)
            print("Róźnica7 f roll off        : ", lista_7)
            print("Róźnica8 amp roll off      : ", lista_8)
            print("Róźnica9 zer crosssing     : ", lista_9)
            print("Róźnica10 amp spektrogram  : ", lista_10)
            print("Róźnica11 centroid         : ", lista_11)
            print("Róźnica12 centroid roll off: ", lista_12)
            print("Róźnica13 Euklides dis 1   : ", lista_13)
            print("Róźnica14 Euklides dis 2   : ", lista_14)
            print("Róźnica15 Dynamic          : ", lista_15)
            print("Róźnica16 Dynamic roll off : ", lista_16)

            srednia_1 = sum(lista_1) / (len(lista_1))
            srednia_2 = sum(lista_2) / (len(lista_2))
            srednia_3 = sum(lista_3) / (len(lista_3))
            srednia_4 = sum(lista_4) / (len(lista_4))
            srednia_5 = sum(lista_5) / (len(lista_5))
            srednia_6 = sum(lista_6) / (len(lista_6))
            srednia_7 = sum(lista_7) / (len(lista_7))
            srednia_8 = sum(lista_8) / (len(lista_8))
            srednia_9 = sum(lista_9) / (len(lista_9))
            srednia_10 = sum(lista_10) / (len(lista_10))
            srednia_11 = sum(lista_11) / (len(lista_11))
            srednia_12 = sum(lista_12) / (len(lista_12))
            srednia_13 = sum(lista_13) / (len(lista_13))
            srednia_14 = sum(lista_14) / (len(lista_14))
            srednia_15 = sum(lista_15) / (len(lista_15))
            srednia_16 = sum(lista_16) / (len(lista_16))

            print("Róźnica1 RMS               : ", srednia_1)
            print("Róźnica2 min amp           : ", srednia_2)
            print("Róźnica3 f min amp         : ", srednia_3)
            print("Róźnica4 MFCC              : ", srednia_4)
            print("Róźnica5 f amx amp         : ", srednia_5)
            print("Róźnica6 suma              : ", srednia_6)
            print("Róźnica7 f roll off        : ", srednia_7)
            print("Róźnica8 amp roll off      : ", srednia_8)
            print("Róźnica9 zer crosssing     : ", srednia_9)
            print("Róźnica10 amp spektrogram  : ", srednia_10)
            print("Róźnica11 centroid         : ", srednia_11)
            print("Róźnica12 centroid roll off: ", srednia_12)
            print("Róźnica13 Euklides dis 1   : ", srednia_13)
            print("Róźnica14 Euklides dis 2   : ", srednia_14)
            print("Róźnica14 Euklides dis 2   : ", srednia_15)
            print("Róźnica14 Euklides dis 2   : ", srednia_16)
            lista_suma = [srednia_1, srednia_2, srednia_3, srednia_4, srednia_5, srednia_6, srednia_7,srednia_8, srednia_9,
                          srednia_10, srednia_11, srednia_12,srednia_13,srednia_14,srednia_15,srednia_16]

            print("Sygnał różni się o:", round(sum(lista_suma) / len(lista_suma),2),"%")

