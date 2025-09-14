def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                
            encrypted_text += encrypted_char
            
        else:
            encrypted_text += char

    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("=" * 50)
    print("     CAESAR CIPHER ENCRYPTION/DECRYPTION")
    print("=" * 50)

    while True:
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n0. Exit\n")
        if choice == '1':
            text = input("Enter text to encrypt:")
            shift = int(input("Enter shift value (1-25):"))
            encrypted = caesar_cipher_encrypt(text, shift)
            print(f"Encrypted text: {encrypted}")
        elif choice == '2':
            text = input("Enter text to decrypt:")
            shift = int(input("Enter shift value (1-25):"))
            decrypted= caesar_cipher_decrypt(text, shift)
            print(f"Decrypted text: {decrypted}")
        elif choice == '0':
            print("Exiting the program.")
            break
        
if __name__ == "__main__":
    print("Caesar Cipher Program")
    print("Example demonstrations:")
    
    # Test encryption
    test_message = "Hello World!"
    test_shift = 3
    encrypted = caesar_cipher_encrypt(test_message, test_shift)
    decrypted = caesar_cipher_decrypt(encrypted, test_shift)
    
    print(f"\nTest Example:")
    print(f"Original: {test_message}")
    print(f"Shift: {test_shift}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted back: {decrypted}")
    
    print("\n" + "="*50)
    
    # Run the main program
    main()