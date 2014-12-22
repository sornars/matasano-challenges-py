"""Set 01 - Challenge 02."""
import binascii

hex_string_1 = b'1c0111001f010100061a024b53535009181c'
hex_string_2 = b'686974207468652062756c6c277320657965'
xor_string = b'746865206b696420646f6e277420706c6179'

def hex_xor(hex_string_1, hex_string_2):
    """Return the XOR of two hex strings."""
    if len(hex_string_1) != len(hex_string_2):
        raise  ValueError('Length of a must be the same as b.')

    hex_data_1 = binascii.a2b_hex(hex_string_1)
    hex_data_2 = binascii.a2b_hex(hex_string_2)
    return binascii.b2a_hex(
        bytearray(
            [char_a ^ char_b for char_a, char_b in zip(hex_data_1, hex_data_2)]
        )
    )

assert hex_xor(hex_string_1, hex_string_2) == xor_string
