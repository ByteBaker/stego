#!/usr/bin/env python3
"""
Steganography Toolkit Demonstration
===================================

This script demonstrates all four steganography methods:
- 4spach: Invisible Unicode characters
- AIT_Steg: Encrypted zero-width steganography  
- TWSM: Text formatting steganography
- Em_st: Emoticon-based encoding
"""

import sys
import os

# Add the src directory to path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from stego.methods.fourspach import FourSpachMethod
from stego.methods.ait_steg import AITStegMethod
from stego.methods.twsm import TWSMMethod
from stego.methods.em_st import EmStMethod


def load_files():
    """Load cover text and secret message from files."""
    with open('cover_text.txt', 'r', encoding='utf-8') as f:
        cover_text = f.read()
    
    with open('secret_message.txt', 'r', encoding='utf-8') as f:
        secret_message = f.read()
    
    return cover_text, secret_message


def demo_4spach(cover_text, secret_message):
    """Demonstrate 4spach method with invisible Unicode characters."""
    print("=" * 60)
    print("🔸 4SPACH - Invisible Unicode Characters")
    print("=" * 60)
    
    method = FourSpachMethod()
    
    # Encode
    encoded = method.encode(cover_text, secret_message)
    print(f"Original length: {len(cover_text)} characters")
    print(f"Encoded length:  {len(encoded)} characters")
    print(f"Hidden message:  {len(secret_message)} characters")
    
    # The encoded text looks identical to original but contains invisible Unicode
    print(f"\nEncoded text (looks identical to original):")
    print(f'"{encoded}"')
    
    # Show that invisible characters are present
    invisible_chars = [c for c in encoded if c in ['\u200B', '\u200C', '\u200D', '\uFEFF']]
    print(f"\nInvisible characters added: {len(invisible_chars)}")
    
    # Decode
    decoded = method.decode(encoded)
    print(f"\nDecoded message:")
    print(f'"{decoded}"')
    
    success = decoded == secret_message
    print(f"\n✅ Success: {success}")
    
    # Save encoded result
    with open('4spach_encoded.txt', 'w', encoding='utf-8') as f:
        f.write(encoded)
    print("📄 Saved to: 4spach_encoded.txt")


def demo_ait_steg(cover_text, secret_message):
    """Demonstrate AIT_Steg method with encryption."""
    print("\n" + "=" * 60)
    print("🔐 AIT_STEG - Encrypted Zero-Width Steganography")
    print("=" * 60)
    
    method = AITStegMethod()
    password = "MySecretPassword123"
    
    # Encode with password
    encoded = method.encode(cover_text, secret_message, key=password)
    print(f"Original length: {len(cover_text)} characters")
    print(f"Encoded length:  {len(encoded)} characters")
    print(f"Encryption key:  {password}")
    
    print(f"\nEncoded text:")
    print(f'"{encoded}"')
    
    # Show zero-width characters
    zero_width_chars = [c for c in encoded if c in method.ZERO_WIDTH_CHARS]
    print(f"\nZero-width characters: {len(zero_width_chars)}")
    
    # Decode with correct password
    decoded_correct = method.decode(encoded, key=password)
    print(f"\nDecoded with correct password:")
    print(f'"{decoded_correct}"')
    
    # Try decoding with wrong password
    try:
        decoded_wrong = method.decode(encoded, key="WrongPassword")
        print(f"\nDecoded with wrong password:")
        print(f'"{decoded_wrong}" (should be empty or wrong)')
    except Exception as e:
        print(f"\nWrong password failed as expected: {e}")
    
    success = decoded_correct == secret_message
    print(f"\n✅ Success: {success}")
    
    # Save encoded result
    with open('ait_steg_encoded.txt', 'w', encoding='utf-8') as f:
        f.write(encoded)
    print("📄 Saved to: ait_steg_encoded.txt")


