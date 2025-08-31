# Steganography Examples

This directory contains practical examples demonstrating all four steganography methods.

## Quick Start

1. **Python Demo** (recommended):
   ```bash
   cd examples/
   python demo.py
   ```

2. **CLI Examples**:
   ```bash
   cd examples/
   ./cli_examples.sh
   ```

## Files

### Input Files
- **`cover_text.txt`** - Sample cover text for hiding messages
- **`secret_message.txt`** - Sample secret message to hide

### Demo Scripts  
- **`demo.py`** - Interactive Python demonstration of all methods
- **`cli_examples.sh`** - Shell script showing CLI usage
- **`README.md`** - This documentation

## What Each Method Does

### 🔸 4spach
- Adds invisible Unicode characters to text
- Output looks identical to input but contains hidden data
- Perfect for hiding data in plain text communications

### 🔐 AIT_Steg  
- Uses zero-width characters with encryption
- Requires password for decoding
- Most secure method with key derivation

### 📝 TWSM
- Adds formatting like **bold** and *italic* to text  
- Works in chat apps (WhatsApp, Telegram, Discord)
- Text remains readable while hiding data

### 😀 Em_st
- Inserts emoticons and symbols into text
- Natural-looking :) and {} symbols
- Fun method that doesn't look suspicious

## Expected Output

After running the demos, you'll see:

```
Original: "Hello everyone! This is a sample cover text..."
4spach:   "Hello everyone! This is a sample cover text..." (looks identical, has invisible chars)
TWSM:     "*Hello* **everyone!** _This_ *is* ..."
Em_st:    "Hello :) everyone! :D This {} is [] ..."
AIT_Steg: "Hello everyone! This is a sample cover text..." (looks identical, encrypted)
```

## CLI Examples

```bash
# Encode secret into cover text
stego 4spach encode --cover cover_text.txt --data secret_message.txt --output hidden.txt

# Decode secret from encoded text  
stego 4spach decode --input hidden.txt --output revealed.txt

# Verify it worked
diff secret_message.txt revealed.txt
```

## File Size Comparison

Typical file sizes after encoding:
- Original cover: ~400 bytes
- Original secret: ~150 bytes  
- 4spach encoded: ~650 bytes (invisible Unicode added)
- AIT_Steg encoded: ~700 bytes (zero-width + encryption overhead)
- TWSM encoded: ~800 bytes (formatting markers added)
- Em_st encoded: ~900 bytes (emoticons/symbols added)

## Tips

1. **Invisible Methods** (4spach, AIT_Steg):
   - Use a hex editor to see the hidden Unicode characters
   - Perfect for email, documents, web content

2. **Visible Methods** (TWSM, Em_st):  
   - Great for social media and chat platforms
   - Text remains engaging and readable
   - Can be combined with invisible methods for multi-layer hiding

3. **Security**:
   - AIT_Steg is most secure (encryption + key derivation)
   - Other methods provide obscurity through steganography
   - Combine methods for maximum security

## Testing

The demo scripts will verify that:
- ✅ All methods encode successfully
- ✅ All methods decode correctly  
- ✅ Original secret matches decoded output
- ✅ Wrong passwords fail (for AIT_Steg)
- ✅ File I/O works properly

Run the examples to see the steganography toolkit in action!