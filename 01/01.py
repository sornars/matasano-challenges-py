"""Set 01 - Challenge 01."""
import base64

hex_string = ('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f'
              '69736f6e6f7573206d757368726f6f6d')
b64_string = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def hex2b64(hex_string):
    """Convert a hex string into a base64 encoded byte string."""
    hex_data = bytearray.fromhex(hex_string)
    # Strip trailing newline
    return base64.encodebytes(hex_data)[:-1]

assert hex2b64(hex_string) == b64_string
