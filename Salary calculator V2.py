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


print("Most a műszak pótlékok megadása következik, általános szituációt feltételezünk szóval nappalos/délutános illetve éjjeles pótlékkal számolunk, amennyiben valamelyiket nem kapod, kérlek 0 értéket adj meg")

nappalos_potlek = int(input("Nappalos / délutános pótlék százaléka: "))
n_potlek_szazalekban = nappalos_potlek / 100
ejjeles_potlek = int(input("Éjjeles pótlék százaléka: "))
e_potlek_szazalekban = ejjeles_potlek / 100
nappalos_napok = int(input("Kérlek add meg mennyi nap dolgoztál nappal / délután: "))
ejjeles_napok = int(input("Kérlek add meg mennyi nap dolgoztál éjjel: "))



                                                            #pótlékok összege

n_potlek_1napra = napi_ber * n_potlek_szazalekban
e_potlek_1napra = napi_ber * e_potlek_szazalekban
n_ossz_potlek = n_potlek_1napra * nappalos_napok
e_ossz_potlek = e_potlek_1napra * ejjeles_napok
ossz_potlek = n_ossz_potlek + e_ossz_potlek
print("Nappalos pótlékod a hónapban: ")
print(int(round(n_ossz_potlek, 0)))
print("Éjjeles pótlékod a hónapban: ")
print(int(round(e_ossz_potlek, 0)))





                                                            #fizu pótlékkal

fizu_potlekkal = brutto_fizu + ossz_potlek
print("Így a fizetésed pótlékokkal: ")
print(int(round(fizu_potlekkal, 0)))

                                                            #juttatás

juttatas = str(input("Van bármi egyéb fizetés kiegészítő juttatás? (i / n): "))
juttatas_i = 'i'
juttatas_n = 'n'
if juttatas == juttatas_i:
    juttatas_osszeg = int(input("Juttatás összege: "))

else:
    juttatas_osszeg = 0


                                                          #túlórák




tulorak_megadasa = str(input("Volt-e túlórád a hónapban? (i / n): "))
t_i = 'i'
if tulorak_megadasa == t_i:
    tulora_napok = int(input("Add meg hány nap túlórád volt a hónapban: "))
    n_tulora = int(input("Ebből mennyi nap volt nappal / délután: "))
    e_tulora = int(input("És végül mennyi volt éjjel: "))
    tulora_potlek = napi_ber * 1
    n_tulora_potlek = n_tulora * n_potlek_1napra   # nappalos műszakpótlék még rámegy a túlórára
    e_tulora_potlek = e_tulora * e_potlek_1napra   # éjjeles műszakpótlék még rámegy a túlórára
    tulora_osszeg = ((napi_ber + tulora_potlek) * tulora_napok) + n_tulora_potlek + e_tulora_potlek
    print("Túlóráid összege: ")
    print(int(round(tulora_osszeg, 0)))





else:
    tulora_osszeg = 0



                                                            #mozgóbérrel, pótlékkal, túlórával bruttó

ossz_fizu = fizu_potlekkal + juttatas_osszeg + tulora_osszeg
levonasok = ossz_fizu * ado_alap_szazalekban
netto_ossz_fizu = ossz_fizu - levonasok



print('Bruttó össz fizetésed: ')
print(int(round(ossz_fizu, 0)))
print('Nettó össz fizetésed: ')
print(int(round(netto_ossz_fizu, 0)))






                                                            #újrainditó funkció

