# Question 3



def encrypt(message, date):
    encrypted = ""

    for i in range(len(message)):
        shift = int(date[i % len(date)])
        letter = message[i]

        new_position = (ord(letter) - ord("A") + shift) % 26
        encrypted_letter = chr(new_position + ord("A"))

        encrypted += encrypted_letter

    return encrypted


def decrypt(ciphertext, date):
    decrypted = ""

    for i in range(len(ciphertext)):
        shift = int(date[i % len(date)])
        letter = ciphertext[i]

        new_position = (ord(letter) - ord("A") - shift) % 26
        decrypted_letter = chr(new_position + ord("A"))

        decrypted += decrypted_letter

    return decrypted


def main():
    message = input("Enter a message: ")
    date = input("Enter a date (MM/DD/YY): ")

    date = date.replace("/", "")
    message = message.upper()

    ciphertext = encrypt(message, date)
    print("Encrypted message:", ciphertext)

    plaintext = decrypt(ciphertext, date)
    print("Decrypted message:", plaintext)


main()
    