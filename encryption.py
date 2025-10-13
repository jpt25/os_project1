#!/usr/bin/env python3
import sys

# encrypt text
def encrypt(text, key):
    result = ""
    key_length = len(key)

    for i in range(len(text)):
        text_char = text[i]
        key_char = key[i % key_length]

        shift = ord(key_char) - ord('A')
        new_char = chr(((ord(text_char) - ord('A') + shift) % 26) + ord('A'))
        result += new_char

    return result

# decrypt text
def decrypt(text, key):
    result = ""
    key_length = len(key)

    for i in range(len(text)):
        text_char = text[i]
        key_char = key[i % key_length]

        shift = ord(key_char) - ord('A')
        new_char = chr(((ord(text_char) - ord('A') - shift) % 26) + ord('A'))
        result += new_char

    return result

def main():
    key = None

    while True:
        line = sys.stdin.readline().strip()

        # Ignore empty lines
        if line == "":
            continue

        parts = line.split(maxsplit=1)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        # QUIT
        if command == "QUIT":
            break

        # PASS
        elif command == "PASS":
            key = argument
            print("RESULT")

        # ENCRYPT - result + error
        elif command == "ENCRYPT":
            if key is None:
                print("ERROR Password not set")
            else:
                encrypted = encrypt(argument, key)
                print("RESULT", encrypted)

        # DECRYPT - result + error
        elif command == "DECRYPT":
            if key is None:
                print("ERROR Password not set")
            else:
                decrypted = decrypt(argument, key)
                print("RESULT", decrypted)

        sys.stdout.flush()

if __name__ == "__main__":
    main()
