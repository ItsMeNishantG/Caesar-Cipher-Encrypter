#!/usr/bin/env python3
"""
Caesar Cipher CLI Tool
A script to encrypt and decrypt text using the classic Caesar Cipher technique.
"""

import sys

def caesar_cipher(text: str, shift: int, mode: str) -> str:
    """
    Encrypts or decrypts text by shifting characters by a set amount.
    
    :param text: The string message to be processed.
    :param shift: The number of positions to shift the alphabet.
    :param mode: 'encrypt' or 'decrypt'.
    :return: The processed string message.
    """
    # Adjust shift direction based on mode
    if mode == 'decrypt':
        shift = -shift
        
    result = []
    
    for char in text:
        # Process uppercase letters
        if char.isupper():
            # Shift within 0-25 range, then convert back to ASCII
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted_char)
        # Process lowercase letters
        elif char.islower():
            # Shift within 0-25 range, then convert back to ASCII
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted_char)
        else:
            # Leave punctuation, numbers, and spaces unchanged
            result.append(char)
            
    return "".join(result)

def get_valid_shift() -> int:
    """Prompts user for a shift key until a valid integer is provided."""
    while True:
        try:
            shift_input = input("Enter shift key (integer, e.g., 3): ").strip()
            return int(shift_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
    print("=" * 40)
    print("      CAESAR CIPHER CLI TOOL      ")
    print("=" * 40)
    
    # 1. Select Mode
    while True:
        mode = input("Choose action (encrypt / decrypt / quit): ").strip().lower()
        if mode in ['e', 'encrypt']:
            mode = 'encrypt'
            break
        elif mode in ['d', 'decrypt']:
            mode = 'decrypt'
            break
        elif mode in ['q', 'quit']:
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please type 'encrypt', 'decrypt', or 'quit'.")
            
    # 2. Get Message Input
    message = input(f"Enter the message to {mode}: ").strip()
    if not message:
        print("Message cannot be empty.")
        return

    # 3. Get Shift Key
    shift = get_valid_shift()
    
    # 4. Process and Display Result
    processed_message = caesar_cipher(message, shift, mode)
    
    print("\n" + "-" * 40)
    print(f"Original:  {message}")
    print(f"Result:    {processed_message}")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
        sys.exit(0)
