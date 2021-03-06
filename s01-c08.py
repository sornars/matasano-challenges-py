"""Set 01 - Challenge 08.

Detect AES in ECB mode

In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
"""
import binascii
import os
from Crypto.Cipher import AES

with open(os.path.join(os.path.dirname(__file__), 's01-c08.txt'), 'rb') as f:
    for line in f:
        line = line.strip()
        blocks = [line[i:i+16] for i in range(0, len(line), 16)]
        for block in blocks:
            if blocks.count(block) > 1:
                ecb_encrypted = line
                break

assert ecb_encrypted == b'd880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a'
