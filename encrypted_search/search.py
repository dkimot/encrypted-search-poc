import crypto_primitives
import sys
import traceback

from .xor_word import xor_word


def chunk_split(chunk, length):
    return (chunk[0 + i:length + i] for i in range(0, len(chunk), length))


def search(word: str, in_file, key: bytearray):
    # search each file

    # if word is too long, trim it
    word_len = len(bytearray(word, 'utf-8'))
    if word_len > 16:
        padded_word_ba = bytearray(word, 'utf-8')[:32]
    else:
        padded_word = word.ljust(32, '.')
        padded_word_ba = bytearray(padded_word, 'utf-8')

    enc_search_term = crypto_primitives.BlockCipher(key).encrypt(padded_word_ba)

    s_aes_cipher = crypto_primitives.BlockCipher(key)
    found_word = 0

    in_data = in_file.read(32)
    while in_data:
        ti = xor_word(enc_search_term, in_data)
        ti = list(chunk_split(ti, 16))

        if s_aes_cipher.encrypt(ti[0]) == ti[1]:
            found_word = 1
            break
        in_data = in_file.read(32)

    print('Present' if found_word else 'Not present')
