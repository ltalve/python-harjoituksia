# Ota käyttöön muuttuja, johon voit tallentaa maanantain ja perjantain välisenä 
# aikana neljä mittaustulosta jokaiselta päivältä (mittaustulos on sademäärä 
# milleinä). Lue käyttäjältä nämä mittaustulokset ja tulosta lopuksi jokaisen 
# päivän mittaustulosten keskiarvo seuraavan esimerkin mukaisesti :

# Maanantai   : 12.0 mm
# Tiistai     : 0.0 mm
# Keskiviikko : 1.9 mm
# Torstai     : 22.8 mm
# Perjantai   : 0.9 mm


# Dictionary, jossa avain on päivä ja arvo on neljän mittaustuloksen lista:

paivanTarkistus = ("Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai")

mittaustulokset = {}
while True:
    paiva = (input("Anna viikonpäivä (aloita isolla alkukirjaimella): "))
    if paiva not in paivanTarkistus:  #Päivän pitää olla joku sallituista 
        print("Tarkista päivä. Syötä viikonpäivän nimi isolla alkukirjaimella. Sallitut päivät ma-pe.")
        continue
    if paiva in mittaustulokset:  #Jos ko. päivän tulokset on jo syötetty, ei voi syöttää uudestaan.
        print("Päivän havainnot on jo syötetty.")
        continue
    sademaara1 = int(input("Anna sademaara 1: "))
    sademaara2 = int(input("Anna sademaara 2: "))
    sademaara3 = int(input("Anna sademaara 3: "))
    sademaara4 = int(input("Anna sademaara 4: "))
    paivanSademaarat = [sademaara1, sademaara2, sademaara3, sademaara4]
    mittaustulokset[paiva] = paivanSademaarat

    #Kun kaikki päivät on syötetty, eli dictionaryn pituus on viisi, lasketaan keskiarvot
    if (len(mittaustulokset) == 5):
        ka_ma = sum(mittaustulokset["Maanantai"]) / len(paivanSademaarat)
        ka_ti = sum(mittaustulokset["Tiistai"]) / len(paivanSademaarat)
        ka_ke = sum(mittaustulokset["Keskiviikko"]) / len(paivanSademaarat)
        ka_to = sum(mittaustulokset["Torstai"]) / len(paivanSademaarat)
        ka_pe = sum(mittaustulokset["Perjantai"]) / len(paivanSademaarat)
        
        # Lopuksi tulostetaan keskiarvot
        print(" Maanantai:\t", ka_ma, " mm\n","Tiistai:\t", 
        ka_ti, " mm\n","Keskiviikko:\t", ka_ke, " mm\n","Torstai:\t", ka_to, " mm\n",
        "Perjantai:\t", ka_pe, " mm\n") 

        break
