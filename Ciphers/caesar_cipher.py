
def encrypt(message, k):
    lower_message = message.lower()
    cipher = ""

    for ch in message:
        dex = (ord(ch)-LOW_LIMIT+k) % 26
        cipher += alphabets[dex]

    return cipher

def decrypt(cipher, k):
    lower_cipher = cipher.lower()
    original_message = ""

    for ch in lower_cipher:
        dex = (ord(ch)-LOW_LIMIT-k) % 26

        if dex < 0:
            dex = 25 - dex

        original_message += alphabets[dex]

    return original_message

LOW_LIMIT = 97
HIGH_LIMIT = 123

alphabets = list()
m = ""

for i in range(LOW_LIMIT, HIGH_LIMIT):
    alphabets.append(chr(i))
    m += chr(i)

# m is now abcdefghijklmnopqrstuvwxyz

cipher = encrypt(m, 3)
print(cipher)
print(decrypt(cipher, 3))
