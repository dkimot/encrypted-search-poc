import crypto_primitives
import re

from .xor_word import xor_word

STREAM_CIPHER_KEY = bytearray('thiskeyisverybad', 'utf-8')  # it is 128 bits though

# Isolating words and not any punctuation marks
r_word = re.compile("(\w[\w']*\w|\w)")


def word_iter(file_obj):
    for line in file_obj:
        for word in r_word.findall(line.decode('utf-8')):
            yield word


def encrypt(file, out_path, key: bytearray):
    stream_cipher = crypto_primitives.StreamCipher(STREAM_CIPHER_KEY)
    w_block_cipher = crypto_primitives.BlockCipher(key)
    s_block_cipher = crypto_primitives.BlockCipher(key)

    with open(out_path, 'wb') as out_file:
        for word in word_iter(file):
            # Pad and encrypt word
            word_len = len(bytearray(word, 'utf-8'))
            if word_len > 16:
                padded_word_ba = bytearray(word, 'utf-8')[:32]
            else:
                padded_word = word.ljust(32, '.')
                padded_word_ba = bytearray(padded_word, 'utf-8')

            enc_word = w_block_cipher.encrypt(padded_word_ba)

            si = stream_cipher.generate()
            enc_si = s_block_cipher.encrypt(si)
            ti = si + enc_si
            ciphertxt = xor_word(enc_word, ti)
            out_file.write(ciphertxt)
