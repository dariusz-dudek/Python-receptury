# Gramatyka pythona ↓    (PEP8: https://www.python.org/dev/peps/pep-0008/)
# Komentarze - używaj jednej spacji za hashem jeśli komentujesz pełną linię,
print('Hello, world!')  # oraz o dwóch spacji przed hashem i jedną za  # jeśli komentujesz inline
# Wcięcia - stosuj 4 spacje zamiast 1 tabulatora
# Maksymalna długość linii - ogranicz wszystkie wiersze do maksymalnie 79 znaków

# Zmienne i typy ↓
text = 'Dowolny łańcuch znaków'  # str(), łańcuchy znaków
one = 1  # int(), liczba całkowita
three = 3  # int(), liczba całkowita
five = 5  # int(), liczba całkowita
pi = 3.14  # float(), liczba zmiennoprzecinkowa
boolean = True  # boll(), typ logiczny. Przyjmuje wartości True(1) lub False(0)
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Operatory arytmetyczne ↓
three + five  # dodawanie
five - three  # odejmowanie
three * five  # mnożenie
five / three  # dzielenie
three // five  # dzielenie całkowite
three % five  # modulo - zwraca resztę z dzielenia
five ** three  # potęgowanie
-one  # liczba przeciwna

# Operatory logiczne ↓
one == 1  # równe
one != 10  # różne
five > 3  # większe
five >= 5  # większe lub równe
five < 10  # mniejsze
five <= 5  # mniejsze lub równe
one and five  # 'i'
one or three  # 'lub'
one is one  # 'jest'
one is not three  # 'nie jest'
one in number_list  # 'zawiera się w..'
