from __future__ import print_function
import Wynik

class odleglosc():

    def roznica(self,parameters,parameters_deg,i,ilosc_probek,lista_1,lista_2,lista_3,lista_4,lista_5,
                lista_6,lista_7,lista_8,lista_9,lista_10,lista_11,lista_12,lista_13,lista_14):


        lista_1.insert(i, round(abs(100 - ((parameters_deg[0][i] * 100) / parameters[0][i])), 2))
        lista_2.insert(i, round(abs(100 - ((parameters_deg[1][i] * 100) / parameters[1][i])), 2))
        lista_3.insert(i, round(abs(100 - ((parameters_deg[2][i] * 100) / parameters[2][i])), 2))
        lista_4.insert(i, round(abs(100 - ((parameters_deg[3][i] * 100) / parameters[3][i])), 2))
        lista_5.insert(i, round(abs(100 - ((parameters_deg[4][i] * 100) / parameters[4][i])), 2))
        lista_6.insert(i, round(abs(100 - ((parameters_deg[5][i] * 100) / parameters[5][i])), 2))
        lista_7.insert(i, round(abs(100 - ((parameters_deg[6][i] * 100) / parameters[6][i])), 2))
        lista_8.insert(i, round(abs(100 - ((parameters_deg[7][i] * 100) / parameters[7][i])), 2))
        lista_9.insert(i, round(abs(100 - ((parameters_deg[8][i] * 100) / parameters[8][i])), 2))
        lista_10.insert(i, round(abs(100 - ((parameters_deg[9][i] * 100) / parameters[9][i])), 2))
        lista_11.insert(i, round(abs(100 - ((parameters_deg[10][i] * 100) / parameters[10][i])), 2))
        lista_12.insert(i, round(abs(100 - ((parameters_deg[11][i] * 100) / parameters[11][i])), 2))
        lista_13.insert(i, round(abs(100 - ((parameters_deg[12][i] * 100) / parameters[12][i])), 2))
        lista_14.insert(i, round(abs(100 - ((parameters_deg[13][i] * 100) / parameters[13][i])), 2))

        if lista_1[i] > 100:
            lista_1.remove(lista_1[i])
            lista_1.insert(i, 100)
        if lista_2[i] > 100:
            lista_2.remove(lista_2[i])
            lista_2.insert(i, 100)
        if lista_3[i] > 100:
            lista_3.remove(lista_3[i])
            lista_3.insert(i, 100)
        if lista_4[i] > 100:
            lista_4.remove(lista_4[i])
            lista_4.insert(i, 100)
        if lista_5[i] > 100:
            lista_5.remove(lista_5[i])
            lista_5.insert(i, 100)
        if lista_6[i] > 100:
            lista_6.remove(lista_6[i])
            lista_6.insert(i, 100)
        if lista_7[i] > 100:
            lista_7.remove(lista_7[i])
            lista_7.insert(i, 100)
        if lista_8[i] > 100:
            lista_8.remove(lista_8[i])
            lista_8.insert(i, 100)
        if lista_9[i] > 100:
            lista_9.remove(lista_9[i])
            lista_9.insert(i, 100)
        if lista_10[i] > 100:
            lista_10.remove(lista_10[i])
            lista_10.insert(i, 100)
        if lista_11[i] > 100:
            lista_11.remove(lista_11[i])
            lista_11.insert(i, 100)
        if lista_12[i] > 100:
            lista_12.remove(lista_12[i])
            lista_12.insert(i, 100)
        if lista_13[i] > 100:
            lista_13.remove(lista_13[i])
            lista_13.insert(i, 100)
        if lista_14[i] > 100:
            lista_14.remove(lista_14[i])
            lista_14.insert(i, 100)

        #odejmujemy od 100 aby zbadać jak sygnał sie zmienił niezleżnie czy wartośc jet powyżej 100 czy poniżej 100-104=-4; 100-96=4 na końcu zaokrąglamy

        Wynik.wynik.srednia(self,ilosc_probek,lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,lista_7,lista_8,lista_9,lista_10,lista_11,lista_12,lista_13,lista_14)


