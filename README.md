# Stego

Simple steganography toolkit with four encoding methods:

- **4spach**: Four invisible Unicode characters for binary encoding
- **ait_steg**: Zero-width Unicode with dynamic keys  
- **twsm**: Text formatting (bold/italic) encoding
- **em_st**: Emoticon-based encoding

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

```bash
# 4spach method
stego 4spach encode --cover cover.txt --data secret.txt --output encoded.txt
stego 4spach decode --input encoded.txt --output decoded.txt

# Other methods (coming soon)
stego ait-steg encode --cover cover.txt --data secret.txt --key "password" --output encoded.txt
stego twsm encode --cover cover.txt --data secret.txt --output encoded.txt
stego em-st encode --cover cover.txt --data secret.txt --output encoded.txt
```

## Structure

```
stego/
├── setup.py             # Package configuration  
├── src/stego/          # Main package
│   ├── cli.py          # CLI entry point
│   ├── methods/        # Method implementations
│   │   ├── base.py     # Abstract base class
│   │   ├── fourspach.py # 4spach implementation
│   │   ├── ait_steg.py  # AIT_Steg (TODO)
│   │   ├── twsm.py      # TWSM (TODO)  
│   │   └── em_st.py     # Em_st (TODO)
│   └── __init__.py     # Package exports
└── requirements.txt
```
