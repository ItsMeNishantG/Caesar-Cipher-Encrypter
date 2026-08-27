# Caesar-Cipher-Encrypter

Caesar Cipher Encrypter  CLI Tool Using Python 

A lightweight, robust command-line interface (CLI) tool built in Python to encrypt and decrypt text using the historic Caesar Cipher technique. 

This implementation utilizes pure algorithmic logic using Python standard libraries, making it completely self-contained with no external dependencies or external packages required.

## Features

- **Bidirectional Processing:** Seamlessly encrypts plaintext messages or decrypts ciphertext messages.
- **Case Preservation:** Maintains the precise case of letters (uppercase letters remain uppercase, lowercase remain lowercase).
- **Character Immunity:** Numbers, symbols, spaces, and punctuation marks pass through untouched without distortion.
- **Dynamic Shift Wrapping:** Supports shift keys of any size (including negative keys and shifts greater than 26) using mathematical modulo constraints.
- **Input Validation:** Gracefully catches user formatting errors and system interrupts (Ctrl+C) without crashing.

## How It Works

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a fixed number of places down the alphabet. 

For instance, with a right shift of 3:
- A becomes D
- B becomes E
- Z wraps around to become C

Mathematically, the encryption phase for a single letter x with a shift n is defined as:

E_n(x) = (x + n) mod 26

## Prerequisites

To run this tool locally, ensure you have Python installed:
- Python 3.6 or higher

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com
cd caesar-cipher
```

### 2. Run the Script
Execute the tool directly inside your terminal using Python:
```bash
python caesar_cipher.py
```

## Usage Example

```text
========================================
      CAESAR CIPHER CLI TOOL      
========================================
Choose action (encrypt / decrypt / quit): encrypt
Enter the message to encrypt: Hello, World! 2026
Enter shift key (integer, e.g., 3): 4

----------------------------------------
Original:  Hello, World! 2026
Result:    Lipps, Asvph! 2026
----------------------------------------
```

## Project Architecture

- `caesar_cipher.py`: The executable entry point containing user prompt validations, control loops, and string processing functions via ASCII character code transformations (ord and chr).

## License

This project is open-source and available for personal use 
