# 🔐 Image Encryption & Decryption Tool

## 📌 Task 02 - Cybersecurity Internship (SkillCraft Technology)

---

## 📖 Description
This project is a simple Image Encryption and Decryption Tool built using Python.

The program encrypts an image by modifying its pixel values using a secret key and can decrypt it back to the original image using the same key.

It demonstrates basic concepts of:
- Image processing
- Cryptography (simple key-based encryption)
- Pixel manipulation

---

## ⚙️ How It Works

### 🔒 Encryption:
- Each pixel has RGB values (Red, Green, Blue)
- The program adds a key value to each RGB component
- Uses modulo operation (`% 256`) to keep values within valid range

### 🔓 Decryption:
- Subtracts the same key from each RGB value
- Restores the original image

---

## 🚀 Features
- Encrypt any image (JPG / PNG)
- Decrypt encrypted images
- Simple and easy to understand logic
- Beginner-friendly project

---

## 🛠️ Requirements

- Python installed
- Pillow library

### Install Pillow:
```bash
python -m pip install pillow