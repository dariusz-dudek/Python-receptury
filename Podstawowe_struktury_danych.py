# # Gramatyka pythona ↓    (PEP8: https://www.python.org/dev/peps/pep-0008/)
# • Komentarze - używaj jednej spacji za hashem jeśli komentujesz pełną linię,
# oraz o dwóch spacji przed hashem i jedną za  # jeśli komentujesz inline
# • Wcięcia - stosuj 4 spacje zamiast 1 tabulatora
# • Maksymalna długość linii - ogranicz wszystkie wiersze do maksymalnie 79 znaków


# # Zmienne i typy ↓
# String = 'tekst'  # str(), Zmienna przechowująca napisy. Definiuj za pomocą pojedynczego lub podwójnego cudzysłowu
# print(f'{String} {type(String)}')
#
# Integer = 5  # int(), Liczba całkowita
# print(f'{Integer} {type(Integer)}')
#
# Float = 3.14  # float(), Liczba rzeczywista
# print(f'{Float} {type(Float)}')
#
# Boolean = True  # bollean(), Typ logiczny. Przyjmuje wartości True(1) lub False(0)
# print(f'{Boolean} {type(Boolean)}')


# # Operatory arytmetyczne ↓
# x, y = 3, 5
# print(x + y)   # 8      dodawanie
# print(x - y)   # 2      odejmowanie
# print(x * y)   # 15     mnożenie
# print(x / y)   # 0.6    dzielenie
# print(x // y)  # 0      dzielenie całkowite
# print(x % y)   # 3      modulo - zwraca resztę z dzielenia
# print(x ** y)  # 243    potęgowanie
# print(-x)      # -3     liczba przeciwna


# # Operatory logiczne ↓
# x, y, z, numbers = 3, 5, 3, [1, 2, 3]
# print(x == z)       # x jest równe od z
# print(x != y)       # x jest różne od y
# print(y > x)        # y jest większe od x
# print(x >= z)       # x jest większe lub równe z
# print(x < y)        # x jest mniejsze od y
# print(x <= z)       # x jest mniejsze lub równe z
# print(x and y)      # operator 'i'
# print(x or y)       # operator 'lub'
# print(x is x)       # operator 'jest'
# print(x is not y)   # operator 'nie jest'
# print(x in numbers) # operator 'zawiera się w..'
