######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Opiskelijanumero: 000524560
# Päivämäärä: 16.11.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä Harjoitustyö perustaso
# eof
import HTPerusKirjasto as kirjasto
#Tässä on oltava ohjelman pääohjelma ja Valikko-aliohjelma

#valikko-aliohjelma
def valikko():
    print('Valitse haluamasi toiminto:\n1) Lue tiedosto\n2) Analysoi\n3) Kirjoita tiedosto\n4) Analysoi viikonpäivittäiset sademäärät\n0) Lopeta')
    valinta = int(input('Anna valintasi: '))
    return valinta

def paaohjelma():
    viikon_paivat_lista = []
    olio = ''
    dictionary_data = {}
    #Index 0 = luettavan tiedoston nimi, Index 1 = kirjoitettavan tiedoston nimi
    while True:
        valinta = valikko()

        if valinta == 1:
            olio, dictionary_data = kirjasto.valinta_yksi_lue_tiedosto()
            
            continue
        elif valinta == 2:
            try:
                olio, viikon_paivat_lista = kirjasto.valinta_kaksi_analyysi(olio,dictionary_data)
                continue
            except AttributeError:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.\n")
                continue
        elif valinta == 3:
            if olio == '':
                print('Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.\n')
                continue
            else:
                try:   
                    kirjasto.valinta_kolme_kirjoita_tiedosto(olio)
                    continue
                except OSError:
                    print('Test#1')
        elif valinta == 4:
            try:
                kirjasto.valinta_nelja_kirjoita_tiedost(olio, viikon_paivat_lista)
                continue
            except AttributeError:
                print('Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.\n')
        elif valinta == 0:
            print('Lopetetaan.\n')
            break
        else:
            print('Tuntematon valinta, yritä uudestaan.\n')
            continue
         
    viikon_paivat_lista.clear()
    return None 

paaohjelma()

print('Kiitos ohjelman käytöstä.')