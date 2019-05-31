ramki=[0]
liczba_ramek = 100000


for i,x in enumerate(ramki):
    if ramki[i] <= liczba_ramek:
        ramki[0] = 0
        ramki.insert(i+1,ramki[i] + 2048)
        #print(x)
print("ramki: ", ramki)

ciag_parzysty=[2]
for i,x in enumerate(ciag_parzysty):
    if len.ramki <= len.ciag_parzysty:
        ciag_parzysty.insert(i,ciag_parzysty[i] + 4)

print("Ciąg parzysty: ",ciag_parzysty)


ciag_parzysty=[2]
for i,x in enumerate(ciag_parzysty):
    if len(ramki) > len(ciag_parzysty):
        ciag_parzysty.insert(i+1,ciag_parzysty[i] + 4)
#print("Ciąg parzysty: ",ciag_parzysty)
#print(len(ramki)," ", len(ciag_parzysty))

ciag_nieparzysty=[3]
for i,x in enumerate(ciag_nieparzysty):
    if len(ramki) > len(ciag_nieparzysty):
        ciag_nieparzysty.insert(i+1,ciag_nieparzysty[i] + 4)