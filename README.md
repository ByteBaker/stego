# Stego

Steganography toolkit implementing four methods for hiding data in plain sight.

## Methods

**4spach** - Invisible Unicode characters  
**AIT_Steg** - Encrypted zero-width steganography  
**TWSM** - Text formatting (bold/italic)  
**Em_st** - Emoticon-based encoding  

## Installation

```bash
pip install git+https://github.com/bytebaker/stego.git
```

## Usage

```bash
# Encode secret into cover text
stego 4spach encode --cover cover.txt --data secret.txt --output encoded.txt

# Decode secret from encoded text  
stego 4spach decode --input encoded.txt --output decoded.txt

# Other methods: ait-steg, twsm, em-st
stego ait-steg encode --cover cover.txt --data secret.txt --key "password" --output encoded.txt
```

### Python API

```python
from stego.methods.fourspach import FourSpachMethod

method = FourSpachMethod()
encoded = method.encode("Hello world!", "secret data")
decoded = method.decode(encoded)
```

See `examples/` directory for comprehensive demonstrations of all methods.

## Testing

```bash
pytest tests/ -v
```
