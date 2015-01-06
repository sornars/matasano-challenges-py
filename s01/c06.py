"""Set 01 - Challenge 06.

Break repeating-key XOR
It is officially on, now.

This challenge isn't conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

    Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
    Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:

    this is a test

    and

    wokka wokka!!!

    is 37. Make sure your code agrees before you proceed.
    For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
    The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
    Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
    Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
    Solve each block as if it was single-character XOR. You already have code to do this.
    For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.

This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.
No, that's not a mistake.

We get more tech support questions for this challenge than any of the other ones. We promise, there aren't any blatant errors in this text. In particular: the "wokka wokka!!!" edit distance really is 37.
"""
import binascii
import io
import os
import c03

hamming_s1 = b'this is a test'
hamming_s2 = b'wokka wokka!!!'
expected_distance = 37



def hamming_distance(string_1, string_2):
    """Calculate the Hamming Distance between two bytestrings."""
    if len(string_1) != len(string_2):
        raise  ValueError('Length of inputs must match.')

    return sum(bin(char_1 ^ char_2).count('1') for char_1, char_2 in zip(string_1, string_2))

def decrypt_repeating_key_xor(input_text):
    """Decrypt a bytestring that has been encrypted with a repeating key."""
    keysize_distances = []
    for keysize in range(2, 41):
        with io.BytesIO(input_text) as f:
            block_1 = f.read(keysize)
            block_2 = f.read(keysize)
            block_3 = f.read(keysize)
            block_4 = f.read(keysize)
            h_distance_1 = hamming_distance(block_1, block_2)
            h_distance_2 = hamming_distance(block_2, block_3)
            h_distance_3 = hamming_distance(block_3, block_4)
            h_distance = (h_distance_1 + h_distance_2 + h_distance_3)/3
            keysize_distances.append((keysize, h_distance/keysize))

    keysize_distances.sort(key=lambda x: x[1])

    keys = []
    for keysize, keysize_distance in keysize_distances[:3]:
        blocks = []
        with io.BytesIO(input_text) as f:
            block = f.read(keysize)
            while block:
                blocks.append(block)
                block = f.read(keysize)

        blocks = filter(lambda x: len(x) == keysize, blocks)

        key = b''
        for transposed_block in zip(*blocks):
            result = c03.decrypt_hex_single_byte_xor(
                ''.join(['{:02x}'.format(c) for c in transposed_block]).encode())
            key += bytes([result[0]])

        keys.append(key)

    return keys



if __name__ == '__main__':
    assert hamming_distance(hamming_s1, hamming_s2) == expected_distance
    with open(os.path.join(os.path.dirname(__file__), 'c06.txt'), 'rb') as f:
        input_text = binascii.a2b_base64(f.read())

    assert b'Terminator X: Bring the noise' in decrypt_repeating_key_xor(input_text)


