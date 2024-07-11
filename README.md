# Image Encryption Tool

This is a simple image encryption tool using pixel manipulation. It can encrypt and decrypt images by performing operations like swapping pixel values or applying basic mathematical operations to each pixel.

## How to Use

1. **Encrypt an Image**:
   ```python
   from image_encryption import encrypt_image
   encrypt_image('input_image.png', 'encrypted_image.png', key=5)

   DECRYPT AN IMAGE

   from image_encryption import decrypt_image
decrypt_image('encrypted_image.png', 'decrypted_image.png', key=5)

Requirrments
.python 3.x
.pillow

INSTALL the pillow library using pip:

pip install pillow

LICENSE
this project is licensed under the MIT licence.
