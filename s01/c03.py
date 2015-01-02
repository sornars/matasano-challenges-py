"""Set 01 - Challenge 03.

Single-byte XOR cipher

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
Achievement Unlocked

You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
"""
import binascii
import c02

hex_string = (b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a39'
              b'3b3736')

# Character Frequencies taken from
# http://en.wikipedia.org/wiki/Letter_frequency on 2015-01-02
# Frequencies for ' ' and numerals extrapolated from article
CHAR_FREQUENCY = {' ': 12.703,
                  'E': 12.702,
                  'T': 9.056,
                  '0': 8.6115,
                  '1': 8.6115,
                  '2': 8.6115,
                  '3': 8.6115,
                  '4': 8.6115,
                  '5': 8.6115,
                  '6': 8.6115,
                  '7': 8.6115,
                  '8': 8.6115,
                  '9': 8.6115,
                  'A': 8.167,
                  'O': 7.507,
                  'I': 6.966,
                  'N': 6.749,
                  'S': 6.327,
                  'H': 6.094,
                  'R': 5.987,
                  'D': 4.253,
                  'L': 4.025,
                  'C': 2.782,
                  'U': 2.758,
                  'M': 2.406,
                  'W': 2.360,
                  'F': 2.228,
                  'G': 2.015,
                  'Y': 1.974,
                  'P': 1.929,
                  'B': 1.492,
                  'V': 0.978,
                  'K': 0.772,
                  'J': 0.153,
                  'X': 0.150,
                  'Q': 0.095,
                  'Z': 0.074
                 }

def decrypt_hex_single_byte_xor(hex_string):
    """Decrypt a hex bytestring that has been XOR'd by a single char and return the key, decoded bytestring and word count score."""
    best_score = 0
    best_string = b''
    best_key = 0
    for char in range(0, 256):
        # Convert int to hex string
        xor_string = (bytes(hex(char)[2:].encode()) * len(hex_string))[:len(hex_string)]
        xor_data = c02.hex_xor(hex_string, xor_string)

        xor_data = binascii.a2b_hex(xor_data)

        score = 0
        try:
            for c in xor_data.decode().upper():
                if c in CHAR_FREQUENCY:
                    score += CHAR_FREQUENCY[c]
        except UnicodeDecodeError:
            # Skip invalid Unicode
            continue

        if score > best_score:
            best_score = score
            best_key = char
            best_string = xor_data

    return best_key, best_string, round(best_score, 2)

if __name__ == '__main__':
    assert decrypt_hex_single_byte_xor(hex_string) == (88, b"Cooking MC's like a pound of bacon", 214.29)
