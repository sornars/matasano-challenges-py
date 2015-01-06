"""Set 01 - Challenge 02.

Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179

"""
import binascii

hex_string_1 = b'1c0111001f010100061a024b53535009181c'
hex_string_2 = b'686974207468652062756c6c277320657965'
xor_string = b'746865206b696420646f6e277420706c6179'

def hex_xor(hex_string_1, hex_string_2):
    """Return the XOR of two hex bytestrings."""
    if len(hex_string_1) != len(hex_string_2):
        raise ValueError('Length of inputs must match.')

    hex_data_1 = binascii.a2b_hex(hex_string_1)
    hex_data_2 = binascii.a2b_hex(hex_string_2)
    return binascii.b2a_hex(
        bytes(
            [char_a ^ char_b for char_a, char_b in zip(hex_data_1, hex_data_2)]
        )
    )

if __name__ == '__main__':
    assert hex_xor(hex_string_1, hex_string_2) == xor_string
