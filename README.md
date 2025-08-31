# Stego

Simple steganography toolkit with four encoding methods:

- **4spach**: Four invisible Unicode characters for binary encoding
- **ait_steg**: Zero-width Unicode with dynamic keys  
- **twsm**: Text formatting (bold/italic) encoding
- **em_st**: Emoticon-based encoding

## Usage

```bash
# 4spach method
python main.py 4spach encode --text "Hello World" --data "secret"
python main.py 4spach decode --text "encoded_text"

# Other methods (coming soon)
python main.py ait-steg encode --text "cover" --data "secret" --key "password"
python main.py twsm encode --text "cover" --data "secret"
python main.py em-st encode --text "cover" --data "secret"
```

## Structure

```
stego/
├── main.py              # CLI entry point
├── methods/             # Method implementations
│   ├── base.py         # Abstract base class
│   ├── fourspach.py    # 4spach implementation
│   ├── ait_steg.py     # AIT_Steg (TODO)
│   ├── twsm.py         # TWSM (TODO)
│   └── em_st.py        # Em_st (TODO)
└── requirements.txt
```
