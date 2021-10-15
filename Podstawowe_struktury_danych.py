# Zmienne dla poradnika
text = 'Dowolny łańcuch znaków'
one = 1
three = 3
five = 5
pi = 3.14
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
boolean = True


# # Gramatyka pythona ↓    (PEP8: https://www.python.org/dev/peps/pep-0008/)
# • Komentarze - używaj jednej spacji za hashem jeśli komentujesz pełną linię,
#   oraz o dwóch spacji przed hashem i jedną za  # jeśli komentujesz inline
# • Wcięcia - stosuj 4 spacje zamiast 1 tabulatora
# • Maksymalna długość linii - ogranicz wszystkie wiersze do maksymalnie 79 znaków


# Zmienne i typy ↓
print(f'{text} {type(text)}')        # str(), łańcuchy znaków
print(f'{one} {type(one)}')          # int(), liczba całkowita
print(f'{pi} {type(pi)}')            # float(), liczba zmiennoprzecinkowa
print(f'{boolean} {type(boolean)}')  # bollean(), typ logiczny. Przyjmuje wartości True(1) lub False(0)


# Operatory arytmetyczne ↓
print(three + five)   # 8    dodawanie
print(five - three)   # 2    odejmowanie
print(three * five)   # 15   mnożenie
print(five / three)   # 0.6  dzielenie
print(three // five)  # 0    dzielenie całkowite
print(three % five)   # 3    modulo - zwraca resztę z dzielenia
print(five ** three)  # 243  potęgowanie
print(-one)           # -1   liczba przeciwna


# Operatory logiczne ↓
print(one == 1)            # równe
print(one != 10)           # różne
print(five > 3)            # większe
print(five >= 5)           # większe lub równe
print(five < 10)           # mniejsze
print(five <= 5)           # mniejsze lub równe
print(one and five)        # 'i'
print(one or three)        # 'lub'
print(one is one)          # 'jest'
print(one is not three)    # 'nie jest'
print(one in number_list)  # 'zawiera się w..'
