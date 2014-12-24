"""Set 01 - Challenge 01."""

import binascii

hex_string = (b'49276d206b696c6c696e6720796f757220627261696e206c696b6520612070'
              b'6f69736f6e6f7573206d757368726f6f6d')
b64_string = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def hex2b64(hex_string):
    """Convert a hex string into a base64 encoded string."""
    return binascii.b2a_base64(binascii.a2b_hex(hex_string)).strip()

if __name__ == '__main__':
    assert hex2b64(hex_string) == b64_string
