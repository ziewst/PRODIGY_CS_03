from PIL import Image

def encrypt_image(input_path, output_path, key):
    # Open the image
    original_image = Image.open(input_path)
    
    # Get image dimensions
    width, height = original_image.size
    
    # Create a new image with the same dimensions
    encrypted_image = Image.new("RGB", (width, height))
    
    # Iterate through each pixel and apply XOR operation with the key
    for x in range(width):
        for y in range(height):
            original_pixel = original_image.getpixel((x, y))
            encrypted_pixel = tuple([(p ^ key) for p in original_pixel])
            encrypted_image.putpixel((x, y), encrypted_pixel)
    
    # Save the encrypted image
    encrypted_image.save(output_path)
    print("Image encrypted successfully.")

def decrypt_image(input_path, output_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(input_path)
    
    # Get image dimensions
    width, height = encrypted_image.size
    
    # Create a new image with the same dimensions
    decrypted_image = Image.new("RGB", (width, height))
    
    # Iterate through each pixel and apply XOR operation with the key
    for x in range(width):
        for y in range(height):
            encrypted_pixel = encrypted_image.getpixel((x, y))
            decrypted_pixel = tuple([(p ^ key) for p in encrypted_pixel])
            decrypted_image.putpixel((x, y), decrypted_pixel)
    
    # Save the decrypted image
    decrypted_image.save(output_path)
    print("Image decrypted successfully.")

def main():
    input_image_path = "IMGL5139.JPG"  # Replace with your input image file path
    encrypted_image_path = "IMG-20240305-WA0016.jpg"  # Replace with the desired output path for encrypted image
    decrypted_image_path = "IMG-20240305-WA0016.jpg"  # Replace with the desired output path for decrypted image

    key = int(input("Enter the encryption key (integer): "))
    
    # Encrypt the image
    encrypt_image(input_image_path, encrypted_image_path, key)
    
    # Decrypt the image
    decrypt_image(encrypted_image_path, decrypted_image_path, key)

if __name__ == "__main__":
    main()