def restart():
    # bruttó fizu és adó
    brutto_fizu = float(input("Bruttó fizetés: "))
    ado_alap = float(input("Adózási százalék az országban: "))
    ado_alap_szazalekban = ado_alap / 100
    fizu_ado = brutto_fizu * (ado_alap / 100)

    # nettó fizetés

    netto_fizu = brutto_fizu - fizu_ado
    print("Fizetés nettója pótlék, minden nélkül: ")
    print(int(netto_fizu))

    # napi bér

    dolgozott_napok = int(input("Ledolgozott napok száma 1 hónapban: "))
    napi_ber = brutto_fizu / dolgozott_napok
    print("Napi béred: ")
    print(int(napi_ber))

    # műszakpótlék

    print(
        "Most a műszak pótlékok megadása következik, általános szituációt feltételezünk szóval nappalos/délutános illetve éjjeles pótlékkal számolunk, amennyiben valamelyiket nem kapod, kérlek 0 értéket adj meg")

    nappalos_potlek = int(input("Nappalos / délutános pótlék százaléka: "))
    n_potlek_szazalekban = nappalos_potlek / 100
    ejjeles_potlek = int(input("Éjjeles pótlék százaléka: "))
    e_potlek_szazalekban = ejjeles_potlek / 100
    nappalos_napok = int(input("Kérlek add meg mennyi nap dolgoztál nappal / délután: "))
    ejjeles_napok = int(input("Kérlek add meg mennyi nap dolgoztál éjjel: "))

    # pótlékok összege

    n_potlek_1napra = napi_ber * n_potlek_szazalekban
    e_potlek_1napra = napi_ber * e_potlek_szazalekban
    n_ossz_potlek = n_potlek_1napra * nappalos_napok
    e_ossz_potlek = e_potlek_1napra * ejjeles_napok
    ossz_potlek = n_ossz_potlek + e_ossz_potlek
    print("Nappalos pótlékod a hónapban: ")
    print(int(round(n_ossz_potlek, 0)))
    print("Éjjeles pótlékod a hónapban: ")
    print(int(round(e_ossz_potlek, 0)))

    # fizu pótlékkal

    fizu_potlekkal = brutto_fizu + ossz_potlek
    print("Így a fizetésed pótlékokkal: ")
    print(int(round(fizu_potlekkal, 0)))

    # juttatás

    juttatas = str(input("Van bármi egyéb fizetés kiegészítő juttatás? (i / n): "))
    juttatas_i = 'i'
    juttatas_n = 'n'
    if juttatas == juttatas_i:
        juttatas_osszeg = int(input("Juttatás összege: "))

    else:
        juttatas_osszeg = 0

        # túlórák

    tulorak_megadasa = str(input("Volt-e túlórád a hónapban? (i / n): "))
    t_i = 'i'
    if tulorak_megadasa == t_i:
        tulora_napok = int(input("Add meg hány nap túlórád volt a hónapban: "))
        n_tulora = int(input("Ebből mennyi nap volt nappal / délután: "))
        e_tulora = int(input("És végül mennyi volt éjjel: "))
        tulora_potlek = napi_ber * 1
        n_tulora_potlek = n_tulora * n_potlek_1napra  # nappalos műszakpótlék még rámegy a túlórára
        e_tulora_potlek = e_tulora * e_potlek_1napra  # éjjeles műszakpótlék még rámegy a túlórára
        tulora_osszeg = ((napi_ber + tulora_potlek) * tulora_napok) + n_tulora_potlek + e_tulora_potlek
        print("Túlóráid összege: ")
        print(int(round(tulora_osszeg, 0)))





    else:
        tulora_osszeg = 0

        # mozgóbérrel, pótlékkal, túlórával bruttó

    ossz_fizu = fizu_potlekkal + juttatas_osszeg + tulora_osszeg
    levonasok = ossz_fizu * ado_alap_szazalekban
    netto_ossz_fizu = ossz_fizu - levonasok

    print('Bruttó össz fizetésed: ')
    print(int(round(ossz_fizu, 0)))
    print('Nettó össz fizetésed: ')
    print(int(round(netto_ossz_fizu, 0)))

        #bezárás

    # kilépés / újrainditás

    exit = 'x'
    program_end = str(input("Amennyiben beszeretnéd zárni a programot, nyomj 'x'-et, ellenben a program újraindul: "))
    import time
    import sys
    while program_end == 'x':
        if program_end == exit:
            print("Ne köszönd, hogy használhattad, fizesd ki!")
            counter_1 = 3
            while counter_1 > 0:
                time.sleep(1)
                if counter_1 == 0:
                    break
                counter_1 -= 1
            sys.exit()
        else:
            pass

    counter = 5
    while counter > 0:
        print(counter)
        time.sleep(1)
        if counter == 0:
            break
        counter -= 1

    restart()







                                                            #kilépés / újrainditás


exit = 'x'
program_end = str(input("Amennyiben beszeretnéd zárni a programot, nyomj 'x'-et, ellenben a program újraindul: "))
import time
import sys
while program_end == 'x':
    if program_end == exit:
        print("Ne köszönd, hogy használhattad, fizesd ki!")
        counter_1 = 3
        while counter_1 > 0:
            time.sleep(1)
            if counter_1 == 0:
                break
            counter_1 -= 1
        sys.exit('Úgy néz ki ez működik')
    else:
        pass

counter = 5
while counter > 0:
    print(counter)
    time.sleep(1)
    if counter == 0:
        break
    counter -= 1

restart()







