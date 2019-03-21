import encrypted_search
import os
import sys

BLOCK_CIPHER_KEY = bytearray('sixteen byte key', 'utf-8')


def main():
    try:
        os.remove(os.path.join('./file/encrypted/test.enc'))
    except FileNotFoundError:
        pass

    with open(os.path.join('./files/raw/test.txt'), 'rb') as in_file:
        encrypted_search.encrypt(in_file, os.path.join('./files/encrypted/test.enc'), BLOCK_CIPHER_KEY)

    while True:
        try:
            search_word = input('Word to search for: ')
            if not search_word:
                        print('Must enter some text to proceed')
                        sys.exit(1)

            with open(os.path.join('./files/encrypted/test.enc'), 'rb') as in_file:
                encrypted_search.search(search_word, in_file, BLOCK_CIPHER_KEY)
        except EOFError:
            print('\nQuitting...\n')
            sys.exit(0)
        except KeyboardInterrupt:
            print('\nQuitting...\n')
            sys.exit(0)


if __name__ == "__main__":
    main()
