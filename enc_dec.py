import random


def ran_pass_gen(str_len):
    letters = ["!", "@", "$", "%", "^", "&", "*", "+", "=", "-", "~", "1", "2", "3", "4", "5", "6", "7", "8", "9",
               "0",
               "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
               "U",
               "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
               "p",
               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    return ''.join(random.choice(letters) for _ in range(str_len))


def encrypt(filename):
    key = 239
    file = open(filename, "rb")
    data = file.read()
    file.close()
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(filename, "wb")
    file.write(data)
    file.close()


def decrypt(filename):
    key = 239
    file = open(filename, "rb")
    data = file.read()
    file.close()
    data = bytearray(data)

    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(("decrypted" + filename), "wb")
    file.write(data)
    file.close()
