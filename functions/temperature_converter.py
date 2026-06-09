""" 
Write functions to convert between Celsius, Fahrenheit, and Kelvin. Then write a main function that
 accepts a value, source unit, and target unit, and returns the converted result.
"""

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))




def convert(value, target, source = "c"): 
    if source == 'c' and target == 'f':
        return celsius_to_fahrenheit(value)
    elif source == 'c' and target == 'k':
        return celsius_to_kelvin(value)
    elif source == 'f' and target == 'c':
        return fahrenheit_to_celsius(value)
    elif source == 'f' and target == 'k':
        return fahrenheit_to_kelvin(value)
    elif source =='k' and target == 'c':
        return kelvin_to_celsius(value)
    elif source == 'k' and target == 'f':
        return kelvin_to_fahrenheit(value)

value = float(input("Enter temperature value:  "))
source = input("Enter source unit (c/f/k) : ")
target = input("Enter target (c/f/k) : ")

result = convert(value, target, source)

print(f"{value}{source} = {result}{target}")
