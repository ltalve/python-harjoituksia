# Lue käyttäjältä auton rekisterinumero/rekisteröintipäivä 
# -tietoja. Talleta Dictionaryyn. Rekisteröintipäivä 
# syötetään merkkijonona ja muutetaan datetime-tyyppiseksi 
# muuttujaksi käyttäen datetime.strptime() -funktiota. 
# Toteuta ratkaisu niin, että pelkkä päiväys riittää. 
# Tutustu funktioon omatoimisesti. Vasta pvm-muunnon 
# jälkeen arvo viedään dictionaryyn. LOPPU 
# rekisterinumeroksi  lopettaa tietojen syötön.

# Ohjelma ei saa kaatua, jos rekisteröintipäivä syötetään 
# väärässä formaatissa

# Talleta syötetyt tiedot tiedostoon autot.txt allekkain. 
# Rekisteröintipäivästä tulostuu tiedostoon van päiväys, ei kloaika

# Ja lopuksi tulosta autot näytölle siten, että luet ne 
# tiedostosta ennen sitä.

# Ohjelma ei saa kaatua, jos tiedostoa ei voida lukea tai 
# sinne ei voida kirjoittaa

# Käytä funktioita:
# LueAutot
# TalletaTiedostoon
# LueTiedostosta
# TulostaTiedot

# Alla ote esimerkkiajosta:
# Anna rekkari: abc-123
# rekisteröintipäivä: 1.23.1990
# Rekisteröintipäivä ei kelpaa! Syötä tiedot uudelleen
# Anna rekkari: abc-123
# rekisteröintipäivä: 1.2.1990
# Anna rekkari: cba-321
# rekisteröintipäivä: 3.3.2000
# Anna rekkari: LOPPU
# abc-123 01.02.1990
# cba-321 03.03.2000

###

from datetime import datetime
import os

rekisteroinnit = {}    #luodaan tyhjä dictionary

def RekisterointiJarjestelma():
    LueAutot()
    TulostaTiedot(LueTiedostosta())
    
def LueAutot():
    while True:
        rekisterinumero = (input("Anna rekisterinumero: "))   #kysytään rekisterinumero ja talletetaan muuttujaan
        if rekisterinumero in rekisteroinnit:
            print("Rekisterinumero on jo syötetty.")    #samaa rekkaria ei voi syöttää monta kertaa
            continue
        elif rekisterinumero == "LOPPU":
            break
        try:
            syotettyPvm = (input("Anna rekisteröintipäivämäärä muodossa pp.kk.vvvv: "))    #kysytään rekisteröintipäivämäärä ja talletetaan muuttujaan
            pvmDate = datetime.strptime(syotettyPvm, "%d.%m.%Y").date()  #muutetaan syötetty pvm datetime-muotoon ilman kellonaikaa
            pvm = pvmDate.strftime("%d.%m.%Y")
            rekisteroinnit.update({rekisterinumero: pvm})    #syötetään annettu rekkari ja pvm dictionaryyn
            TalletaTiedostoon(rekisterinumero, pvm)  #lisätään tiedot tiedostoon apufunktiossa
        except:      #jos päivämäärässä häikkää, palataan syötön alkuun
            print("Rekisteröintipäivä ei kelpaa! Syötä tiedot uudelleen")
            LueAutot()

def TalletaTiedostoon(x,y):
    try:
        tieto1 = x  #otetaan funkitolle annetut arvot talteen kirjoittamista varten
        tieto2 = y
        tiedosto = open("autot.txt", "a+") #luodaan tai avataan tiedosto ja lisätään sisältöä mahdollisen vanhan perään
        tiedosto.write(tieto1 + " " + tieto2 + "\n")  
        tiedosto.close()  #suljetaan tiedosto
    except:
        print("Virhe tiedostoon kirjoittamisessa.")

def LueTiedostosta():
    try:
        tiedosto = open("autot.txt", "r+") #avataan tiedosto lukumuodossa 
        tulostettavatTiedot = tiedosto.read()  #luetaan tiedoston sisältö
        return tulostettavatTiedot
    except:
        print("Virhe tiedostosta lukemisessa.")

def TulostaTiedot(tiedot):
    print(tiedot)

RekisterointiJarjestelma()