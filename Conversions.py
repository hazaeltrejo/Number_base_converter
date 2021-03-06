

def binary_to_decimal(number):
    position=0
    decimal=0
    number=str(number)
    number=number[::-1]
    for i in number:
        multi=2**position
        decimal += int(i)*multi
        position += 1
    print(decimal)
    return decimal
def octal_to_decimal(number):
    position=0
    decimal=0
    number=str(number)
    number=number[::-1]
    for i in number:
        multi=8**position
        decimal += int(i)*multi
        position += 1
    print(decimal)
    return decimal
def hexadecimal_to_decimal(hexadecimal):
    hexadecimal = hexadecimal.lower()
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    position = 0
    for i in hexadecimal:
        value = get_real_number(i)
        multi=16**position
        equivalence=multi*value
        decimal += equivalence
        position += 1
    print(decimal)
    return decimal
def  get_character_hexadecimal(value):
    value = str(value)
    equival = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if value in equival:
        return equival[value]
    else:
        return value
def get_real_number(character_hexadecimal):
    equival = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if character_hexadecimal in equival:
        return equival[character_hexadecimal]
    else:
        return int(character_hexadecimal)
def decimal_to_binary(number):
    if number <= 0:
        return "0"
    binary = ""
    while number > 0:
        resid = int(number % 2)
        number = int(number / 2)
        binary = str(resid) + binary
    return binary
def decimal_to_octal(decimal):
    octal=""
    while decimal>0:
        resid=decimal % 8
        octal=str(resid)+octal
        decimal=int(decimal/8)
    return octal
def decimal_to_hexadecimal(decimal):
    hexadecimal=""
    while decimal>0:
        resid=decimal % 16
        character=get_real_number(resid)
        hexadecimal=character+hexadecimal
        decimal=decimal/16
    return hexadecimal
            
