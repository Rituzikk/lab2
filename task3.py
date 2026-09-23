year = int(input("Введите год: "))

if year % 4 != 0:
    is_leap = False
elif year % 100 != 0:
    is_leap = True
elif year % 400 != 0:
    is_leap = False
else:
    is_leap = True

if is_leap:
    print(f"{year} год — високосный")
else:
    print(f"{year} год — не високосный")
