import base64
from Crypto.Cipher import AES
import secrets


def unpad(s): return s[:-ord(s[len(s) - 1:])]


block_iv = secrets.randbits(16 * 8).to_bytes(16, 'big')


class BlockCipher:
    def __init__(self, key: bytearray):
        self.e_key = key

    def encrypt(self, raw: bytearray):
        cipher = AES.new(self.e_key, AES.MODE_CBC, block_iv)
        return cipher.encrypt(raw)

    def decrypt(self, enc: bytearray):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.ekey, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))
