

# Ohjelman käynnistys
def start():
    print("Tervetuloa kalenteriin!\n")
    print("Lisää muistutus, muokkaa & poista muistutus tai tarkastele kalenteria")

import calendar
# Ellun tekele
# Tulostaa kuukausikalenterin ja merkitsee tapahtumapäivät tähdellä (*)
def tarkastelu(vuosi, kuukausi, tapahtumat):

    # Luodaan kalenteri, jossa viikko alkaa maanantaista
    kalenteri = calendar.TextCalendar(calendar.MONDAY)
    kuukauden_paivat = kalenteri.formatmonth(vuosi, kuukausi).split("\n")

    numerot = "1234567890"
    tulostettava = [] # Lista muokatuille riveille

    for rivi in kuukauden_paivat:
        uusi_rivi = "" # Muokattava rivi
        for sana in rivi.split(): # Käydään läpi rivin sanat
            if sana in numerot and int(sana) in tapahtumat: # Katsotaan onko päivälle tapahtuma
                uusi_rivi += f"{sana}*" # Lisätään tähti (*) tapahtumapäivään
            else:
                uusi_rivi += f"{sana}" # Lisätään normaalipäivä ilman tapahtumaa
        tulostettava.append(uusi_rivi.rstrip()) # Lisätään muokattu rivi listaan ilman ylimääräisiä välilyöntejä
   
    # Tulostetaan muokattu kuukausikalenteri
    print("\n".join(tulostettava))

    def main():

        if __name__ == "__main__":

            vuosi = input("Valitse vuosi: ")
            kuukausi = input("Valitse kuukausi: ")

            tarkastelu(vuosi, kuukausi, tapahtumat)
            
        main()