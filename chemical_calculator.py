# Chemical Calculator
# Author: Suraj Gade
# BSc Chemistry @ SPPU

import math


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Enter a number.")


def calculate_ph(h_concentration):
    if h_concentration <= 0:
        raise ValueError("H+ concentration must be greater than 0.")
    return round(-math.log10(h_concentration), 2)


def calculate_molarity(moles, volume_liters):
    if volume_liters <= 0:
        raise ValueError("Volume must be greater than 0.")
    return round(moles / volume_liters, 4)


def calculate_concentration_from_mass(mass, molar_mass, volume):
    if molar_mass <= 0:
        raise ValueError("Molar mass must be greater than 0.")
    if volume <= 0:
        raise ValueError("Volume must be greater than 0.")

    moles = mass / molar_mass
    return round(moles / volume, 4)


while True:
    print("\n=== Chemical Calculator ===")
    print("1. pH Calculator")
    print("2. Molarity Calculator")
    print("3. Concentration Calculator")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    try:
        if choice == "1":
            h = get_float("Enter H+ concentration (mol/L): ")
            print(f"pH = {calculate_ph(h)}")

        elif choice == "2":
            mol = get_float("Enter moles: ")
            vol = get_float("Enter volume (L): ")
            print(f"Molarity = {calculate_molarity(mol, vol)} mol/L")

        elif choice == "3":
            mass = get_float("Enter mass (g): ")
            molar_mass = get_float("Enter molar mass (g/mol): ")
            vol = get_float("Enter volume (L): ")

            concentration = calculate_concentration_from_mass(
                mass, molar_mass, vol
            )
            print(f"Concentration = {concentration} mol/L")

        elif choice == "4":
            print("Exiting calculator...")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

    except ValueError as error:
        print(f"Error: {error}")
