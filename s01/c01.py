"""Set 01 - Challenge 01.

Convert hex to base64

The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.
Cryptopals Rule

Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
"""
import binascii

hex_string = (b'49276d206b696c6c696e6720796f757220627261696e206c696b6520612070'
              b'6f69736f6e6f7573206d757368726f6f6d')
b64_string = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def hex2b64(hex_string):
    """Convert a hex string into a base64 encoded string."""
    return binascii.b2a_base64(binascii.a2b_hex(hex_string)).strip()

if __name__ == '__main__':
    assert hex2b64(hex_string) == b64_string
