# Stego

A comprehensive steganography toolkit implementing four distinct encoding methods for hiding data in plain sight.

## Methods

### 🔸 4spach - Unicode Binary Encoding
Uses four invisible Unicode characters for 2-bit binary encoding:
- `\u200B` (Zero Width Space) → 00
- `\u200C` (Zero Width Non-Joiner) → 01  
- `\u200D` (Zero Width Joiner) → 10
- `\uFEFF` (Zero Width No-Break Space) → 11

### 🔐 AIT_Steg - Encrypted Zero-Width Steganography
Advanced method using 8 zero-width Unicode characters with encryption:
- Dynamic key generation from content hash + timestamp
- XOR encryption with PBKDF2 key derivation
- Supports both user keys and automatic key generation

### 📝 TWSM - Text Formatting Steganography  
Encodes data using text formatting patterns compatible with chat platforms:
- `*text*` → 00, `**text**` → 01, `_text_` → 10, `__text__` → 11
- Works across WhatsApp, Telegram, Discord, and other markdown platforms
- Maintains text readability while hiding data

### 😀 Em_st - Emoticon-Based Encoding
Uses emoticons and symbols for 4-bit encoding (16 patterns):
- `:)` → 0000, `:D` → 0010, `{}` → 1010, `++` → 1110, etc.
- Natural-looking symbol placement at word boundaries
- Supports extended symbol sets for additional patterns

## Installation

```bash
# Install directly from GitHub
pip install git+https://github.com/bytebaker/stego.git

# Or clone and install locally  
git clone https://github.com/bytebaker/stego.git
cd stego
pip install -e .
```

## Usage

### Command Line Interface

```bash
# 4spach method - Invisible Unicode
stego 4spach encode --cover cover.txt --data secret.txt --output encoded.txt
stego 4spach decode --input encoded.txt --output decoded.txt

# AIT_Steg method - Encrypted zero-width
stego ait-steg encode --cover cover.txt --data secret.txt --key "password" --output encoded.txt
stego ait-steg decode --input encoded.txt --key "password" --output decoded.txt

# TWSM method - Text formatting
stego twsm encode --cover cover.txt --data secret.txt --output encoded.txt  
stego twsm decode --input encoded.txt --output decoded.txt

# Em_st method - Emoticons
stego em-st encode --cover cover.txt --data secret.txt --output encoded.txt
stego em-st decode --input encoded.txt --output decoded.txt
```

### Python API

```python
from stego.methods.fourspach import FourSpachMethod
from stego.methods.ait_steg import AITStegMethod
from stego.methods.twsm import TWSMMethod
from stego.methods.em_st import EmStMethod

# 4spach example
method = FourSpachMethod()
encoded = method.encode("Hello world!", "secret data")
decoded = method.decode(encoded)

# AIT_Steg with encryption
method = AITStegMethod()
encoded = method.encode("Hello world!", "secret data", key="password")
decoded = method.decode(encoded, key="password")

# TWSM formatting
method = TWSMMethod()
encoded = method.encode("Hello world!", "secret")
# Result: "*Hello* **world!**" (contains hidden "secret")
decoded = method.decode(encoded)

# Em_st emoticons
method = EmStMethod()  
encoded = method.encode("Hello world!", "secret")
# Result: "Hello :) world! :D :(" (contains hidden "secret")
decoded = method.decode(encoded)
```

## Examples

### 4spach Output
```
Input:  "Hello World!"
Secret: "Hi"
Output: "Hello World!‌‍‌‍‌‍‌‍‌‍‌‍‌‍‌‍‌‍" (contains invisible Unicode)
```

### TWSM Output  
```
Input:  "Hello World How are you"
Secret: "Hi"  
Output: "*Hello* *World* **How** *are*" (formatting encodes "Hi")
```

### Em_st Output
```
Input:  "Hello World How are you"  
Secret: "Hi"
Output: "Hello :) World :( How are you" (emoticons encode "Hi")
```

## Features

- 🔒 **Encryption**: AIT_Steg method includes XOR encryption with key derivation
- 🌐 **Unicode Support**: Full UTF-8 compatibility across all methods
- 📱 **Cross-Platform**: TWSM works with WhatsApp, Telegram, Discord formatting
- 🔄 **Multiple Cycles**: Support for encoding into already-encoded text
- 📄 **File I/O**: Complete file-based command-line interface
- ✅ **Tested**: 41 comprehensive tests covering all functionality
- 📦 **Pip Install**: Easy installation from GitHub

## Testing

```bash
# Run all tests
pytest tests/ -v

# Test specific method
pytest tests/test_fourspach.py -v
pytest tests/test_ait_steg.py -v  
pytest tests/test_twsm.py -v
pytest tests/test_em_st.py -v

# CLI integration tests  
pytest tests/test_cli.py -v
```

## Architecture

```
stego/
├── setup.py                 # Package configuration
├── src/stego/              # Main package
│   ├── cli.py              # CLI entry point with argparse
│   ├── methods/            # Steganography implementations
│   │   ├── base.py         # Abstract StegoMethod base class
│   │   ├── fourspach.py    # 4spach Unicode method ✅
│   │   ├── ait_steg.py     # AIT_Steg encrypted method ✅
│   │   ├── twsm.py         # TWSM formatting method ✅
│   │   └── em_st.py        # Em_st emoticon method ✅
│   └── __init__.py         # Package exports
├── tests/                  # Comprehensive test suite
│   ├── conftest.py         # Test fixtures
│   ├── test_fourspach.py   # 4spach tests (6 tests)
│   ├── test_ait_steg.py    # AIT_Steg tests (7 tests)  
│   ├── test_twsm.py        # TWSM tests (8 tests)
│   ├── test_em_st.py       # Em_st tests (10 tests)
│   └── test_cli.py         # CLI tests (10 tests)
└── requirements.txt        # Dependencies
```

## Security Notes

- AIT_Steg uses PBKDF2 key derivation with 1000 iterations
- Dynamic key generation uses SHA-256 + timestamp components
- All methods handle UTF-8 encoding properly for international text
- Length prefixes prevent data corruption during decode
- Comprehensive input validation and error handling

## License

MIT License - Feel free to use for educational and research purposes.
