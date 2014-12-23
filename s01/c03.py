"""Set 01 - Challenge 03."""
import binascii
import collections
import c02

hex_string = (b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a39'
              b'3b3736')

with open('/usr/share/dict/words') as f:
    ENGLISH_WORDS = tuple(word.upper().strip() for word in f)

def decrypt_hex_single_byte_xor(hex_string):
    """Decrypt a hex string that has been XOR'd by a single char and return the key and decoded bytestring."""
    word_count = collections.defaultdict(int)
    best_word_count = 0
    best_string = b''
    best_key = 0
    for char in range(0, 256):
        # Convert int to hex string
        xor_string = (bytes(hex(char)[2:].encode()) * len(hex_string))[:len(hex_string)]
        xor_data = c02.hex_xor(hex_string, xor_string)

        xor_data = binascii.a2b_hex(xor_data)

        for word in ENGLISH_WORDS:
            try:
                if word in xor_data.decode().upper():
                    word_count[char] += 1
            except UnicodeDecodeError:
                # Skip invalid Unicode
                continue

        if word_count[char] > best_word_count:
            best_word_count = word_count[char]
            best_key = char
            best_string = xor_data

    return best_key, best_string

assert decrypt_hex_single_byte_xor(hex_string) == (88, b"Cooking MC's like a pound of bacon")
