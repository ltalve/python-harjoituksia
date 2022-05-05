# Tee ohjelma, joka laskee mäkihyppääjän yhden kierroksen 
# suorituspisteet. Ohjelma kysyy hypyn pituuden 
# (liukuluku 0.5 metrin välein) sekä viiden 
# arvostelutuomarin tyylipisteet 
# (0-20 välillä 0.5 välein eli esim. 
# 16.5 tai 17.0 tai 18.5). 
# Hyppääjän pisteet muodostuvat kaavasta.

# pisteet = (hypyn pituus - kriittinen piste) * 1.8 + 
# kolmen keskimmäisen tuomarin tyylipisteet + 60. 

# Tyylipisteissä siis parhain ja huonoin pistemäärä tipahtaa pois.

# Ohjelman hyppyrimäen kriittinen piste on 90 metrin kohdalla. Laita kriittinen piste vakioon 
# KR_PISTE. Tulosta lopuksi hypyn pituus ja hypyn pisteet. Käytä ohjelmassa funktioita:

# KysyHypynPituus
# KysyTuomareidenPisteet
# LaskeHypynPisteet
# Tulosta

###

# Luodaan vakio mäen kriittiselle pisteelle
KR_PISTE = 90

# Funktio, joka kutsuu apufunktioita ja kerää niistä tiedot hypyn pituudesta ja tuomariarvosanoista,
# laskee hypyn pisteet kaavan mukaisesti ja tulostaa lopuksi apufunktiolla pituuden ja pisteet.
def LaskeHypynPisteet():
    hypynPituus = KysyHypynPituus()
    tuomareidenPisteet = KysyTuomareidenPisteet()
    hypynPisteet = round(((hypynPituus - KR_PISTE) * 1.8 + sum(tuomareidenPisteet) + 60),2)
    Tulosta(hypynPituus, hypynPisteet)

# Funktio kysyy hypyn pituuden ja palauttaa sen.
def KysyHypynPituus():
    try:
        while True:
            hypynPituus = input("Syötä hypyn pituus puolen metrin tarkkuudella: ")
            hypynPituus = float(hypynPituus)
            return hypynPituus
    except:     # Virhetilanteessa palataan alkuun.
        print("Jokin meni vikaan hypyn pituuden syötössä. Yritä uudestaan.")
        LaskeHypynPisteet() 

# Funktio kerää tuomareiden pisteet listamuuttujaan, josta on poistettu suurin ja pienin tuomariarvosana, ja palauttaa tämän listan.
def KysyTuomareidenPisteet():
    try:
        tuomareidenPisteet = []  #tuomaripisteet kerätään listamuuttujaan
        tuomarinumero = 1
        while tuomarinumero <= 5:  #luupataan 5 apufunktiossa kerättyä ja tarkastettua tuomariarvosanaa ja lisätään ne listaan
            pisteet = None
            while pisteet == None:
                pisteet = KysyJaTarkistaYhdenTuomarinPisteet(tuomarinumero)
            tuomareidenPisteet.append(pisteet)
            print(tuomareidenPisteet)
            tuomarinumero = tuomarinumero + 1

        tuomareidenPisteet.sort()  #järjestetään tuomaripisteet listassa suuruusjärjestykseen
        tuomareidenPisteet.pop()   #poistetaan pienin pisteluku
        tuomareidenPisteet.pop(0)  #poistetaan suurin pisteluku
        return tuomareidenPisteet  
    except:   #Virhetilanteessa palataan alkuun
        print("Jokin meni vikaan tuomaripisteiden syötössä. Aloita alusta.")
        LaskeHypynPisteet()

# Funktio kysyy yhden tuomarin pisteet ja tarkastaa että se on syötetty oikeassa muodossa 
def KysyJaTarkistaYhdenTuomarinPisteet(x):
    try:
        while True:
            pisteet = input("Anna tuomarin pisteet puolen pisteen tarkkuudella väliltä 0-20: ")
            pisteet = float(pisteet)  #muutetaan float-muotoon laskujen onnistumiseksi
            if pisteet > 20 or pisteet < 0:   #tarkastetaan, että pisteet sallitulla välillä ja pyydetään korjaamaan jos tarvetta
                print("Luku liian suuri tai pieni. Syötä pisteet väliltä 0-20.")
                continue
            else:   #jos kaikki ok, palautetaan tuomarin pisteet.
                return pisteet
    except:
        print("Tuomaripisteen syötössä tapahtui virhe. Pisteet syötettiin väärässä muodossa.")


# Funktio, joka tulostaa lopuksi tarvitut tiedot saamillaan parametrin arvoilla.
def Tulosta(hpituus, hpisteet):
    print("Hypyn pituus:", hpituus)
    print("Hypyn kokonaispisteet:", hpisteet)

# Funktion kutsu
LaskeHypynPisteet()