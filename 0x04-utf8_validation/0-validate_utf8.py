#!/usr/bin/python3

"""uft validation"""


def validUTF8(data):
    """ValidUTF function

    """
    num_bytes = 0
    for byte in data:
        byte = byte & 0XFF

        if num_bytes == 0:
            if byte & 0b10000000 == 0b00000000:
                num_bytes = 0
            elif byte & 0b11100000 == 0b11000000:
                num_bytes = 1
            elif byte & 0b11110000 == 0b11100000:
                num_bytes = 2
            elif byte & 0b11111000 == 0b11110000:
                num_bytes = 3
            else:
                return False

        else:
            if byte & 0b11000000 != 0b10000000:
                return False
            num_bytes -= 1

    return num_bytes == 0
