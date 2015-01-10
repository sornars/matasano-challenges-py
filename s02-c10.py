r"""Set 02 - Challenge 10.

Implement CBC mode

CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, despite the fact that a block cipher natively only transforms individual blocks.

In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.

The first plaintext block, which has no associated previous ciphertext block, is added to a "fake 0th ciphertext block" called the initialization vector, or IV.

Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test), and using your XOR function from the previous exercise to combine them.

The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)
Don't cheat.

Do not use OpenSSL's CBC code to do CBC mode, even to verify your results. What's the point of even doing this stuff if you aren't going to learn from it?
"""
import binascii
import os
import cryptopals

with open(os.path.join(os.path.dirname(__file__), 's02-c10.txt'), 'rb') as f:
    input_text = binascii.a2b_base64(f.read())

key = b'YELLOW SUBMARINE'

assert cryptopals.decrypt_cbc(key, input_text) == b"""I'm back and I'm ringin' the bell\x20
A rockin' on the mike while the fly girls yell\x20
In ecstasy in the back of me\x20
Well that's my DJ Deshay cuttin' all them Z's\x20
Hittin' hard and the girlies goin' crazy\x20
Vanilla's on the mike, man I'm not lazy.\x20

I'm lettin' my drug kick in\x20
It controls my mouth and I begin\x20
To just let it flow, let my concepts go\x20
My posse's to the side yellin', Go Vanilla Go!\x20

Smooth 'cause that's the way I will be\x20
And if you don't give a damn, then\x20
Why you starin' at me\x20
So get off 'cause I control the stage\x20
There's no dissin' allowed\x20
I'm in my own phase\x20
The girlies sa y they love me and that is ok\x20
And I can dance better than any kid n' play\x20

Stage 2 -- Yea the one ya' wanna listen to\x20
It's off my head so let the beat play through\x20
So I can funk it up and make it sound good\x20
1-2-3 Yo -- Knock on some wood\x20
For good luck, I like my rhymes atrocious\x20
Supercalafragilisticexpialidocious\x20
I'm an effect and that you can bet\x20
I can take a fly girl and make her wet.\x20

I'm like Samson -- Samson to Delilah\x20
There's no denyin', You can try to hang\x20
But you'll keep tryin' to get my style\x20
Over and over, practice makes perfect\x20
But not if you're a loafer.\x20

You'll get nowhere, no place, no time, no girls\x20
Soon -- Oh my God, homebody, you probably eat\x20
Spaghetti with a spoon! Come on and say it!\x20

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino\x20
Intoxicating so you stagger like a wino\x20
So punks stop trying and girl stop cryin'\x20
Vanilla Ice is sellin' and you people are buyin'\x20
'Cause why the freaks are jockin' like Crazy Glue\x20
Movin' and groovin' trying to sing along\x20
All through the ghetto groovin' this here song\x20
Now you're amazed by the VIP posse.\x20

Steppin' so hard like a German Nazi\x20
Startled by the bases hittin' ground\x20
There's no trippin' on mine, I'm just gettin' down\x20
Sparkamatic, I'm hangin' tight like a fanatic\x20
You trapped me once and I thought that\x20
You might have it\x20
So step down and lend me your ear\x20
'89 in my time! You, '90 is my year.\x20

You're weakenin' fast, YO! and I can tell it\x20
Your body's gettin' hot, so, so I can smell it\x20
So don't be mad and don't be sad\x20
'Cause the lyrics belong to ICE, You can call me Dad\x20
You're pitchin' a fit, so step back and endure\x20
Let the witch doctor, Ice, do the dance to cure\x20
So come up close and don't be square\x20
You wanna battle me -- Anytime, anywhere\x20

You thought that I was weak, Boy, you're dead wrong\x20
So come on, everybody and sing this song\x20

Say -- Play that funky music Say, go white boy, go white boy go\x20
play that funky music Go white boy, go white boy, go\x20
Lay down and boogie and play that funky music till you die.\x20

Play that funky music Come on, Come on, let me hear\x20
Play that funky music white boy you say it, say it\x20
Play that funky music A little louder now\x20
Play that funky music, white boy Come on, Come on, Come on\x20
Play that funky music\x20
\x04\x04\x04\x04"""

