# Vigenère Cipher:

Invented in the 16th century and considered secure until well into the twentieth century, the Vigenère Cipher is a type of Substitution Cipher.

# Encryption

The steps:

    Choose a keyword.
    Convert the plaintext and key to integers based upon the alphabetic position of the letters (e.g. A = 0, B = 1, …, Z = 25).
    Repeat the key if necessary so that it is at least as long as the plaintext to be sent.
    Add the values of the (repeated) key to the values of the plain text and take the modulus of them mod 26.*
    Convert the numbers back to letters.
    
   
   # Decryption

To decrypt ciphertext encrypted using Vigenère’s cipher one must know the key. From here getting back to the original plaintext message is relatively simple. Do the reverse of the encryption algorithm; that is take the value of the corresponding letter of the key from the values of the letters of ciphertext and convert back to the English alphabet.

The decryption (Key is Known):

    Convert both the ciphertext and the known key to integers based upon the alphabetic position of the letters (e.g. A = 0, B = 1, …, Z = 25).
    Repeat the key if necessary so that it is at least as long as the ciphertext received.
    Subtract the values of the (repeated) key from the corresponding values of the ciphertext and take the modulus of them mod 26.
    Convert the numbers back to letters and you have the original message.
    
 # Mode of Attack
 Chosen plaintext attack

In the case of Vigenère’s cipher getting the key under a chosen plaintext attack is simple. We simply choose plaintext of AAAAAA… and then receive the key repeated. The repetition can be noted and then used to find the key.
