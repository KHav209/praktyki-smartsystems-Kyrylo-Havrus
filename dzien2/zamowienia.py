import csv
import os

zamowienia = []

if os.path.exists("zamowienia.csv"):
    with open("zamowienia.csv", "r", newline="", encoding="utf-8") as plik:
        czytnik = csv.DictReader(plik)
        for wiersz in czytnik:
            wiersz["ilosc"] = int(wiersz["ilosc"])
            zamowienia.append(wiersz)

while True:
    print("\n=== SYSTEM ZAMOWIEN ===")
    print("1. Dodaj zamowienie")
    print("2. Pokaz wszystkie zamowienia")
    print("3. Zmien status zamowienia")
    print("4. Filtruj zamowienia wedlug statusu")
    print("5. Wyjscie")

    wybor = input("Wybierz opcje: ")

    if wybor not in ["1", "2", "3", "4", "5"]:
        print("Nieprawidlowa opcja!")
        continue

    if wybor == "5":
        print("Koniec programu!")
        break

    if wybor == "1":
        klient = input("Podaj imie klienta: ")
        swieca = input("Podaj nazwe swiecy: ")
        
        try:
            ilosc = int(input("Podaj ilosc: "))
        except ValueError:
            print("Ilosc musi byc liczba")
            continue
        
        if ilosc <= 0:
            print("Ilosc musi byc wieksza od 0")
            continue

        zamowienie = {
            "klient": klient,
            "swieca": swieca,
            "ilosc": ilosc,
            "status": "nowe"
        }

        zamowienia.append(zamowienie)
        
        with open("zamowienia.csv", "w", newline="", encoding="utf-8") as plik:
            pola = ["klient", "swieca", "ilosc", "status"]
            zapis = csv.DictWriter(plik, fieldnames=pola)
            
            zapis.writeheader()
            zapis.writerows(zamowienia)

        print("Zamowienie dodane!")

    elif wybor == "2":
        if len(zamowienia) == 0:
            print("Brak zamowien!")
        else:
            for zamowienie in zamowienia:
                print("--------------------")
                print("Klient:", zamowienie["klient"])
                print("Swieca:", zamowienie["swieca"])
                print("Ilosc:", zamowienie["ilosc"])
                print("Status:", zamowienie["status"])
                
    elif wybor == "3":
        if len(zamowienia) == 0:
            print("Brak zamowien!")
        else:
            for i, zamowienie in enumerate(zamowienia):
                print(i + 1, zamowienie["klient"], zamowienie["swieca"])
                
            try:
                numer = int(input("Podaj numer zamowienia: "))
            except ValueError:
                print("Numer musi byc liczba!")
                continue
                
            if numer >= 1 and numer <= len(zamowienia):
                print("1. nowe")
                print("2. w przygotowaniu")
                print("3. wyslane")
                
                status = input("Wybierz nowy status: ")
                
                if status == "1":
                    zamowienia[numer - 1]["status"] = "nowe"
                elif status == "2":
                    zamowienia[numer - 1]["status"] = "w przygotowaniu"
                elif status == "3":
                    zamowienia[numer - 1]["status"] = "wyslane"
                else:
                    print("Nieprawidlowy status!")
                    continue
                
                print("Status zostal zmieniony!")
                with open("zamowienia.csv", "w", newline="", encoding="utf-8") as plik:
                    pola = ["klient", "swieca", "ilosc", "status"]
                    zapis = csv.DictWriter(plik, fieldnames=pola)

                    zapis.writeheader()
                    zapis.writerows(zamowienia)
            else:
                print("Nieprawidlowy numer zamowienia!")
    
    elif wybor == "4":
        print("1. nowe")
        print("2. w przygotowaniu")
        print("3. wyslane")

        status = input("Wybierz status: ")

        if status == "1":
            wybrany_status = "nowe"
        elif status == "2":
            wybrany_status = "w przygotowaniu"
        elif status == "3":
            wybrany_status = "wyslane"
        else:
            print("Nieprawidlowy status!")
            continue
    
        znaleziono = False

        for zamowienie in zamowienia:
            if zamowienie["status"] == wybrany_status:
                print("--------------------")
                print("Klient:", zamowienie["klient"])
                print("Swieca:", zamowienie["swieca"])
                print("Ilosc:", zamowienie["ilosc"])
                print("Status:", zamowienie["status"])
                znaleziono = True

        if not znaleziono:
            print("Brak1 zamowien o takim statusie!")
    
    
    
    
    
              
