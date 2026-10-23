# Question 5

checkerboard = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "W", "X", "YZ"]
]

def find_letter(checkerboard, letter):
    for row in range(5):
        for col in range(5):
            if letter in checkerboard[row][col]:
                return row, col


def encrypt(message, checkerboard):
    encrypted = ""

    for letter in message:
        row, col = find_letter(checkerboard, letter)
        encrypted += str(row) + str(col) + " "

    return encrypted


def decrypt(ciphertext, checkerboard):
    decrypted = ""

    numbers = ciphertext.split()

    for pair in numbers:
        row = int(pair[0])
        col = int(pair[1])

        letter = checkerboard[row][col]

        if letter == "YZ":
            letter = "Y"

        decrypted += letter

    return decrypted


def main():

    message = input("Enter a message: ")
    message = message.upper()

    ciphertext = encrypt(message, checkerboard)
    print("Encrypted message:", ciphertext)

    plaintext = decrypt(ciphertext, checkerboard)
    print("Decrypted message:", plaintext)

main()