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
import cryptopals

hex_string = (b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a39'
              b'3b3736')

assert cryptopals.decrypt_hex_single_byte_xor(hex_string) == (88, b"Cooking MC's like a pound of bacon", 214.29)
