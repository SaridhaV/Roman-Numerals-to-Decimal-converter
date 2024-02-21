def roman_to_decimal(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    prev_value = 0
    
    for numeral in reversed(roman):
        value = roman_numerals[numeral]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value
    
    return decimal

# Get input from the user
roman_numeral = input("Enter a Roman numeral: ").upper()

# Convert Roman numeral to decimal
decimal_value = roman_to_decimal(roman_numeral)

# Output the result
print(f"The decimal value of {roman_numeral} is {decimal_value}")