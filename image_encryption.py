from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key=5):
    image = Image.open(input_image_path)
    image_data = np.array(image)

    # Encrypt the image by adding a key to each pixel value
    encrypted_data = (image_data + key) % 256

    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(encrypted_image_path, output_image_path, key=5):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_data = np.array(encrypted_image)

    # Decrypt the image by subtracting the key from each pixel value
    decrypted_data = (encrypted_data - key) % 256

    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

# Paths for the input and output images
input_image_path = 'input_image.png'
encrypted_image_path = 'encrypted_image.png'
decrypted_image_path = 'decrypted_image.png'

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, key=5)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, key=5)
