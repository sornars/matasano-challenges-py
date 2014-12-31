"""Set 01 - Challenge 04.

Detect single-character XOR

One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""
import os
import c03

best_fit = (b'', 0, b'', 0)
with open(os.path.join(os.path.dirname(__file__), 'c04.txt'), 'rb') as f:
    for input_hex in f:
        scored_input = c03.decrypt_hex_single_byte_xor(input_hex.strip())
        if scored_input[2] > 0:
            if scored_input[2] > best_fit[3]:
                best_fit = (input_hex,) + scored_input

assert best_fit == (b'7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f\n',
                    53, b'Now that the party is jumping\n', 6)

