import time
import sys 
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

#Ohjeet:
#Tässä on oltava kaikki valintarakenteesta kutsuttavat aliohjelmat.
#Käytä luettavan ja kirjoitettavien tiedostojen nimien kysymiseen samaa aliohjelmaa
#Sademäärää käsitellään desimaalilukuna ja aikaleimaa time-kirjaston avulla. Aikaleima tallennetaan olion jäsenmuuttujaksi
#Pyöristysongelmien välttämiseksi kaikki laskenta tulee tehdä alkuperäisissä yksiköissä ja tulosten muotoilun yhteydessä keskiarvot pyöristetään yhden desimaalin tarkkuuteen
class DATA:
    def __init__(self):
        #Dict jäsenmuuttujaksi
        self.TimeStampDict = {}
        self.CategoryDict = {1:0, 2:0, 3:0, 4:0}
        return None
    
    #Funktiot, jokta mahdollistavat dictien käyttö
    def get_TimeStampDict(self):
        #Tämä funktio mahdollistaa kirjaston käyttöä myöhemmin.
        return self.TimeStampDict
    def get_CategoryDict(self):
        return self.CategoryDict

#Aliohjelma, joka kysyy käyttäjätlä kirjoitettava tai luettavan tiedoston nimi ja palauttaa kyseisen nimen kutsuvaan ohjelmaan
def kysy_tiedoston_nimi(luettava = False, kirjoitettava = False):
    tiedoston_nimi = ''
    if luettava == True:
        try:
            tiedoston_nimi = input('Anna luettavan tiedoston nimi: ')
        except FileNotFoundError:
            print('Tiedoston \'{}\' käsittelyssä virhe, lopetetaan.'.format(tiedoston_nimi))
            sys.exit(0)
        
             

    if kirjoitettava == True:
       try:
        tiedoston_nimi = input('Anna kirjoitettavan tiedoston nimi: ')
       except OSError or PermissionError:
            print('Tiedoston \'{}\' käsittelyssä virhe, lopetetaan.'.format(tiedoston_nimi))
            sys.exit(0)
         
    return tiedoston_nimi
 

#############################################################
#Luettava tiedosto näyttää tältä                            #
# Aikaleima (YYYY.mm.dd HH:MM);Aikavyöhyke;Sademäärä (mm)   #
# 2016.01.01 02:00;UTC+2;0                                  #
# 2016.01.04 00:00;UTC+2;0.1                                #
# 2016.01.04 01:00;UTC+2;0.5                                #
# 2016.01.18 05:00;UTC+2;0.1                                #
# 2016.01.18 06:00;UTC+2;0.5                                #
#############################################################

def valinta_yksi_lue_tiedosto():
    
    tiedoston_nimi = kysy_tiedoston_nimi(luettava=True)
    data_olio = DATA()

    dict= lue_tiedosto(tiedoston_nimi)
    
    return data_olio, dict

def lue_tiedosto(tiedoston_nimi):
    puhdistettu_lista = []
    index_of_temp_lst = 0   
    try:
        tiedosto_avattu = open(tiedoston_nimi, 'r', encoding='UTF-8')
    except FileNotFoundError:
        print('Tiedoston \'{}\' käsittelyssä virhe, lopetetaan.'.format(tiedoston_nimi))
        sys.exit(0)
    for line in tiedosto_avattu.readlines():
        #lisätään tyhjä lista palautettavaan listaan
        puhdistettu_lista.append([])
        
        #Tämä muodostaa uuden listan 
        line_split = line.split(';')

        for item in line_split:
            #Puhdistetaan ylimääräiset merkkit pois!
            puhdistettu_lista[index_of_temp_lst].append(item.strip())
        #Siirrytään seuraavaan slottiin listassa.
        index_of_temp_lst+=1
    tiedosto_avattu.close()
    print('Tiedosto \'{}\' luettu.'.format(tiedoston_nimi))
    print('Tiedostosta lisättiin {} datariviä listaan.\n'.format(len(puhdistettu_lista)-1))
    #Voisi yhdistää myöhemmin yhdeksi riviksi!
    dict_palautettavaksi_kutsuvalle_ohjelmalle = aikaleimat_dict_lista(puhdistettu_lista)
    return dict_palautettavaksi_kutsuvalle_ohjelmalle

