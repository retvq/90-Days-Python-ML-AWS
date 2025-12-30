# ==================================================
# PROJECT 3: Temperature Converter
# ==================================================
# WHAT: Convert between Celsius and Fahrenheit
# WHY: Real-world data transformation pattern
# SKILLS: input(), arithmetic, conditionals, formatting
# ==================================================

# --------------------------------------------------
# STEP 1: Display welcome and menu
# --------------------------------------------------
print("=" * 50)
print("       TEMPERATURE CONVERTER 🌡️")
print("=" * 50)
print("\nConvert temperatures between Celsius, Kelvin and Fahrenheit")
print("\nOptions:")
print("  1. Celsius → Fahrenheit")
print("  2. Fahrenheit → Celsius")
print("  3. Celsius → Kelvin")
print("  4. Kelvin → Celsius")
print()

# --------------------------------------------------
# STEP 2: Get user choice
# --------------------------------------------------
while True:
    choice = input("Enter your choice (1, 2, 3 or 4) or 'E'to exit: ").strip().lower()
    if choice == "e": break
    # --------------------------------------------------
    # STEP 3: Process based on choice
    # --------------------------------------------------

    elif choice == "1":
        # Celsius to Fahrenheit
        print("\n--- CELSIUS → FAHRENHEIT ---")
        celsius = float(input("Enter temperature in Celsius: "))

        # Formula: F = (C × 9/5) + 32
        fahrenheit = (celsius * 9/5) + 32

        # Display result
        print("\n" + "-" * 40)
        print(f"  {celsius}°C = {fahrenheit:.2f}°F")
        print("-" * 40)

    elif choice == "2":
        # Fahrenheit to Celsius
        print("\n--- FAHRENHEIT → CELSIUS ---")
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))

        # Formula: C = (F - 32) × 5/9
        celsius = (fahrenheit - 32) * 5/9

        # Display result
        print("\n" + "-" * 40)
        print(f"  {fahrenheit}°F = {celsius:.2f}°C")
        print("-" * 40)

    elif choice == "3":
        # Celsius to Fahrenheit
        print("\n--- CELSIUS → KELVIN ---")
        celsius = float(input("Enter temperature in Celsius: "))

        # Formula: C = K - 273
        kelvin = celsius - 273

        # Display result
        print("\n" + "-" * 40)
        print(f"  {celsius}°C = {kelvin:.2f}°K")
        print("-" * 40)

    elif choice == "2":
        # Fahrenheit to Celsius
        print("\n--- KELVIN → CELSIUS ---")
        kelvin = float(input("Enter temperature in Kelvin: "))

        # Formula: C = (F - 32) × 5/9
        celsius = kelvin + 273

        # Display result
        print("\n" + "-" * 40)
        print(f"  {kelvin}°K = {celsius:.2f}°C")
        print("-" * 40)

    else:
        print(f"\nInvalid choice: '{choice}'")
