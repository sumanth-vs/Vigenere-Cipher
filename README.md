# Vigenère Cipher:

Vigenère’s cipher was invented in the 16th century and was considered secure until well into the twentieth century despite attacks being developed in the 19th century by the British mathematician Charles Babbage and the German cryptographer Friedrich Kasiski. 

# Encryption

The steps of Vigenère’s cipher are as follows:

    Choose a keyword or a key length and subsequently a set of characters equal to that length.
    Convert both the plaintext and key to integers based upon the alphabetic position of the letters (e.g. A = 0, B = 1, …, Z = 25).
    Repeat the key if necessary so that it is at least as long as the plaintext to be sent.
    Add the values of the (repeated) key to the values of the plain text and take the modulus of them mod 26.*
    Convert the numbers back to letters.
    
   
   # Decryption

To decrypt ciphertext encrypted using Vigenère’s cipher one must know the key. From here getting back to the original plaintext message is relatively simple. Do the reverse of the encryption algorithm; that is take the value of the corresponding letter of the key from the values of the letters of ciphertext and convert back to the English alphabet.

The decryption algorithm therefore follows the steps below:

    Convert both the ciphertext and the known key to integers based upon the alphabetic position of the letters (e.g. A = 0, B = 1, …, Z = 25).
    Repeat the key if necessary so that it is at least as long as the ciphertext received.
    Subtract the values of the (repeated) key from the corresponding values of the ciphertext and take the modulus of them mod 26.
    Convert the numbers back to letters and you have the original message.
    
 # Mode of Attack
 Chosen plaintext attack

In the case of Vigenère’s cipher getting the key under a chosen plaintext attack is simple. One simply chooses plaintext of AAAAAA… and then receives the key repeated. The repetition can be noted and then used to find the key.
