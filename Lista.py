from __future__ import print_function
import Odleglosc

parameters = []
lista_1_high = []
lista_2_high = []
lista_3_high = []
lista_4_high = []
lista_5_high = []
lista_6_high = []
lista_7_high = []
lista_8_high = []
lista_9_high = []
lista_10_high = []
lista_11_high = []
lista_12_high = []
lista_13_high = []
lista_14_high = []
lista_15_high = []
lista_16_high = []
lista_17_high = []
lista_18_high = []
lista_19_high = []
lista_20_high = []
lista_21_high = []
lista_22_high = []
lista_23_high = []
lista_24_high = []
lista_25_high = []
lista_26_high = []
lista_27_high = []
lista_28_high = []

parameters_deg = []
lista_1_low = []
lista_2_low = []
lista_3_low = []
lista_4_low = []
lista_5_low = []
lista_6_low = []
lista_7_low = []
lista_8_low = []
lista_9_low = []
lista_10_low = []
lista_11_low = []
lista_12_low = []
lista_13_low = []
lista_14_low = []
lista_15_low = []
lista_16_low = []
lista_17_low = []
lista_18_low = []
lista_19_low = []
lista_20_low = []
lista_21_low = []
lista_22_low = []
lista_23_low = []
lista_24_low = []
lista_25_low = []
lista_26_low = []
lista_27_low = []
lista_28_low = []

class listy():

    def Zapis_do_listy(self,rms,min_amp,f_min_amp,f_max_amp,suma,f_roll_off,amp_roll_off,zero,amp_spek,cent,cent_roll_off,mfcc,dst_1,dst_2,dyn,dyn_roll,
                       rms_deg,min_amp_deg,f_min_amp_deg,f_max_amp_deg,suma_deg,f_roll_off_deg,amp_roll_off_deg,zero_deg,amp_spek_deg,cent_deg,cent_roll_off_deg,mfcc_deg,dst_1_deg,dst_2_deg,dyn_deg,dyn_roll_deg,
                       i,ilosc_probek,lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,lista_7,lista_8,lista_9,lista_10,lista_11,lista_12,lista_13,lista_14,
                       lista_15,lista_16,lista_17,lista_18,lista_19,lista_20,lista_21,lista_22,lista_23,lista_24,lista_25,lista_26,lista_27,lista_28):

        lista_1_high.insert(i, rms)
        lista_2_high.insert(i, min_amp)
        lista_3_high.insert(i, f_min_amp)
        lista_4_high.insert(i, f_max_amp)
        lista_5_high.insert(i, suma)
        lista_6_high.insert(i, f_roll_off)
        lista_7_high.insert(i, amp_roll_off)
        lista_8_high.insert(i, zero)
        lista_9_high.insert(i, amp_spek)
        lista_10_high.insert(i, cent)
        lista_11_high.insert(i, cent_roll_off)
        lista_12_high.insert(i, dst_1)
        lista_13_high.insert(i, dst_2)
        lista_14_high.insert(i, dyn)
        lista_15_high.insert(i, dyn_roll)
        lista_16_high.insert(i, mfcc[0])
        lista_17_high.insert(i, mfcc[1])
        lista_18_high.insert(i, mfcc[2])
        lista_19_high.insert(i, mfcc[3])
        lista_20_high.insert(i, mfcc[4])
        lista_21_high.insert(i, mfcc[5])
        lista_22_high.insert(i, mfcc[6])
        lista_23_high.insert(i, mfcc[7])
        lista_24_high.insert(i, mfcc[8])
        lista_25_high.insert(i, mfcc[9])
        lista_26_high.insert(i, mfcc[10])
        lista_27_high.insert(i, mfcc[11])
        lista_28_high.insert(i, mfcc[12])


        lista_1_low.insert(i, rms_deg)
        lista_2_low.insert(i, min_amp_deg)
        lista_3_low.insert(i, f_min_amp_deg)
        lista_4_low.insert(i, f_max_amp_deg)
        lista_5_low.insert(i, suma_deg)
        lista_6_low.insert(i, f_roll_off_deg)
        lista_7_low.insert(i, amp_roll_off_deg)
        lista_8_low.insert(i, zero_deg)
        lista_9_low.insert(i, amp_spek_deg)
        lista_10_low.insert(i, cent_deg)
        lista_11_low.insert(i, cent_roll_off_deg)
        lista_12_low.insert(i, dst_1_deg)
        lista_13_low.insert(i, dst_2_deg)
        lista_14_low.insert(i, dyn_deg)
        lista_15_low.insert(i, dyn_roll_deg)
        lista_16_low.insert(i, mfcc_deg[0])
        lista_17_low.insert(i, mfcc_deg[1])
        lista_18_low.insert(i, mfcc_deg[2])
        lista_19_low.insert(i, mfcc_deg[3])
        lista_20_low.insert(i, mfcc_deg[4])
        lista_21_low.insert(i, mfcc_deg[5])
        lista_22_low.insert(i, mfcc_deg[6])
        lista_23_low.insert(i, mfcc_deg[7])
        lista_24_low.insert(i, mfcc_deg[8])
        lista_25_low.insert(i, mfcc_deg[9])
        lista_26_low.insert(i, mfcc_deg[10])
        lista_27_low.insert(i, mfcc_deg[11])
        lista_28_low.insert(i, mfcc_deg[12])

        parameters = [lista_1_high, lista_2_high, lista_3_high, lista_4_high, lista_5_high, lista_6_high, lista_7_high, lista_8_high,lista_9_high,lista_10_high,lista_11_high,lista_12_high,lista_13_high,
                      lista_14_high,lista_15_high,lista_16_high,lista_17_high,lista_18_high,lista_19_high,lista_20_high,lista_21_high,lista_22_high,lista_23_high,lista_24_high,lista_25_high,lista_26_high,lista_27_high,lista_28_high]
        parameters_deg = [lista_1_low, lista_2_low, lista_3_low, lista_4_low, lista_5_low, lista_6_low, lista_7_low, lista_8_low,lista_9_low,lista_10_low,lista_11_low,lista_12_low,lista_13_low,
                          lista_14_low,lista_15_low,lista_16_low,lista_17_low,lista_18_low,lista_19_low,lista_20_low,lista_21_low,lista_2_low,lista_23_low,lista_24_low,lista_25_low,lista_26_low,lista_27_low,lista_18_low]

        Odleglosc.odleglosc.roznica(self,parameters,parameters_deg,i,ilosc_probek,lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,lista_7,lista_8,lista_9,lista_10,lista_11,lista_12,
                                    lista_13,lista_14,lista_15,lista_16,lista_17,lista_18,lista_19,lista_20,lista_21,lista_22,lista_23,lista_24,lista_25,lista_26,lista_27,lista_28)
