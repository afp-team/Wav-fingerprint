from __future__ import print_function
import Wynik

class odleglosc():

    def roznica(self,parameters,parameters_deg,i,ilosc_probek,lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,
                lista_7,lista_8,lista_9,lista_10,lista_11,lista_12,lista_13,lista_14,lista_15,lista_16,lista_17,
                lista_18,lista_19,lista_20,lista_21,lista_22,lista_23,lista_24,lista_25,lista_26,lista_27,lista_28):


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
        lista_15.insert(i, round(abs(100 - ((parameters_deg[14][i] * 100) / parameters[14][i])), 2))

        lista_16.insert(i, round(abs(100 - ((parameters_deg[15][i] * 100) / parameters[15][i])), 2))
        lista_17.insert(i, round(abs(100 - ((parameters_deg[16][i] * 100) / parameters[16][i])), 2))
        lista_18.insert(i, round(abs(100 - ((parameters_deg[17][i] * 100) / parameters[17][i])), 2))
        lista_19.insert(i, round(abs(100 - ((parameters_deg[18][i] * 100) / parameters[18][i])), 2))
        lista_20.insert(i, round(abs(100 - ((parameters_deg[19][i] * 100) / parameters[19][i])), 2))
        lista_21.insert(i, round(abs(100 - ((parameters_deg[20][i] * 100) / parameters[20][i])), 2))
        lista_22.insert(i, round(abs(100 - ((parameters_deg[21][i] * 100) / parameters[21][i])), 2))
        lista_23.insert(i, round(abs(100 - ((parameters_deg[22][i] * 100) / parameters[22][i])), 2))
        lista_24.insert(i, round(abs(100 - ((parameters_deg[23][i] * 100) / parameters[23][i])), 2))
        lista_25.insert(i, round(abs(100 - ((parameters_deg[24][i] * 100) / parameters[24][i])), 2))
        lista_26.insert(i, round(abs(100 - ((parameters_deg[25][i] * 100) / parameters[25][i])), 2))
        lista_27.insert(i, round(abs(100 - ((parameters_deg[26][i] * 100) / parameters[26][i])), 2))
        lista_28.insert(i, round(abs(100 - ((parameters_deg[27][i] * 100) / parameters[27][i])), 2))



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
        if lista_15[i] > 100:
            lista_15.remove(lista_15[i])
            lista_15.insert(i, 100)
        if lista_16[i] > 100:
            lista_16.remove(lista_16[i])
            lista_16.insert(i, 100)
        if lista_17[i] > 100:
            lista_17.remove(lista_17[i])
            lista_17.insert(i, 100)
        if lista_18[i] > 100:
            lista_18.remove(lista_18[i])
            lista_18.insert(i, 100)
        if lista_19[i] > 100:
            lista_19.remove(lista_19[i])
            lista_19.insert(i, 100)
        if lista_20[i] > 100:
            lista_20.remove(lista_20[i])
            lista_20.insert(i, 100)
        if lista_21[i] > 100:
            lista_21.remove(lista_21[i])
            lista_21.insert(i, 100)
        if lista_22[i] > 100:
            lista_22.remove(lista_22[i])
            lista_22.insert(i, 100)
        if lista_23[i] > 100:
            lista_23.remove(lista_23[i])
            lista_23.insert(i, 100)
        if lista_24[i] > 100:
            lista_24.remove(lista_24[i])
            lista_24.insert(i, 100)
        if lista_25[i] > 100:
            lista_25.remove(lista_25[i])
            lista_25.insert(i, 100)
        if lista_26[i] > 100:
            lista_26.remove(lista_26[i])
            lista_26.insert(i, 100)
        if lista_27[i] > 100:
            lista_27.remove(lista_27[i])
            lista_27.insert(i, 100)
        if lista_28[i] > 100:
            lista_28.remove(lista_28[i])
            lista_28.insert(i, 100)

        #odejmujemy od 100 aby zbadać jak sygnał sie zmienił niezleżnie czy wartośc jet powyżej 100 czy poniżej 100-104=-4; 100-96=4 na końcu zaokrąglamy

        Wynik.wynik.srednia(self,ilosc_probek,lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,lista_7,lista_8,lista_9,lista_10,lista_11,lista_12,lista_13,lista_14,
                            lista_15,lista_16,lista_17,lista_18,lista_19,lista_20,lista_21,lista_22,lista_23,lista_24,lista_25,lista_26,lista_27,lista_28)



