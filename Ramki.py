from __future__ import print_function
import Parametry

lista_1 = []
lista_2 = []
lista_3 = []
lista_4 = []
lista_5 = []
lista_6 = []
lista_7 = []
lista_8 = []
lista_9 = []
lista_10 = []
lista_11 = []
lista_12 = []
lista_13 = []
lista_14 = []
lista_15 = []
lista_16 = []
lista_17 = []
lista_18 = []
lista_19 = []
lista_20 = []
lista_21 = []
lista_22 = []
lista_23 = []
lista_24 = []
lista_25 = []
lista_26 = []
lista_27 = []
lista_28 = []

class ramki():
    def __init__(self):
        print("init")
    def __del__(self):
        print("del")
    def podzial(self,data, liczba_ramek, fs_rate, data_deg, liczba_ramek_deg, fs_rate_deg):

        poczatek_ramki=[0]
        for i,x in enumerate(poczatek_ramki):
            if poczatek_ramki[i] <= liczba_ramek:
                poczatek_ramki.insert(i+1,poczatek_ramki[i] + 2000)

        koniec_ramki=[2048]
        for i,x in enumerate(koniec_ramki):
            if koniec_ramki[i] <= liczba_ramek:
                koniec_ramki.insert(i+1,koniec_ramki[i] + 2000)

        for i,x in enumerate(poczatek_ramki):
            if poczatek_ramki[i] <= liczba_ramek:

                fragment_data = data[poczatek_ramki[i]: koniec_ramki[i]]
                ilosc_probek = len(fragment_data)

                #print("######################################################################################################################")
                #print(ilosc_probek)
                #print("ramka: ",i+1,",","pczątek ramki:",poczatek_ramki[i],",","koniec ramki:",koniec_ramki[i],",","fragment: ",fragment_data)
                #print("i: ", i)

                fragment_data_deg = data_deg[poczatek_ramki[i]: koniec_ramki[i]]
                ilosc_probek_deg = len(fragment_data_deg)

                #print("######################################################################################################################")
                #print(ilosc_probek_deg)
                #print("ramka_deg: ",i+1,",","pczątek ramki_deg:",poczatek_ramki[i],",","koniec ramki_deg:",koniec_ramki[i],",","fragment_deg: ",fragment_data_deg)
                #print("liczba ramek: ", liczba_ramek)

                # procent
                procent = (100 * i) / len(poczatek_ramki)
                print("Postęp parametryzacji:", round(procent, 2), "%")

                Parametry.parametry.parameters(self,data, fragment_data, fs_rate, ilosc_probek, data_deg, fragment_data_deg, fs_rate_deg, ilosc_probek_deg,i,
                                               lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,lista_7,lista_8,lista_9,lista_10,lista_11,lista_12,lista_13,lista_14,
                                               lista_15,lista_16,lista_17,lista_18,lista_19,lista_20,lista_21,lista_22,lista_23,lista_24,lista_25,lista_26,lista_27,lista_28)