def aikaleimat_dict_lista(lista_puhdistettuna):
    aikaleima_dict = {}
    data_without_header = lista_puhdistettuna[1:]
    
    #käydään tässä läpi jokaista listaa ja otetaan sieltä avain-ja-arvo-yhdistelmä, joilla päivitettään tuo alussa tekemämme listaa 
    #Pästään tällä eroon ensimmäisestä rivistä, joka sisältää tarpeetonta dataa

    for data in data_without_header: 
        key = data[0]
        key_value = time.strptime(key.split(' ')[0], "%Y.%m.%d")
        if key_value not in aikaleima_dict:
            aikaleima_dict.update({key_value: 0})
    
    for data in data_without_header: 
        
        value = data[-1]
        
        key = data[0]
        key_value = time.strptime(key.split(' ')[0], "%Y.%m.%d")
        aikaleima_dict[key_value] +=  float(value)
       
     
    return aikaleima_dict



def valinta_kaksi_analyysi(obj, dict):
    viikko_lst = ['Maanantai', 'Tiistai', 'Keskiviikko' , 'Torstai' , 'Perjantai' , 'Lauantai' , 'Sunnuntai' ]
    paivien_luku_maara = 0
    obj.TimeStampDict.update(dict)
    for value in obj.get_TimeStampDict().values():
        
        value = float(value)
        if value >= 4.5:
            obj.CategoryDict[1] += 1
            paivien_luku_maara +=1
        elif 1.0 <= value < 4.5:
            obj.CategoryDict[2] += 1
            paivien_luku_maara +=1
        elif 0.3 <= value < 1.0:
            obj.CategoryDict[3] += 1
            paivien_luku_maara +=1
        else:
            obj.CategoryDict[4] += 1
            paivien_luku_maara +=1
    
    print('Päivittäiset summat laskettu {} päivälle.'.format(paivien_luku_maara))
    print('Päivät kategorisoitu 4 kategoriaan.\n')
    return  obj, viikko_lst

       



def valinta_kolme_kirjoita_tiedosto(obj):
    tiedoston_nimi = kysy_tiedoston_nimi(kirjoitettava=True)
    try:
        uusi_tiedosto = open(tiedoston_nimi, 'w', encoding='UTF-8')

        #Kirjataan ensimmäinen rivi
        uusi_tiedosto.write('Kategoria;Päivien lukumäärä:\n')
        for key, value in obj.get_CategoryDict().items():
            uusi_tiedosto.write('Kategoria {};{}\n'.format(key, round(value,1)))


        uusi_tiedosto.write('\n')

        #Kirjataan ensimmäiset kaksia riviä 
        uusi_tiedosto.write('Kaikki päivittäiset sademäärät:\n')
        uusi_tiedosto.write('Pvm;mm\n')
        for key, value in obj.get_TimeStampDict().items():
            uusi_tiedosto.write('{};{}\n'.format(time.strftime('%d.%m.%Y', key), round(value,1)))
        uusi_tiedosto.close()
        print('Tiedosto \'{}\' kirjoitettu.\n'.format(tiedoston_nimi))
        
    
    except OSError:
        print('Tiedoston \'{}\' käsittelyssä virhe, lopetetaan.'.format(tiedoston_nimi))
        sys.exit(0)

    return None



def valinta_nelja_kirjoita_tiedost(obj, lst):
  
        viikon_paivat = {}
        for item in lst:
            viikon_paivat[item] = 0.0

        for key, value in obj.get_TimeStampDict().items():
            weekday = key.tm_wday
            if weekday == 0:
                viikon_paivat['Maanantai'] += value
            elif weekday == 1:
                viikon_paivat['Tiistai'] += value
            elif weekday == 2:
                viikon_paivat['Keskiviikko'] += value
            elif weekday == 3:
                viikon_paivat['Torstai'] += value
            elif weekday == 4:
                viikon_paivat['Perjantai'] += value
            elif weekday == 5:
                viikon_paivat['Lauantai'] += value
            elif weekday == 6:
                viikon_paivat['Sunnuntai'] += value

        tiedoston_nimi = kysy_tiedoston_nimi(kirjoitettava=True)

        try:
            uusi_tiedosto = open(tiedoston_nimi, 'w', encoding='UTF-8')
            uusi_tiedosto.write('Viikonpäivä;Sadekertymä\n')
            for key, value in viikon_paivat.items():
                uusi_tiedosto.write('{};{}\n'.format(key, round(value,1)))
            uusi_tiedosto.close()
            print('Tiedosto \'{}\' kirjoitettu.\n'.format(tiedoston_nimi))
        except OSError:
            print('Tiedoston \'{}\' käsittelyssä virhe, lopetetaan.'.format(tiedoston_nimi))
            sys.exit(0)  

        return None 
    