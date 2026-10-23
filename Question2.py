# Question 2

#encrypts
def encrypt(message, rows):
    columns = len(message) // rows
    encrypted = ""

    for col in range(columns):
        for row in range(rows):
            index = row * columns + col
            encrypted = encrypted + message[index]

    return encrypted


#decrypts
def decrypt(ciphertext, rows):
    columns = len(ciphertext) // rows
    decrypted = ""

    for row in range(rows):
        for col in range(columns):
            index = col * rows + row
            decrypted = decrypted + ciphertext[index]

    return decrypted



def main ():
    message = input("Enter a message: ")
    rows = int(input("Enter the number of rows: "))

    while len(message) % rows != 0:
        message = message + "X"

    columns = len(message) // rows

    ciphertext = encrypt(message, rows)
    print("Encrypted message:", ciphertext)

    plaintext = decrypt(ciphertext, rows)
    print("Decrypted message:", plaintext)

main()