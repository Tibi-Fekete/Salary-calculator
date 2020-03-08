                                                            #bruttó fizu és adó
brutto_fizu = float(input("Bruttó fizetés: "))
ado_alap = float(input("Adózási százalék az országban: "))
ado_alap_szazalekban = ado_alap / 100
fizu_ado = brutto_fizu * (ado_alap / 100)



                                                            #nettó fizetés

netto_fizu = brutto_fizu - fizu_ado
print("Fizetés nettója pótlék, minden nélkül: ")
print(int(netto_fizu))


                                                            #napi bér

dolgozott_napok = int(input("Ledolgozott napok száma 1 hónapban: "))
napi_ber = brutto_fizu / dolgozott_napok
print("Napi béred: ")
print(int(napi_ber))


                                                            #műszakpótlék

potlek = int(input("Pótlék százaléka: "))
potlek_szazalekban = potlek / 100
napi_potlek = napi_ber * potlek_szazalekban
print("1 napra jutó pótlékod: ")
print(int(round(napi_potlek, 0)))


                                                            #össz pótlék

ossz_potlek = dolgozott_napok * napi_potlek
print("Pótlék 1 hónapban: ")
print(int(ossz_potlek))


                                                            #fizu pótlékkal

fizu_potlekkal = brutto_fizu + ossz_potlek
print("Így a fizetés pótlékkal: ")
print(int(fizu_potlekkal))

                                                            #juttatás

juttatas = str(input("Van bármi egyéb fizetés kiegészítő juttatás? (i / n): "))
juttatas_i = 'i'
juttatas_n = 'n'
if juttatas == juttatas_i:
    juttatas_osszeg = int(input("Juttatás összege: "))

else:
    juttatas_osszeg = 0

                                                            #mozgóbérrel bruttó

ossz_fizu = fizu_potlekkal + juttatas_osszeg
levonasok = ossz_fizu * ado_alap_szazalekban
netto_ossz_fizu = ossz_fizu - levonasok



print('Bruttó össz fizetésed: ')
print(int(round(ossz_fizu, 0)))
print('Nettó össz fizetésed: ')
print(int(round(netto_ossz_fizu, 0)))


