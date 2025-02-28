def int_to_roman(num):
    roman_numbers = [
        (1000, "M"), (900, "CM"), (500, "D"),  (400, "CD"), 
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    result = ""
    for integer, romen in roman_numbers:
        while num >= integer:
            result += romen
            num -= integer
    
    return result

print(int_to_roman(24))


#    """
#   Convert an integer to a Roman numeral.
#
#    :param num: Integer value between 1 and 3999 inclusive.
#    :return: A string representing the Roman numeral of the integer.
#    """
    