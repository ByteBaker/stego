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
stego 4spach encode --text "Hello World" --data "secret"
stego 4spach decode --text "encoded_text"

# Other methods (coming soon)
stego ait-steg encode --text "cover" --data "secret" --key "password"
stego twsm encode --text "cover" --data "secret"
stego em-st encode --text "cover" --data "secret"
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
