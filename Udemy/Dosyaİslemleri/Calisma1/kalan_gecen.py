def kalan_gecen(satir):

    satir = satir[:-1]
    liste = satir.split("=")
    harf_notu = liste[1]
    isim = liste[0]

    if (harf_notu == "FD"):
        sonuc = "Kaldı"

    elif (harf_notu == "FF"):
        sonuc = "Kaldı"

    else:
        sonuc = "Geçer"

    return isim + " = " + sonuc + "\n"

with open("notlar.txt","r",encoding="utf-8") as file:

    ekleme_liste = []

    for i in file:

        ekleme_liste.append(kalan_gecen(i))

    with open("kalanlarvegecenler.txt" , "w", encoding="utf-8") as file2:

        for i in ekleme_liste:
            file2.write(i)