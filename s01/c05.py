"""Set 01 - Challenge 05."""
import c02
import binascii

input_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = 'ICE'
encrypted_string = b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

def encrypt_repeating_key_xor(input_string, key):
    """XOR an input_string with a repeating key."""
    hex_input_string = bytes(''.join(['{:02x}'.format(ord(char)) for char in input_string]).encode())
    hex_key = bytes(''.join(['{:02x}'.format(ord(char)) for char in key]).encode())
    hex_key = (hex_key * (len(hex_input_string)//len(hex_key)) + hex_key[:(len(hex_input_string) % len(hex_key))])
    return c02.hex_xor(hex_input_string, hex_key)

if __name__ == '__main__':
    assert encrypt_repeating_key_xor(input_string, key) == encrypted_string