def demo_twsm(cover_text, secret_message):
    """Demonstrate TWSM method with text formatting."""
    print("\n" + "=" * 60)
    print("📝 TWSM - Text Formatting Steganography")
    print("=" * 60)
    
    method = TWSMMethod()
    
    # Encode
    encoded = method.encode(cover_text, secret_message)
    print(f"Original text:")
    print(f'"{cover_text[:100]}..."')
    
    print(f"\nFormatted text (contains hidden message):")
    print(f'"{encoded[:200]}..."')
    
    # Show formatting patterns
    formatting_count = sum([encoded.count(fmt) for fmt in ['*', '**', '_', '__']])
    print(f"\nFormatting markers added: {formatting_count}")
    print("Patterns: * (italic), ** (bold), _ (underline), __ (bold underline)")
    
    # Decode
    decoded = method.decode(encoded)
    print(f"\nDecoded message:")
    print(f'"{decoded}"')
    
    success = decoded == secret_message
    print(f"\n✅ Success: {success}")
    
    # Save encoded result
    with open('twsm_encoded.txt', 'w', encoding='utf-8') as f:
        f.write(encoded)
    print("📄 Saved to: twsm_encoded.txt")


def demo_em_st(cover_text, secret_message):
    """Demonstrate Em_st method with emoticons."""
    print("\n" + "=" * 60)
    print("😀 EM_ST - Emoticon-Based Encoding")
    print("=" * 60)
    
    method = EmStMethod()
    
    # Encode
    encoded = method.encode(cover_text, secret_message)
    print(f"Original text:")
    print(f'"{cover_text[:100]}..."')
    
    print(f"\nText with emoticons (contains hidden message):")
    print(f'"{encoded[:200]}..."')
    
    # Show emoticons/symbols used
    symbols_used = []
    for symbol in method.SYMBOL_MAP.values():
        if symbol in encoded:
            symbols_used.append(symbol)
    
    print(f"\nEmoticons/symbols used: {symbols_used}")
    print(f"Total symbols added: {len([s for s in encoded.split() if s in method.SYMBOL_MAP.values()])}")
    
    # Decode
    decoded = method.decode(encoded)
    print(f"\nDecoded message:")
    print(f'"{decoded}"')
    
    success = decoded == secret_message
    print(f"\n✅ Success: {success}")
    
    # Save encoded result
    with open('em_st_encoded.txt', 'w', encoding='utf-8') as f:
        f.write(encoded)
    print("📄 Saved to: em_st_encoded.txt")


def main():
    """Run all demonstrations."""
    print("🔐 STEGANOGRAPHY TOOLKIT DEMONSTRATION")
    print("=====================================")
    print("This demo shows all four steganography methods in action.")
    
    # Load test data
    try:
        cover_text, secret_message = load_files()
        print(f"\n📖 Cover text loaded: {len(cover_text)} characters")
        print(f"🔒 Secret message: {len(secret_message)} characters")
        print(f'    "{secret_message[:50]}..."')
    except FileNotFoundError as e:
        print(f"❌ Error: Could not load files. Make sure you're in the examples directory.")
        print(f"    {e}")
        return
    
    # Run demonstrations
    demo_4spach(cover_text, secret_message)
    demo_ait_steg(cover_text, secret_message)
    demo_twsm(cover_text, secret_message)
    demo_em_st(cover_text, secret_message)
    
    print("\n" + "=" * 60)
    print("🎉 ALL DEMONSTRATIONS COMPLETED")
    print("=" * 60)
    print("Check the generated files:")
    print("- 4spach_encoded.txt (invisible Unicode)")
    print("- ait_steg_encoded.txt (encrypted zero-width)")
    print("- twsm_encoded.txt (formatted text)")
    print("- em_st_encoded.txt (emoticons)")
    print("\nYou can also use the CLI:")
    print("stego 4spach decode --input 4spach_encoded.txt --output decoded.txt")


if __name__ == "__main__":
    main()