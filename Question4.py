# Question 4

def encrypt(message, alphabet, cipher_alphabet):
    encrypted = ""

    for letter in message:
        index = alphabet.find(letter)
        encrypted += cipher_alphabet[index]

    return encrypted


def decrypt(ciphertext, alphabet, cipher_alphabet):
    decrypted = ""

    for letter in ciphertext:
        index = cipher_alphabet.find(letter)
        decrypted += alphabet[index]

    return decrypted


def main():
    keyword = input("Enter a keyword: ")
    message = input("Enter a message: ")

    keyword = keyword.upper()
    message = message.upper()

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alphabet = ""

    for letter in keyword:
        if letter not in cipher_alphabet:
            cipher_alphabet += letter

    for letter in alphabet: 
        if letter not in cipher_alphabet:
            cipher_alphabet += letter

    print("Original alphabet:", alphabet)
    print("Cipher alphabet:", cipher_alphabet)

    ciphertext = encrypt(message, alphabet, cipher_alphabet)
    print("Encrypted message:", ciphertext)

    plaintext = decrypt(ciphertext, alphabet, cipher_alphabet)
    print("Decrypted message:", plaintext)

main()