import calendar
from tabulate import tabulate


# Tulostaa kuukausikalenterin ja merkitsee tapahtumapäivät tähdellä (*)
def tarkastelu(vuosi, kuukausi, tapahtumat):

    # Luodaan kalenteri, jossa viikko alkaa maanantaista
    kalenteri = calendar.TextCalendar(firstweekday=calendar.MONDAY)
    kuukauden_paivat = kalenteri.monthdayscalendar(vuosi, kuukausi)

    # Muokataan kalenterin päivät ja lisätään tähdet tapahtumapäiville
    muokattu_kuukausi = []
    for viikko in kuukauden_paivat:
        muokattu_viikko = []
        for paiva in viikko:
            if paiva == 0:  # Tyhjät päivät
                muokattu_viikko.append("")
            elif paiva in tapahtumat:  # Tapahtumapäivät
                muokattu_viikko.append(f"{paiva}*")
            else:  # Tavalliset päivät
                muokattu_viikko.append(str(paiva))
        muokattu_kuukausi.append(muokattu_viikko)
    
    # Tulostetaan kalenteri taulukkomuodossa
    otsikot = ["Ma", "Ti", "Ke", "To", "Pe", "La", "Su"]
    print(f"\n{calendar.month_name[kuukausi]} {vuosi}".center(30))
    print(tabulate(muokattu_kuukausi, headers=otsikot, tablefmt="grid"))

def main():
    
    vuosi = int(input("Valitse vuosi: "))
    kuukausi = int(input("Valitse kuukausi: "))
    tapahtumat = [5, 10, 17]

    tarkastelu(vuosi, kuukausi, tapahtumat)

if __name__ == "__main__":  
    main()