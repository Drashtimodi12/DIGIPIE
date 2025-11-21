# Task 12: Create a class Temperature with:
# static method to convert °C → °F
# static method to convert °F → °C
# Ask user input and convert.

class Temperature:

    @staticmethod
    def Celsius():
        c = float(input("Enter temperature in Celsius: "))
        F = (9/5 * c)+32
        print(f"Celsius = {c} C \nFahrenheit = {F} F.")

    @staticmethod
    def Fahrenheit():
        f = float(input("Enter temperature in Fahrenheit: "))
        C = 5/9*(f-32)
        print(f"Fahrenheit = {f} F \nCelsius = {C} C")

T = Temperature()
T.Celsius()
T.Fahrenheit()
