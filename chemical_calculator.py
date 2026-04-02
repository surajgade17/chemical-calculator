# Chemical Calculator
# Author: Suraj Gade
# BSc Chemistry @ SPPU

import math

def calculate_ph(h_concentration):
    return round(-math.log10(h_concentration), 2)

def calculate_molarity(moles, volume_liters):
    return round(moles / volume_liters, 4)

def calculate_concentration(mass, molar_mass, volume):
    moles = mass / molar_mass
    return round(moles / volume, 4)

print("=== Chemical Calculator ===")
print("1. pH Calculator")
print("2. Molarity Calculator")
print("3. Concentration Calculator")

choice = input("\nEnter choice (1/2/3): ")

if choice == "1":
    h = float(input("Enter H+ concentration: "))
    print(f"pH = {calculate_ph(h)}")
elif choice == "2":
    mol = float(input("Enter moles: "))
    vol = float(input("Enter volume (L): "))
    print(f"Molarity = {calculate_molarity(mol, vol)} mol/L")
elif choice == "3":
    mass = float(input("Enter mass (g): "))
    mm = float(input("Enter molar mass: "))
    vol = float(input("Enter volume (L): "))
    print(f"Concentration = {calculate_concentration(mass, mm, vol)} mol/L")
