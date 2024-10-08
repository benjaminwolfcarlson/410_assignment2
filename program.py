# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:54:06 2024

@author: benja
"""

from temperatureconverter import fahrenheit_to_celsius, celsius_to_fahrenheit

def display_title():
    print("Temperature Converter")

def display_menu():
    print("\nSelect:")
    print("1. F to C")
    print("2. C to F")
    print("3. Exit")

def main():
    display_title()
    
    while True:
        display_menu()
        choice = input("Select an Option: ")
        
        if choice == '1':
            fahrenheit = float(input("Enter temperature in F: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius}°C")
        
        elif choice == '2':
            celsius = float(input("Enter temperature in C: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit}°F")
        
        elif choice == '3':
            print("Exiting.")
            break
        
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()