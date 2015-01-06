"""Set 02 - Challenge 09.

Implement PKCS#7 padding

A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. But we almost never want to transform a single block; we encrypt irregularly-sized messages.

One way we account for irregularly-sized messages is by padding, creating a plaintext that is an even multiple of the blocksize. The most popular padding scheme is called PKCS#7.

So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. For instance,

"YELLOW SUBMARINE"

... padded to 20 bytes would be:

"YELLOW SUBMARINE\x04\x04\x04\x04"
"""

input_block = b'YELLOW SUBMARINE'
pad_size = 20
padded_block = b'YELLOW SUBMARINE\x04\x04\x04\x04'

def pad_block(block, size):
    """Pad a bytestring to a specified number of bytes."""
    if len(block) > size:
        raise ValueError('Block cannot be larger than size to be padded.')
    elif len(block) < size:
        block += ('\x04' * (size - len(block))).encode()
    return block

if __name__ == '__main__':
    assert pad_block(input_block, pad_size) == padded_block
