class Temperature:
    def convert_to_fahrenheit(self, temp):
        print(temp * 1.8 + 32)

    def convert_to_celsius(self, temp):
        print((temp - 32)/1.8)

first = float(input("Введите температуру: "))
second = str(input("C для Цельсия, F для Фаренгейта: "))
if second == "C":
    temperature = Temperature()
    temperature.convert_to_celsius(first)
if second == "F":
    temperature = Temperature()
    temperature.convert_to_fahrenheit(first)
