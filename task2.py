# Коэффициенты перевода единиц измерения в метры
units_to_m = {
    "км": 1000,
    "м": 1,
    "см": 0.01,
    "мм": 0.001,
    "mi": 1609.344,
    "yd": 0.9144,
}

print("Доступные единицы измерения: км, м, см, мм, mi, yd")
from_unit = input("Введите исходную единицу измерения: ").strip()
to_unit = input("Введите целевую единицу измерения: ").strip()
value = float(input(f"Введите значение в {from_unit}: "))

value_in_m = value * units_to_m[from_unit]
result = value_in_m / units_to_m[to_unit]

print(f"{value} {from_unit} = {result:.4f} {to_unit}")
