**Pixel manipulation for image encryption**


The provided code is a simple image encryption and decryption system using a XOR operation with a given key. The encrypt_image function reads an image, applies the XOR operation on each pixel's RGB value and the key, and saves the encrypted image. The decrypt_image function does the reverse - it reads the encrypted image, applies the XOR operation again with the same key to restore the original pixel values, and saves the decrypted image. The main function sets up the file paths and key for encryption and decryption. Note that the same key is used for both encryption and decryption, and the key must be known to perform decryption successfully.
