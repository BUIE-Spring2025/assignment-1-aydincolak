def int_to_roman(num):
    roman_numbers = [
        (1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"),
        (40, "XL"), (50, "L"), (90, "XC"), (100, "C"),
        (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")
    ]
    
    result = ""
    while num >= roman_numbers[0]:
        result += roman_numbers[1]
        num -= roman_numbers[0]
    
    return result

int_to_roman(23)



#    """
#   Convert an integer to a Roman numeral.
#
#    :param num: Integer value between 1 and 3999 inclusive.
#    :return: A string representing the Roman numeral of the integer.
#    """
    