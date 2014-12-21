import binascii

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def hex2b64(hex_string):
    return binascii.b2a_base64(binascii.a2b_hex(hex_string)).strip()

assert hex2b64(hex_string) == b64_string
