# Olet aloittanut osakesijoittamisen ja haluat arvioida sijoituksesi arvoa. Ohjelmalla (pääohjelmassa) on lista, 
# johon käyttäjä voi lisätä Osake-olioita. Ohjelma kysyy käyttäjältä ”Lisätäänkö uusi osake (k/e)”.
# Kun osakkeet on lisätty listaan, kysyy ohjelma käyttäjältä kuvitteellisen kasvuprosentin sekä ajanjakson vuosina.

# Tee luokka Osake, jolla on jäsenmuuttujat:
# - Nimi
# - Ostohinta/osake (>0)
# - Osakemäärä (> 0)

# Osakkeella on metodit:

# - TulostaArvo, joka ottaa vastaan  oletetun kasvuprosentin ja ajanjakson vuosina.

# TulostaArvo-metodi kutsuu toista Osake-luokan metodia LaskeTuottoYhdelleVuodelle, joka laskee vuosikohtaisen tuoton. 
# Tuottoa tuotolle ei tarvitse huomioida eli tilannetta, jossa vuosituoton laskenta perustuu aina 
# edellisenä vuonna kasvaneeseen pääomaan. 
# 
# - LaskeTuottoYhdelleVuodelle -metodi palauttaa osakepotin tuoton yhdelle vuodelle. 
# 
# Vuosikohtaiset tuotot lasketaan yhteen ajanjakson aikana, lisätään potin arvoon ja 
# tulostetaan TulostaArvo-metodin lopussa.

# Laske pääohjelmassa  myös koko osakepotin arvo(sama % ja samat vuodet) käymällä lista läpi eli 
# joudut miettimään sitä, miten pääohjelmaan palautetaan tieto yhden osakkeen potin arvo vuosien jälkeen.
# Tulostus voisi näyttää vaikkapa tältä:

# Lisää osakkeita (k/e): k
# Anna osakkeen nimi: Nokia
# Anna osakkeen ostohinta/kpl: 3.44
# Anna osakemäärä: 3400
# Lisää osakkeita (k/e): k
# Anna osakkeen nimi: Neste
# Anna osakkeen ostohinta/kpl: 5.66
# Anna osakemäärä: 1200
# Lisää osakkeita (k/e): e
# Anna kasvuprosentti: 3
# Anna vuodet: 4
# Nokia 3400 3.44
# Osakkeen potin arvo on  13099.52 ja tuotto on 1403.52
# Neste 1200 5.66
# Osakkeen potin arvo on  7607.04 ja tuotto on 815.04
# Koko portin arvo on nyt 20706.56

###

class Osake:
    def __init__(self, nimi, ostohinta, osakemaara):
        self.nimi = nimi
        self.ostohinta = ostohinta
        self.osakemaara = osakemaara
        
    @property
    def nimi(self):  # palauttaa _nimi-muuttujan arvon
        return self._nimi

    @nimi.setter   # syöttää arvon ostohinta-muuttujaan
    def nimi(self, value):
        self._nimi = value
    
    @property
    def ostohinta(self):  # palauttaa _ostohinta-muuttujan arvon
        return self._ostohinta

    @ostohinta.setter   # syöttää arvon ostohinta-muuttujaan
    def ostohinta(self, value):  
        if value <= 0:   # jos syötetty lukumäärä pienempi on kuin nolla, syötetään lukumääräksi 1
            value = 1
        self._ostohinta = value
        
    @property
    def osakemaara(self):  # palauttaa _ostohinta-muuttujan arvon
        return self._osakemaara

    @osakemaara.setter   # syöttää arvon ostohinta-muuttujaan
    def osakemaara(self, value):  
        if value <= 0:   # jos syötetty lukumäärä pienempi on kuin nolla, syötetään lukumääräksi 1
            value = 1
        self._osakemaara = value
    
    def LaskeVuosituotto(self, tuottoprosentti):    # palauttaa osakkeen tuoton yhdelle vuodelle
        return tuottoprosentti * self.ostohinta * self.osakemaara

    def TulostaArvo(self, tuottoprosentti, aika):   # laskee osakeolion vuosikohtaiset tuotot yhteen ajanjaksolta, laskee kokonaispotin arvon ja tulostaa tiedot
        print(self.nimi, self.osakemaara, self.ostohinta)
        print("Osakkeen potin arvo on", 
            round((self.ostohinta * self.osakemaara + self.LaskeVuosituotto(tuottoprosentti) * aika), 2), 
            "ja tuotto on", round((self.LaskeVuosituotto(tuottoprosentti) * aika), 2))

if __name__ == '__main__':
    osakkeet = []
    vastaus = input("Lisää osakkeita (k/e): ")   # ohjelma alkaa kysymyksellä haluaako käyttäjä lisätä osakkeita
    while vastaus == "k":  #jos vastaus kyllä, aletaan kysyä tietoja ja kysytään kunnes käyttäjä haluaa jatkaa
        nimi = input("Anna osakkeen nimi: ")
        ostohinta = float(input("Anna ostohinta/osake: "))
        osakemaara = int(input("Anna osakemäärä: "))
        osakkeet.append(Osake(nimi, ostohinta, osakemaara))  # osaketta koskevat tiedot talletetaan olioon 'Osake' ja olio lisätään listaan 'osakkeet'
        vastaus = input("Lisää osakkeita (k/e): ")  # kysytään käyttäjältä haluaako hän jatkaa osakkeiden syöttöä. syöttöluuppi pyörii kunnes ei halua.
    tuottoprosentti = float(input("Anna tuottoprosentti: ")) / 100  # kysytään tuottoprosentti (sama kaikille osakkeille)
    aika = int(input("Anna vuosien lukumäärä: "))  # kysytään vuosien lkm
    kokonaispotti = 0  #luodaan muuttuja kokonaispotin laskemista varten
    for x in osakkeet:  # luupataan osakelista läpi ja lisätään arvo
        x.TulostaArvo(tuottoprosentti, aika)  # haetaan olion metodin avulla kunkin osakkeen potti ja tuotto ja tulostetaan ne
        kokonaispotti = kokonaispotti + (x.ostohinta * x.osakemaara + x.LaskeVuosituotto(tuottoprosentti) * aika)  # lasketaan salkun kokonaisarvo
    print("Koko potin arvo on nyt", round(kokonaispotti, 2))  # tulostetaan salkun kokonaisarvo
    
