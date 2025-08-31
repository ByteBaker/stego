# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Stego is a simple steganography toolkit implementing four distinct encoding methods:

- **4spach**: Four invisible Unicode characters for binary encoding (currently implemented)
- **ait_steg**: Zero-width Unicode characters with dynamic keys (TODO)
- **twsm**: Text formatting (bold/italic) encoding (TODO)  
- **em_st**: Emoticon-based encoding (TODO)

## Architecture

The project follows a simple modular CLI architecture:

1. **CLI Layer** (`main.py`): Entry point using argparse with nested subcommands
   - Pattern: `python main.py <method> <action> [options]`
   - Methods: `4spach`, `ait-steg`, `twsm`, `em-st`
   - Actions: `encode`, `decode`
   - Common args: `--text`, `--data`, `--key`, `--output`

2. **Method Layer** (`methods/`): Pluggable steganography implementations
   - `base.py`: Abstract `StegoMethod` class with `encode()` and `decode()` methods
   - Each method inherits from `StegoMethod` and implements the interface
   - CLI routes to method classes based on command-line arguments

## Development Commands

```bash
# Environment setup
source venv/bin/activate
pip install -r requirements.txt

# Basic usage and testing
python main.py --help                    # View all available methods
python main.py 4spach encode --text "Hello World" --data "secret"
python main.py 4spach decode --text "encoded_result"

# Test other methods (will show NotImplementedError)
python main.py ait-steg encode --text "test" --data "secret" --key "password"
```

## Adding New Methods

1. Create new method class in `methods/` inheriting from `StegoMethod`
2. Implement `encode()` and `decode()` methods
3. Import and add to method routing in `main.py` (lines 95-102)
4. CLI arguments are automatically available via the existing parser structure

## Commit Rules

- No mentions of "Claude" in commit messages
- Messages should be short, humane, and crisp
- Avoid excess details that the diff shows easily