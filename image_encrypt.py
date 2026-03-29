# Task 02 - Image Encrypt Tool
# Cybersecurity Internship - SkillCraft Technology

from PIL import Image

img = Image.open("test.jpg")
pixels = img.load()
width, height = img.size

key = int(input("Enter encryption key: "))

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]

        r = (r + key) % 256
        g = (g + key) % 256
        b = (b + key) % 256

        pixels[x, y] = (r, g, b)

img.save("encrypted_image.png")
print("Encrypted image saved!")

img2 = Image.open("encrypted_image.png")
pixels2 = img2.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels2[x, y]

        r = (r - key) % 256
        g = (g - key) % 256
        b = (b - key) % 256

        pixels2[x, y] = (r, g, b)

img2.save("decrypted_image.png")
print("Decrypted image saved!")