from Crypto.Cipher import AES
import secrets

rand_word = secrets.randbits(16 * 8).to_bytes(16, 'big')


class StreamCipher:
    def __init__(self, key: bytearray):
        self.s_key = key

    def generate(self):
        # Create a new instance of a counter-mode stream cipher
        ctr_cipher = AES.new(self.s_key, mode=AES.MODE_CTR)
        return ctr_cipher.encrypt(rand_word)

    def decrypt(self, enc: bytearray):
        # Create a new counter-mode stream cipher
        ctr_cipher = AES.new(self.s_key, mode=AES.MODE_CTR)
        return ctr_cipher.decrypt(enc)
