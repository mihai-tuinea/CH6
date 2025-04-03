import math

p = 193
q = 3
e = 7

n = p * q
phi_n = (p - 1) * (q - 1)

if math.gcd(e, phi_n) != 1:
    raise ValueError

def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

d = modInverse(e, phi_n)


# Function to encrypt a message
def encrypt_message(message, n, e):
    encrypted_message = []
    for char in message:
        m = ord(char)  # Convert char to its ASCII value
        encrypted_char = pow(m, e, n)  # Encrypt using RSA
        encrypted_message.append(encrypted_char)
    return encrypted_message


# Function to decrypt a message
def decrypt_message(encrypted_message, n, d):
    decrypted_message = ''
    for encrypted_char in encrypted_message:
        m = pow(encrypted_char, d, n)  # Decrypt using RSA
        decrypted_message += chr(m)  # Convert back to character
    return decrypted_message


# Test function to encrypt and decrypt a message
def test_rsa_encryption_decryption():
    message = "HELLO"

    # Encrypt the message
    encrypted_message = encrypt_message(message, n, e)
    print(f"Encrypted message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, n, d)
    print(f"Decrypted message: {decrypted_message}")

    # Check if the original message is the same as the decrypted message
    if decrypted_message == message:
        print("RSA Encryption/Decryption works correctly!")
    else:
        print("There is an issue with the encryption/decryption process.")


# Run the test
test_rsa_encryption_decryption()

with open("CH6.txt","r") as file:
    data = file.read().strip().split()
    message = list(map(int, data))

encrypted_text = "۽ෛᓋӂ۽஢छڰ஢۽"

unicode_values = [ord(char) for char in encrypted_text]

# Print results
print("Unicode values:", unicode_values)

print(decrypt_message(unicode_values, n, e))
