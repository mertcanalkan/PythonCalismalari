def not_hesapla(satir):

    #Dosya sonundaki /n kaldırılır !
    satir = satir[:-1]
    #stringleri virgüllere göre ayıracağız !
    liste = satir.split(",")
    #stringi virgüllere göre ayırdı, her birini listeledi
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    ortalama = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (ortalama >= 90):

        harf_notu = "AA"

    elif (ortalama >= 85):
        harf_notu = "BA"

    elif (ortalama >= 80):
        harf_notu = "BB"

    elif (ortalama >= 75):
        harf_notu = "CB"

    elif (ortalama >= 70):
        harf_notu = "CC"

    elif (ortalama >= 65):
        harf_notu = "DC"

    elif (ortalama >= 60):
        harf_notu = "DD"

    elif (ortalama >= 55):
        harf_notu = "FD"

    else:
        harf_notu = "FF"

    return isim + "=" + harf_notu + "\n"

with open("dosya.txt" , "r", encoding="utf-8") as file:

    eklenecekler_listesi = []

    for i in file:

        eklenecekler_listesi.append(not_hesapla(i))

    with open("notlar.txt", "w", encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)