def length_converter():
    print("Escolha a unidade de comprimento de entrada:")
    print("1. Metros")
    print("2. Quilômetros")
    print("3. Milhas")
    choice = int(input("Digite o número correspondente à sua escolha: "))
    length = float(input("Digite a quantidade: "))

    if choice == 1:
        meters_to_kilometers(length)
        meters_to_miles(length)
    elif choice == 2:
        kilometers_to_meters(length)
        kilometers_to_miles(length)
    elif choice == 3:
        miles_to_meters(length)
        miles_to_kilometers(length)
    else:
        print("Escolha inválida")

def temperature_converter():
    print("Escolha a unidade de temperatura de entrada:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    choice = int(input("Digite o número correspondente à sua escolha: "))
    temp = float(input("Digite a temperatura: "))

    if choice == 1:
        celsius_to_fahrenheit(temp)
        celsius_to_kelvin(temp)
    elif choice == 2:
        fahrenheit_to_celsius(temp)
        fahrenheit_to_kelvin(temp)
    elif choice == 3:
        kelvin_to_celsius(temp)
        kelvin_to_fahrenheit(temp)
    else:
        print("Escolha inválida")

def main():
    print("Bem-vindo ao Conversor de Medidas!")
    print("Escolha a categoria:")
    print("1. Comprimento")
    print("2. Temperatura")
    category = int(input("Digite o número correspondente à sua escolha: "))

    if category == 1:
        length_converter()
    elif category == 2:
        temperature_converter()
    else:
        print("Escolha inválida")

def meters_to_kilometers(length):
    kilometers = length / 1000
    print(f"{length} metros equivalem a {kilometers} quilômetros.")

def kilometers_to_meters(length):
    meters = length * 1000
    print(f"{length} quilômetros equivalem a {meters} metros.")

def meters_to_miles(length):
    miles = length * 0.000621371
    print(f"{length} metros equivalem a {miles} milhas.")

def miles_to_meters(length):
    meters = length / 0.000621371
    print(f"{length} milhas equivalem a {meters} metros.")

def kilometers_to_miles(length):
    miles = length * 0.621371
    print(f"{length} quilômetros equivalem a {miles} milhas.")

def miles_to_kilometers(length):
    kilometers = length / 0.621371
    print(f"{length} milhas equivalem a {kilometers} quilômetros.")

def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp} Celsius equivalem a {fahrenheit} Fahrenheit.")

def celsius_to_kelvin(temp):
    kelvin = temp + 273.15
    print(f"{temp} Celsius equivalem a {kelvin} Kelvin.")

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5/9
    print(f"{temp} Fahrenheit equivalem a {celsius} Celsius.")

def fahrenheit_to_kelvin(temp):
    kelvin = (temp - 32) * 5/9 + 273.15
    print(f"{temp} Fahrenheit equivalem a {kelvin} Kelvin.")

def kelvin_to_celsius(temp):
    celsius = temp - 273.15
    print(f"{temp} Kelvin equivalem a {celsius} Celsius.")

def kelvin_to_fahrenheit(temp):
    fahrenheit = (temp - 273.15) * 9/5 + 32
    print(f"{temp} Kelvin equivalem a {fahrenheit} Fahrenheit.")

if __name__ == "__main__":
    main()
