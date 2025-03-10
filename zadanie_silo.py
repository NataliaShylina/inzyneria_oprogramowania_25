#Zadanie 1 - Silo
#Twoim zadaniem jest obliczenie liczby piętrem do przejścia.
#Dane wejściowe: piętro startowe, piętro końcowe
#Przykład: 15, 166
#Dane wyjściowe: ciąg znaków (string)
#Przykład: 151 w dół
#Funkcja nazywać się ma: oblicz_pietra
#Kod do uzupełnienia:
#Variant1
"""
def oblicz_pietra(pietro_startowe, pietro_koncowe):
    if pietro_startowe<pietro_koncowe:
        return f"{pietro_koncowe-pietro_startowe} w dol"
    elif pietro_startowe>pietro_koncowe:
        return f"{pietro_startowe-pietro_koncowe} w gore"

print(oblicz_pietra(15, 66))
print(oblicz_pietra(77, 29))
"""
#Variant2
def oblicz_pietra():
    try:
        pietro_startowe = int(input("Podaj piętro startowe: "))
        pietro_koncowe = int(input("Podaj piętro końcowe: "))

        if pietro_startowe < pietro_koncowe:
            print(f"{pietro_koncowe - pietro_startowe} w dol")
        elif pietro_startowe > pietro_koncowe:
            print(f"{pietro_startowe - pietro_koncowe} w gore")
        else:
            print("Zostajesz na tym samym pietrze")

    except ValueError:
        print("Error")

oblicz_pietra()
